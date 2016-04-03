import math
from scipy.spatial import KDTree

f1 = open('test.info','r')
f2 = open('gal_info_id.txt','r')

o1 = open('radec-info.txt','w')

masterlist = []
masterlist_transformed = []

def MakeCoord(ra, dec):
    #Euclidean distance in this transformed space is a better measure of angular separation.
    return (ra * math.pi / 180 * math.cos(dec * math.pi / 180), dec * math.pi / 180)

f2.readline()
for line in f2:
    list = line.split(' ')
    plateid2 = list[0]
    fiberid2 = list[2]
    ra2 = float(list[3]) 
    dec2 = float(list[4]) 
    masterlist.append((ra2, dec2))
    masterlist_transformed.append(MakeCoord(ra2, dec2))

print "Building kd-Tree..."
kdtree = KDTree(masterlist_transformed)
print "Done."
for row in f1:
    item = row.split(' ')  
    plateid1 = item[6]
    fiberid1 = item[7]  
    ra1 = float(item[4]) 
    dec1 = float(item[5])
    coord = MakeCoord(ra1, dec1)
    (distance, index) = kdtree.query([coord])
    o1.write("(%f, %f) -> (%f, %f) %f  %f\n" % (ra1, dec1, masterlist[index][0], masterlist[index][1], distance * 180 * 3600 / math.pi, index))
    
    #print coord, masterlist[index]
    # o1.write("%d %d %d %d \n" % (ra1, ra2, dec1, dec2))
o1.close()
f1.close()
f2.close()

