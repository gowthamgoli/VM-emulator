from helpers import *
def mov(arg0, arg1, registers, addresses):
	val_arg1 = get_value(arg1, registers, addresses)
	#print val_arg1
	if is_mem_address(arg0):
		print 'argo is mem'
		addresses[get_value_num(arg0[1:-1])] = val_arg1
	elif is_register(arg0, registers):
		print 'arg0 is reg'
		registers[arg0] = val_arg1
