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


def generate_answer(wiki_text_block, question):
    """
    returns an answer to the question based on the wiki text
        :param wiki_text_block: Wikipedia text
        :param question: question to be answered
    """
    answer = qa_main.get_answer(wiki_text_block, question)
    return answer


if __name__ == "__main__":
    wiki_text_block = """Pittsburgh is a city in the state of Pennsylvania in the United States, and is the county seat of Allegheny County. A population of about 301,048 residents live within the city limits, making it the 66th-largest city in the US. The metropolitan population of 2,324,743 is the largest in both the Ohio Valley and Appalachia, the second-largest in Pennsylvania (behind Philadelphia), and the 27th-largest in the US. Pittsburgh is located in Pennsylvania. Pittsburgh was named in 1758 by General John Forbes, in honor of British statesman William Pitt, 1st Earl of Chatham."""

    # question = "What is Pittsburgh?"
    # question = "When was Pittsburgh named?"
    # question = "What is the county seat of Allegheny County?"
    # question = "What is located in the southwest of the state?"
    # question = "Where is Pittsburgh located?"
    # question = "Which city is 66th-largest city in the US?"
    # question = "Which city is located in the southwest of the state?"
    question = "Who named pittsburgh?"
    ans = generate_answer(wiki_text_block, question)
    print(ans)
