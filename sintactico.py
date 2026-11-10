def sintactico(tokens, i):
	if i<len(tokens) and tokens[i] == 170: 
		i, error = variable(tokens,i)
	if error != '':
		return i, error
	else:
		return i , 'Error se esperaba una variable'	
	i = i + 1

def variable(tokens, i):
	if i<len(tokens) and tokens[i] == 170:
		i = i + 1 
	else:
		return 'Error se esperaba una letra'
	if i<len(tokens) and tokens[i] in (160,170):
		i = i + 1 
	return  i, ''

