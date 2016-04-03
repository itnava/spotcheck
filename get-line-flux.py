
f = open("register.txt", 'r')
g = open("gal_info.txt", 'r')

masterlist = {}

i = 0

for line in g:
    list = line.split(' ')     
    masterlist[i] = list
    i += 1


for line in f:
    i = int(line) - 1
    print masterlist[i]
    
    
    