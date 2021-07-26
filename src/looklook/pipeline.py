import spacy
from nlp_functions import get_study_sentiment
from collections import Counter

from dotenv import load_dotenv

load_dotenv()

cookie = os.getenv("COOKIE")
hostname = os.getenv("HOSTNAME")


text_blob = get_study_sentiment(46)

nlp = spacy.load("en_core_web_sm")
# print(nlp.pipe_names)
# print(nlp.pipeline)

# print(text_blob[0:])

text_blob = '<p>'.join(text_blob)

doc = nlp(text_blob)

print(len(doc.ents))


labels = [ent.label_ for ent in doc.ents]
print(Counter(labels))

items = [ent.text for ent in doc.ents]
print(Counter(items).most_common(10))

# print(list(doc.noun_chunks))

print(len(list(doc.sents)))

for sent in doc.sents:
    print(sent.text)
# # print([(ent.text, ent.label_) for ent in doc.ents])
