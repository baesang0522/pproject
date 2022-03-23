import yake


def yake_keyword_extract(text):
    kw_extractor = yake.KeywordExtractor(lan="en", n=3, dedupLim=0.3, top=20, features=None)
    keywords = kw_extractor.extract_keywords(text)

    return keywords
