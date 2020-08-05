L = ['Michael','Sarah','Tracy','Bob','Jack']

#取出前n个元素

#笨方法
print([L[0],L[1],L[2]])

#循环的方式
r = []
n = 3
for i in range(n):
	r.append(L[i])
print(r)

#用切片的方式(！！！！注意切片切出来的一定是从前往后排列)
print(L[0:3]) #从下标0开始，直到3不包括3的元素
print(L[:3])#0可以省略

print(L[-5:-2])#倒数第一个元素的下标是-1


#切片的应用
L = list(range(101))#生成0-100的整数，并放入一个list
print(L[:10])#取出前10个数
print(L[-10:])#取出后10个数
print(L[10:20])#前11-20个数

print(L[:10:2])#前10个数，每隔两个取一个
print(L[::5])#所有数，每隔5个取一个

print(L[:])#一样的list

#tuple也可以使用切片操作
print( (0,1,2,3,4,5)[:3] )

#字符串也可以看成是一种list，也同样可是使用切片操作
print( 'ABCDEFG'[:3] )
print( 'ABCDEFG'[::2] )
