from util import coref_resolution
from util import tokenization
from util import ner
from util import dependency_parse as dep_parse
from util import cosine_similarity
from util import pos

"""
interface for accessing util functions.
"""


def get_coref(text):
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


def get_tokenized_form(text):
    """
    docstring here
        :param text: 
    """
    tokens = tokenization.tokenize_text(text)
    return tokens


def sentenize(text):
    sentences = tokenization.get_sentences(text)
    return sentences


def get_cosine_similarity(question, sentence):
    cosine_sim_score = cosine_similarity.get_cosine_similarity_spacy(question, sentence)
    return cosine_sim_score


def get_lemmatize_form(text):
    """
    docstring here
        :param text: 
    """
    pass


def get_stem_form(text):
    """
    docstring here
        :param text: 
    """
    pass


def get_constituency_parse(text):
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


def get_dep_parse_tree_Evan(text):
    """
    Used to get the heads and children for text
    """
    dependency_parse_tree = dep_parse.get_dep_parse_head_children(text)
    return dependency_parse_tree


def get_dep_parse_tree(text):
    """
    Nianjie added this function because the get_dependency_parse only returns the dependency tags but not relations.
        :param text: the text that needs to be parsed.
    """
    dependency_parse = dep_parse.get_dep_parse_tree_spacy(text)
    return dependency_parse


def get_pos(text):
    # spacy's implementation
    res = pos.get_pos_spacy(text)
    return res


def get_pos_tokens_only(text):
    # spacy's implementation
    res = pos.get_pos_tokens_only_spacy(text)
    return res


if __name__ == '__main__':
    get_coref("My sister has a dog. She loves him.")
