from pymongo import MongoClient
import xml.etree.ElementTree as ET
import pandas as pd
# from __future__ import unicode_literals
from hazm import Normalizer
import re

client = MongoClient("localhost", 27017)
db = client.search_engine
ham = db.ham

def read_news():
    tree = ET.parse('data/1.xml')
    root = tree.getroot()
    df = pd.DataFrame(columns=['title', 'text'])
    for index, doc in enumerate(root):
        title_text = None
        news_text = None
        for x in doc:
            if x.tag == "TITLE":
                title_text = x.text
                title_text = re.sub("\n", "", title_text)
            elif x.tag == "TEXT":
                news_text = x.text
                news_text = re.sub("\n", "", news_text)
        if (news_text is not None and news_text != "") and (title_text is not None and title_text != ""):
            df = df.append({'title': title_text, 'text': news_text}, ignore_index=True)
    return df

def preprocessing(df):
    normalizer = Normalizer()
    for i in range(len(df)):
        df.iloc[i] = replace_unsual_chars(df.iloc[i])
        df.iloc[i]["text"] = normalizer.normalize(df.iloc[i]["text"])
    return df

def replace_unsual_chars(sentence):
    replacement = {
        'ْ': '',
        'ٌ': '',
        'ٍ': '',
        'ً': '',
        'ُ': '',
        'ِ': '',
        'َ': '',
        'ّ': '',
        'ؤ': 'و',
        'ئ': 'ئ',
        'ي': 'ی',
        'إ': 'ا',
        'أ': 'ا',
        'أ': 'ا',
        'آ': 'ا',
        'ة': 'ه',
        'ك': 'ک',
        'ٓ': '',
        'ٰ': '',
        '‌': '',
        'ٔ': '',
        'ء': '',
    }
    for symbol in replacement.keys():
        sentence["text"] = re.sub(symbol, replacement[symbol], sentence["text"])
    return sentence

def save_in_database(df):
    for i in range(len(df)):
        ham.insert_one({"title": df.iloc[i]["title"], "text": df.iloc[i]["text"]})

if __name__ == '__main__':
    df = read_news()
    df = preprocessing(df)
    save_in_database(df)
    # df.to_csv("text.csv", columns=["title", "text"], sep='\t', encoding="utf-8")
    # print(df)
