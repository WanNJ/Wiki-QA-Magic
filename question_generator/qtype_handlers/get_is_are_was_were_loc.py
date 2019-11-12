
def which_acomp(ner_tokens_sentence):
    # print(ner_tokens_sentence)
    final_flag = ""
    is_are_index = 0
    is_flag = False
    are_flag = False
    was_flag = False
    were_flag = False
    for i in range(len(ner_tokens_sentence)):
        if ner_tokens_sentence[i][0] == "is":
            is_are_index = i
            is_flag = True
            are_flag = False
            was_flag = False
            were_flag = False
            break # break for now, could continue to find more questions
        elif ner_tokens_sentence[i][0] == "are":
            is_are_index = i
            is_flag = False
            are_flag = True
            was_flag = False
            were_flag = False
            break # break for now, could continue to find more questions
        elif ner_tokens_sentence[i][0] == "was":
            is_are_index = i
            is_flag = False
            are_flag = False
            was_flag = True
            were_flag = False
            break # break for now, could continue to find more questions
        elif ner_tokens_sentence[i][0] == "were":
            is_are_index = i
            is_flag = False
            are_flag = False
            was_flag = False
            were_flag = True
            break # break for now, could continue to find more questions

    if is_flag: final_flag = "Is "
    elif are_flag: final_flag = "Are "
    elif was_flag: final_flag = "Was "
    elif were_flag: final_flag = "Were "
    return (final_flag, is_are_index)
