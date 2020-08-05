# 打印给定字符串中元音的个数

def vowels_count(string) :
    ret = 0
    for c in string :
        if c in 'aeiouAEIOU' :
            ret += 1

    return ret

print (vowels_count("lisirui"))

