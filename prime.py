#l = [1,2,3,4,5,6,7,8,9,10]

# For Prime Numbers
def get_prime(l):
	for i in l:
		count = True
		if i == 2:
			print i
			continue
		for j in range(2, i):
			if i%j==0:
				count = False
				break
			else:pass
		if count:print i

# get_prime([5, 3, 6, 8])			



def check_prime(ele, count=False):
	if ele==2:return ele
	for j in range(2, ele):
		if ele%j==0:break
		else:
			count = True
	if count:return ele

# print filter(check_prime, [3, 5,4,2,6,7])


def check_prime_new(ele):
	if ele==2:return ele
	if False not in [True if ele%i!=0 else False for i in range(2, ele)]:
		return ele
# print filter(check_prime_new, [3, 5, 2, 6, 7])


def check_prime_new(ele):
	if ele==2:return ele
	if False not in map(lambda i: ele%i!=0, range(2, ele)):return ele
print filter(check_prime_new, range(10, 101))


# For fibonacci series
def fibo(number):
	a, b = 0, 1
	print a, b,
	count = 2
	for k in range(2, number):
		print a+b,
		a, b = b, a+b
# fibo(10)


# For Polyndrome - 1  

def check_polyndrome(ele):
	if str(ele) == str(ele)[::-1]:
		return "{0} is polyndrome".format(ele)
	else:
		return "{0} is not a Polyndrome".format(ele)
# print check_polyndrome(121)


# For Polyndrome - 2
'''
a = lambda x: str(x)==str(x)[::-1]
print a(112)
'''

