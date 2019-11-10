import sys
sys.path.append("..")
import util_service

import numpy as np

"""
def make_question(coref_text, tokenized_text_coref, parsing, named_entities, sentence, named_entity_index):
    entity = named_entities[named_entity_index][0]
    entity_type = named_entities[named_entity_index][3]
    if entity_type == "PERSON":
        wh_word = "Who"
    elif entity_type == "ORG":
        wh_word = "What"
    #elif 
    start_i = named_entities[named_entity_index][1]
    end_i = named_entities[named_entity_index][2]
    new_text = sentence[0:start_i] + wh_word + sentence[end_i:len(sentence)-1] + "?"
    question = new_text
    return question
"""

def make_wh_question(curr_sent, ents_in_sent):
    """
    generates a wh question based a sentence and named entity.
    right now just puts a wh word in place of the named entity
        :param curr_sent: string representing a sentence
        :param ents_in_sent: list of a named entity, where:
            [0] is a string of the entity
            [1] is the index where the entity starts in the sentence
            [2] is the index where the entity ends in the sentence
            [3] is the type of the named entity (ie, "PERSON", "ORG", etc...)
    """

    
    # Version 1, just replaces the NER with a wh word
    entity = ents_in_sent[0]
    entity_type = ents_in_sent[3]
    if entity_type == "PERSON":
        wh_word = "Who"
    elif entity_type == "ORG":
        wh_word = "What"
    elif entity_type == "CARDINAL":
        wh_word = "What"
    elif entity_type == "DATE":
        wh_word = "What"
    elif entity_type == "ORG":
        wh_word = "What" 
    start_i = ents_in_sent[1]
    end_i = ents_in_sent[2]
    question = curr_sent[0:start_i] + wh_word + curr_sent[end_i:len(curr_sent)-1] + "?"
    return question


"""
def make_wh_quest_swap(curr_sent, parsing, tokenized_sent):
    new_tok_sent = tokenized_sent
    for nsubj_i, parse_val in enumerate(parsing):
        if parse_val == "nsubj": # The subject of the sentence
            # check the named entities for type of entity
            new_tok_sent[nsubj_i] = "WH" # "WH" is a placeholder for now instead of actual wh word
        if parse_val == "pobj": # The object of the sentence
"""




def get_questions(wiki_text, no_of_questions):
    """
    generates the questions based on the wiki text.
    Contains only business logic, WHAT to do rather than HOW to do.
    Common helper functions to be accessed from util_service module.
        :param wiki_text: string of a wikipedia article
        :param no_of_questions: int for number of questions
    """
    
    # 1. coref resolution
    # 2. tokenization, lemma, stem --> we will decide later
    # 3. parsing dependency, constituency --> weigh adv disadv 
    # 4. Question generation logic  
        # dependency parse
        # other ways
    # 5. get ranking from question evaluator for generated questions
    # 6. return ranked questions

    coref_text = util_service.get_coref(wiki_text)
    sentences = util_service.sentenize(coref_text)

    questions = []
    sentence_num = 0

    """
    for i in range(no_of_questions):
        if sentence_num < len(sentences):
            curr_sent = str(sentences[sentence_num])
            parsing = util_service.dependency_parse(curr_sent)
            tokenized_sent = util_service.tokenize(curr_sent)
            #ents_in_sent = util_service.ner(curr_sent)
            wh_question = make_wh_quest_swap(curr_sent, parsing, tokenized_sent)
            questions.append(wh_question)
            sentence_num += 1
    """

    
    # Version 1, NER
    sentence_num = 0
    for i in range(no_of_questions):
        # This will only generate as many questions as there are NER in sentences
        if sentence_num < len(sentences):
            # For each sentence, get the entities, tokens, and parse of the sentence
            curr_sent = str(sentences[sentence_num])
            ents_in_sent = util_service.get_ner(curr_sent)
            tokenized_text_coref = util_service.get_tokenized_form(curr_sent)
            #tokenized_original = util_service.tokenize(wiki_text)
            parsing = util_service.get_dependency_parse(curr_sent)
            named_ent_num = 0
            # For each entity in the sentence, make a wh question
            while named_ent_num < len(ents_in_sent):
                wh_question = make_wh_question(curr_sent, ents_in_sent[named_ent_num])
                questions.append(wh_question)
                named_ent_num += 1
            sentence_num += 1
    
        

    
    #tokenized_text_coref = util_service.tokenize(coref_text)
    #tokenized_original = util_service.tokenize(wiki_text)
    #parsing = util_service.dependency_parse(coref_text)
    #named_entities = util_service.ner(coref_text)
    #named_entities_annot = util_service.ner

    #print()
    #print("COREF: ", coref_text)
    #print()
    #print("TOKEN COREF: ", tokenized_text_coref)
    #print()
    #print("TOKEN ORIG: ", tokenized_original)
    #print()
    #print("PARSE: ", parsing)
    #print()
    #print("ENTITY: ", named_entities)
    #print()

    #tokenized_text_coref_np = np.asarray(tokenized_text_coref)
    #print(tokenized_text_coref_np)
    #print(named_entities[0][0])
    # For 2 part names (like Evan Kaaret instead of Evan), can go through named_entities and search 
    # for where tokenized_text_coref_np == first name, then again where tokenized_text_coref_np == last name
    #print(np.where(tokenized_text_coref_np == named_entities[0][0]))
    """
    question = make_question(coref_text, tokenized_text_coref, parsing, named_entities, sentences, named_entity_index = 0)
    
    questions = []
    named_entity_index = 0
    for i in range(no_of_questions):
        if named_entity_index < len(named_entities):
            question = make_question(coref_text, tokenized_text_coref, parsing, named_entities, sentences, named_entity_index = 0)
        questions.append(question)
    """

    return questions
    

if __name__ == "__main__":

    #print(get_questions("This is an article about Evan Kaaret. He is 22, halfway to 23. This is to test if the program spacy will correctly found out that he refers to Evan.", 1))
    print(get_questions("President Evan is the subject of this article. He is 22, halfway to 23. This is to test if the program spacy will correctly found out that he refers to Evan.", 4))
    #print(get_questions("Who is that.", 1))