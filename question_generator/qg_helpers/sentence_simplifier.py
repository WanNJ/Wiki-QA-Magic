import sys
sys.path.append("../..")
import util_service

# TODO: break compound sentences
def simplify(text):
    sentences = util_service.sentenize(text)
    return sentences


if __name__ == "__main__":
    with open('/Users/gauravshegokar/Documents/CMU/FALL_2019/NLP/project/Wiki-QA-Magic/data/Development_data/set1/a1.txt', 'r') as content_file:
        text = content_file.read()
    simplify(text)
