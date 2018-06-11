def convert_to_decimal(dec):
	a = []
	b = ""
	while(dec > 0):
		a.append(dec % 2)
		dec = dec // 2
	while(a):
		b = b + str(a.pop())
	length = len(b)
	for i in range(0, 16- length):
		b = '0' + b
	
	return b



