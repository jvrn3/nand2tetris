def is_int(s):
	try: 
		int(s)
		return True
	except ValueError:
		return False
def code_jmp(str):
	if(str == ""):
		ret = "000"
	if(str == "JGT"):
		ret = "001"
	if(str == "JEQ"):
		ret = "010"
	if(str == "JGE"):
		ret = "011"
	if(str == "JLT"):
		ret = "100"
	if(str == "JNE"):
		ret = "101"
	if(str == "JLE"):
		ret = "110"
	if(str == "JMP"):
		ret = "111"
	return ret
	

def code_dest(str):
	if(str == ""):
		ret = "000"
	if(str =="M"):
		ret = "001"
	if(str =="D"):
		ret = "010"
	if(str == "MD"):
		ret = "011"
	if(str == "A"):
		ret = "100"
	if(str == "AM"):
		ret = "101"
	if(str == "AD"):
		ret = "111"
	
	return ret
def code_comp(str):
	if(str == "0"):
		ret = "0101010"
	if(str == "1"):
		ret = "0111111"
	if(str == "-1"):
		ret = "0111010"
	if(str== "D"):
		ret = "0001100"
	if(str == "A"):
		ret = "0110000"
	if(str == "!D"):
		ret = "0001101"
	if(str == "!A"):
		ret = "0110001"
	if(str == "-D"):
		ret = "0001111"
	if(str == "-A"):
		ret = "0110011"
	if(str == "D+1"):
		ret = "0011111"
	if(str == "A+1"):
		ret = "0110111"
	if(str == "D-1"):
		ret = "0001110"
	if(str == "A-1"):
		ret = "0110010"
	if(str == "D+A"):
		ret = "0000010"
	if(str == "D-A"):
		ret = "0010011"
	if(str == "A-D"):
		ret = "0000111"
	if(str == "D&A"):
		ret = "0000000"
	if(str == "D|A"):
		ret = "0010101"
	if(str == "M"):
		ret = "1110000"
	if(str == "!M"):
		ret = "1110001"
	if(str == "-M"):
		ret = "1110011"
	if(str == "M+1"):
		ret = "1110111"
	if(str == "M-1"):
		ret = "1110010"
	if(str == "D+M"):
		ret = "1000010"
	if(str == "D-M"):
		ret = "1010011"
	if(str == "M-D"):
		ret = "1000111"
	if(str == "D&M"):
		ret = "1000000"
	if(str == "D|M"):
		ret = "1010101"
	return ret




