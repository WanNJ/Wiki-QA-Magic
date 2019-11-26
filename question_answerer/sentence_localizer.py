import sys

sys.path.append("..")

import util_service


def get_localized_statement(question, text):
    sentences = util_service.sentenize(text)

    cosines_sim_scores = []
    for sentence in sentences:
        cosines_sim_scores.append(util_service.get_cosine_similarity(question, sentence))

    localized_statement = str(sentences[cosines_sim_scores.index(max(cosines_sim_scores))])
    return localized_statement
