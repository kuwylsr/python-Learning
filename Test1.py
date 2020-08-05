#单独的小括号是元组turple
#单独的中括号是列表list
#单独的大括号是字典dict(key必须为不可变对象)
#set加一个小括号加一个中括号是集合set
#函数名其实就是指向一个函数对象的引用
#位置参数
#默认参数可以简化函数的调用,将参数变化较小的参数作为默认参数
#可变参数(只接收数个单个的参数)(这些可变参数在函数调用时自动组装为一个tuple,但传入不得不能是一个tuple)
#关键字参数(这些关键字参数在函数内部自动组装为一个dict，但传入的不能是一个dict)
#命名关键字参数
#为什么要发明命名关键字，这和普通的参数有区别吗

def power(x,n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

def calc(*number):
	sum = 0
	for n in number:
		sum = sum + n*n
	return sum


def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)

def person1(name,age,**kw):
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print('name:',name,'age:',age,'other:',kw)

def person2(name,age,*,gender,city):
	print('name:',name,'age:',age,'city:',city,'gender:',gender)

person2('LiSirui',21,gender='M',city='TangShan')


def product(x,*number):
	s = 1
	for y in number:
	    s = s * y
	return s*x

print(product(1,2,3,4))
