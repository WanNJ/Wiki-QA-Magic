"""
This file must have implementations for tokenization lemmatization and stemming
"""


# from stanfordcorenlp import StanfordCoreNLP
# import stanfordnlp

# from spacy.tokenizer import Tokenizer
# from spacy.lang.en import English
# nlp = English()

import spacy

nlp = spacy.load("en_core_web_lg")



def tokenize_text(wiki_text):
    """
    returns a list of tokens from a wikipedia article
        :param wiki_text: wikipedia article
    """

    # tokenizer = nlp.Defaults.create_tokenizer(nlp)
    # tokens = tokenizer(wiki_text)


    document = nlp(wiki_text)
    tokens = []
    for token in document:
        tokens.append(token.text)
    return tokens


def lemmatize_text(wiki_text):
    """
    docstring here
        :param wiki_text: 
    """
    document = nlp(wiki_text)
    tokens = []
    for token in document:
        tokens.append(token.lemma_)
    return tokens
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
        sentences.append(str(sentence))
    return sentences

