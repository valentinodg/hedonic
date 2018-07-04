import os
import shutil
import pathlib
import platform
import random
import networkx as nx
import matplotlib.pyplot as plt
import pydot
import time

import itertools
import sys
from pprint import pprint

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
matplotlib = False


#############################################################
#################### PROGRAM MODE BLOCK #####################
#############################################################

title = 'Select EXEC MODE'

# FILESYSTEM :
#
# SINGLE EXEC
# MULTIPLE EXEC
#
#

options = ['SINGLE EXEC', 'MULTIPLE EXEC']
option, index = pick(options, title, indicator='>', multi_select=False)


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

if option is "SINGLE EXEC":


	#######################################################
	#################### SEARCH BLOCK #####################
	#######################################################

	p = pathlib.Path.cwd().parents[0].joinpath('generator').joinpath('gen')
	[x for x in p.iterdir() if x.is_dir()]

	a = list(p.glob('**/*.edgelist'))

	filelist =[]
	optionfilelist =[]
	absfilepath =[]

	for i in a :
		rel = pathlib.Path(*i.parts[8:])
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


	# G = nx.read_weighted_edgelist(absfilepath[index], create_using=nx.Graph())
	G = nx.read_edgelist(absfilepath[index], nodetype=int, edgetype=int, create_using=nx.Graph())

	#name = "read-copy-of--" + str(filelist[index].name)
	dirname = str(filelist[index].stem)
	init_ext = str(filelist[index].stem) + ".init"
	out_ext = str(filelist[index].stem) + ".out"


	# print(Style.BRIGHT + Fore.RED + "\nGRAPH PRINT == NODES/NO-COLORS -- EDGES/WEIGHTS\n" + Style.RESET_ALL)
	#
	# for (node,data) in G.nodes(data=True):
	# 	print(node,data)
	# print('\n')
	# for (u,v,w) in G.edges(data=True):
	#     print(u,v,w)
	# print('\n')


	########################################################################
	#################### COLOURING/PROFITS CHOICE BLOCK ####################
	########################################################################

	print('\n')
	while(True):
	    maxc = int(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' COLOR MAX NUMBER ' + Fore.CYAN + '--- [ 0 <= colors <= ' + Fore.YELLOW + ' COLOR MAX NUMBER ' + Fore.CYAN + '] [ MUST BE <= ' + str(G.number_of_nodes()) + ' ]: ' + Style.RESET_ALL))
	    if(maxc <= G.number_of_nodes()):
	        break
	    else:
	        print(Style.BRIGHT + Fore.RED + "[!] INVALID VALUE --> NUMBER OF COLORS MUST BE <= NUMBER OF NODES (" + str(G.number_of_nodes()) + ")\n" + Style.RESET_ALL)
	        continue

	print("\n")
	maxp = int(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' PROFIT MAX VALUE ' + Fore.CYAN + '--- [ 0 <= profits <= ' + Fore.YELLOW + ' PROFIT MAX VALUE ' + Fore.CYAN + ']: ' + Style.RESET_ALL))

	print("\n")

	################################################################
	#################### COLORS LIST INIT BLOCK ####################
	################################################################

	colors = list(range(maxc))
	# print(Style.BRIGHT + Fore.RED + "COLORS (LIST)\n" + Style.RESET_ALL)
	# print(colors)
	# print("\n")

	with open(init_ext,'w') as f:
			f.write("\nCOLORS (LIST)\n\n" + str(colors))


	######################################################################
	#################### INITIAL COLOURING INIT BLOCK ####################
	######################################################################

	for (n,c) in G.nodes(data=True):
	    c['color'] = random.choice(colors)

	# print(Style.BRIGHT + Fore.RED + "NODE -- COLOR (LIST OF DICTIONARY) == INITIAL COLOURING\n" + Style.RESET_ALL)
	# for (node,data) in G.nodes(data=True):
	#     print(node,data)
	#
	# print("\nnumber of nodes:  " + str(G.number_of_nodes()))
	# print("\n")

	with open(init_ext,'a') as f:
		f.write("\n\n\nNODE -- COLOR (LIST OF DICTIONARY) == INITIAL COLOURING\n\n")
		for (node,data) in G.nodes(data=True):
			f.write(str(node) + " " + str(data) + "\n")
		f.write("\n[number of nodes] = " + str(G.number_of_nodes()))


	######################################################################
	#################### COLORS -- PROFITS INIT BLOCK ####################
	######################################################################

	profits = {node:{color:random.randint(0,maxp) for color in colors} for node in G.nodes()}

	# print(Style.BRIGHT + Fore.RED + "NODE -- COLORS -- PROFITS (NESTED DICTIONARY)\n" + Style.RESET_ALL)
	# pprint(profits)
	# print("\n")

	with open(init_ext,'a') as f:
		f.write("\n\n\nNODE -- COLORS -- PROFITS (NESTED DICTIONARY)\n\n")
		for k,v in profits.items():
			f.write(str(k) + " " + str(v) + "\n")


	#####################################################################
	#################### EDGE -- WEIGHTS PRINT BLOCK ####################
	#####################################################################

	# print(Style.BRIGHT + Fore.RED + "NODE -- NODE -- EDGE WEIGHT (LIST OF LIST OF DICTIONARY)\n" + Style.RESET_ALL)
	# for (u,v,w) in G.edges(data=True):
	#     print(u,v,w)
	#
	# print("\nnumber of edges:  " + str(G.number_of_edges()))
	# print("\n")

	with open(init_ext,'a') as f:
		f.write("\n\nNODE -- NODE -- EDGE WEIGHT (LIST OF LIST OF DICTIONARY)\n\n")
		for (u,v,w) in G.edges(data=True):
			f.write(str(u) + " " + str(v) + " " + str(w) + "\n")
		f.write("\n[number of edges] = " + str(G.number_of_edges()))


	###########################################################
	#################### MOVING .init FILE ####################
	###########################################################

	hub_dir = pathlib.Path.cwd().joinpath('result').joinpath(dirname)
	pathlib.Path(hub_dir).mkdir(parents=True, exist_ok=True)

	init_file_path = pathlib.Path.cwd().joinpath(init_ext)
	new_init_file_path = pathlib.Path.cwd().joinpath('result').joinpath(dirname).joinpath(init_ext)
	shutil.move(init_file_path, new_init_file_path)


	################################################################################################
	#################### GRAPH PRINT & INITIAL COLOURING MATPLOITLIB DRAW BLOCK ####################
	################################################################################################

	if(matplotlib):

		plt.figure("NODE -- EDGE VALUES [ INITIAL GRAPH ]")

		nx.draw_networkx(G, nx.circular_layout(G), with_labels=True, node_size=400, node_color='black', width=2.0, style='solid', font_color='white', font_weight='bold')

		edge_labels = nx.get_edge_attributes(G,'weight')
		nx.draw_networkx_edge_labels(G, nx.circular_layout(G), edge_labels = edge_labels)

		plt.axis('off')

		plt.figure("INITIAL NODE COLORS")

		nx.draw_networkx(G, nx.circular_layout(G), with_labels=False, node_size=400, node_color='yellow', width=2.0, style='solid', font_color='black', font_weight='bold')

		edge_labels = nx.get_edge_attributes(G,'weight')
		nx.draw_networkx_edge_labels(G, nx.circular_layout(G), edge_labels = edge_labels)

		node_labels = nx.get_node_attributes(G,'color')
		nx.draw_networkx_labels(G, nx.circular_layout(G), labels = node_labels, font_color = 'black', font_weight = 'bold')

		plt.axis('off')


	##############################################################
	#################### 'ZEROFILL' .out FILE ####################
	##############################################################

	with open(out_ext,'w') as f:
			f.write("")


	########################################################################
	#################### OPT / NASH / EXIT CHOICE BLOCK ####################
	########################################################################

	check_utilitarian_social_welfare = False;
	check_egalitarian_social_welfare = False;

	while(True):

		title = 'What do you want to calculate ?'

		# OPTIONS :
		#
		# optimal colouring (utilitarian social welfare)
		# optimal colouring (egalitarian social welfare)
		# stable colouring (nash equilibrium)
		# exit
		#

		options = ['optimal colouring [OPT -- UTILITARIAN SOCIAL WELFARE]', 'optimal colouring [OPT -- EGALITARIAN SOCIAL WELFARE]', 'stable colouring [NASH EQUILIBRIUM]', 'exit']
		option, index = pick(options, title, indicator='>', multi_select=False)


		################################################################################
		# optimal colouring computation [UTILITARIAN SOCIAL WELFARE]
		if option is "optimal colouring [OPT -- UTILITARIAN SOCIAL WELFARE]":

			start = time.time()
			limit = 60 # 1 minuto
			time_limit = False

			with open(out_ext,'a') as f:
				f.write("\n######################################################################\n[EXEC : UTILITARIAN SOCIAL WELFARE]\n\n\n")

			utilitarian_social_welfare = 0
			permutations = list(itertools.product(colors, repeat=G.number_of_nodes()))

			with open(out_ext,'a') as f:
				f.write("COLOR LIST PERMUTATION (pre-assignment)\n\n" + str(permutations) + "\n\n\n")
			# print(Style.BRIGHT + Fore.RED + 'COLOR LIST PERMUTATION (pre-assignment)\n' + Style.RESET_ALL)
			# print(permutations)
			# print('\n')
			for permutation in permutations:
				if(time.time() > start + limit):
					print(Style.BRIGHT + Back.MAGENTA + Fore.YELLOW + "\nTIME LIMIT REACHED !!!" + Style.RESET_ALL)
					time_limit = True
					with open(out_ext,'a') as f:
						f.write("\nTIME LIMIT REACHED !!!\n")
					break
				print("\n----------------------------------------------------------------------")
				colouring_old = permutation
				print(Style.BRIGHT + Fore.CYAN + str(colouring_old))
				for (node,data) in G.nodes(data=True):
					data['color'] = permutation[node]
					print(Style.BRIGHT + Fore.YELLOW + str("NODE " + str(node) + " --- COLOR " + str(data['color'])))
				temp_utilitarian_social_welfare = 0
				for (node,data) in G.nodes(data=True):
					temp_utilitarian_social_welfare += profits[node][data['color']]
					print(Style.BRIGHT + Fore.GREEN + "\nNODE " + str(node) + " --- COLOR " + str(data['color']) + Style.RESET_ALL)
					print(Style.BRIGHT + Fore.GREEN + "INITIAL PROFIT " + str(profits[node][data['color']]) + " ---> [TEMP] UTILITARIAN SOCIAL WELFARE " + str(temp_utilitarian_social_welfare) + Style.RESET_ALL)
					neighbors = G.neighbors(node)
					for neighbor in neighbors:
						if(G.node[neighbor]['color'] != G.node[node]['color']):
							edge_weight = G[node][neighbor]['weight']
							temp_utilitarian_social_welfare += edge_weight
							print("DIFFERENT COLORS --- NODES ( " + str(node) + ", " + str(neighbor) + " ) --- COLORS [ " + str(G.node[node]['color']) + " != " + str(G.node[neighbor]['color']) + " ] ---> ADD " + str(edge_weight) + " to [TEMP] UTILITARIAN SOCIAL WELFARE")
						else:
							print("EQUAL COLORS --- NODES ( " + str(node) + ", " + str(neighbor) + " ) --- COLORS [ " + str(G.node[node]['color']) + " == " + str(G.node[neighbor]['color']) + " ] ---> NO ADD")
					print(Style.BRIGHT + Fore.RED + "[TEMP] UTILITARIAN SOCIAL WELFARE VALUE " + str(temp_utilitarian_social_welfare) + Style.RESET_ALL + "\n")
				print(Style.BRIGHT + Fore.YELLOW + "\nUTILITARIAN SOCIAL WELFARE VALUE " + str(temp_utilitarian_social_welfare) + " --- COLOURING " + str(colouring_old) + Style.RESET_ALL + "\n")
				if(temp_utilitarian_social_welfare > utilitarian_social_welfare):
					print(Style.BRIGHT + Fore.CYAN + str(temp_utilitarian_social_welfare) + " > " + str(utilitarian_social_welfare) + Style.RESET_ALL)
					utilitarian_social_welfare = temp_utilitarian_social_welfare
					colouring_best = colouring_old
					print(Style.BRIGHT + Back.MAGENTA + Fore.CYAN + "\nBEST UTILITARIAN SOCIAL WELFARE VALUE " + str(utilitarian_social_welfare) + " --- COLOURING " + str(colouring_old) + Style.RESET_ALL + "\n")
					with open(out_ext,'a') as f:
						f.write("[NEW BEST] UTILITARIAN SOCIAL WELFARE ---> VALUE " + str(utilitarian_social_welfare) + " --- COLOURING " + str(colouring_old) + "\n")
				else:
					print(Style.BRIGHT + Fore.CYAN + str(temp_utilitarian_social_welfare) + " <= " + str(utilitarian_social_welfare) + Style.RESET_ALL)

			if(time_limit == False):
				print(Style.BRIGHT + Back.MAGENTA + Fore.YELLOW + "\n[FINAL] UTILITARIAN SOCIAL WELFARE VALUE " + str(utilitarian_social_welfare) + " --- COLOURING " + str(colouring_best) + Style.RESET_ALL)
				with open(out_ext,'a') as f:
					f.write("\n[FINAL] UTILITARIAN SOCIAL WELFARE ---> VALUE " + str(utilitarian_social_welfare) + " --- COLOURING " + str(colouring_best) + "\n")

				check_utilitarian_social_welfare = True;
				opt_utilitarian_social_welfare = utilitarian_social_welfare

			input("\nPress ENTER key to continue...")


		################################################################################
		# optimal colouring computation [EGALITARIAN SOCIAL WELFARE]
		if option is "optimal colouring [OPT -- EGALITARIAN SOCIAL WELFARE]":

			start = time.time()
			limit = 60 # 1 minuto
			time_limit = False

			with open(out_ext,'a') as f:
				f.write("\n######################################################################\n[EXEC : EGALITARIAN SOCIAL WELFARE]\n\n\n")

			temp_egalitarian_social_welfare = 0
			egalitarian_social_welfare = 0
			permutations = list(itertools.product(colors, repeat=G.number_of_nodes()))
			first_iter_check = True
			first_iter_opt_check = True

			with open(out_ext,'a') as f:
				f.write("COLOR LIST PERMUTATION (pre-assignment)\n\n" + str(permutations) + "\n\n\n")
			# print(Style.BRIGHT + Fore.RED + 'COLOR LIST PERMUTATION (pre-assignment)\n' + Style.RESET_ALL)
			# print(permutations)
			# print('\n')
			for permutation in permutations:
				if(time.time() > start + limit):
					print(Style.BRIGHT + Back.MAGENTA + Fore.YELLOW + "\nTIME LIMIT REACHED !!!" + Style.RESET_ALL)
					time_limit = True
					with open(out_ext,'a') as f:
						f.write("\nTIME LIMIT REACHED !!!\n")
					break
				print("\n----------------------------------------------------------------------")
				colouring_old = permutation
				print(Style.BRIGHT + Fore.CYAN + str(colouring_old))
				for (node,data) in G.nodes(data=True):
					data['color'] = permutation[node]
					print(Style.BRIGHT + Fore.YELLOW + str("NODE " + str(node) + " --- COLOR " + str(data['color'])))
				for (node,data) in G.nodes(data=True):
					local_egalitarian_social_welfare = 0
					local_egalitarian_social_welfare += profits[node][data['color']]
					print(Style.BRIGHT + Fore.GREEN + "\nNODE " + str(node) + " --- COLOR " + str(data['color']) + Style.RESET_ALL)
					print(Style.BRIGHT + Fore.GREEN + "INITIAL PROFIT " + str(profits[node][data['color']]) + " ---> [TEMP] EGALITARIAN SOCIAL WELFARE " + str(local_egalitarian_social_welfare) + Style.RESET_ALL)
					neighbors = G.neighbors(node)
					for neighbor in neighbors:
						if(G.node[neighbor]['color'] != G.node[node]['color']):
							edge_weight = G[node][neighbor]['weight']
							local_egalitarian_social_welfare += edge_weight
							print("DIFFERENT COLORS --- NODES ( " + str(node) + ", " + str(neighbor) + " ) --- COLORS [ " + str(G.node[node]['color']) + " != " + str(G.node[neighbor]['color']) + " ] ---> ADD " + str(edge_weight) + " to [LOCAL] EGALITARIAN SOCIAL WELFARE")
						else:
							print("EQUAL COLORS --- NODES ( " + str(node) + ", " + str(neighbor) + " ) --- COLORS [ " + str(G.node[node]['color']) + " == " + str(G.node[neighbor]['color']) + " ] ---> NO ADD")
					print(Style.BRIGHT + Fore.RED + "[LOCAL] EGALITARIAN SOCIAL WELFARE VALUE " + str(local_egalitarian_social_welfare) + Style.RESET_ALL + "\n")
					if(first_iter_check):
						temp_egalitarian_social_welfare = local_egalitarian_social_welfare
						first_iter_check = False
						print(Style.BRIGHT + Fore.MAGENTA + "[FIRST CYCLE] [TEMP] EGALITARIAN SOCIAL WELFARE " + str(temp_egalitarian_social_welfare) + Style.RESET_ALL)
						continue
					if(local_egalitarian_social_welfare < temp_egalitarian_social_welfare):
						print(Style.BRIGHT + Fore.MAGENTA + "[NEW BEST] [TEMP] EGALITARIAN SOCIAL WELFARE " + str(local_egalitarian_social_welfare) + " < " + str(temp_egalitarian_social_welfare) + Style.RESET_ALL)
						temp_egalitarian_social_welfare = local_egalitarian_social_welfare
					else:
						print(Style.BRIGHT + Fore.MAGENTA + "NO OP " + str(local_egalitarian_social_welfare) + " >= " + str(temp_egalitarian_social_welfare) + Style.RESET_ALL)
						continue
				print(Style.BRIGHT + Fore.YELLOW + "\nBEST [TEMP] EGALITARIAN SOCIAL WELFARE " + str(temp_egalitarian_social_welfare) + " --- COLOURING " + str(colouring_old) + Style.RESET_ALL + "\n")
				first_iter_check = True
				if(first_iter_opt_check):
					egalitarian_social_welfare = temp_egalitarian_social_welfare
					colouring_best = colouring_old
					first_iter_opt_check = False
					print(Style.BRIGHT + Fore.CYAN + "[FIRST CYCLE] [NEW BEST] EGALITARIAN SOCIAL WELFARE " + str(egalitarian_social_welfare) + " --- COLOURING " + str(colouring_best) + Style.RESET_ALL)
					continue
				if(temp_egalitarian_social_welfare > egalitarian_social_welfare):
					print(Style.BRIGHT + Fore.CYAN + "[NEW BEST] EGALITARIAN SOCIAL WELFARE " + str(temp_egalitarian_social_welfare) + " > " + str(egalitarian_social_welfare) + Style.RESET_ALL)
					egalitarian_social_welfare = temp_egalitarian_social_welfare
					colouring_best = colouring_old
					print(Style.BRIGHT + Fore.CYAN + "\nBEST SOCIAL WELFARE " + str(egalitarian_social_welfare) + " for COLOURING " + str(colouring_best) + Style.RESET_ALL + "\n")
					with open(out_ext,'a') as f:
						f.write("[NEW BEST] EGALITARIAN SOCIAL WELFARE ---> VALUE " + str(egalitarian_social_welfare) + " --- COLOURING " + str(colouring_best) + "\n")
				else:
					print(Style.BRIGHT + Fore.CYAN + "NO OP " + str(temp_egalitarian_social_welfare) + " <= " + str(egalitarian_social_welfare) + Style.RESET_ALL)

			if(time_limit == False):
				print(Style.BRIGHT + Back.MAGENTA + Fore.YELLOW + "\n[FINAL] EGALITARIAN SOCIAL WELFARE VALUE " + str(egalitarian_social_welfare) + " --- COLOURING " + str(colouring_best) + Style.RESET_ALL)
				with open(out_ext,'a') as f:
					f.write("\n[FINAL] EGALITARIAN SOCIAL WELFARE ---> VALUE " + str(egalitarian_social_welfare) + " --- COLOURING " + str(colouring_best) + "\n")

				check_egalitarian_social_welfare = True;
				opt_egalitarian_social_welfare = egalitarian_social_welfare

			input("\nPress ENTER key to continue...")


		################################################################################
		# stable colouring computation
		elif option is "stable colouring [NASH EQUILIBRIUM]":

			with open(out_ext,'a') as f:
				f.write("\n######################################################################\n[EXEC : NASH EQUILIBRIUM]\n\n\n")

			count = 0;
			restart = True
			last_improved_node = None

			while restart:
				restart = False
				for (node,data) in G.nodes(data=True):
					color_init = data['color']
					color_best = data['color']
					profit_old = profits[node][data['color']]
					if(node == last_improved_node):
						print("\n----------------------------------------------------------------------\n")
						print(Style.BRIGHT + Back.RED + Fore.WHITE + "&&&&&&&&&&&&&&&&&&&&&&&&& LAST IMPROVED NODE &&&&&&&&&&&&&&&&&&&&&&&&&" + Style.RESET_ALL)
						continue
					print("\n----------------------------------------------------------------------\n")
					print(Style.BRIGHT + Fore.GREEN + "\nNODE " + str(node) + " --- COLOR " + str(color_init) + Style.RESET_ALL)
					print(Style.BRIGHT + Fore.GREEN + "INITIAL PROFIT " + str(profit_old) + Style.RESET_ALL)
					neighbors = G.neighbors(node)
					for neighbor in neighbors:
						if(G.node[neighbor]['color'] != G.node[node]['color']):
							edge_weight = G[node][neighbor]['weight']
							profit_old += edge_weight
							print("DIFFERENT COLORS --- NODES ( " + str(node) + ", " + str(neighbor) + " ) --- COLORS [ " + str(G.node[node]['color']) + " != " + str(G.node[neighbor]['color']) + " ] ---> ADD " + str(edge_weight) + " to PROFIT")
						else:
							print("EQUAL COLORS --- NODES ( " + str(node) + ", " + str(neighbor) + " ) --- COLORS [ " + str(G.node[node]['color']) + " == " + str(G.node[neighbor]['color']) + " ] ---> NO ADD")
					print(Style.BRIGHT + Fore.GREEN + "TOTAL PROFIT " + str(profit_old) + Style.RESET_ALL + "\n")
					for current_color in colors:
						if(current_color != color_init):
							print(Style.BRIGHT + Fore.CYAN + "TEST COLOR " + str(current_color) + " --- NODE " + str(node) + " --- COLOR " + str(color_init) + Style.RESET_ALL)
							data['color'] = current_color
							color_new = current_color
							profit_new = profits[node][current_color]
							print(Style.BRIGHT + Fore.CYAN + "NEW INITIAL PROFIT " + str(profit_new) + Style.RESET_ALL)
							neighbors = G.neighbors(node)
							for neighbor in neighbors:
								if(G.node[neighbor]['color'] != G.node[node]['color']):
									edge_weight = G[node][neighbor]['weight']
									profit_new += edge_weight
									print("DIFFERENT COLORS --- NODES ( " + str(node) + ", " + str(neighbor) + " ) --- COLORS [ " + str(G.node[node]['color']) + " != " + str(G.node[neighbor]['color']) + " ] ---> ADD " + str(edge_weight) + " to PROFIT_NEW")
								else:
									print("EQUAL COLORS --- NODES ( " + str(node) + ", " + str(neighbor) + " ) --- COLORS [ " + str(G.node[node]['color']) + " == " + str(G.node[neighbor]['color']) + " ] ---> NO ADD")
							print(Style.BRIGHT + Fore.CYAN + "NEW TOTAL PROFIT " + str(profit_new) + Style.RESET_ALL)
							if(profit_new > profit_old):
								print(Style.BRIGHT + Fore.YELLOW + "\n" + str(profit_new) + " > " + str(profit_old) + "\n" + Style.RESET_ALL)
								profit_old = profit_new
								color_best = current_color
							else:
								print(Style.BRIGHT + Fore.YELLOW + "\n" + str(profit_new) + " <= " + str(profit_old) + "\n" + Style.RESET_ALL)
						else:
							print(Style.BRIGHT + Fore.RED + "NO TEST COLOR " + str(current_color) + " --- NODE " + str(node) + " --- COLOR " + str(color_init) + Style.RESET_ALL + "\n")
							continue
					data['color'] = color_best
					if(data['color'] != color_init):
						print(Style.BRIGHT + Back.MAGENTA + Fore.CYAN + "!!!!!!!!!!!!!!!!!!!!!!!!!!! IMPROVING MOVE !!!!!!!!!!!!!!!!!!!!!!!!!!!" + Style.RESET_ALL)
						print(Style.BRIGHT + Fore.YELLOW + "NEW COLOR " + str(data['color']) + " --- NODE " + str(node) + " --- NEW PROFIT " + str(profit_old) + Style.RESET_ALL)
						count += 1
						print(Style.BRIGHT + Fore.YELLOW + "NEW COUNT VALUE " + str(count) + Style.RESET_ALL)
						restart = True
						last_improved_node = node
						print(Style.BRIGHT + Fore.YELLOW + "LAST IMPROVED NODE " + str(last_improved_node) + Style.RESET_ALL)
						print(Style.BRIGHT + Back.MAGENTA + Fore.CYAN + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!! RESTARTING !!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + Style.RESET_ALL)
						with open(out_ext,'a') as f:
							f.write("[IMPROVING MOVE] [NEW BEST] COLOR " + str(data['color']) + " --- NODE " + str(node) + " --- [NEW BEST] PROFIT " + str(profit_old) + "\n")
						break

			print(Style.BRIGHT + Fore.YELLOW + "\n#######################################################################" + Style.RESET_ALL)
			egalitarian_social_welfare = 0
			utilitarian_social_welfare = 0
			first_iter_check = True
			for (node,data) in G.nodes(data=True):
				print("\n----------------------------------------------------------------------\n")
				print(Style.BRIGHT + Fore.GREEN + "\nNODE " + str(node) + " --- COLOR " + str(data['color']) + Style.RESET_ALL)
				print(Style.BRIGHT + Fore.GREEN + "INITIAL PROFIT " + str(profits[node][data['color']]) + " ---> UTILITARIAN SOCIAL WELFARE " + str(utilitarian_social_welfare) + Style.RESET_ALL)
				temp_egalitarian_social_welfare = 0
				temp_egalitarian_social_welfare += profits[node][data['color']]
				utilitarian_social_welfare += profits[node][data['color']]
				print(Style.BRIGHT + Fore.YELLOW + "\n[TEMP] EGALITARIAN VALUE " + str(temp_egalitarian_social_welfare) + Style.RESET_ALL)
				print(Style.BRIGHT + Fore.YELLOW + "UTILITARIAN VALUE " + str(utilitarian_social_welfare) + Style.RESET_ALL)
				neighbors = G.neighbors(node)
				for neighbor in neighbors:
					if(G.node[neighbor]['color'] != G.node[node]['color']):
						edge_weight = G[node][neighbor]['weight']
						print("DIFFERENT COLORS --- NODES ( " + str(node) + ", " + str(neighbor) + " ) --- COLORS [ " + str(G.node[node]['color']) + " != " + str(G.node[neighbor]['color']) + " ] ---> ADD " + str(edge_weight) + " to UTILITARIAN SOCIAL WELFARE and [TEMP] EGALITARIAN SOCIAL WELFARE")
						utilitarian_social_welfare += edge_weight
						temp_egalitarian_social_welfare += edge_weight
					else:
						print("EQUAL COLORS --- NODES ( " + str(node) + ", " + str(neighbor) + " ) --- COLORS [ " + str(G.node[node]['color']) + " == " + str(G.node[neighbor]['color']) + " ] ---> NO ADD")
				print(Style.BRIGHT + Fore.YELLOW + "\n[TEMP] EGALITARIAN VALUE " + str(temp_egalitarian_social_welfare) + Style.RESET_ALL)
				print(Style.BRIGHT + Fore.YELLOW + "UTILITARIAN VALUE " + str(utilitarian_social_welfare) + Style.RESET_ALL)
				if(first_iter_check):
					egalitarian_social_welfare = temp_egalitarian_social_welfare
					first_iter_check = False
					print(Style.BRIGHT + Fore.CYAN + "\n[FIRST ITER] EGALITARIAN " + str(egalitarian_social_welfare) + "\nUTILITARIAN " + str(utilitarian_social_welfare) + Style.RESET_ALL)
					continue
				if(temp_egalitarian_social_welfare < egalitarian_social_welfare):
					egalitarian_social_welfare = temp_egalitarian_social_welfare
					print(Style.BRIGHT + Fore.CYAN + "\n[<] NEW EGALITARIAN " + str(egalitarian_social_welfare) + "\nUTILITARIAN " + str(utilitarian_social_welfare) + Style.RESET_ALL)
				else:
					print(Style.BRIGHT + Fore.RED + "\n[>=] EGALITARIAN " + str(egalitarian_social_welfare) + "\nUTILITARIAN " + str(utilitarian_social_welfare) + Style.RESET_ALL)


			print(Style.BRIGHT + Back.MAGENTA + Fore.YELLOW + "\n[FINAL] EGALITARIAN " + str(egalitarian_social_welfare) + Style.RESET_ALL + Style.BRIGHT + Back.MAGENTA + Fore.YELLOW + "\n\n[FINAL] UTILITARIAN " + str(utilitarian_social_welfare) + Style.RESET_ALL)
			print(Style.BRIGHT + Back.MAGENTA + Fore.YELLOW + "\n[FINAL] COUNT " + str(count) + Style.RESET_ALL)

			with open(out_ext,'a') as f:
				f.write("\n[FINAL] EGALITARIAN SOCIAL WELFARE ---> VALUE " + str(egalitarian_social_welfare))
				f.write("\n[FINAL] UTILITARIAN SOCIAL WELFARE ---> VALUE " + str(utilitarian_social_welfare))
				f.write("\n[FINAL] COUNT ---> VALUE " + str(count))

			nash_utilitarian_social_welfare = utilitarian_social_welfare
			nash_egalitarian_social_welfare = egalitarian_social_welfare

			if(check_utilitarian_social_welfare):
				utilitarian_price_of_anarchy = opt_utilitarian_social_welfare / nash_utilitarian_social_welfare
				with open(out_ext,'a') as f:
					f.write("\n\n######################################################################\n[EXEC : UTILITARIAN PRICE OF ANARCHY]\n\n")
					f.write("\n[OPT] UTILITARIAN SOCIAL WELFARE : " + str(opt_utilitarian_social_welfare) + " / [NASH] UTILITARIAN SOCIAL WELFARE : " + str(nash_utilitarian_social_welfare) + " = " + str(utilitarian_price_of_anarchy))

			if(check_egalitarian_social_welfare):
				egalitarian_price_of_anarchy = opt_egalitarian_social_welfare / nash_egalitarian_social_welfare
				with open(out_ext,'a') as f:
					f.write("\n\n######################################################################\n[EXEC : EGALITARIAN PRICE OF ANARCHY]\n\n")
					f.write("\n[OPT] EGALITARIAN SOCIAL WELFARE : " + str(opt_egalitarian_social_welfare) + " / [NASH] EGALITARIAN SOCIAL WELFARE : " + str(nash_egalitarian_social_welfare) + " = " + str(egalitarian_price_of_anarchy))

			break


		################################################################################
		elif option is "exit":
			break


	################################################################################
	#################### FINAL COLOURING MATPLOITLIB DRAW BLOCK ####################
	################################################################################

	if(matplotlib):

		plt.figure("FINAL NODE COLORS [ NASH EQUILIBRIUM ]")

		nx.draw_networkx(G, nx.circular_layout(G), with_labels=False, node_size=400, node_color='orange', width=2.0, style='solid', font_color='black', font_weight='bold')

		edge_labels = nx.get_edge_attributes(G,'weight')
		nx.draw_networkx_edge_labels(G, nx.circular_layout(G), edge_labels = edge_labels)

		node_labels = nx.get_node_attributes(G,'color')
		nx.draw_networkx_labels(G, nx.circular_layout(G), labels = node_labels, font_color = 'black', font_weight = 'bold')

		plt.axis('off')

		plt.show()


	##########################################################
	#################### MOVING .out FILE ####################
	##########################################################

	out_file_path = pathlib.Path.cwd().joinpath(out_ext)
	new_out_file_path = pathlib.Path.cwd().joinpath('result').joinpath(dirname).joinpath(out_ext)
	shutil.move(out_file_path, new_out_file_path)


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

if option is "MULTIPLE EXEC":


	#######################################################
	#################### SEARCH BLOCK #####################
	#######################################################

	list_hub_dir = []

	p = pathlib.Path.cwd().parents[0].joinpath('generator').joinpath('mgen')
	hub_path = [x for x in p.iterdir() if x.is_dir()]

	for path in hub_path:
		list_hub_dir.append(path.name)

	title = 'hub dir select '

	# DIRECTORY SELECTION :
	#
	#
	#
	#

	options = list_hub_dir
	option, index = pick(options, title, indicator='>', multi_select=False)

	p = pathlib.Path.cwd().parents[0].joinpath('generator').joinpath('mgen').joinpath(option)
	[x for x in p.iterdir() if x.is_dir()]

	a = list(p.glob('**/*.edgelist'))


	filelist =[]
	optionfilelist =[]
	absfilepath =[]

	for i in a :
		rel = pathlib.Path(*i.parts[8:])
		optionfilelist.append(str(rel)) #string path from /hedonic
		absfilepath.append(str(i)) # string path from root
		filelist.append(i) # pathlib path from root


	############################################################
	#################### PATH ELEMENTS INIT ####################
	############################################################

	dirname = str(option)
	init_ext = str(option) + ".init"
	out_ext = str(option) + ".out"


	#########################################################################
	#################### 'ZEROFILL' .init and .out FILES ####################
	#########################################################################

	with open(init_ext,'w') as f:
			f.write("")

	with open(out_ext,'w') as f:
			f.write("")


	########################################################
	#################### ITERATION INIT ####################
	########################################################

	first_iter = True
	for i in range(len(absfilepath)):

		G = nx.read_edgelist(absfilepath[i], nodetype=int, edgetype=int, create_using=nx.Graph())

		########################################################################
		#################### COLOURING/PROFITS CHOICE BLOCK ####################
		########################################################################

		if first_iter:

			# print("\n")
			# out_name = str(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' NAME ' + Fore.CYAN + 'for ' + Fore.YELLOW + ' OUTPUT FILE ' + Fore.CYAN + ': ' + Style.RESET_ALL))
			# out_ext = str(out_name) + ".out"

			# print("\n")
			# title = 'STATIC MODE or DINAMIC MODE for color insert ? '
			#
			# # FILESYSTEM :
			# #
			# # STATIC MODE
			# # DINAMIC MODE
			# #
			# #
			#
			# options = ['STATIC MODE ---> ([input]:numero di colori <= numero di nodi)', 'DINAMIC MODE ---> numero di colori = (numero di nodi - [input]:valore da sottrarre)']
			# option, index = pick(options, title, indicator='>', multi_select=False)
			#
			# if option is "STATIC MODE ---> ([input]:numero di colori <= numero di nodi)":
			# 	dinamic_mode = False
			# 	while(True):
			# 	    maxc = int(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' COLOR MAX NUMBER ' + Fore.CYAN + '--- [ 0 <= colors <= ' + Fore.YELLOW + ' COLOR MAX NUMBER ' + Fore.CYAN + '] : ' + Style.RESET_ALL))
			# 	    if(maxc <= G.number_of_nodes()):
			# 	        break
			# 	    else:
			# 	        print(Style.BRIGHT + Fore.RED + "[!] INVALID VALUE --> NUMBER OF COLORS MUST BE <= NUMBER OF NODES (" + str(G.number_of_nodes()) + ")\n" + Style.RESET_ALL)
			# 	        continue
			#
			# elif option is "DINAMIC MODE ---> numero di colori = (numero di nodi - [input]:valore da sottrarre)":
			# 	dinamic_mode = True
			# 	while(True):
			# 	    maxc = int(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' VALUE TO SUBTRACT ' + Fore.CYAN + '--- number_of_colors = [ number_of_nodes - ' + Fore.YELLOW + ' VALUE TO SUBTRACT ' + Fore.CYAN + '] : ' + Style.RESET_ALL))
			# 	    if(maxc < G.number_of_nodes()):
			# 	        break
			# 	    else:
			# 	        print(Style.BRIGHT + Fore.RED + "[!] INVALID VALUE --> VALUE TO SUBTRACT MUST BE < NUMBER OF NODES (" + str(G.number_of_nodes()) + ")\n" + Style.RESET_ALL)
			# 	        continue
			#


			print("\n")
			maxp = int(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' PROFIT MAX VALUE ' + Fore.CYAN + '--- [ 0 <= profits <= ' + Fore.YELLOW + ' PROFIT MAX VALUE ' + Fore.CYAN + ']: ' + Style.RESET_ALL))

			print("\n")
			first_iter = False


		################################################################
		#################### COLORS LIST INIT BLOCK ####################
		################################################################

		with open(init_ext,'a') as f:
			f.write("\n\n\n######################################################################\n[INIT : " + str(a[i].name) + "]\n\n")

		# if dinamic_mode:
		# 	# print(Style.BRIGHT + Fore.RED + "COLORS (LIST)\n" + Style.RESET_ALL)
		# 	colors = list(range(G.number_of_nodes() - maxc))
		# 	num_colors = len(colors)
		# 	# print(colors)
		# 	# print("\n")
		# 	with open(init_ext,'a') as f:
		# 			f.write("\nCOLORS (LIST) [DINAMIC MODE]\n\n" + str(colors) + "\n\n" + str(num_colors))
		#
		# else:
		# 	# print(Style.BRIGHT + Fore.RED + "COLORS (LIST)\n" + Style.RESET_ALL)
		# 	colors = list(range(maxc))
		# 	num_colors = len(colors)
		# 	# print(colors)
		# 	# print("\n")
		# 	with open(init_ext,'a') as f:
		# 			f.write("\nCOLORS (LIST) [STATIC MODE]\n\n" + str(colors) + "\n\n[number of colors] = " + str(num_colors))


		random_node_number = random.randint(2,G.number_of_nodes())

		print(Style.BRIGHT + Fore.RED + "COLORS (LIST)\n" + Style.RESET_ALL)
		colors = list(range(random_node_number))
		num_colors = len(colors)
		# print(colors)
		# print("\n")
		with open(init_ext,'a') as f:
				f.write("\nCOLORS (LIST)\n\n" + str(colors) + "\n\n" + str(num_colors))


		######################################################################
		#################### INITIAL COLOURING INIT BLOCK ####################
		######################################################################

		for (n,c) in G.nodes(data=True):
		    c['color'] = random.choice(colors)

		# print(Style.BRIGHT + Fore.RED + "NODE -- COLOR (LIST OF DICTIONARY) == INITIAL COLOURING\n" + Style.RESET_ALL)
		# for (node,data) in G.nodes(data=True):
		#     print(node,data)
		#
		# print("\nnumber of nodes:  " + str(G.number_of_nodes()))
		# print("\n")

		with open(init_ext,'a') as f:
			f.write("\n\n\nNODE -- COLOR (LIST OF DICTIONARY) == INITIAL COLOURING\n\n")
			for (node,data) in G.nodes(data=True):
				f.write(str(node) + " " + str(data) + "\n")
			f.write("\n[number of nodes] = " + str(G.number_of_nodes()))


		######################################################################
		#################### COLORS -- PROFITS INIT BLOCK ####################
		######################################################################


		profits = {node:{color:random.randint(0,maxp) for color in colors} for node in G.nodes()}

		# print(Style.BRIGHT + Fore.RED + "NODE -- COLORS -- PROFITS (NESTED DICTIONARY)\n" + Style.RESET_ALL)
		# pprint(profits)
		# print("\n")

		with open(init_ext,'a') as f:
			f.write("\n\n\nNODE -- COLORS -- PROFITS (NESTED DICTIONARY)\n\n")
			for k,v in profits.items():
				f.write(str(k) + " " + str(v) + "\n")


		#####################################################################
		#################### EDGE -- WEIGHTS PRINT BLOCK ####################
		#####################################################################

		# print(Style.BRIGHT + Fore.RED + "NODE -- NODE -- EDGE WEIGHT (LIST OF LIST OF DICTIONARY)\n" + Style.RESET_ALL)
		# for (u,v,w) in G.edges(data=True):
		#     print(u,v,w)
		#
		# print("\nnumber of edges:  " + str(G.number_of_edges()))
		# print("\n")

		with open(init_ext,'a') as f:
			f.write("\n\nNODE -- NODE -- EDGE WEIGHT (LIST OF LIST OF DICTIONARY)\n\n")
			for (u,v,w) in G.edges(data=True):
				f.write(str(u) + " " + str(v) + " " + str(w) + "\n")
			f.write("\n[number of edges] = " + str(G.number_of_edges()))


		##########################################################
		#################### K-COLORING BLOCK ####################
		##########################################################

		with open(out_ext,'a') as f:
			f.write("\n\n\n######################################################################\n[EXEC : NASH EQUILIBRIUM]\n[GRAPH : " + str(a[i].name) + "]\n[COLORS : " + str(num_colors) + "]\n\n")

		start = time.time()
		limit = 60 # 1 minuto
		time_limit = False

		count = 0;
		restart = True
		last_improved_node = None

		while restart:
			if(time.time() > start + limit):
				print(Style.BRIGHT + Back.MAGENTA + Fore.YELLOW + "\nTIME LIMIT REACHED !!!" + Style.RESET_ALL)
				time_limit = True
				with open(out_ext,'a') as f:
					f.write("\nTIME LIMIT REACHED !!!")
				break
			restart = False
			for (node,data) in G.nodes(data=True):
				color_init = data['color']
				color_best = data['color']
				profit_old = profits[node][data['color']]
				if(node == last_improved_node):
					print("\n----------------------------------------------------------------------\n")
					print(Style.BRIGHT + Back.RED + Fore.WHITE + "&&&&&&&&&&&&&&&&&&&&&&&&& LAST IMPROVED NODE &&&&&&&&&&&&&&&&&&&&&&&&&" + Style.RESET_ALL)
					continue
				print("\n----------------------------------------------------------------------\n")
				print(Style.BRIGHT + Fore.GREEN + "\nNODE " + str(node) + " --- COLOR " + str(color_init) + Style.RESET_ALL)
				print(Style.BRIGHT + Fore.GREEN + "INITIAL PROFIT " + str(profit_old) + Style.RESET_ALL)
				neighbors = G.neighbors(node)
				for neighbor in neighbors:
					if(G.node[neighbor]['color'] != G.node[node]['color']):
						edge_weight = G[node][neighbor]['weight']
						profit_old += edge_weight
						print("DIFFERENT COLORS --- NODES ( " + str(node) + ", " + str(neighbor) + " ) --- COLORS [ " + str(G.node[node]['color']) + " != " + str(G.node[neighbor]['color']) + " ] ---> ADD " + str(edge_weight) + " to PROFIT")
					else:
						print("EQUAL COLORS --- NODES ( " + str(node) + ", " + str(neighbor) + " ) --- COLORS [ " + str(G.node[node]['color']) + " == " + str(G.node[neighbor]['color']) + " ] ---> NO ADD")
				print(Style.BRIGHT + Fore.GREEN + "TOTAL PROFIT " + str(profit_old) + Style.RESET_ALL + "\n")
				for current_color in colors:
					if(current_color != color_init):
						print(Style.BRIGHT + Fore.CYAN + "TEST COLOR " + str(current_color) + " --- NODE " + str(node) + " --- COLOR " + str(color_init) + Style.RESET_ALL)
						data['color'] = current_color
						color_new = current_color
						profit_new = profits[node][current_color]
						print(Style.BRIGHT + Fore.CYAN + "NEW INITIAL PROFIT " + str(profit_new) + Style.RESET_ALL)
						neighbors = G.neighbors(node)
						for neighbor in neighbors:
							if(G.node[neighbor]['color'] != G.node[node]['color']):
								edge_weight = G[node][neighbor]['weight']
								profit_new += edge_weight
								print("DIFFERENT COLORS --- NODES ( " + str(node) + ", " + str(neighbor) + " ) --- COLORS [ " + str(G.node[node]['color']) + " != " + str(G.node[neighbor]['color']) + " ] ---> ADD " + str(edge_weight) + " to PROFIT_NEW")
							else:
								print("EQUAL COLORS --- NODES ( " + str(node) + ", " + str(neighbor) + " ) --- COLORS [ " + str(G.node[node]['color']) + " == " + str(G.node[neighbor]['color']) + " ] ---> NO ADD")
						print(Style.BRIGHT + Fore.CYAN + "NEW TOTAL PROFIT " + str(profit_new) + Style.RESET_ALL)
						if(profit_new > profit_old):
							print(Style.BRIGHT + Fore.YELLOW + "\n" + str(profit_new) + " > " + str(profit_old) + "\n" + Style.RESET_ALL)
							profit_old = profit_new
							color_best = current_color
						else:
							print(Style.BRIGHT + Fore.YELLOW + "\n" + str(profit_new) + " <= " + str(profit_old) + "\n" + Style.RESET_ALL)
					else:
						print(Style.BRIGHT + Fore.RED + "NO TEST COLOR " + str(current_color) + " --- NODE " + str(node) + " --- COLOR " + str(color_init) + Style.RESET_ALL + "\n")
						continue
				data['color'] = color_best
				if(data['color'] != color_init):
					print(Style.BRIGHT + Back.MAGENTA + Fore.CYAN + "!!!!!!!!!!!!!!!!!!!!!!!!!!! IMPROVING MOVE !!!!!!!!!!!!!!!!!!!!!!!!!!!" + Style.RESET_ALL)
					print(Style.BRIGHT + Fore.YELLOW + "NEW COLOR " + str(data['color']) + " --- NODE " + str(node) + " --- NEW PROFIT " + str(profit_old) + Style.RESET_ALL)
					count += 1
					print(Style.BRIGHT + Fore.YELLOW + "NEW COUNT VALUE " + str(count) + Style.RESET_ALL)
					restart = True
					last_improved_node = node
					print(Style.BRIGHT + Fore.YELLOW + "LAST IMPROVED NODE " + str(last_improved_node) + Style.RESET_ALL)
					print(Style.BRIGHT + Back.MAGENTA + Fore.CYAN + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!! RESTARTING !!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + Style.RESET_ALL)
					with open(out_ext,'a') as f:
						f.write("[IMPROVING MOVE] [NEW BEST] COLOR " + str(data['color']) + " --- NODE " + str(node) + " --- [NEW BEST] PROFIT " + str(profit_old) + "\n")
					break

		if(time_limit == False):
			print(Style.BRIGHT + Fore.YELLOW + "\n#######################################################################" + Style.RESET_ALL)
			egalitarian_social_welfare = 0
			utilitarian_social_welfare = 0
			first_iter_check = True
			for (node,data) in G.nodes(data=True):
				print("\n----------------------------------------------------------------------\n")
				print(Style.BRIGHT + Fore.GREEN + "\nNODE " + str(node) + " --- COLOR " + str(data['color']) + Style.RESET_ALL)
				print(Style.BRIGHT + Fore.GREEN + "INITIAL PROFIT " + str(profits[node][data['color']]) + " ---> UTILITARIAN SOCIAL WELFARE " + str(utilitarian_social_welfare) + Style.RESET_ALL)
				temp_egalitarian_social_welfare = 0
				temp_egalitarian_social_welfare += profits[node][data['color']]
				utilitarian_social_welfare += profits[node][data['color']]
				print(Style.BRIGHT + Fore.YELLOW + "\n[TEMP] EGALITARIAN VALUE " + str(temp_egalitarian_social_welfare) + Style.RESET_ALL)
				print(Style.BRIGHT + Fore.YELLOW + "UTILITARIAN VALUE " + str(utilitarian_social_welfare) + Style.RESET_ALL)
				neighbors = G.neighbors(node)
				for neighbor in neighbors:
					if(G.node[neighbor]['color'] != G.node[node]['color']):
						edge_weight = G[node][neighbor]['weight']
						print("DIFFERENT COLORS --- NODES ( " + str(node) + ", " + str(neighbor) + " ) --- COLORS [ " + str(G.node[node]['color']) + " != " + str(G.node[neighbor]['color']) + " ] ---> ADD " + str(edge_weight) + " to UTILITARIAN SOCIAL WELFARE and [TEMP] EGALITARIAN SOCIAL WELFARE")
						utilitarian_social_welfare += edge_weight
						temp_egalitarian_social_welfare += edge_weight
					else:
						print("EQUAL COLORS --- NODES ( " + str(node) + ", " + str(neighbor) + " ) --- COLORS [ " + str(G.node[node]['color']) + " == " + str(G.node[neighbor]['color']) + " ] ---> NO ADD")
				print(Style.BRIGHT + Fore.YELLOW + "\n[TEMP] EGALITARIAN VALUE " + str(temp_egalitarian_social_welfare) + Style.RESET_ALL)
				print(Style.BRIGHT + Fore.YELLOW + "UTILITARIAN VALUE " + str(utilitarian_social_welfare) + Style.RESET_ALL)
				if(first_iter_check):
					egalitarian_social_welfare = temp_egalitarian_social_welfare
					first_iter_check = False
					print(Style.BRIGHT + Fore.CYAN + "\n[FIRST ITER] EGALITARIAN " + str(egalitarian_social_welfare) + "\nUTILITARIAN " + str(utilitarian_social_welfare) + Style.RESET_ALL)
					continue
				if(temp_egalitarian_social_welfare < egalitarian_social_welfare):
					egalitarian_social_welfare = temp_egalitarian_social_welfare
					print(Style.BRIGHT + Fore.CYAN + "\n[<] NEW EGALITARIAN " + str(egalitarian_social_welfare) + "\nUTILITARIAN " + str(utilitarian_social_welfare) + Style.RESET_ALL)
				else:
					print(Style.BRIGHT + Fore.RED + "\n[>=] EGALITARIAN " + str(egalitarian_social_welfare) + "\nUTILITARIAN " + str(utilitarian_social_welfare) + Style.RESET_ALL)


			print(Style.BRIGHT + Back.MAGENTA + Fore.YELLOW + "\n[FINAL] EGALITARIAN " + str(egalitarian_social_welfare) + Style.RESET_ALL + Style.BRIGHT + Back.MAGENTA + Fore.YELLOW + "\n\n[FINAL] UTILITARIAN " + str(utilitarian_social_welfare) + Style.RESET_ALL)
			print(Style.BRIGHT + Back.MAGENTA + Fore.YELLOW + "\n[FINAL] COUNT " + str(count) + Style.RESET_ALL)

			with open(out_ext,'a') as f:
				f.write("\n[FINAL] EGALITARIAN SOCIAL WELFARE ---> VALUE " + str(egalitarian_social_welfare))
				f.write("\n[FINAL] UTILITARIAN SOCIAL WELFARE ---> VALUE " + str(utilitarian_social_welfare))
				f.write("\n[FINAL] COUNT ---> VALUE " + str(count))


	###########################################################
	#################### MOVING .init FILE ####################
	###########################################################

	hub_dir = pathlib.Path.cwd().joinpath('mresult').joinpath(dirname)
	pathlib.Path(hub_dir).mkdir(parents=True, exist_ok=True)

	init_file_path = pathlib.Path.cwd().joinpath(init_ext)
	new_init_file_path = pathlib.Path.cwd().joinpath('mresult').joinpath(dirname).joinpath(init_ext)
	shutil.move(init_file_path, new_init_file_path)

	##########################################################
	#################### MOVING .out FILE ####################
	##########################################################

	out_file_path = pathlib.Path.cwd().joinpath(out_ext)
	new_out_file_path = pathlib.Path.cwd().joinpath('mresult').joinpath(dirname).joinpath(out_ext)
	shutil.move(out_file_path, new_out_file_path)
