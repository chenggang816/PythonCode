def str2int(s):
	def char2num(c):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]
	return reduce(lambda x,y:x*10+y,map(char2num,s))
print str2int('123')

def primaryUpper(L):
	def firstUpper(w):
		if len(w) < 1:
			return w
		return w[0].upper() + w[1:].lower()
	return map(firstUpper,L)
print primaryUpper(['aBC','ChengGang','c',''])

def prod(L):
	return reduce(lambda x,y:x*y, L)
print prod([1,2,3,4])