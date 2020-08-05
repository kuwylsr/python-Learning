#列表生成式
#=================================================
#生成简单的List
print(list(range(1,11)))

#生成较为复杂的List
#1--用循环的方式（麻烦且复杂）
L = []
for x in range(1,11):
	L.append(x * x)
print(L)
#2--用列表生成式
L = [x * x for x in range(1,11)]
print(L)
#带有条件的列表生成式
L = [x * x for x in range(1,11) if x%2 == 0]
print(L)
#双层列表生成式
L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)
#==================================================

#因为循环可以有两个甚至多个变量，所以列表生成式也可以使用两个变量来生成
d = {'x':1,'y':2,'z':3,'t':4}
L = [k + ':' + 'v' for k,v in d.items()]
print(L)

#将list中所有的字符串变成小写
L = ['Hello','World','IBM','Apple']
L1 = [s.lower() for s in L]
print(L1)