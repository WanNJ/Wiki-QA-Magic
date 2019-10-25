from util import coref_resolution
from util import tokenization
from util import ner
from util import dependency_parse as dep_parse
from util import cosine_similarity

"""
interface for accessing util functions.
"""

def coref(text):
    """
    returns co reference resolved text
        :param text: Wiki text
    """
    coref_text = coref_resolution.resolve_spacy(text)
    return coref_text

def get_ner(text):
    """
    docstring here
        :param text: 
    """
    named_entities = ner.get_ner_spacy(text)
    return named_entities

def get_ner_per_token(text):
    """
    docstring here
        :param text: 
    """
    named_entities = ner.get_ner_per_token_spacy(text)
    return named_entities

def tokenize(text):
    """
    docstring here
        :param text: 
    """
    pass

def sentenize(text):
    sentences = tokenization.get_sentences(text)
    return sentences


def get_cosine_similarity(question, sentence):
    cosine_sim_score = cosine_similarity.get_cosine_similarity_spacy(question, sentence)
    return cosine_sim_score


def lemmatize(text):
    """
    docstring here
        :param text: 
    """
    pass

def stem(text):
    """
    docstring here
        :param text: 
    """
    pass

def constituency_parse(text):
    """
    docstring here
        :param text: 
    """
    pass

def get_dependency_parse(text):
    """
    docstring here
        :param text: 
    """
    dependency_parse = dep_parse.get_dependency_parse_spacy(text)
    return dependency_parse


if __name__ == '__main__':
    coref("My sister has a dog. She loves him.")