#python可以迭代没有下标的对象
#=============================================
#1--迭代dict
d = {'a':1,'b':2,'c':3}
for key in d:
	print(key)

#迭代value值
for value in d.values():
	print(value)

#同时迭代key值和value值
for k,v in d.items():
	print(k,":",v)

#2--迭代str
for ch in 'ABC':
	print(ch)
#==============================================
#判断一个对象是否可迭代
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))

#==============================================
#实现下标循环迭代
for i,value in enumerate(['A','B','C']):
	print(i,value)
#python可以同时引用两个变量进行循环迭代
for x,y in [(1,1),(2,4),(3,9)]:
	print(x,y)