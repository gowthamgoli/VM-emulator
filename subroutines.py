from helpers import *
def mov(arg0, arg1, mainMemory, pc):
	#get the value of arg1 (could be number, value stored in mem/reg)
	val_arg1 = get_value(arg1, mainMemory)
	#store val_arg1 in arg0 whihch could be a mem address/register
	store_val(arg0, val_arg1, mainMemory)

def push(arg0, arg1, mainMemory, pc):
	val_arg0 = get_value(arg0, mainMemory)
	mainMemory.stack.append(val_arg0)

def pop(arg0, arg1, mainMemory, pc):
	store_val(arg0, mainMemory.stack.pop(), mainMemory)

def pushf(arg0, arg1, mainMemory, pc):
	mainMemory.stack.append(mainMemory.registers['flags'])

def popf(arg0, arg1, mainMemory, pc):
	mainMemory.registers['flags'] = mainMemory.stack.pop()

def call(arg0, arg1, mainMemory, pc):
	if arg0+':' in pc.labels:
		mainMemory.stack.append((pc.curr_label, pc.inst_num))
		pc.curr_label = arg0+':'
		pc.inst_num = -1
	#print pc.curr_label
	#print pc.inst_num

def ret(arg0, arg1, mainMemory, pc):
	pc.curr_label, pc.inst_num = mainMemory.stack.pop()
