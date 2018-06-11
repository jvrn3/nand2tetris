import sys
from code import *
from converter import convert_to_decimal
from symbol_table import *


with open(sys.argv[1]) as f:
	writeC = open(sys.argv[1][0:len(sys.argv[1])-4] + ".hack", "w")


	read_data = f.read()
	read_data = read_data.replace(" ", "")
	symbol(read_data)
	available = 16
	for t in read_data.split():
		#check if it is not a symbol or label
		if(t[0] != '@' and t[0] != '('  and t[0] !='/'):
			
				#D=D-A
				dest = t.split("=")[0]
				if(dest[0] != '/'):
					if(t[1] == '=' or t[2] == '='):
						comp = t.split("=")[1]
					else:
						comp = t[0]
						dest = ""
					comp = comp.split("/")[0]
					jmp = t.partition(";")[2]
					jmp = jmp[0:3]
					code = "111" + code_comp(comp) + code_dest(dest) + code_jmp(jmp)
					writeC.write(code)
					writeC.write("\n")
					print(code)



		else:
			if(t[0] == '@'):
				c = t.split("/")[0]
				if(is_int(c[1::])):
					print(convert_to_decimal(int(c[1::])))
					writeC.write(convert_to_decimal(int(c[1::])))
					writeC.write("\n")

				else:
					if(find(c[1::])):
						print(convert_to_decimal(get(c[1::])))
						writeC.write(convert_to_decimal(get(c[1::])))
						writeC.write("\n")
					else:
						add(c[1::], available)
						print(convert_to_decimal(get(c[1::])))
						writeC.write(convert_to_decimal(get(c[1::])))
						writeC.write("\n")
						available +=1

writeC.close()
				# print(convert_to_decimal(int(t[1::])))



#dec_to_binary



