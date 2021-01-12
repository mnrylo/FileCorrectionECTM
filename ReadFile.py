#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 09:01:22 2020

@author: marcos
"""

import tkinter as tk
import webbrowser
from tkinter import filedialog

print("Choose File to be Corrected:")
root=tk.Tk()
root.withdraw()
file_path=filedialog.askopenfilename()
myfile = open(file_path, "r") 
outF = open("myOutFile.txt", "w")  
print("Inform Engine 1 Serial Number (AA0000):")
eng1 = input()
print("Inform Engine 2 Serial Number (AA0000):")
eng2 = input()
list_of_lists=[]
i=0
for line in myfile:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  list_of_lists.append(line_list)
  if(i%2 != 0): 
        stripped_line= line.strip()
        line_list = stripped_line.split()
        line_list[0] = line_list[0].replace("xxxxxx",eng2)
        
        if len(line_list[1])==3:
            line_list[0] = line_list[0].replace(line_list[0],line_list[0].ljust(len(line_list[0])+2))
        else:
            line_list[0] = line_list[0].replace(line_list[0],line_list[0].ljust(len(line_list[0])+1))
        line_list[1] = line_list[1].replace(line_list[1],line_list[1].ljust(len(line_list[1])+4))
        if len(line_list[3])==4:
            line_list[2] = line_list[2].replace(line_list[2],line_list[2].ljust(len(line_list[2])+2))
        else:
            line_list[2] = line_list[2].replace(line_list[2],line_list[2].ljust(len(line_list[2])+1))
        line_list[3] = line_list[3].replace(line_list[3],line_list[3].ljust(len(line_list[3])+1))
        line_list[4] = line_list[4].replace(line_list[4],line_list[4].ljust(len(line_list[4])+1))
        line_list[5] = line_list[5].replace(line_list[5],line_list[5].ljust(len(line_list[5])+1))
        line_list[6] = line_list[6].replace(line_list[6],line_list[6].ljust(len(line_list[6])+1))
        line_list[7] = line_list[7].replace(line_list[7],line_list[7].ljust(len(line_list[7])+1))
        line_list[8] = line_list[8].replace(line_list[8],line_list[8].ljust(len(line_list[8])+1))
        if len(line_list)==10:
            line_list[9] = line_list[9].replace(line_list[9],line_list[9].ljust(len(line_list[9])+3))
        else:
            line_list[9] = line_list[9].replace(line_list[9],line_list[9].ljust(len(line_list[9])+1))
        line="".join(line_list)
        outF.write("\n")
        outF.write(line)
  else: 
        stripped_line = line.strip()
        line_list = stripped_line.split()
        line_list[0] = line_list[0].replace("xxxxxx",eng1)
        if len(line_list[1])==3:
            line_list[0] = line_list[0].replace(line_list[0],line_list[0].ljust(len(line_list[0])+2))
        else:
            line_list[0] = line_list[0].replace(line_list[0],line_list[0].ljust(len(line_list[0])+1))
        line_list[1] = line_list[1].replace(line_list[1],line_list[1].ljust(len(line_list[1])+4))
        if len(line_list[3])==4:
            line_list[2] = line_list[2].replace(line_list[2],line_list[2].ljust(len(line_list[2])+2))
        else:
            line_list[2] = line_list[2].replace(line_list[2],line_list[2].ljust(len(line_list[2])+1))
        line_list[3] = line_list[3].replace(line_list[3],line_list[3].ljust(len(line_list[3])+1))
        line_list[4] = line_list[4].replace(line_list[4],line_list[4].ljust(len(line_list[4])+1))
        line_list[5] = line_list[5].replace(line_list[5],line_list[5].ljust(len(line_list[5])+1))
        line_list[6] = line_list[6].replace(line_list[6],line_list[6].ljust(len(line_list[6])+1))
        line_list[7] = line_list[7].replace(line_list[7],line_list[7].ljust(len(line_list[7])+1))
        line_list[8] = line_list[8].replace(line_list[8],line_list[8].ljust(len(line_list[8])+1))
        if len(line_list)==10:
            line_list[9] = line_list[9].replace(line_list[9],line_list[9].ljust(len(line_list[9])+3))
        else:
            line_list[9] = line_list[9].replace(line_list[9],line_list[9].ljust(len(line_list[9])+1))
        line="".join(line_list)
        outF.write("\n")
        outF.write(line)
  i=i+1


outF.close()
webbrowser.open("myOutFile.txt")
