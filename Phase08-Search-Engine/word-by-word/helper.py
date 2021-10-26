import xml.etree.ElementTree as ET

def search_word(data, words):
    for x in data:
        text = x['text']
        title = x['title']
        if text is None:
            continue
        text = text.split()
        start = 0
        flag = True
        for word in words:
            try:
                start = text.index(word)
            except Exception as err:
                flag = False
            if flag:
                return ' '.join(text[max(0, start - 2):min(len(text) - 1, start + 3)]), title
    return False, None
