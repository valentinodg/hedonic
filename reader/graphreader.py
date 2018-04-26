import os
import shutil
import pathlib
import platform
import random
import networkx as nx
import matplotlib.pyplot as plt
import pydot
from pick import pick


if platform.system() is "Windows":
	os.system("cls")
else :
	os.system("clear")

print("\n")
