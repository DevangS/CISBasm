import sys

def parse(line):
    instruction, target = line.replace('\n', '').split(' ')
    if instruction not in instructions:
        raise ParseError(instruction + ' is not a valid instruction')
    else:
        operation = instructions[instruction]
        if operation[0] is 'r':
            return operation[1] + registers[target]
        elif operation[0] is 'i':
            return operation[1] + "{0:04b}".format(target)
        else:
            return operation[1] + '0000'


def assemble_file(input_file_location, output_file_location):
    input_file = open(input_file_location, 'r')
    output_file = open(output_file_location, 'w')
    for line_number, line in enumerate(input_file):
        try:
            output = '{0}: instruction = 9\'b{1};\n'.format(line_number, parse(line))
            output_file.write(output)
        except ParseError as e:
            print line_number, e.message
    input_file.close()
    output_file.close()


class ParseError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)

instructions = {
    'copyTo': ('r', '00010', 't'),
    'copyFr': ('r', '00011', 't'),
    'strTar': ('r', '00101', 't'),
    'lodMem': ('r', '00110', 't'),
    'addReg': ('r', '00000', 't'),
    'subReg': ('r', '00001', 't'),
    'andAsn': ('r', '00100', 't'),
    'setTar': ('r', '01000', 'TAR_REG'),
    'difReg': ('r', '01011', 't'),
    'compLT': ('r', '01100', 'LT_REG'),
    'compGT': ('r', '01101', 'GT_REG'),
    'compEQ': ('r', '01110', 'EQ_REG'),
    'compNE': ('r', '01111', 'NE_REG'),
    'addTar': ('i', '10000', 't'),
    'subTar': ('i', '10001', 't'),
    'shiftL': ('i', '10010', 't'),
    'shiftR': ('i', '10011', 't'),
    'setSec': ('i', '10010', None),
    'ggnore': ('', '11000', None),
    'jmpCnd': ('i', '11001', None),
    'jmpAlw': ('i', '11010', None),
    'TBD': ('', '11011', None),
    'clrReg': ('r', '11101', None),
    'decReg': ('r', '11110', None),
    'incReg': ('r', '11111', None)
}

registers = {
'$0': '0000',
'$1': '0001',
'$2': '0010',
'$3': '0011',
'$4': '0100',
'$5': '0101',
'$6': '0111',
'$7': '0111',
'EQ_REG': '1000',
'NE_REG': '1001',
'DIFF_REG': '1011',
'LT_REG': '1100',
'GT_REG': '1101',
'TAR_REG': '1110',
'SEC_REG': '1111'
}

if  __name__ =='__main__':
    assemble_file(sys.argv[1], sys.argv[2])

