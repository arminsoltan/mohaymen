from sklearn.feature_extraction.text import TfidfVectorizer
from parsivar import Tokenizer
from pymongo import MongoClient
import pandas as pd
import operator, re



def search_word(data, client_text):
    tokenizer = Tokenizer()
    df = pd.DataFrame(columns=["title", "text"])
    vocabular = set()
    for x in data:
        title = x["title"]
        text = x["text"]
        words = tokenizer.tokenize_words(text)
        for i in range(len(words)):
            if "\u200c" in words[i]:
                words[i] = re.sub("\u200c", "", words[i])
        vocabular.update(words)
        df.append({
            "title": title,
            "text": ' '.join(words)
        })
    vocabular = list(vocabular)
    tfidf = TfidfVectorizer(vocabulary=vocabular)
    tfidf.fit(df.text)
    tfidf.transform(df.text)
    print(title)
    return
    pass
