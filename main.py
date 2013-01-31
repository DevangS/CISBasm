def parse(line):
    instruction, target = line.split(' ')
    if instruction not in instructions:
        raise ParseError(instruction + ' is not a valid instruction')
    else:
        operation = instructions['instruction']
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
            result = parse(line)
            output_file.writeLine(result)  # Append '\n'?
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
    'setTar': ('r', '00000', 'TAR_REG'),
    'addTar': ('i', '00001', 't'),
    'subTar': ('i', '00010', 't'),
    'shiftR': ('i', '00011', 't'),
    'shiftL': ('i', '00100', 't'),
    'copyTo': ('r', '00110', 't'),
    'copyFr': ('r', '00111', 't'),
    'addReg': ('r', '01000', 't'),
    'subReg': ('r', '01001', 't'),
    'difReg': ('r', '01010', 't'),
    'andAsn': ('r', '01011', 't'),
    'strTar': ('r', '01100', 't'),
    'lodMem': ('r', '01101', 't'),
    'compLT': ('r', '01110', 'LT_REG'),
    'compGT': ('r', '01111', 'GT_REG'),
    'compEQ': ('r', '10000', 'EQ_REG'),
    'compNE': ('r', '10001', 'NE_REG'),
    'setSec': ('i', '10010', None),
    'clrReg': ('r', '10011', None),
    'incReg': ('r', '10100', None),
    'decReg': ('r', '10101', None),
    'ggnore': ('', '10110', None),
    'TBD': ('', '10111', None),
    'jmpCnd': ('i', '11100', None),
    'jmpAlw': ('i', '11110', None)
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
'TAR_REG': '1000',
'SEC_REG': '1001',
'DIFF_REG': '1011',
'LT_REG': '1100',
'GT_REG': '1101',
'EQ_REG': '1110',
'NE_REG': '1111'
}
