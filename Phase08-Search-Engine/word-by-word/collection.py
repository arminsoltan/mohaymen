from os import read
import xml.etree.ElementTree as ET
from pymongo import MongoClient
import re

client = MongoClient('localhost', 27017)
db = client.search_engine
ham = db.ham

def read_news():
    data = dict()
    tree = ET.parse("con1.xml")
    root = tree.getroot()
    for index, doc in enumerate(root):
        title_text = None
        news_text = None
        for x in doc:
            if x.tag == "TITLE":
                title_text = x.text
            elif x.tag == "TEXT":
                news_text = x.text
        if (news_text is not None) and (title_text is not None):
            ham.insert_one({"title": title_text, "text": news_text})
            print(index)
if __name__ == "__main__":
    read_news()
