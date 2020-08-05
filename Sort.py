# 排序函数，按指定内容进行排序
students = [["zhang",84],["li",22],["zhao",100]]

def f(a) :
    return a[1]

students.sort(key= f , reverse = True)

print (students)

#匿名函数
students.sort(key= lambda x:x[1],reverse =False)
print (students)
