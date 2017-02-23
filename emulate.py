import sys
from collections import OrderedDict
from subroutines import *

instructions = OrderedDict()
instruction = {'op': None, 'arg0': None, 'arg1': None}
labels = []
registers = {'eax':0, 'ebx':0,'ecx':0, 'edx':0, 'esi':0, 'edi':0, 'esp':0, 'ebp':0, 'eip':0, 'R08':0, 'R09':0, 'R10':0, 'R11':0, 'R12':0, 'R13':0, 'R14':0, 'R15':0}
addresses = {}

call_subroutine = {'mov': mov}

def parseFile(filename):
	lines = open(filename,'r').read().split('\n')
	#print lines
	currLabel = 'Null'
	instructions[currLabel] = []
	for line in lines:
		if line.startswith('#') or not line or line.isspace():
			continue
		if ':' in line:
			tokens = line.split(':')
			currLabel = tokens[0]+':'
			instructions[currLabel] = []
			if len(tokens) == 2:
				line = tokens[1]
		if not ':' in line:
			line = line.strip()
			#print line
			if line:
				line = line.split('#')[0].strip()
				instructions[currLabel].append(line)

	if not instructions['Null']: del instructions['Null']


	for label in instructions:
		labels.append(label)
		'''print label
		for inst in instructions[label]:
			print inst'''

def main():
	filename = sys.argv[1]

	#parses file and adds insts to the dict 'instructions' to the form of {label:[inst]}
	parseFile(filename)

	#represesnts the current instruction number within that label
	inst_num = 0
	#represents the current label to be executed or in execution
	curr_label = 'start:' if 'start:' in labels else labels[0]

	while inst_num != len(instructions[curr_label]):
		#get current instructions
		curr_inst = instructions[curr_label][inst_num]
		tokens = curr_inst.split(None, 1)

		#get the op code
		instruction['op'] = tokens[0]

		#get the arguments
		args = [item.strip() for item in tokens[1].split(',')]
		instruction['arg0'] = args[0]
		instruction['arg1'] = args[1] if len(args) == 2 else None
		print args

		call_subroutine[instruction['op']](instruction['arg0'], instruction['arg1'], registers, addresses)
		print registers
		print addresses

		inst_num += 1

if __name__ == "__main__":
    main()