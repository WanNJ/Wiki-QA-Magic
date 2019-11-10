"""
This file must have 3 different implementations for coreferenc resolution.

Add implementations of coref resolution from different tools. As of now I have only from added Spacy. 
We need to compare the accuracy from the different tools and choose the best one.
We can do the testing manually by checking the output of different implementations.
"""

import spacy
import neuralcoref
nlp = spacy.load("en")#("en_core_web_sm")
neuralcoref.add_to_pipe(nlp)


def resolve_spacy(text):
    """
    returns coref resolution text from spacy implementation
        :param text: wiki text
    """
    doc = nlp(text)
    return doc._.coref_resolved


def sample_use_spacy():
    doc = nlp('My sister has a dog. She loves him.')
    print(doc._.coref_resolved)
    # Prints -> My sister has a dog. My sister loves a dog.
