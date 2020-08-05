#python中的生成器

g = (x * x for x in range(10))
#可以用g 中自带的函数next来访问每一个元素next(g)
#也可以用循环（方便）
for n in g:
	print(n)
#===========================================================
#generator的函数，在每次调用next()的时候执行，
#遇到yield语句返回，再次执行从上次返回的yield语句处继续执行
#generator函数的“调用”实际返回一个generator对象
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'

for n in fib(6):
	print(n)

g = fib(6)
while True:
	try:
		x = next(g)
		print('g:',x)
	except StopIteration as e:
		print('Generator return value:',e.value)
		break
	#===========================================================
def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield(3)
	print('step 3')
	yield(5)

o = odd()
print(next(o))
print(next(o))
print(next(o))