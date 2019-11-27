import os
import sys

sys.path.append("..")
from question_answerer import qa_main

data_folder_path = "./data"


def read_file(filepath):
    with open(filepath, 'r') as content_file:
        content = content_file.read()
    return content


def get_fixture():
    test_suite = {}
    subfolders = [f.path for f in os.scandir(data_folder_path) if f.is_dir()]
    for folder_path in subfolders:
        folder_name = os.path.basename(folder_path)

        article_path = os.path.join(folder_path, "article.txt")
        questions_path = os.path.join(folder_path, "questions.txt")
        answers_path = os.path.join(folder_path, "answers.txt")

        article = read_file(article_path)
        questions = read_file(questions_path).splitlines()
        answers = read_file(answers_path).splitlines()
        answers = [a.split(" || ") for a in answers]

        test_suite[folder_name] = {
            "article": article,
            "questions": questions,
            "answers": answers
        }

    return test_suite


# TODO:  Add text similarity for partially correct answers
def is_correct_answer(ground_truth, predicted_answers):
    ground_truth = [a.lower().strip() for a in ground_truth]
    if predicted_answers.lower().strip() in ground_truth:
        return True

    if predicted_answers[-1] == ".":
        if predicted_answers[:-1].lower().strip() in ground_truth:
            return True

    return False


def is_partial_correct_answer(ground_truth, predicted_answers):
    ground_truth = [a.lower().strip() for a in ground_truth]
    for g in ground_truth:
        if g in predicted_answers.lower():
            return True
    return False


def pretty(d, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            pretty(value, indent + 1)
        else:
            print('\t' * (indent + 1) + str(value))


if __name__ == "__main__":
    test_suite = get_fixture()
    results = {}
    correct_counter = 0
    incorrect_counter = 0
    p_correct_counter = 0
    failed_cases = {}
    partial_cases = {}

    for key, val in test_suite.items():
        predicted_answers = qa_main.get_answers(
            val["article"], val["questions"])
        correct_answers = val["answers"]

        for i in range(0, len(correct_answers)):
            if is_correct_answer(correct_answers[i], predicted_answers[i]):
                correct_counter += 1
            elif is_partial_correct_answer(correct_answers[i], predicted_answers[i]):
                p_correct_counter += 1
                if key not in partial_cases:
                    partial_cases[key] = {}
                q_key = "q." + str(i + 1)
                partial_cases[key][q_key] = {}
                partial_cases[key][q_key]["question"] = val["questions"][i]
                partial_cases[key][q_key]["ground_truth"] = val["answers"][i]
                partial_cases[key][q_key]["predicted_answer"] = predicted_answers[i]
            else:
                incorrect_counter += 1
                if key not in failed_cases:
                    failed_cases[key] = {}
                q_key = "q." + str(i + 1)
                failed_cases[key][q_key] = {}
                failed_cases[key][q_key]["question"] = val["questions"][i]
                failed_cases[key][q_key]["ground_truth"] = val["answers"][i]
                failed_cases[key][q_key]["predicted_answer"] = predicted_answers[i]

    total_cases = correct_counter + incorrect_counter + p_correct_counter
    report = {
        "accuracy": correct_counter / total_cases,
        "partial_accuracy": (correct_counter+p_correct_counter)/total_cases,
        "correct_answers": correct_counter,
        "partial_correct_answers": p_correct_counter,
        "incorrect_answers": incorrect_counter,
        "test_cases": total_cases,
        "articles_tested": len(test_suite),
        "partial_correct_cases": partial_cases,
        "failed_cases": failed_cases
    }

    # print(report)
    pretty(report)
    # print(json.dumps(report, indent=4))
