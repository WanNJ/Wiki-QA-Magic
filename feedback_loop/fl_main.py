# TODO
# pipeline for feedback loop

from question_answerer import qa_main

def get_answerable_questions(wikitext, question_list):
    answerable_question_list = []
    return question_list

    answers = qa_main.get_answers(wikitext, question_list)

    for i, ans in enumerate(answers):
        if ans != "I don't know the answer.":
            answerable_question_list.append(question_list[i])
        else:
            # print("*-==-=-")
            # print("QE dropping unanswerable question - ", question_list[i])
            # print("*-==-=-")
            pass

    return answerable_question_list
