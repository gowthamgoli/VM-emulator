import sys
from collections import OrderedDict
from collections import defaultdict
from pprint import pprint
from subroutines import *

class MainMemory():
	registers = {'eax':0, 'ebx':0,'ecx':0, 'edx':0, 'esi':0, 'edi':0, 'esp':0, 'ebp':0, 'eip':0, 'r08':0, 'r09':0, 'r10':0, 'r11':0, 'r12':0, 'r13':0, 'r14':0, 'r15':0, 'flags':0, 'rem':0}
	addresses = defaultdict(int)
	stack = []

class ProgramCounter():
	inst_num = 0		#inst num within the label
	curr_label = None	#current label being executed
	labels = []			#list of labels acc. to the order in which they appear in the code
	label_index = 0		#index of the current label being executed
	instructions = OrderedDict()


instruction = {'op': None, 'arg0': None, 'arg1': None}


call_subroutine = {'mov':mov, 'push':push, 'pop':pop, 'pushf':pushf, 'popf':popf, 'call':call, 'ret':ret, 'inc':inc, 'dec':dec, 'add':add, 'sub':sub,\
				   'mul':mul, 'div':div, 'mod':mod, 'rem':rem, 'not':binnot, 'xor':binxor, 'or':binor, 'and':binand, 'shl':binshl, 'shr':binshr, 'cmp':cmpr,\
				   'jmp':jmp, 'je':je, 'jne':jne, 'jg':jg, 'jge':jge, 'jl':jl, 'jle':jle, 'prn':prn}


def parseFile(filename, pc):
	lines = open(filename,'r').read().split('\n')
	#print lines
	currLabel = 'Null'
	pc.instructions[currLabel] = []
	for line in lines:
		if line.strip().startswith('#') or not line or line.isspace():
			continue
		if ':' in line:
			tokens = line.split(':')
			currLabel = tokens[0]+':'
			pc.instructions[currLabel] = []
			if len(tokens) == 2:
				line = tokens[1]
		if not ':' in line:
			line = line.strip()
			#print line
			if line:
				line = line.split('#')[0].strip()
				pc.instructions[currLabel].append(line)

	if not pc.instructions['Null']: del pc.instructions['Null']


	for label in pc.instructions:
		pc.labels.append(label)
		'''print label
		for inst in pc.instructions[label]:
			print inst'''

def main():
	filename = sys.argv[1]

	mainMemory = MainMemory()
	pc = ProgramCounter()

	#parses file and adds insts to the dict 'instructions' to the form of {label:[inst]}
	parseFile(filename, pc)

	#print pc.labels
	#represesnts the current instruction number within that label
	pc.inst_num = 0

	if 'start:' in pc.labels:
		pc.curr_label = 'start:'
		pc.label_index = pc.labels.index('start:')
	else:
		pc.curr_label = pc.labels[0]

	#Keep executing until we reach the last instrunction of the current label
	while pc.inst_num != len(pc.instructions[pc.curr_label]):
		#get current instructions
		curr_inst = pc.instructions[pc.curr_label][pc.inst_num]
		#print curr_inst
		#print pc.curr_label, pc.inst_num
		tokens = curr_inst.split(None, 1)

		#get the op code
		instruction['op'] = tokens[0]

		#get the arguments
		if len(tokens) == 2:
			args = [item.strip() for item in tokens[1].split(',')]
			if args:
				instruction['arg0'] = args[0]
				instruction['arg1'] = args[1] if len(args) == 2 else None
		else:
			instruction['arg0'] = None
			instruction['arg1'] = None

		#print args

		call_subroutine[instruction['op']](instruction['arg0'], instruction['arg1'], mainMemory, pc)
		#pprint(mainMemory.registers)
		#pprint(mainMemory.addresses)
		#print MainMemory.stack
		#print ''

		pc.inst_num += 1
		#check if we reached the last intruction of the current label
		if pc.inst_num == len(pc.instructions[pc.curr_label]):

			#go to next label
			pc.label_index += 1
			#if the current label is the last label in the sequence of the labels in the code then break out of loop
			if pc.label_index == len(pc.labels): break
			pc.curr_label = pc.labels[pc.label_index]
			pc.inst_num = 0

if __name__ == "__main__":
    main()