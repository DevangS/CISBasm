TAR_REG = ''
DIFF_REG = ''
LT_REG = ''
GT_REG = ''
EQ_REG = ''
NE_REG = ''

def r_to_binary()
	pass

end 

def needs_reg(instruction)
	if risters.index(instruction)
end
def parse(line)
	instruction,t = line.split(' ')



	return to_binary(instruction) + to_binary(t)
end

def assemble_file(input_file, output_file)
	for line_number, line in enumerate(input_file.readLines()):
		result = parse(line)
		if result.contains('Error: '):
			print 'Error on line ' + str(line_number) + result
			return
		else:
			output_file.writeLine(result) #Append '\n'?


instrs = {
'setTar': ( r, 00000, TAR_REG),
'addTar': (i, 00001, t),
'subTar': (i, 00010, t),
'shiftR': (i, 00011, t),
'shiftL': (i, 00100, t),
'copyTo': (r, 00110, t),
'copyFr': (r, 00111, t),
'addReg': (r, 01000, t),
'subReg': (r, 01001, t),
'difReg': (r, 01010, t, DIFF_REG),
'andAsn': (r, 01011, t),
'strTar': (r, 01100, t),
'ldMem' : (r, 01101, t),
'compLT': (r, 01110, LT_REG),
'compGT': (r, 01111, GT_REG),
'compEQ': (r, 10000, , EQ_REG),
'compNE': (r, 10001, NE_REG),
'setSec': (i, 10010, None),
'clrReg': (r, 10011, None),
'incReg': (r, 10100, None),
'decReg': (r, 10101, None),
'ggnore': ('', 10110, None),
'TBD'   : ('', 10111, ''),
'jmpCnd': ('', 1110_, None),
'jmpAlw': ('', 1111_, None),
}