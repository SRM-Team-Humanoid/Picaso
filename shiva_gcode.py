import time
def load_numbers():
    filename = "shiva.txt"
    in_file = open(filename, "r")
    G = open('G.txt','a')
    X = open('X.txt','a')
    Y = open('Y.txt','a')
    cnt = 0
    for line in iter(in_file):	
	'''	
	if cnt < 13001 or cnt > 19174:
		cnt+=1
		continue
	cnt+=1
	out_file = open('Shiva4.txt', 'a')
	out_file.write(line)
	'''	
	if len(line) < 10 or line[0] == ';':
		continue	
	line = line.strip().split(" ")
	vals = []
	for val in line:
		if val[0] == 'F' or val[0] == 'E':
			continue		
		val = list(val)[1:len(val)]
		val = "".join(val)
		vals.append(val)
	try:	
		g,x,y = vals
		print g,x,y
		G.write(g+" ")
		X.write(x+" ")
		Y.write(y+" ")
	except:
		continue
	#time.sleep(0.1)
    G.close()
    X.close()
    Y.close()
    in_file.close()

load_numbers()

