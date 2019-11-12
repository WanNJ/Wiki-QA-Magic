
def get_questions_by_no(question_list, no_of_questions):
    """
    return questions based on the no_of_questions, duplicates last question if 
    questions are not sufficient
        :param question_list: 
        :param no_of_questions: 
    """
    if len(question_list) == 0:
        return question_list

    if len(question_list) == no_of_questions:
        return question_list
    
    if len(question_list) > no_of_questions:
        return question_list[:no_of_questions]
    
    while len(question_list) != no_of_questions:
        question_list.append(question_list[-1])
    return question_list
