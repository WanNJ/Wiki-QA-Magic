import re

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
    return text

if __name__ == "__main__":
    with open('/Users/gauravshegokar/Documents/CMU/FALL_2019/NLP/project/Wiki-QA-Magic/data/Development_data/set1/a1.txt', 'r') as content_file:
        content = content_file.read()
    print(clean_text(content))
