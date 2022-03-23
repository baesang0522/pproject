from rake_nltk import Rake
import nltk


def rake_keyword_extract(text):
    nltk.download('stopwords')
    rake_nltk_var = Rake()
    rake_nltk_var.extract_keywords_from_text(text)
    keyword_extracted = rake_nltk_var.get_ranked_phrases()

    return keyword_extracted


