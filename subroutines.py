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
		pc.label_index = pc.labels.index(arg0+':')

def ret(arg0, arg1, mainMemory, pc):
	pc.curr_label, pc.inst_num = mainMemory.stack.pop()
	pc.label_index = pc.labels.index(pc.curr_label)

def inc(arg0, arg1, mainMemory, pc):
	val_arg0 = get_value(arg0, mainMemory)
	store_val(arg0, val_arg0+1, mainMemory)

def dec(arg0, arg1, mainMemory, pc):
	val_arg0 = get_value(arg0, mainMemory)
	store_val(arg0, val_arg0-1, mainMemory)

def add(arg0, arg1, mainMemory, pc):
	val_arg0 = get_value(arg0, mainMemory)
	val_arg1 = get_value(arg1, mainMemory)
	store_val(arg0, val_arg0+val_arg1, mainMemory)

def sub(arg0, arg1, mainMemory, pc):
	val_arg0 = get_value(arg0, mainMemory)
	val_arg1 = get_value(arg1, mainMemory)
	store_val(arg0, val_arg0-val_arg1, mainMemory)

def mul(arg0, arg1, mainMemory, pc):
	val_arg0 = get_value(arg0, mainMemory)
	val_arg1 = get_value(arg1, mainMemory)
	store_val(arg0, val_arg0*val_arg1, mainMemory)

def div(arg0, arg1, mainMemory, pc):
	val_arg0 = get_value(arg0, mainMemory)
	val_arg1 = get_value(arg1, mainMemory)
	store_val(arg0, val_arg0/val_arg1, mainMemory)
	mainMemory.registers['rem'] = val_arg0%val_arg1

def mod(arg0, arg1, mainMemory, pc):
	val_arg0 = get_value(arg0, mainMemory)
	val_arg1 = get_value(arg1, mainMemory)
	mainMemory.registers['rem'] = val_arg0%val_arg1

def rem(arg0, arg1, mainMemory, pc):
	store_val(arg0, mainMemory.registers['rem'], mainMemory)

def binnot(arg0, arg1, mainMemory, pc):
	val_arg0 = get_value(arg0, mainMemory)
	store_val(arg0, ~val_arg0, mainMemory)

def binxor(arg0, arg1, mainMemory, pc):
	val_arg0 = get_value(arg0, mainMemory)
	val_arg1 = get_value(arg1, mainMemory)
	store_val(arg0, val_arg0^val_arg1, mainMemory)

def binor(arg0, arg1, mainMemory, pc):
	val_arg0 = get_value(arg0, mainMemory)
	val_arg1 = get_value(arg1, mainMemory)
	store_val(arg0, val_arg0|val_arg1, mainMemory)

def binand(arg0, arg1, mainMemory, pc):
	val_arg0 = get_value(arg0, mainMemory)
	val_arg1 = get_value(arg1, mainMemory)
	store_val(arg0, val_arg0&val_arg1, mainMemory)

def binshl(arg0, arg1, mainMemory, pc):
	val_arg0 = get_value(arg0, mainMemory)
	val_arg1 = get_value(arg1, mainMemory)
	store_val(arg0, val_arg0<<val_arg1, mainMemory)

def binshr(arg0, arg1, mainMemory, pc):
	val_arg0 = get_value(arg0, mainMemory)
	val_arg1 = get_value(arg1, mainMemory)
	store_val(arg0, val_arg0>>val_arg1, mainMemory)

def cmpr(arg0, arg1, mainMemory, pc):
	val_arg0 = get_value(arg0, mainMemory)
	val_arg1 = get_value(arg1, mainMemory)
	mainMemory.registers['flags'] = val_arg0 - val_arg1

def jmp(arg0, arg1, mainMemory, pc):
	val_arg0 = get_value(arg0, mainMemory)
	if val_arg0 == 'x' and  arg0+':' in pc.labels:
		#mainMemory.stack.append((pc.curr_label, pc.inst_num))
		pc.curr_label = arg0+':'
		pc.inst_num = -1
		pc.label_index = pc.labels.index(arg0+':')

def je(arg0, arg1, mainMemory, pc):
	val_arg0 = get_value(arg0, mainMemory)
	if val_arg0 == 'x' and  arg0+':' in pc.labels and mainMemory.registers['flags'] == 0:
		#mainMemory.stack.append((pc.curr_label, pc.inst_num))
		pc.curr_label = arg0+':'
		pc.inst_num = -1
		pc.label_index = pc.labels.index(arg0+':')

def jne(arg0, arg1, mainMemory, pc):
	val_arg0 = get_value(arg0)
	if val_arg0 == 'x' and  arg0+':' in pc.labels and mainMemory.registers['flags'] != 0:
		mainMemory.stack.append((pc.curr_label, pc.inst_num))
		pc.curr_label = arg0+':'
		pc.inst_num = -1
		pc.label_index = pc.labels.index(arg0+':')

def jg(arg0, arg1, mainMemory, pc):
	val_arg0 = get_value(arg0, mainMemory)
	if val_arg0 == 'x' and  arg0+':' in pc.labels and mainMemory.registers['flags'] > 0:
		#mainMemory.stack.append((pc.curr_label, pc.inst_num))
		pc.curr_label = arg0+':'
		pc.inst_num = -1
		pc.label_index = pc.labels.index(arg0+':')

def jge(arg0, arg1, mainMemory, pc):
	val_arg0 = get_value(arg0, mainMemory)
	if val_arg0 == 'x' and  arg0+':' in pc.labels and mainMemory.registers['flags'] >= 0:
		#mainMemory.stack.append((pc.curr_label, pc.inst_num))
		pc.curr_label = arg0+':'
		pc.inst_num = -1
		pc.label_index = pc.labels.index(arg0+':')

def jl(arg0, arg1, mainMemory, pc):
	val_arg0 = get_value(arg0, mainMemory)
	if val_arg0 == 'x' and  arg0+':' in pc.labels and mainMemory.registers['flags'] < 0:
		#mainMemory.stack.append((pc.curr_label, pc.inst_num))
		pc.curr_label = arg0+':'
		pc.inst_num = -1
		pc.label_index = pc.labels.index(arg0+':')	

def jle(arg0, arg1, mainMemory, pc):
	val_arg0 = get_value(arg0, mainMemory)
	if val_arg0 == 'x' and  arg0+':' in pc.labels and mainMemory.registers['flags'] <= 0:
		#mainMemory.stack.append((pc.curr_label, pc.inst_num))
		pc.curr_label = arg0+':'
		pc.inst_num = -1
		pc.label_index = pc.labels.index(arg0+':')

def prn(arg0, argq, mainMemory, pc):
	val_arg0 = get_value(arg0, mainMemory)
	print val_arg0