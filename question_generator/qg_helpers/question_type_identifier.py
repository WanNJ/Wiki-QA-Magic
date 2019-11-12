from question_generator.qg_helpers import qg_constants
import sys
sys.path.append("../..")

import util_service

def get_possible_question_types(sentences):
    """
    Based on the NER entities identifies possible questions to be generated 
        :param sentence: 
    """
    q_types_list = []

    for sentence in sentences:
        # sentence = sentences[19]
        q_types = []

        sent_tokens = util_service.get_tokenized_form(sentence)
        sent_tokens = [s.lower() for s in sent_tokens]
        if ("is" in sent_tokens
            or "was" in sent_tokens
            or "were" in sent_tokens
            or "are" in sent_tokens):
            q_types.append(qg_constants.WHAT_QUESTION)
            q_types.append(qg_constants.IS_QUESTION)
        if "as a" in sentence.lower():
            q_types.append(qg_constants.WHAT_QUESTION)
        if (("is" in sent_tokens
            or "was" in sent_tokens
            or "were" in sent_tokens
            or "are" in sent_tokens)
            and "or" in sent_tokens):
            q_types.append(qg_constants.EITHER_OR_QUESTION)
            
        
        # util_service.get_ner_per_token(sentence)

        sent_ner = util_service.get_ner(sentence)
        
        # Where type
        for entry in sent_ner:
            if entry[3] in ["LOC", "ORG"]:
                if qg_constants.WHERE_QUESTION not in q_types:
                    q_types.append(qg_constants.WHERE_QUESTION)

        for entry in sent_ner:
            if entry[3] in ["DATE", "TIME"]:
                if qg_constants.WHEN_QUESTION not in q_types:
                    q_types.append(qg_constants.WHEN_QUESTION)

        for entry in sent_ner:
            if entry[3] in ["PERSON", "ORG", "NORP"]:
                if qg_constants.WHO_QUESTION not in q_types:
                    q_types.append(qg_constants.WHO_QUESTION)

        for entry in sent_ner:
            if entry[3] in ["CARDINAL"]:
                if qg_constants.HOWMANY_QUESTION not in q_types:
                    q_types.append(qg_constants.HOWMANY_QUESTION)
                    
        for entry in sent_ner:
            if entry[3] in ["QUANTITY", "MONEY", "PERCENT"]:
                if qg_constants.HOWMANY_QUESTION not in q_types:
                    q_types.append(qg_constants.HOWMANY_QUESTION)
                    
        for entry in sent_ner:
            if entry[3] in ["FAC"]:
                if qg_constants.WHAT_QUESTION not in q_types:
                    q_types.append(qg_constants.WHAT_QUESTION)
        q_types_list.append(q_types)

    return q_types_list














