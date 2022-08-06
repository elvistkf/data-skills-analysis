import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from annotation.textcat_data import textcat_data

training_data, testing_data = train_test_split(textcat_data, test_size=0.3)

def convert(data, output):
    nlp = spacy.blank("en")                     # load a new spacy model
    db = DocBin()                               # create a DocBin object

    for text, cat in tqdm(data):
        doc = nlp.make_doc(text)
        for k, v in cat.items():
            doc.cats[k] = v
        db.add(doc)
    
    db.to_disk(output)

convert(training_data, "nlp/processed_data/textcat_train.spacy")
convert(testing_data, "nlp/processed_data/textcat_dev.spacy")