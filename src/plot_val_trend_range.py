#===========================#
# Plot Value Trend and Range
#===========================#
import os
import cv2
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


# 1. Read from CSV
dir = os.path.abspath(os.getcwd())
csv_path = dir + "/src/simple-reachability/bags/manip_ur5.csv"

idx_list    = []
icn_list    = []
mm_list     = []
msv_list    = []
mscore_list = []
with open(csv_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        # idx,x,y,z,j1,j2,j3,j4,j5,j6,row
        # print(row)
        idx_list.append(row['idx'])

        if row['icn']!=None:
            icn_list.append(float(row['icn'])) 
        else:
            icn_list.append(0) #row['icn'])

        if row['mm']!=None:
            mm_list.append(float(row['mm'])) 
        else:
            mm_list.append(0) #row['mm'])

        if row['msv']!=None:
            msv_list.append(float(row['msv'])) 
        else:
            msv_list.append(0) #row['msv'])

        if row['mscore']!=None:
            mscore_list.append(float(row['mscore'])) 
        else:
            mscore_list.append(0) #row['mscore'])

# 2. Plot Value of different manipulability indicators
# Inverse Condition Number (icn)
# Manipulability Measure (mm)
# Minimum Singular Value (msv)
# M Score Value          (mscore)
            
plt.plot(idx_list, icn_list,   '-*', linewidth=1, markersize=5, color='#4971A6')#r')   # red line without marker
plt.plot(idx_list, mm_list,    '--+', color='#D97652')#'k--+')   # black dashed line, with "+" markers
plt.plot(idx_list, msv_list,   ':+', color='#4D5950')#'b-o')     # blue solid line with filled circle marker
plt.plot(idx_list, mscore_list,'-+', color='#56A662')#'r:')     # red dotted line (no marker)
# plt.plot(x, y, 'gd') # green dimonds (no line)
plt.legend(['Inverse Condition Number (icn)','Manipulability Measure (mm)','Minimum Singular Value (msv)','M Score Value (mscore)'])
plt.show()                
            
# # print(mcolors.CSS4_COLORS['lightcoral'])

# # split window
# # f, ax = plt.subplots(4,1,sharex='col',sharey='row')
# f, ax = plt.subplots(1,4,sharex='col',sharey='row')
# #Plot1
# ax[0].plot(idx_list, icn_list, color='#4971A6')#mcolors.CSS4_COLORS['lightcoral'])
# # ax[0].set_title(r'Inverse Condition Number (icn)')
# # ax[0].legend(r'Inverse Condition Number (icn)')
# ax[0].set_ylim([0,0.175])

# #Plot2
# ax[1].plot(idx_list, mm_list, color='#56A662')
# ax[1].set_title(r'Manipulability Measure (mm)')
# # ax[1].legend(r'Manipulability Measure (mm)')
# ax[1].set_ylim([0,0.175])

# #Plot3
# ax[2].plot(idx_list, msv_list, color='#4D5950')
# ax[2].set_title(r'Minimum Singular Value (msv)')
# # ax[2].legend(r'Minimum Singular Value (msv)')
# ax[2].set_xticks(np.linspace(0,75,5))
# ax[2].set_ylim([0,0.175])

# #Plot4
# ax[3].plot(idx_list, mscore_list, color='#D97652')
# # ax[3].set_xscale('log')
# ax[3].set_title(r'M Score Value (mscore)')
# # ax[3].legend(r'M Score Value (mscore)')
# # ax[3].set_xlabel('log(x)')
# ax[3].set_ylim([0,0.175])

# # plt.legend([l1, l2, l3],["HHZ 1", "HHN", "HHE"])
# plt.show()

# 3. Plot Range
icn_min,    icn_max    = min(icn_list)   , max(icn_list)
mm_min,     mm_max     = min(mm_list)    , max(mm_list)
msv_min,    msv_max    = min(msv_list)   , max(msv_list)
mscore_min, mscore_max = min(mscore_list), max(mscore_list)

# # sudo pip3 install seaborn
# import seaborn as sns
# sns.violinplot(y=icn_list)