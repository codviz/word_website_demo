def create_dict():

    most_used_file = open(r"data/most_used_words.txt","r")
    most_used_content = most_used_file.read()
    most_used_list = most_used_content.split()

    analysis_words_file = open(r"data/changemeanings_emotion.csv","r")
    analysis_words_dictionary = {}
    line = analysis_words_file.readline()
    while True:
        if analysis_words_file.readline():
            line_list = line.split(',')
            if line_list[1] in most_used_list:
                analysis_words_dictionary[line_list[1]] = line_list[2:]
            line = analysis_words_file.readline()
        else:
            break

    most_used_file.close()
    analysis_words_file.close()
    
    return analysis_words_dictionary