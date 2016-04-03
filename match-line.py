import math
from scipy.spatial import KDTree

f1 = open('test.info','r') #test file with 50 sources
f2 = open('gal_line.txt','r') #file with all the mph database info. 

o1 = open('gal-line.info','w')

masterlist_from_line_no_to_id = {}
masterlist_from_id_to_data = {}

#masterlist = {}
#masterlist_transformed = []
# Do not need to do Euclidean distance, as we are matching plate and fiberids
#def MakeCoord(ra, dec):
    #Euclidean distance in this transformed space is a better measure of angular separation.
#    return (ra * math.pi / 180 * math.cos(dec * math.pi / 180), dec * math.pi / 180)

f2.readline()
i = 1
for line in f2:
    list = line.split(' ')
    plateid2 = list[0]
    fiberid2 = list[1]
    masterlist_from_line_no_to_id[i] = (plateid2, fiberid2)
    masterlist_from_id_to_data[(plateid2, fiberid2)] = list
    i += 1
#    masterlist_transformed.append(MakeCoord(ra2, dec2))


#print "Building kd-Tree..."
#kdtree = KDTree(masterlist_transformed)
#print "Done."
#i = 0
f2.seek(0)

for row in f1:
    item = row.split(' ')  
    plateid1 = item[6]
    fiberid1 = item[7]  
    query = (plateid1, fiberid1)
    if query in masterlist_from_id_to_data:
        print query, masterlist_from_id_to_data[query]
#    i += 1
       
    
    
#        o1.write("(%f, %f) -> (%f, %f) %f  %f\n" % (plateid1, , masterlist[index][0], masterlist[index][1], distance * 180 * 3600 / math.pi, index))
    
    #print coord, masterlist[index]
    # o1.write("%d %d %d %d \n" % (ra1, ra2, dec1, dec2))
#o1.close()
f1.close()
#f2.close()

