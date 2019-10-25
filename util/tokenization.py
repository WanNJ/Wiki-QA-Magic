
"""
This file must have implementations for tokenization lemmatization and stemming
"""

import spacy
nlp = spacy.load("en_core_web_lg")

def tokenize_text(wiki_text):
    """
    docstring here
        :param wiki_text: 
    """
    pass

def lemmatize_text(wiki_text):
    """
    docstring here
        :param wiki_text: 
    """
    pass

def stem_text(wiki_text):
    """
    docstring here
        :param wiki_text: 
    """
    pass

def get_sentences(wiki_text):
    """
    gets the sentences of a wikipedia article, with each sentence in a list
        :param wiki_text: wikipedia article 
    """
    document = nlp(wiki_text)
    sentences = []
    for sentence in document.sents:
        sentences.append(sentence)
    return sentences