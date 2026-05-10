def count_words(sentence):
    # replace is a nice tool in word splitting 

    sentence = sentence.lower()
    sentence = sentence.replace(",", " ")
    sentence = sentence.replace(".", " ")
    sentence = sentence.replace("?", " ")
    sentence = sentence.replace("!", " ")
    sentence = sentence.replace(":", " ")
    sentence = sentence.replace("_", " ")
    sentence = sentence.replace("-", " ")
    sentence = sentence.replace("\"", " ")
    sentence = sentence.replace("&", " ")
    sentence = sentence.replace("$", " ")
    sentence = sentence.replace("%", " ")
    sentence = sentence.replace("^", " ")
    sentence = sentence.replace("&", " ")
    sentence = sentence.replace("@", " ")

    word_list = sentence.split()
    count = len(word_list)

    for i in range(count):
        word_list[i] = word_list[i].strip("\'")

    histogram = {}
    for word in word_list:
        if word == "":
            continue
        histogram[word] = histogram.get(word, 0) + 1

    print(histogram)
    return histogram
