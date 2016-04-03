
#getting sdss demographics, how many galaxies show 3sigma hbeta, halpha

import math
import numpy as np

line_info = open("gal_line.txt",'r')
z_info = open("gal_info.txt",'r')

line_info.readline()
z_info.readline()

