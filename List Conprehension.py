#列表解析或推导
lst = []
for x in range(1,10) :
    lst.append(x**2)

print (lst)

#列表解析
lst1 = [x**2 for x in range(1,10)]
print (lst1)
