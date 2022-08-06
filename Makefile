train-ner:
	python nlp/ner_preprocess.py
	python -m spacy train nlp/ner_config.cfg --output nlp/ner_model

train-textcat:
	python nlp/textcat_preprocess.py
	python -m spacy train nlp/textcat_config.cfg --output nlp/textcat_model

crawl:
	scrapy crawl skills