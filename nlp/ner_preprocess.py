import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from annotation.ner_data import ner_data

training_data, testing_data = train_test_split(ner_data, test_size=0.3)

def convert(data, output):
    nlp = spacy.blank("en")                      # load a new spacy model
    db = DocBin()                                # create a DocBin object
    for text, annotations in tqdm(data):         # data in previous format
        doc = nlp.make_doc(text)                 # create doc object from text
        ents = []
        for start, end, label in annotations:    # add character indexes
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is None:
                print("Skipping entry...", text, text[start:end])
            else:
                ents.append(span)
        try:
            doc.ents = ents                     # label the text with the ents
            db.add(doc)
        except:
            print(text, annotations)
    db.to_disk(output)                          # save the docbin object

convert(training_data, "nlp/processed_data/ner_train.spacy")
convert(testing_data, "nlp/processed_data/ner_dev.spacy")