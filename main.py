from __future__ import unicode_literals, print_function
import plac
import spacy
import pandas as pd
nlp_0 = spacy.load('en_core_web_sm')
with open('wallstreetmorning_news.txt','r') as file:
    text_0 = file.read()

TEXTS = []
# for start,end in tokens.sents:
#     temp = ''.join(tokens[x].string for x in range(strat,end))
#     TEXTS.append(temp)
# print(TEXTS)

doc_0 = nlp_0(text_0)

# for entity in doc_0.ents:
#     print(entity.label_,entity.text)
#
for span_0 in doc_0.sents:
    TEXTS.append(str(span_0))



@plac.annotations(
    model=("Model to load (needs parser and NER)", "positional", None, str))
def main(model='en_core_web_sm'):
    nlp = spacy.load(model)
    # print("Loaded model '%s'" % model)
    # print("Processing %d texts" % len(TEXTS))
    temp1,temp2,temp3,temp4,temp5 = [], [], [], [], []
    for text in TEXTS:
        doc = nlp(text)
        # temp1 = extract_percent_relations(doc)
        temp1_0, temp2_0 = extract_information_relations(doc)
        temp1.append(temp1_0)
        temp2.append(temp2_0)
        temp3.append(extract_time(doc))
        temp4.append(extract_tags(doc))
        temp5.append(extract_geo(doc))
    result=[{'time':remove_none(temp3),'data':{'percent':remove_none(temp2),'currency':remove_none(temp1)},'tags':remove_none(temp4),'location':remove_none(temp5)}]
    return result
def remove_none(li):
    re = []
    for val in li:
        if isinstance(val, list):
            for item in val:
                re.append(item)
        else:
            continue
    return re

def extract_tags(doc):
    re = []
    for entity in doc.ents:
        if entity.label_=='ORG' or entity.label_=='PERSON':
            re.append(entity.text)
        else:
            continue
    if re == []:
        return None
    return re
def extract_geo(doc):
    re = []
    for entity in doc.ents:
        if entity.label_=='GPE':
            re.append(entity.text)
        else:
            continue
    if re == []:
        return None
    return re
def extract_time(doc):
    re = []
    for entity in doc.ents:
        if entity.label_=='DATE':
            re.append(entity.text)
        else:
            continue
    if re == []:
        return None
    return re

def extract_information_relations(doc):
    # merge entities and noun chunks into one token
    spans = list(doc.ents) + list(doc.noun_chunks)
    for span in spans:
        span.merge()

    relations = []

    for money in filter(lambda w: w.ent_type_ == 'CARDINAL' or w.ent_type_ == 'MONEY', doc):
        #print(money,money.dep_,money.head.dep_)
        if money.dep_ in ('attr', 'dobj'):
            subject = [w for w in money.head.lefts if w.dep_ == 'nsubj']
            if subject:
                subject = subject[0]
                relations.append((subject, money))
        elif money.dep_ == 'pobj' and money.head.dep_ == 'prep':
            relations.append((money.head.head, money))

    relations_0 = []

    for percent in filter(lambda w: w.ent_type_ == 'PERCENT', doc):
        # print(percent.dep_,percent,percent.head.dep_,percent.left_edge,percent.right_edge)
        if percent.dep_ in ('attr', 'dobj'):
            subject = [w for w in percent.head.lefts if w.dep_ == 'nsubj']
            if subject:
                subject = subject[0]
                relations_0.append((subject, percent))
        elif percent.head.dep_ == 'prep' or percent.left_edge == percent.right_edge:
            relations_0.append((percent.head.head, percent))
    if relations == []:
        relations = None
    if relations_0 == []:
        relations_0 = None
    return relations,relations_0


if __name__ == '__main__':
    data = plac.call(main)
    df = pd.DataFrame(data)
    df.to_csv('result.csv')
