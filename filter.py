from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

from profanity_filter import ProfanityFilter


class Filter:
    def __init__(self):
        self.stemmer = PorterStemmer()

    def process(self, text):
        for word in text.split(' '):
            self.direct_match(word)
            self.levenshtein_distance(word)
        pass

    # tokenize, stem, then compare to work list
    def direct_match(self, word):
        pass

    def calc_levenshtein_distance(self, word):
        pass

    def convert_leetspeak(self, word):
        pass

    # tokenize, stem, etc.
    def sanitize_text(self, text):
        token_words = word_tokenize(text)

        stemmed_text = []
        for word in token_words:
            stemmed_text.append(self.stemmer.stem(word))
            stemmed_text.append(' ')

        sanitized_text = "".join(stemmed_text)
        return sanitized_text


text = 'this is a damn profanity test'

filter = Filter()
filter.process(text)
