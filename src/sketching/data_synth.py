import numpy as np
import csv

# GEOID,ST10,COU10,TRACT10,AREAL10,AREAW10,CSA09,CBSA09,CBSA_T,MDIV09,CSI,COFLG,POP00,HU00,POP10,HU10,NPCHG,PPCHG,NHCHG,PHCHG
# 01001020100,01,001,020100,3.787640715,0.01402014218,388,33860,"Montgomery, AL",,1,O,1906,764,1912,752,6,0.31,-12,-1.57

col_names = ["GEOID","ST10","COU10","TRACT10","AREAL10","AREAW10","CSA09","CBSA09","CBSA_T","MDIV09","CSI","COFLG","POP00","HU00","POP10","HU10","NPCHG","PPCHG","NHCHG","PHCHG"]
col_specs = [(int, 11), (int, 2), (int, 3), (int, 6), (float, None), (float, None), (int, 3), (int, 5), (str, None), (any, None), (int, None), (str, None), (int, None), (int, None), (int, None), (int, None), (int, None), (float, None), (int, None), (float, None)]
name_specs = dict(zip(col_names, col_specs))

num_rows = 4
name = "AREAL10"
print(int == name_specs[name][0])
arlist = []
for name in name_specs.keys():
	if (name_specs[name][0] == int) and (name_specs[name][1] is not None):
		num_min = 10**(name_specs[name][1]-1)
		num_max = 10**name_specs[name][1]-1
		ar = np.random.randint(num_min, num_max, (num_rows, 1))
		arlist.append(ar)
	elif (name_specs[name][0] == int) and (name_specs[name][1] is None):
		num_min = 0
		num_max = 10**5
		ar = np.random.randint(num_min, num_max, (num_rows, 1))
		arlist.append(ar)
arstack = np.hstack(arlist)

print(arstack)

# geo_column = np.random.randint(10**10,10**11-1, (4,1))
# st10_column = np.random.randint(10,10**2-1, (4,1))


# print(ar[3,0])