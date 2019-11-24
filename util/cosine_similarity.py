import spacy


nlp = spacy.load("en_core_web_lg")


def get_cosine_similarity_spacy(text_1, text_2):
    doc1 = nlp(text_1)
    doc2 = nlp(str(text_2))
    return doc1.similarity(doc2)

