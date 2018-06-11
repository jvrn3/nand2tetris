x = {'SP': 0, 'LCL': 1, 'ARG': 2,
		'THIS': 3, 
		'THAT': 4,
		}
for i in range(16):
	x["R" + str(i)] = i

x['SCREEN'] = 16384
x['KBD'] = 24576
def symbol(str):
	i = 0
	for t in str.split():
		if(t[0] != '@' and t[0] != '('):
			dest = t.split("=")[0]
			if(dest[0] != '/'):
				i+=1
		else:
			if(t[0] == '@'):
				i+=1
			if(t[0] == '('):
				print("aaa")
				x[t[1:len(t)-1]] = i
	return x
def find(s):
	if s in x:
		return True
	else:
		return False
def add(str, n):
	x[str] = n
def get_all():
	print(x)
def get(str):
	return x[str]
