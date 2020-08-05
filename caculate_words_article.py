#统计文章中常见的单词

import matplotlib.pyplot as plt
f = open("article.txt")
word_freq = {}
for line in f:
    words = line.split()
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

word_freq_lst = []
for word, freq in word_freq.items():
    word_freq_lst.append((freq,word))

word_freq_lst.sort(reverse=True)

for freq, word in word_freq_lst[:10]:
    print(word, freq)

y = [i[0] for i in word_freq_lst[:20]]
words = [i[1] for i in word_freq_lst[:20]]
x_pos = range(len(words))

plt.bar(x_pos,y)
plt.xticks(x_pos,words)
plt.show()
