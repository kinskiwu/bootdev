import json
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

def remove_punctuation(text: str):
    if len(text) == 0:
        return ""

    translator = str.maketrans("", "", string.punctuation)

    return text.translate(translator)

def cleanse_text(text: str) -> str:
    if len(text) == 0:
        return ""

    text = text.lower()
    text = remove_punctuation(text)
    words = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    stemmer = PorterStemmer()
    clean_words = []

    for word in words:
        if word not in stop_words and word.isalpha():
            clean_words.append(stemmer.stem(word))

    return " ".join(clean_words)

def search_movies(query: str) -> list:
    query_tokens = cleanse_text(query).split(" ")
    if len(query_tokens) == 0:
        return []

    with open("data/movies.json", "r") as file:
        data = json.load(file)

    result = []
    for token in query_tokens:
        for movie in data["movies"]:
            if token in cleanse_text(movie["title"]):
                result.append(movie)

    return result
