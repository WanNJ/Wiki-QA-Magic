"""
This file must have at least 2 different implementations for constituency parse.

Add implementations of coref resolution from different tools.
We need to compare the accuracy from the different tools and choose the best one.
We can do the testing manually by checking the output of different implementations.
"""

#from stanfordnlp.server import CoreNLPClient
#import os



def get_constituency_parse_spacy(wiki_text_sent):
    """
    docstring here
        :param wiki_text_sent: 
    """
    pass

def get_constituency_parse_corenlp(wiki_text_sent):
    """
    docstring here
        :param wiki_text_sent: 
    """

    """
    env = os.environ
    with CoreNLPClient(annotators=['tokenize', 'ssplit', 'pos', 'lemma', 'ner', 'parse', 'depparse', 'coref'],
                   timeout=80000, memory='16G') as client:
        ann = client.annotate(text)
        sentence = ann.sentence[0]

        # get the constituency parse of the first sentence
        constituency_parse = sentence.parseTree

        # get the first subtree of the constituency parse
        #print(constituency_parse.child[0])

        # get the value of the first subtree
        #print(constituency_parse.child[0].value)
    """

def get_constituency_parse_othertool(wiki_text_sent):
    """
    docstring here
        :param wiki_text_sent: 
    """
    pass


