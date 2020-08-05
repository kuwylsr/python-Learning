#正向最大匹配分词

def load_dic(filename):
    f = open(filename)
    word_dic = set()
    max_length = 1
    for line in f:
        word = line.strip()
        word_dic.add(word)
        if len(word) > max_length:
            max_length = len(word)
    return max_length , word_dic

def fmm_word_seg(sentence,word_dic,max_length):
    begin = 0
    words = []

    while begin < len(sentence):
        for end in range(min(begin + max_length , len(sentence)),begin,-1):
            word = sentence[begin:end]
            if word in word_dic or end == begin + 1 :
                words.append(word)
                break
            begin = end
        return words

max_length , word_dic = load_dic('lexicon.txt')
words = fmm_word_seg(input(),word_dic,max_length)
for word in words:
    print(word)

