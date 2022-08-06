# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from datetime import datetime
import pymongo
import spacy


class DaSkillsPipeline:
    def process_item(self, item, spider):
        return item


class TextClassificationPipeline:
    def __init__(self) -> None:
        self.nlp = spacy.load("nlp/textcat_model/model-best/")

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        position = adapter["position"]

        doc = self.nlp(position)
        cat = str(max(doc.cats, key=doc.cats.get))
        if cat == "Irrelevant":
            raise DropItem("Irrelevant job position")

        adapter["category"] = cat
        return item


class NamedEntityRecognitionPipeline:
    def __init__(self) -> None:
        self.nlp = spacy.load("nlp/ner_model/model-best/")

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        skills = {}
        description = adapter.get("description")
        for sent in description:
            sent = sent.strip()
            sent.replace("\n", "")
            if len(sent) == 0:
                continue
            doc = self.nlp(sent)
            for ent in doc.ents:
                label = str(ent.label_)
                skill = str(ent).lower()
                if label not in skills:
                    skills[label] = set()
                skills[label].add(skill)
        for key, value in skills.items():
            adapter[key] = list(value)

        adapter.pop("description")
        return item


class LemmatisationPipeline:
    def __init__(self) -> None:
        self.nlp = spacy.load("en_core_web_sm")

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if "degree" in adapter:
            degree_list = []
            for d in adapter["degree"]:
                doc = self.nlp(d)
                degree_list.append(" ".join([token.lemma_ for token in doc]))
            adapter["degree"] = degree_list

        return item


class MongoPipeline:
    def __init__(self, mongo_uri, mongo_db, mongo_collection):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection

    @classmethod
    def from_crawler(cls, crawler):
        import os
        return cls(
            mongo_uri=os.getenv('MONGO_URI'),
            mongo_db="data-analysis",
            mongo_collection="skills-crawling"
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        adapter["date"] = datetime.utcnow()
        try:
            self.db[self.mongo_collection].insert_one(
                ItemAdapter(item).asdict()
            )
        except:
            _id = adapter["_id"]
            if not self.db[self.mongo_collection].find_one({"_id": _id}).get("cleaned", False):
                self.db[self.mongo_collection].replace_one(
                    {"_id": _id},
                    ItemAdapter(item).asdict()
                )
        return item
