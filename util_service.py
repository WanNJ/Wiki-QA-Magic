from util import coref_resolution

"""
interface for accessing util functions.ß
"""

def coref(text):
    """
    returns co reference resolved text
        :param text: Wiki text
    """
    coref_text = coref_resolution.resolve_spacy(text)
    print(coref_text)
    return coref_text

def ner(text):
    """
    docstring here
        :param text: 
    """
    pass

def tokenize(text):
    """
    docstring here
        :param text: 
    """
    pass

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

def dependency_parse(text):
    """
    docstring here
        :param text: 
    """
    pass


if __name__ == '__main__':
    coref("My sister has a dog. She loves him.")