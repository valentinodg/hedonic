import os
import shutil
import pathlib
import platform
import random
import networkx as nx
import matplotlib.pyplot as plt
import pydot

from pick import pick
from colorama import Fore, Back, Style, init
from pathlib import Path


#####################################################
#################### INIT BLOCK #####################
#####################################################

if platform.system() is "Windows":
	os.system("cls")
else :
	os.system("clear")


# colorama init
init()


#######################################################
#################### SEARCH BLOCK #####################
#######################################################

p = pathlib.Path.cwd().parents[0]
[x for x in p.iterdir() if x.is_dir()]

a = list(p.glob('**/*.edgelist'))

filelist =[]
optionfilelist =[]
absfilepath =[]

for i in a :
	rel = pathlib.Path(*i.parts[4:])
	optionfilelist.append(str(rel)) #string path from /hedonic
	absfilepath.append(str(i)) # string path from root
	filelist.append(i) # pathlib path from root


################################################################
#################### CHOICE .edgelist BLOCK ####################
################################################################

title = 'Select .edgelist file'

# FILESYSTEM :
#
# all file .edgelist from home directory (hedonic)
#
#

options = optionfilelist
option, index = pick(options, title, indicator='>', multi_select=False)


G = nx.read_weighted_edgelist(absfilepath[index], create_using=nx.Graph())

#name = "read-copy-of--" + str(filelist[index].name)

for (node,data) in G.nodes(data=True):
    print(node,data)
print('\n')
for (u,v,w) in G.edges(data=True):
    print(u,v,int(w['weight']))


#nx.write_weighted_edgelist(G, name)
