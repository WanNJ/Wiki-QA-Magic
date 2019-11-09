import sys

sys.path.append("..")

import util_service


def get_localized_statement(question, coref_text):
    sentences = util_service.sentenize(coref_text)

    cosines_sim_scores = []
    for sentence in sentences:
        cosines_sim_scores.append(util_service.get_cosine_similarity(question, sentence))

    answer_statement = str(sentences[cosines_sim_scores.index(max(cosines_sim_scores))])
    return answer_statement
