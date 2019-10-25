import sys
sys.path.append("..")
import util_service

def get_answer(question, localized_statement):
    """
    gets answer to the binary question
    TODO: HOW?
    """
    print(question)
    print(util_service.get_dependency_parse(question))
    print(localized_statement)
    print(util_service.get_dependency_parse(localized_statement))
