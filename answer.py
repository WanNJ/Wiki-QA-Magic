#!/usr/bin/env python3

import sys
from question_answerer import qa_main


def generate_answers(wiki_text_block, questions):
    """
    returns a list of answers to the question based on the wiki text
        :param wiki_text_block: Wikipedia text
        :param questions: a list of questions to be answered
    """
    answers = []
    for question in questions:
        answers.append(qa_main.get_answer(wiki_text_block, question))
    return answers


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./answer article.txt questions.txt")
        sys.exit(1)

    article = sys.argv[1]
    questions = sys.argv[2]

    with open(article, 'r', encoding='utf8') as f:
        article_text = f.read()

    with open(questions, 'r', encoding='utf8') as f:
        questions_text = f.readlines()

    question_list = [q.strip() for q in questions_text]

    answers = generate_answers(article_text, questions_text)

    for answer in answers:
        print(answer)