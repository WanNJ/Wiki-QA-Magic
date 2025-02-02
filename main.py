from question_answerer import qa_main
from question_generator import qg_main


def generate_questions(wiki_text_block, no_of_questions):
    """
    generates the questions based on the wiki text and returns the no of 
    questions based on the no_of_questions parameter
        :param wiki_text_block: Wikipedia text
        :param no_of_questions: no of questions to be generated by the generator
    """

    questions = qg_main.get_questions(wiki_text_block, no_of_questions)

    # map questions list to no_of_questions
    return questions


def generate_answer(wiki_text_block, questions):
    """
    returns answers to the questions based on the wiki text
        :param wiki_text_block: Wikipedia text
        :param question: questions to be answered, type list
    """
    answers = qa_main.get_answers(wiki_text_block, questions)
    return answers


if __name__ == "__main__":
    # wiki_text_block = """Pittsburgh is a city in the state of Pennsylvania in the United States, and is the county seat of Allegheny County. A population of about 301,048 residents live within the city limits, making it the 66th-largest city in the US. The metropolitan population of 2,324,743 is the largest in both the Ohio Valley and Appalachia, the second-largest in Pennsylvania (behind Philadelphia), and the 27th-largest in the US. Pittsburgh is located in Pennsylvania."""
    wiki_text_block = """Pittsburgh is a city in the state of Pennsylvania in the United States, and is the county seat of Allegheny County. Pittsburgh is the 66th-largest city in the US. There are 2,000,152 people that live in the city. Pittsburgh is located in Pennsylvania."""

    # question = "What is Pittsburgh?"
    print("WH------------------------------------------------")

    # question = "What is county seat of Allegheny County?"
    # question = "Which city is 66th-largest city in the US?"
    question = ["Where is Pittsburgh located?"]
    # question = "Which city is located in the southwest of the state?"
    # question = "What is located in the southwest of the state?"
    ans1 = generate_answer(wiki_text_block, question)
    print("WH ANSWER: ", ans1)

    print("BINARY------------------------------------------------")
    question2 = ["Is Pittsburgh the county seat?"]
    ans2 = generate_answer(wiki_text_block, question2)
    print("BINARY ANSWER: ", ans2)

    print("EO------------------------------------------------")
    question3 = ["Is Pittsburgh a city or a state?"]
    ans3 = generate_answer(wiki_text_block, question3)
    print("EO ANSWER: ", ans3)

    print("EO------------------------------------------------")
    question3 = ["Is Pittsburgh in the United States or Pennsylvania?"]
    ans3 = generate_answer(wiki_text_block, question3)
    print("EO ANSWER: ", ans3)
