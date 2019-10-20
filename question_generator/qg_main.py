import sys
sys.path.append("..")
import util_service

def get_questions(wiki_text):
    """
    generates the questions based on the wiki text.
    Contains only business logic, WHAT to do rather than HOW to do.
    Common helper functions to be accessed from util_service module.

        :param wiki_text: wikipedia article
    """
    
    # 1. coref resolution
    # 2. tokenization, lemma, stem --> we will decide later
    # 3. parsing dependency, constituency --> weigh adv disadv 
    # 4. Question generation logic  
        # dependency parse
        # other ways
    # 5. get ranking from question evaluator for generated questions
    # 6. return ranked questions
    
    return []

if __name__ == "__main__":
    print("")