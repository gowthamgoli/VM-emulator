def is_mem_address(x):
	if x[0] == '[' and x[-1] == ']': return True

def is_number(x):
	if (x[0] == '0' and x[1] == 'x') or (x[-2] == '|' and x[-1] == 'h') or (x[-2] == '|' and x[-1] == 'b') or (x.isdigit()): return True

def is_register(x, registers):
	if x in registers: return True

def get_value_mem(x, addresses):
	x = get_value_num(x[1:-1])
	return addresses[x]

def get_value_num(x):
	if (x[0] == '0' and x[1] == 'x'):
		return int(x[2:], 16)
	if (x[-2] == '|' and x[-1] == 'h'):
		return int(x[:-2], 16)
	if (x[-2] == '|' and x[-1] == 'b'):
		return int(x[:-2], 2)
	return int(x)

def get_value_reg(x, registers):
	return registers[x] 

def store_val(x, val, mainMemory):
	if is_mem_address(x):
		mainMemory.addresses[get_value_num(x[1:-1])] = val
	elif is_register(x, mainMemory.registers):
		mainMemory.registers[x] = val

def get_value(arg, mainMemory):
	#print 'in get value'
	if is_mem_address(arg):
		#print 'its a mem address'
		return get_value_mem(arg, mainMemory.addresses)
	elif is_number(arg):
		#print 'its a number'
		return get_value_num(arg)
	elif is_register(arg, mainMemory.registers):
		#print 'its a register'
		return get_value_reg(arg, mainMemory.registers)

#is_mem_address('100|b')