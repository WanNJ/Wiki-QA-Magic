# TODO
# pipeline for question evaluator
from question_generator.qg_helpers import postprocess
from feedback_loop import fl_main

def get_questions_by_qg_ranking(questions_dict):
    question_list = []
    question_list += questions_dict["is_wh_generator"]
    question_list += questions_dict["when_generator"]
    question_list += questions_dict["what_generator"]
    question_list += questions_dict["is_generator"]
    question_list += questions_dict["eo_generator"]
    question_list += questions_dict["howmany_generator"]
    question_list += questions_dict["where_generator"]
    return question_list

def get_absolute_questions(questions_dict):
    question_list = []
    question_list += questions_dict["is_wh_generator"]
    question_list += questions_dict["when_generator"]
    return question_list

def filter_by_word_length(question_list):
    # magic numbers -> to be revised later based on the results
    MIN_WORD_LENGTH = 4
    MAX_WORD_LENGTH = 23

    filtered_question_list = []
    for q in question_list:
        if len(q.split()) < MIN_WORD_LENGTH:
            # "discarding on min length basis"
            # print("-=-==-=-=- discarding on min length basis =-=-=-==-")
            # print(q)
            # print("-=--=-=-=-=-=-=-")
            continue
        if len(q.split()) > MAX_WORD_LENGTH:
            # "discarding on max length basis"
            # print("-=-==-=-=- discarding on max length basis =-=-=-==-")
            # print(q)
            # print("-=--=-=-=-=-=-=-")
            continue
        filtered_question_list.append(q)
    return filtered_question_list

def evaluate_questions(wiki_text, questions_dict):

    # rank by question generator ranking
    question_list = get_questions_by_qg_ranking(questions_dict)
    
    # remove duplicates
    question_list = postprocess.remove_duplicates_keep_order(question_list)

    # removing questions based on question length
    question_list = filter_by_word_length(question_list)

    # evaluate questions with feedback_loop
    # only the questions are kept which could be answered by answering system
    try:    
        question_list = fl_main.get_answerable_questions(wiki_text, question_list)
    except:
        pass
    # temp fix for avoiding absolute_questions from well performing generators
    # absolute_questions = get_absolute_questions(questions_dict)
    # question_list = absolute_questions + question_list
    # question_list = postprocess.remove_duplicates_keep_order(question_list)
    # question_list = filter_by_word_length(question_list)

    return question_list
