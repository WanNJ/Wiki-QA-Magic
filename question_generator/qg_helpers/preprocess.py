import re
import sys

sys.path.append("../..")
import util_service


def remove_titles(text):
    lines = text.splitlines()
    new_lines = []
    for line in lines:
        if len(line.split()) < 4:
            # "discarding on length basis"
            continue
        pos_tokens = util_service.get_pos_tokens_only(line)
        if "VERB" not in pos_tokens:
            # "discarding on grammer basis"
            continue
        new_lines.append(line)

    return "\n".join(new_lines)


def clean_text(text):
    """
    removes non ascii keywords and content string inside along with brackets

        :param text: 
    """
    # try:
    #     text = text.encode("ascii", errors="ignore").decode()
    # except:
    #     print("error in parsing text - "+ text)
    #     pass

    text = re.sub(r'\([^)]*\)', '', text)
    text = re.sub(r' +', ' ', text)

    text = remove_titles(text)
    return text


if __name__ == "__main__":
    with open(
            '/Users/gauravshegokar/Documents/CMU/FALL_2019/NLP/project/Wiki-QA-Magic/data/Development_data/set1/a2.txt',
            'r') as content_file:
        content = content_file.read()
    print(clean_text(content))
