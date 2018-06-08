import os
import shutil
import pathlib
import platform
import random
import networkx as nx
import matplotlib.pyplot as plt
import pydot

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

title = 'Select PROGRAM MODE'

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

	print('\n')
	for (node,data) in G.nodes(data=True):
	    print(node,data)
	print('\n')
	for (u,v,w) in G.edges(data=True):
	    print(u,v,w)
	print('\n')


	########################################################################
	#################### COLOURING/PROFITS CHOICE BLOCK ####################
	########################################################################

	while(True):
	    maxc = int(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' MAX COLOR ' + Fore.CYAN + 'range int number [ 0 <= colors <= ' + Fore.YELLOW + ' MAX COLOR ' + Fore.CYAN + '] [ <= ' + str(G.number_of_nodes()) + ' ]: ' + Style.RESET_ALL))
	    if(maxc <= G.number_of_nodes()):
	        break
	    else:
	        print(Style.BRIGHT + Fore.RED + "[!] INVALID VALUE --> NUMBER OF COLORS MUST BE <= NUMBER OF NODES (" + str(G.number_of_nodes()) + ")\n" + Style.RESET_ALL)
	        continue

	print("\n")
	maxp = int(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' MAX PROFIT ' + Fore.CYAN + 'range int number: [ 0 <= profit <= ' + Fore.YELLOW + ' MAX PROFIT ' + Fore.CYAN + ']: ' + Style.RESET_ALL))

	print("\n")


	################################################################
	#################### COLORS LIST INIT BLOCK ####################
	################################################################

	print(Style.BRIGHT + Fore.RED + "COLORS (LIST)\n" + Style.RESET_ALL)
	colors = list(range(maxc))
	print(colors)
	print("\n")


	######################################################################
	#################### INITIAL COLOURING INIT BLOCK ####################
	######################################################################

	for (n,c) in G.nodes(data=True):
	    c['color'] = random.choice(colors)

	print(Style.BRIGHT + Fore.RED + "NODE -- COLOR (LIST OF DICTIONARY) == INITIAL COLOURING\n" + Style.RESET_ALL)
	for (node,data) in G.nodes(data=True):
	    print(node,data)

	print("\nnumber of nodes:  " + str(G.number_of_nodes()))
	print("\n")


	######################################################################
	#################### COLORS -- PROFITS INIT BLOCK ####################
	######################################################################

	print(Style.BRIGHT + Fore.RED + "NODE -- COLORS -- PROFITS (NESTED DICTIONARY)\n" + Style.RESET_ALL)

	result = {node:{color:random.randint(0,maxp) for color in colors} for node in G.nodes()}

	pprint(result)
	print("\n")


	#####################################################################
	#################### EDGE -- WEIGHTS PRINT BLOCK ####################
	#####################################################################

	print(Style.BRIGHT + Fore.RED + "NODE -- NODE -- EDGE WEIGHT (LIST OF LIST OF DICTIONARY)\n" + Style.RESET_ALL)
	for (u,v,w) in G.edges(data=True):
	    print(u,v,w)

	print("\nnumber of edges:  " + str(G.number_of_edges()))
	print("\n")


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


	########################################################################
	#################### OPT / NASH / EXIT CHOICE BLOCK ####################
	########################################################################

	while(True):

		title = 'What do you want to calculate ?'

		# OPTIONS :
		#
		# optimal colouring
		# stable colouring (nash equilibrium)
		# exit
		#

		options = ['optimal colouring [OPT -- UTILITARIAN SOCIAL WELFARE]', 'optimal colouring [OPT -- EGALITARIAN SOCIAL WELFARE]', 'stable colouring [NASH EQUILIBRIUM]', 'exit']
		option, index = pick(options, title, indicator='>', multi_select=False)


		################################################################################
		# optimal colouring computation [UTILITARIAN SOCIAL WELFARE]
		if option is "optimal colouring [OPT -- UTILITARIAN SOCIAL WELFARE]":

			social_welfare_old = 0
			permlist = list(itertools.product(colors, repeat=G.number_of_nodes()))

			print(Style.BRIGHT + Fore.RED + 'COLOR LIST PERMUTATION (pre-assignment)\n' + Style.RESET_ALL)
			print(permlist)
			print('\n')
			for perm in permlist:
				print("\n----------------------------------------------------------------------")
				colouring_old = perm
				print(colouring_old)
				for (node,data) in G.nodes(data=True):
					data['color'] = perm[node]
					print(str("color " + str(data['color'])) + " for node " + str(node))
				temp_social_welfare = 0
				for (node,data) in G.nodes(data=True):
					temp_social_welfare += result[node][data['color']]
					print(Style.BRIGHT + Fore.GREEN + "\n$$$$$$$$$$ NODE " + str(node) + " with COLOR " + str(data['color']) + Style.RESET_ALL)
					print(Style.BRIGHT + Fore.GREEN + "sommo INITIAL PROFIT " + str(result[node][data['color']]) + " a SOCIAL WELFARE TEMP " + str(temp_social_welfare) + Style.RESET_ALL)
					neighbors = G.neighbors(node)
					for neighbor in neighbors:
						if(G.node[neighbor]['color'] != G.node[node]['color']):
							edgeweight = G[node][neighbor]['weight']
							temp_social_welfare += edgeweight
							print("colore DIVERSO per i nodi ( " + str(node) + ", " + str(neighbor) + " ) = [ " + str(G.node[node]['color']) + " != " + str(G.node[neighbor]['color']) + " ] SOMMO " + str(edgeweight) + " a temp_social_welfare")
						else:
							print("colore UGUALE per i nodi ( " + str(node) + ", " + str(neighbor) + " ) = [ " + str(G.node[node]['color']) + " == " + str(G.node[neighbor]['color']) + " ] NON SOMMO NULLA a temp_social_welfare")
					print(Style.BRIGHT + Fore.RED + "temp SOCIAL WELFARE VALUE is " + str(temp_social_welfare) + Style.RESET_ALL + "\n")
				print(Style.BRIGHT + Fore.YELLOW + "\nTOTAL SOCIAL WELFARE VALUE is " + str(temp_social_welfare) + " for COLOURING " + str(colouring_old) + Style.RESET_ALL + "\n")
				if(temp_social_welfare > social_welfare_old):
					print(Style.BRIGHT + Fore.MAGENTA + str(temp_social_welfare) + " > " + str(social_welfare_old) + Style.RESET_ALL)
					social_welfare_old = temp_social_welfare
					colouring_best = colouring_old
					print(Style.BRIGHT + Fore.CYAN + "BEST SOCIAL WELFARE : " + str(social_welfare_old) + " for COLOURING " + str(colouring_old) + Style.RESET_ALL + "\n")
				else:
					print(Style.BRIGHT + Fore.MAGENTA + str(temp_social_welfare) + " <= " + str(social_welfare_old) + Style.RESET_ALL)


			print(Style.BRIGHT + Back.MAGENTA + Fore.YELLOW + "\n$$$$$$$$$$ FINAL SOCIAL WELFARE is " + str(social_welfare_old) + " for COLOURING " + str(colouring_best) + Style.RESET_ALL)

			input("\nPress any key to continue...")


		################################################################################
		# optimal colouring computation [EGALITARIAN SOCIAL WELFARE]
		if option is "optimal colouring [OPT -- EGALITARIAN SOCIAL WELFARE]":

			social_welfare_old = 0
			permlist = list(itertools.product(colors, repeat=G.number_of_nodes()))
			neighbors_check = True
			opt_check = True
			temp_social_welfare_old = 0
			count = 0

			print(Style.BRIGHT + Fore.RED + 'COLOR LIST PERMUTATION (pre-assignment)\n' + Style.RESET_ALL)
			print(permlist)
			print('\n')
			for perm in permlist:
				print("\n----------------------------------------------------------------------")
				colouring_old = perm
				print(colouring_old)
				for (node,data) in G.nodes(data=True):
					data['color'] = perm[node]
					print(str("color " + str(data['color'])) + " for node " + str(node))
				for (node,data) in G.nodes(data=True):
					temp_social_welfare = 0
					temp_social_welfare += result[node][data['color']]
					print(Style.BRIGHT + Fore.GREEN + "\n$$$$$$$$$$ NODE " + str(node) + " with COLOR " + str(data['color']) + Style.RESET_ALL)
					print(Style.BRIGHT + Fore.GREEN + "sommo INITIAL PROFIT " + str(result[node][data['color']]) + " a SOCIAL WELFARE TEMP " + str(temp_social_welfare) + Style.RESET_ALL)
					neighbors = G.neighbors(node)
					for neighbor in neighbors:
						if(G.node[neighbor]['color'] != G.node[node]['color']):
							edgeweight = G[node][neighbor]['weight']
							temp_social_welfare += edgeweight
							print("colore DIVERSO per i nodi ( " + str(node) + ", " + str(neighbor) + " ) = [ " + str(G.node[node]['color']) + " != " + str(G.node[neighbor]['color']) + " ] SOMMO " + str(edgeweight) + " a temp_social_welfare")
						else:
							print("colore UGUALE per i nodi ( " + str(node) + ", " + str(neighbor) + " ) = [ " + str(G.node[node]['color']) + " == " + str(G.node[neighbor]['color']) + " ] NON SOMMO NULLA a temp_social_welfare")
					print(Style.BRIGHT + Fore.RED + "temp SOCIAL WELFARE VALUE is " + str(temp_social_welfare) + Style.RESET_ALL + "\n")
					if(neighbors_check):
						print(Style.BRIGHT + Fore.MAGENTA + "FIRST CYCLE :" + str(temp_social_welfare) + Style.RESET_ALL)
						temp_social_welfare_old = temp_social_welfare
						neighbors_check = False
						continue
					if(temp_social_welfare < temp_social_welfare_old):
						print(Style.BRIGHT + Fore.MAGENTA + str(temp_social_welfare) + " < " + str(temp_social_welfare_old) + Style.RESET_ALL)
						temp_social_welfare_old = temp_social_welfare
					else:
						print(Style.BRIGHT + Fore.MAGENTA + str(temp_social_welfare) + " >= " + str(temp_social_welfare_old) + Style.RESET_ALL)
						continue
				print(Style.BRIGHT + Fore.YELLOW + "\nMINOR SOCIAL WELFARE VALUE is " + str(temp_social_welfare_old) + " for COLOURING " + str(colouring_old) + Style.RESET_ALL + "\n")
				neighbors_check = True
				if(opt_check):
					print(Style.BRIGHT + Fore.CYAN + "FIRST CYCLE -- BEST SOCIAL WELFARE : " + str(temp_social_welfare_old) + Style.RESET_ALL)
					social_welfare_old = temp_social_welfare_old
					colouring_best = colouring_old
					opt_check = False
					continue
				if(temp_social_welfare_old > social_welfare_old):
					print(Style.BRIGHT + Fore.CYAN + str(temp_social_welfare_old) + " > " + str(social_welfare_old) + Style.RESET_ALL)
					social_welfare_old = temp_social_welfare_old
					colouring_best = colouring_old
					count += 1
					print(Style.BRIGHT + Fore.CYAN + "\nBEST SOCIAL WELFARE : " + str(social_welfare_old) + " for COLOURING " + str(colouring_old) + Style.RESET_ALL + "\n")
				else:
					print(Style.BRIGHT + Fore.CYAN + str(temp_social_welfare_old) + " <= " + str(social_welfare_old) + Style.RESET_ALL)


			print(Style.BRIGHT + Back.MAGENTA + Fore.YELLOW + "\n$$$$$$$$$$ FINAL SOCIAL WELFARE is " + str(social_welfare_old) + " for COLOURING " + str(colouring_best) + " -- COUNT " + str(count) + Style.RESET_ALL)

			input("\nPress any key to continue...")


		################################################################################
		# stable colouring computation
		elif option is "stable colouring [NASH EQUILIBRIUM]":

			count = 0;
			restart = True
			last_improved_node = None

			while restart:
				restart = False
				for (node,data) in G.nodes(data=True):
					color_init = data['color']
					color_best = data['color']
					profit_old = result[node][data['color']]
					if(node == last_improved_node):
						print("\n----------------------------------------------------------------------\n")
						print(Style.BRIGHT + Back.RED + Fore.WHITE + "&&&&&&&&&&&&&&&&&&&&&&&&& LAST IMPROVED NODE &&&&&&&&&&&&&&&&&&&&&&&&&" + Style.RESET_ALL)
						continue
					print("\n----------------------------------------------------------------------\n")
					print(Style.BRIGHT + Fore.GREEN + "$$$$$$$$$$ NODE " + str(node) + " with COLOR " + str(color_init) + Style.RESET_ALL)
					print(Style.BRIGHT + Fore.GREEN + "with INITIAL PROFIT " + str(profit_old) + Style.RESET_ALL)
					neighbors = G.neighbors(node)
					for neighbor in neighbors:
						if(G.node[neighbor]['color'] != G.node[node]['color']):
							edgeweight = G[node][neighbor]['weight']
							profit_old += edgeweight
							print("colore DIVERSO per i nodi ( " + str(node) + ", " + str(neighbor) + " ) = [ " + str(G.node[node]['color']) + " != " + str(G.node[neighbor]['color']) + " ] SOMMO " + str(edgeweight) + " a profit_old")
						else:
							print("colore UGUALE per i nodi ( " + str(node) + ", " + str(neighbor) + " ) = [ " + str(G.node[node]['color']) + " == " + str(G.node[neighbor]['color']) + " ] NON SOMMO NULLA a profit_old")
					print(Style.BRIGHT + Fore.GREEN + "with TOTAL PROFIT " + str(profit_old) + Style.RESET_ALL + "\n")
					for current_color in colors:
						if(current_color != color_init):
							print(Style.BRIGHT + Fore.CYAN + "PROVO colore " + str(current_color) + " per il NODO " + str(node) + " colorato con " + str(color_init) + Style.RESET_ALL)
							data['color'] = current_color
							color_new = current_color
							profit_new = result[node][current_color]
							print("profit_new value --> " + str(profit_new) + "\n")
							neighbors = G.neighbors(node)
							for neighbor in neighbors:
								if(G.node[neighbor]['color'] != G.node[node]['color']):
									edgeweight = G[node][neighbor]['weight']
									profit_new += edgeweight
									print("colore DIVERSO per i nodi ( " + str(node) + ", " + str(neighbor) + " ) = [ " + str(G.node[node]['color']) + " != " + str(G.node[neighbor]['color']) + " ] SOMMO " + str(edgeweight) + " a profit_new")
								else:
									print("colore UGUALE per i nodi ( " + str(node) + ", " + str(neighbor) + " ) = [ " + str(G.node[node]['color']) + " == " + str(G.node[neighbor]['color']) + " ] NON SOMMO NULLA a profit_new")
							print("\nprofit_new value UPDATED --> " + str(profit_new))
							if(profit_new > profit_old):
								print(str(profit_new) + " > " + str(profit_old) + "\n")
								profit_old = profit_new
								color_best = current_color
							else:
								print(str(profit_new) + " <= " + str(profit_old) + "\n")
						else:
							print(Style.BRIGHT + Fore.RED + "NON PROVO colore " + str(current_color) + " per il nodo " + str(node) + " colorato con " + str(color_init) + Style.RESET_ALL + "\n")
							continue
					data['color'] = color_best
					if(data['color'] != color_init):
						print(Style.BRIGHT + Fore.MAGENTA + "$$$$$$$$$$ NEW COLOR " + str(data['color']) + " with PROFIT " + str(profit_old) + " for NODE " + str(node) + Style.RESET_ALL)
						count += 1
						print(Style.BRIGHT + Fore.YELLOW + "$$$$$$$$$$ COUNT " + str(count) + Style.RESET_ALL)
						restart = True
						last_improved_node = node
						print(Style.BRIGHT + Fore.CYAN + "$$$$$$$$$$ LAST IMPROVED NODE " + str(last_improved_node) + Style.RESET_ALL)
						print(Style.BRIGHT + Back.MAGENTA + Fore.CYAN + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! RESTARTING !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + Style.RESET_ALL)
						break


			print(Style.BRIGHT + Back.MAGENTA + Fore.YELLOW + "\n$$$$$$$$$$ FINAL COUNT is " + str(count) + Style.RESET_ALL)

			input("\nPress any key to continue...")


		################################################################################
		elif option is "exit":
			sys.exit()


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


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

if option is "MULTIPLE EXEC":


	#######################################################
	#################### SEARCH BLOCK #####################
	#######################################################

	p = pathlib.Path.cwd().parents[0].joinpath('generator').joinpath('mgen')
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

	first_iter = True
	for i in range(len(absfilepath)):

		G = nx.read_edgelist(absfilepath[i], nodetype=int, edgetype=int, create_using=nx.Graph())

		########################################################################
		#################### COLOURING/PROFITS CHOICE BLOCK ####################
		########################################################################

		if first_iter:

			print("\n")
			out_name = str(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' NAME ' + Fore.CYAN + 'for ' + Fore.YELLOW + ' OUTPUT FILE ' + Fore.CYAN + ']: ' + Style.RESET_ALL))
			out_ext = str(out_name) + ".out"

			print("\n")
			title = 'STATIC MODE or DINAMIC MODE for color insert ? '

			# FILESYSTEM :
			#
			# STATIC MODE
			# DINAMIC MODE
			#
			#

			options = ['STATIC MODE ([input]:numero di colori <= numero di nodi)', 'DINAMIC MODE (numero di nodi - [input]:numero di colori)']
			option, index = pick(options, title, indicator='>', multi_select=False)

			if option is "STATIC MODE ([input]:numero di colori <= numero di nodi)":
				dinamic_mode = False
				while(True):
				    maxc = int(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' MAX COLOR ' + Fore.CYAN + 'range int number [ 0 <= colors <= ' + Fore.YELLOW + ' MAX COLOR ' + Fore.CYAN + '] [ <= ' + str(G.number_of_nodes()) + ' ]: ' + Style.RESET_ALL))
				    if(maxc <= G.number_of_nodes()):
				        break
				    else:
				        print(Style.BRIGHT + Fore.RED + "[!] INVALID VALUE --> NUMBER OF COLORS MUST BE <= NUMBER OF NODES (" + str(G.number_of_nodes()) + ")\n" + Style.RESET_ALL)
				        continue

			elif option is "DINAMIC MODE (numero di nodi - [input]:numero di colori)":
				dinamic_mode = True
				while(True):
				    maxc = int(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' NUM COLOR ' + Fore.CYAN + 'sub int number [ number_of_nodes - ' + Fore.YELLOW + ' NUM COLOR ' + Fore.CYAN + '] [ <= ' + str(G.number_of_nodes()) + ' ]: ' + Style.RESET_ALL))
				    if(maxc < G.number_of_nodes()):
				        break
				    else:
				        print(Style.BRIGHT + Fore.RED + "[!] INVALID VALUE --> NUMBER OF COLORS TO SUBTRACT MUST BE < NUMBER OF NODES (" + str(G.number_of_nodes()) + ")\n" + Style.RESET_ALL)
				        continue

			print("\n")
			maxp = int(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' MAX PROFIT ' + Fore.CYAN + 'range int number: [ 0 <= profit <= ' + Fore.YELLOW + ' MAX PROFIT ' + Fore.CYAN + ']: ' + Style.RESET_ALL))

			print("\n")
			first_iter = False


		################################################################
		#################### COLORS LIST INIT BLOCK ####################
		################################################################

		if dinamic_mode:
			print(Style.BRIGHT + Fore.RED + "COLORS (LIST)\n" + Style.RESET_ALL)
			colors = list(range(G.number_of_nodes() - maxc))
			num_colors = len(colors)
			print(colors)
			print("\n")

		else:
			print(Style.BRIGHT + Fore.RED + "COLORS (LIST)\n" + Style.RESET_ALL)
			colors = list(range(maxc))
			num_colors = len(colors)
			print(colors)
			print("\n")


		######################################################################
		#################### INITIAL COLOURING INIT BLOCK ####################
		######################################################################

		for (n,c) in G.nodes(data=True):
		    c['color'] = random.choice(colors)

		print(Style.BRIGHT + Fore.RED + "NODE -- COLOR (LIST OF DICTIONARY) == INITIAL COLOURING\n" + Style.RESET_ALL)
		for (node,data) in G.nodes(data=True):
		    print(node,data)

		print("\nnumber of nodes:  " + str(G.number_of_nodes()))
		print("\n")


		######################################################################
		#################### COLORS -- PROFITS INIT BLOCK ####################
		######################################################################

		print(Style.BRIGHT + Fore.RED + "NODE -- COLORS -- PROFITS (NESTED DICTIONARY)\n" + Style.RESET_ALL)

		result = {node:{color:random.randint(0,maxp) for color in colors} for node in G.nodes()}

		pprint(result)
		print("\n")


		#####################################################################
		#################### EDGE -- WEIGHTS PRINT BLOCK ####################
		#####################################################################

		print(Style.BRIGHT + Fore.RED + "NODE -- NODE -- EDGE WEIGHT (LIST OF LIST OF DICTIONARY)\n" + Style.RESET_ALL)
		for (u,v,w) in G.edges(data=True):
		    print(u,v,w)

		print("\nnumber of edges:  " + str(G.number_of_edges()))
		print("\n")


		##########################################################
		#################### K-COLORING BLOCK ####################
		##########################################################

		count = 0;
		restart = True
		last_improved_node = None

		while restart:
			restart = False
			for (node,data) in G.nodes(data=True):
				color_init = data['color']
				color_best = data['color']
				profit_old = result[node][data['color']]
				if(node == last_improved_node):
					print("\n----------------------------------------------------------------------\n")
					print(Style.BRIGHT + Back.RED + Fore.WHITE + "&&&&&&&&&&&&&&&&&&&&&&&&& LAST IMPROVED NODE &&&&&&&&&&&&&&&&&&&&&&&&&" + Style.RESET_ALL)
					continue
				print("\n----------------------------------------------------------------------\n")
				print(Style.BRIGHT + Fore.GREEN + "$$$$$$$$$$ NODE " + str(node) + " with COLOR " + str(color_init) + Style.RESET_ALL)
				print(Style.BRIGHT + Fore.GREEN + "with INITIAL PROFIT " + str(profit_old) + Style.RESET_ALL)
				neighbors = G.neighbors(node)
				for neighbor in neighbors:
					if(G.node[neighbor]['color'] != G.node[node]['color']):
						edgeweight = G[node][neighbor]['weight']
						profit_old += edgeweight
						print("colore DIVERSO per i nodi ( " + str(node) + ", " + str(neighbor) + " ) = [ " + str(G.node[node]['color']) + " != " + str(G.node[neighbor]['color']) + " ] SOMMO " + str(edgeweight) + " a profit_old")
					else:
						print("colore UGUALE per i nodi ( " + str(node) + ", " + str(neighbor) + " ) = [ " + str(G.node[node]['color']) + " == " + str(G.node[neighbor]['color']) + " ] NON SOMMO NULLA a profit_old")
				print(Style.BRIGHT + Fore.GREEN + "with TOTAL PROFIT " + str(profit_old) + Style.RESET_ALL + "\n")
				for current_color in colors:
					if(current_color != color_init):
						print(Style.BRIGHT + Fore.CYAN + "PROVO colore " + str(current_color) + " per il NODO " + str(node) + " colorato con " + str(color_init) + Style.RESET_ALL)
						data['color'] = current_color
						color_new = current_color
						profit_new = result[node][current_color]
						print("profit_new value --> " + str(profit_new) + "\n")
						neighbors = G.neighbors(node)
						for neighbor in neighbors:
							if(G.node[neighbor]['color'] != G.node[node]['color']):
								edgeweight = G[node][neighbor]['weight']
								profit_new += edgeweight
								print("colore DIVERSO per i nodi ( " + str(node) + ", " + str(neighbor) + " ) = [ " + str(G.node[node]['color']) + " != " + str(G.node[neighbor]['color']) + " ] SOMMO " + str(edgeweight) + " a profit_new")
							else:
								print("colore UGUALE per i nodi ( " + str(node) + ", " + str(neighbor) + " ) = [ " + str(G.node[node]['color']) + " == " + str(G.node[neighbor]['color']) + " ] NON SOMMO NULLA a profit_new")
						print("\nprofit_new value UPDATED --> " + str(profit_new))
						if(profit_new > profit_old):
							print(str(profit_new) + " > " + str(profit_old) + "\n")
							profit_old = profit_new
							color_best = current_color
						else:
							print(str(profit_new) + " <= " + str(profit_old) + "\n")
					else:
						print(Style.BRIGHT + Fore.RED + "NON PROVO colore " + str(current_color) + " per il nodo " + str(node) + " colorato con " + str(color_init) + Style.RESET_ALL + "\n")
						continue
				data['color'] = color_best
				if(data['color'] != color_init):
					print(Style.BRIGHT + Fore.MAGENTA + "$$$$$$$$$$ NEW COLOR " + str(data['color']) + " with PROFIT " + str(profit_old) + " for NODE " + str(node) + Style.RESET_ALL)
					count += 1
					print(Style.BRIGHT + Fore.YELLOW + "$$$$$$$$$$ COUNT " + str(count) + Style.RESET_ALL)
					restart = True
					last_improved_node = node
					print(Style.BRIGHT + Fore.CYAN + "$$$$$$$$$$ LAST IMPROVED NODE " + str(last_improved_node) + Style.RESET_ALL)
					print(Style.BRIGHT + Back.MAGENTA + Fore.CYAN + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! RESTARTING !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + Style.RESET_ALL)
					break


		print(Style.BRIGHT + Back.MAGENTA + Fore.YELLOW + "\n$$$$$$$$$$ FINAL COUNT is " + str(count) + Style.RESET_ALL)


		with open(out_ext,'a') as f:
		        f.write("\nGRAPH : " + str(filelist[i].name) + "\nNUMBER OF NODES : " + str(G.number_of_nodes()) + "\nNUMBER OF COLORS : " + str(num_colors) + "\nCOUNT VALUE : " + str(count) + "\n")

		input("\nPress any Enter to continue...")
