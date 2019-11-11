
def filter(sentences):
    filtered_sentences = []
    for sentence in sentences:
        if len(sentence.split()) > 5 and len(sentence.split()) <= 25:
            filtered_sentences.append(sentence)
    
    # TODO: do some other magic
    return filtered_sentences