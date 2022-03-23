from string import punctuation
import spacy
import en_core_web_sm

nlp = spacy.load("en_core_web_sm")


def spacy_keyword_extract(text):
    result = []
    pos_tag = ['PROPN', 'NOUN', 'ADJ']
    doc = nlp(text.lower())
    for token in doc:
        if token.text in nlp.Defaults.stop_words or token.text in punctuation:
            continue
        if token.pos_ in pos_tag:
            result.append(token.text)

    return set(result)
