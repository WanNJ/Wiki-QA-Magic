from util import coref_resolution, dependency_parse as dep_parse, ner as NER, constituency_parse, tokenization
 

"""
interface for accessing util functions.ß
"""

def coref(text):
    """
    returns co reference resolved text
        :param text: Wiki text
    """
    coref_text = coref_resolution.resolve_spacy(text)
    #print(coref_text)
    return coref_text

def ner(text):
    """
    docstring here
        :param text: 
    """
    named_entities = NER.get_ner(text)
    return named_entities

def tokenize(text):
    """
    docstring here
        :param text: 
    """
    tokens = tokenization.tokenize_text(text)
    return tokens

def sentenize(text):

    sentences = tokenization.get_sentences(text)
    return sentences


def lemmatize(text):
    """
    docstring here
        :param text: 
    """
    pass
    #lemmatized_text = tokenization.tokenize_text(text)

def stem(text):
    """
    docstring here
        :param text: 
    """
    pass
    #stemmed_text = 

def constituency_parse(text):
    """
    docstring here
        :param text: 
    """
    pass

def dependency_parse(text):
    """
    docstring here
        :param text: 
    """
    dependencies = dep_parse.get_dependency_parse_spacy(text)
    #print(coref_text)
    return dependencies


if __name__ == '__main__':
    article = "This is an article about Evan Kaaret. He is 22, halfway to 23. This is to test if the program spacy will correctly found out that he refers to Evan."
    coref("My sister has a dog. She loves him.")


