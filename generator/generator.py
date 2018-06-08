import os
import shutil
import pathlib
import platform
import random
import networkx as nx
import matplotlib.pyplot as plt
import pydot
import sys

from pick import pick
from colorama import Fore, Back, Style, init


#####################################################
#################### INIT BLOCK #####################
#####################################################

graphviz = False

if platform.system() is "Windows":
	os.system("cls")
else :
	os.system("clear")
	graphviz = True


# colorama init
init()


######################################################
#################### CHOICE BLOCK ####################
######################################################

title = 'Choose random graph class: '

# CLASSES :
#
#
# Classic
# Expanders
# *** Lattice
# Small
# Random
# Duplication Divergence
# Degree Sequence (TODO)
# *** Random Clustered
#
#

options = ['Classics', 'Expanders', 'Small', 'Random', 'Duplication Divergence', 'Degree Sequence', 'MULTIPLE']
option, index = pick(options, title, indicator='>', multi_select=False)


##################################################
#################### CLASSICS ####################
##################################################

if option is "Classics":

	title = 'Choose random graph type: '

		# TYPES :
		#
		#
		# balanced_tree
		# complete_graph
		# circular_ladder_graph#
		# cycle_graph
		# dorogovtsev_goltsev_mendes_graph *** molto pesante (dare n basso)
		# ladder_graph
		# lollipop_graph
		# path_graph
		# star_graph
		# turan_graph
		# wheel_graph
		#
		#

	options = ['balanced_tree', 'complete_graph', 'circular_ladder_graph', 'cycle_graph', 'dorogovtsev_goltsev_mendes_graph', 'ladder_graph', 'lollipop_graph', 'path_graph', 'star_graph', 'turan_graph', 'wheel_graph']
	option, index = pick(options, title, indicator='>', multi_select=False)


	if option is "balanced_tree":

		print("\n")
		r = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Branching factor of the tree' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		h = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Height of the tree' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.balanced_tree(r, h, create_using=nx.Graph())


	elif option is "complete_graph":

		print("\n")
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.complete_graph(n, create_using=nx.Graph())


	elif option is "circular_ladder_graph":

		print("\n")
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert length on CLn' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.circular_ladder_graph(n, create_using=nx.Graph())


	elif option is "cycle_graph":

		print("\n")
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.cycle_graph(n, create_using=nx.Graph())


	elif option is "dorogovtsev_goltsev_mendes_graph":

		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert generation number' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		print("\n")
		G=nx.dorogovtsev_goltsev_mendes_graph(n, create_using=nx.Graph())


	elif option is "ladder_graph":

		print("\n")
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.ladder_graph(n, create_using=nx.Graph())


	elif option is "lollipop_graph":

		print("\n")
		m = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + 'range(m) - range(m, m+n) -> ' + Fore.YELLOW + 'm' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + 'range(m) - range(m, m+n) -> ' + Fore.YELLOW + 'n' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.lollipop_graph(m, n, create_using=nx.Graph())


	elif option is "path_graph":

		print("\n")
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.path_graph(n, create_using=nx.Graph())


	elif option is "star_graph":

		print("\n")
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.star_graph(n, create_using=nx.Graph())


	elif option is "turan_graph":

		print("\n")
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		r = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of disjoint subset (partitions)' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.turan_graph(n, r)


	elif option is "wheel_graph":

		print("\n")
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.wheel_graph(n, create_using=nx.Graph())


###################################################
#################### EXPANDERS ####################
###################################################

elif option is "Expanders":

	title = 'Choose random graph type: '

	# TYPES :
	#
	#
	# chordal_cycle_graph
	#
	#

	options = ['chordal_cycle_graph']
	option, index = pick(options, title, indicator='>', multi_select=False)

	if option is "chordal_cycle_graph":

		print("\n")
		p = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes [MUST BE A PRIME NUMBER]' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.chordal_cycle_graph(p, create_using=nx.Graph())


###############################################
#################### SMALL ####################
###############################################

elif option is "Small":

	title = 'Choose random graph type: '

	# TYPES :
	#
	#
	# bull_graph
	# cubical_graph
	# desargues_graph
	# diamond_graph
	# dodecahedral_graph
	# frucht_graph
	# heawood_graph
	# house_graph
	# house_x_graph
	# icosahedral_graph
	# krackhardt_kite_graph
	# moebius_kantor_graph
	# octahedral_graph
	# pappus_graph
	# petersen_graph
	# sedgewick_maze_graph
	# tetrahedral_graph
	# truncated_cube_graph
	# truncated_tetrahedron_graph
	# tutte_graph
	#
	#

	options = ['bull_graph', 'cubical_graph', 'desargues_graph', 'diamond_graph', 'dodecahedral_graph', 'frucht_graph', 'heawood_graph', 'house_graph', 'house_x_graph', 'icosahedral_graph', 'krackhardt_kite_graph', 'moebius_kantor_graph', 'octahedral_graph', 'pappus_graph', 'petersen_graph', 'sedgewick_maze_graph', 'tetrahedral_graph', 'truncated_cube_graph', 'truncated_tetrahedron_graph', 'tutte_graph']
	option, index = pick(options, title, indicator='>', multi_select=False)

	if option is "bull_graph":

		G=nx.bull_graph(create_using=nx.Graph())


	if option is "cubical_graph":

		G=nx.cubical_graph(create_using=nx.Graph())


	if option is "desargues_graph":

		G=nx.desargues_graph(create_using=nx.Graph())


	if option is "diamond_graph":

		G=nx.diamond_graph(create_using=nx.Graph())


	if option is "dodecahedral_graph":

		G=nx.dodecahedral_graph(create_using=nx.Graph())


	if option is "frucht_graph":

		G=nx.frucht_graph(create_using=nx.Graph())


	if option is "heawood_graph":

		G=nx.heawood_graph(create_using=nx.Graph())


	if option is "house_graph":

		G=nx.house_graph(create_using=nx.Graph())


	if option is "house_x_graph":

		G=nx.house_x_graph(create_using=nx.Graph())


	if option is "icosahedral_graph":

		G=nx.icosahedral_graph(create_using=nx.Graph())


	if option is "krackhardt_kite_graph":

		G=nx.krackhardt_kite_graph(create_using=nx.Graph())


	if option is "moebius_kantor_graph":

		G=nx.moebius_kantor_graph(create_using=nx.Graph())


	if option is "octahedral_graph":

		G=nx.octahedral_graph(create_using=nx.Graph())


	if option is "pappus_graph":

		G=nx.pappus_graph()


	if option is "petersen_graph":

		G=nx.petersen_graph(create_using=nx.Graph())


	if option is "sedgewick_maze_graph":

		G=nx.sedgewick_maze_graph(create_using=nx.Graph())


	if option is "tetrahedral_graph":

		G=nx.tetrahedral_graph(create_using=nx.Graph())


	if option is "truncated_cube_graph":

		G=nx.truncated_cube_graph(create_using=nx.Graph())


	if option is "truncated_tetrahedron_graph":

		G=nx.truncated_tetrahedron_graph(create_using=nx.Graph())


	if option is "tutte_graph":

		G=nx.tutte_graph(create_using=nx.Graph())


################################################
#################### RANDOM ####################
################################################

elif option is "Random":

	title = 'Choose random graph type: '

	# TYPES :
	#
	#
	# fast_gnp_random_graph
	# gnp_random_graph
	# dense_gnm_random_graph
	# gnm_random_graph
	# erdos_renyi_graph
	# binomial_graph
	# newman_watts_strogatz_graph
	# watts_strogatz_graph
	# connected_watts_strogatz_graph
	# random_regular_graph
	# barabasi_albert_graph
	# powerlaw_cluster_graph
	# random_lobster
	# random_powerlaw_tree
	#
	#

	options = ['fast_gnp_random_graph', 'gnp_random_graph', 'dense_gnm_random_graph', 'gnm_random_graph', 'erdos_renyi_graph', 'binomial_graph', 'newman_watts_strogatz_graph', 'watts_strogatz_graph', 'connected_watts_strogatz_graph', 'random_regular_graph', 'barabasi_albert_graph', 'powerlaw_cluster_graph', 'random_lobster', 'random_powerlaw_tree']
	option, index = pick(options, title, indicator='>', multi_select=False)

	if option is "fast_gnp_random_graph":

		print("\n")
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		p = float(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the probability of edge creation value' + Fore.CYAN + '(' + Fore.YELLOW + 'float' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.fast_gnp_random_graph(n, p, directed=False)


	if option is "gnp_random_graph":

		print("\n")
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		p = float(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the probability of edge creation value' + Fore.CYAN + '(' + Fore.YELLOW + 'float' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.gnp_random_graph(n, p, directed=False)


	if option is "dense_gnm_random_graph":

		print("\n")
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		m = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of edges' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.dense_gnm_random_graph(n, m)


	if option is "gnm_random_graph":

		print("\n")
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		m = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of edges' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.gnm_random_graph(n, m, directed=False)


	if option is "erdos_renyi_graph":

		print("\n")
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		p = float(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the probability of edge creation value' + Fore.CYAN + '(' + Fore.YELLOW + 'float' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.erdos_renyi_graph(n, p, directed=False)


	if option is "binomial_graph":

		print("\n")
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		p = float(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the probability of edge creation value' + Fore.CYAN + '(' + Fore.YELLOW + 'float' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.binomial_graph(n, p, directed=False)


	if option is "newman_watts_strogatz_graph":

		print("\n")
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		k = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes for ring topology' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		p = float(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the probability of edge creation value' + Fore.CYAN + '(' + Fore.YELLOW + 'float' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.newman_watts_strogatz_graph(n, k, p)


	if option is "watts_strogatz_graph":

		print("\n")
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		k = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes for ring topology' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		p = float(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the probability of edge creation value' + Fore.CYAN + '(' + Fore.YELLOW + 'float' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.watts_strogatz_graph(n, k, p)


	if option is "connected_watts_strogatz_graph":

		print("\n")
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		k = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes for ring topology' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		p = float(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the probability of edge creation value' + Fore.CYAN + '(' + Fore.YELLOW + 'float' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		tries = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of attempts to generate a connected graph' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.connected_watts_strogatz_graph(n, k, p, tries)


	if option is "random_regular_graph":

		print("\n")
		d = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes (n × d MUST BE EVEN && d >= n )' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.random_regular_graph(d, n)


	if option is "barabasi_albert_graph":

		print("\n")
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		m = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of edges to attach from a new node to existing nodes (1 <= m < n)' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.barabasi_albert_graph(n, m)


	if option is "powerlaw_cluster_graph":

		print("\n")
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		m = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of random edges to add for each new node (1 <= m <= n)' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		p = float(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the probability of adding a triangle after adding a random edge (0 <= p <= 1)' + Fore.CYAN + '(' + Fore.YELLOW + 'float' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.powerlaw_cluster_graph(n, m, p)


	if option is "random_lobster":

		print("\n")
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes in the backbone' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		p1 = float(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the probability of adding an edge to the backbone' + Fore.CYAN + '(' + Fore.YELLOW + 'float' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		p2 = float(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the probability of adding an edge one level beyond backbone' + Fore.CYAN + '(' + Fore.YELLOW + 'float' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.random_lobster(n, p1, p2)


	if option is "random_powerlaw_tree":

		print("\n")
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes in the backbone' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		gamma = float(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the exponent of the power law' + Fore.CYAN + '(' + Fore.YELLOW + 'float' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		tries = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of attempts to adjust the sequence to make it a tree' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.random_powerlaw_tree(n, gamma, tries)


################################################################
#################### DUPLICATION DIVERGENCE ####################
################################################################

elif option is "Duplication Divergence":

	title = 'Choose random graph type: '

	# TYPES :
	#
	# duplication_divergence_graph
	# partial_duplication_graph
	#
	#

	options = ['duplication_divergence_graph', 'partial_duplication_graph']
	option, index = pick(options, title, indicator='>', multi_select=False)

	# only Graph()
	if option is "duplication_divergence_graph":

		print("\n")
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes (n >= 2)' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		p = float(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the probability for retaining the edge of the replicated node (0 <= p <= 1)' + Fore.CYAN + '(' + Fore.YELLOW + 'float' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.duplication_divergence_graph(n, p)


	if option is "partial_duplication_graph":

		print("\n")
		N = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the total number of nodes in the final graph' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes in the initial clique' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		p = float(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the probability of joining each neighbor of a node to the duplicate node (0 <= p <= 1)' + Fore.CYAN + '(' + Fore.YELLOW + 'float' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		q = float(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the probability of joining the source node to the duplicate node (0 <= p <= 1)' + Fore.CYAN + '(' + Fore.YELLOW + 'float' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		G=nx.partial_duplication_graph(N, n, p, q)


#########################################################
#################### DEGREE SEQUENCE ####################
#########################################################

# elif option is "Degree Sequence":
#
# 	title = 'Choose random graph type: '
#
# 	# TYPES :
# 	#
# 	# types
# 	#
# 	#
#
# 	options = ['type', 'type', 'type', 'type', 'type', 'type', 'type']
# 	option, index = pick(options, title, indicator='>', multi_select=False)
#
# 	# only Graph()
# 	if option is "type":
#
# 		n = int(input('[*] Insert (int): '))
# 		p = float(input('[*] Insert (float): '))
#
# 		G=nx.typefunction(n, p)


###########################################################
#################### MULTIPLE CREATION ####################
###########################################################

elif option is "MULTIPLE":

	title = 'Choose random graph type: '

	# TYPES :
	#
	# types
	#
	#

	options = ['complete_graph']
	option, index = pick(options, title, indicator='>', multi_select=False)

	# TODO FORSE AGGIUNGI SEQUENTIAL MODE O RANDOM MODE
	if option is "complete_graph":

		print("\n")
		n_min = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the MIN number of nodes [ RANGE : MIN <= node_num <= max ] ' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))
		n_max = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the MAX number of nodes [ RANGE : min <= node_num <= MAX ] ' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

		print("\n")
		MinInt = int(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' MIN ' + Fore.CYAN + 'range int number: ' + Style.RESET_ALL))
		MaxInt = int(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' MAX ' + Fore.CYAN + 'range int number: ' + Style.RESET_ALL))
		print("\n")

		for i in range(n_min, n_max+1):

			G=nx.complete_graph(i, create_using=nx.Graph())

			for (u,v,w) in G.edges(data=True):
			    w['weight'] = random.randint(MinInt, MaxInt)

			# set .edgelist filename
			name = "complete_graph_with_" + str(i) + "_nodes"

			# build home directory path
			hubdir = pathlib.Path.cwd().joinpath('mgen').joinpath(name)
			pathlib.Path(hubdir).mkdir(parents=True, exist_ok=True)

			# build .edgelist filename
			ext = ".edgelist"

			edgelistname = name + ext

			# build .edgelist file
			# nx.write_weighted_edgelist(G, edgelistname)
			nx.write_edgelist(G, edgelistname, data=True)

			# move .edgelist file into home directory
			edgelistpath = pathlib.Path.cwd().joinpath(edgelistname)
			newedgelistpath = pathlib.Path.cwd().joinpath('mgen').joinpath(name).joinpath(edgelistname)
			shutil.move(edgelistpath, newedgelistpath)

		sys.exit()

####################################################
#################### MAIN BLOCK ####################
####################################################

# title = 'Choose edge weight type: '
#
# # LAYOUTS :
# #
# # integer
# # float
# #
#
# options = ['integer', 'float']
# option, index = pick(options, title, indicator='>', multi_select=False)
#
# # integer weights
# if option is "integer":
#
# 	print("\n")
# 	MinInt = int(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' MIN ' + Fore.CYAN + 'range int number: ' + Style.RESET_ALL))
# 	MaxInt = int(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' MAX ' + Fore.CYAN + 'range int number: ' + Style.RESET_ALL))
# 	print("\n")
#
# 	for (u,v,w) in G.edges(data=True):
# 	    w['weight'] = random.randint(MinInt, MaxInt)
#
# # float weights
# elif option is "float":
#
# 	print("\n")
# 	MinInt = int(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' MIN ' + Fore.CYAN + 'range int number: ' + Style.RESET_ALL))
# 	MaxInt = int(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' MAX ' + Fore.CYAN + 'range int number: ' + Style.RESET_ALL))
# 	Aprx = int(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Set' + Fore.YELLOW + ' APPROXIMATION ' + Fore.CYAN + 'value (number of decimals): ' + Style.RESET_ALL))
# 	print("\n")
#
# 	for (u,v,w) in G.edges(data=True):
# 	    w['weight'] = round(random.uniform(MinInt, MaxInt), Aprx)


print("\n")
MinInt = int(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' MIN ' + Fore.CYAN + 'range int number: ' + Style.RESET_ALL))
MaxInt = int(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' MAX ' + Fore.CYAN + 'range int number: ' + Style.RESET_ALL))
print("\n")

for (u,v,w) in G.edges(data=True):
    w['weight'] = random.randint(MinInt, MaxInt)


# set .edgelist filename
name = input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' NAME ' + Fore.CYAN + 'for file' + Fore.YELLOW + ' .edgelist' + Fore.CYAN + ': ' + Style.RESET_ALL)
print("\n")

# build home directory path
hubdir = pathlib.Path.cwd().joinpath('gen').joinpath(name)
pathlib.Path(hubdir).mkdir(parents=True, exist_ok=True)
print(Style.BRIGHT + Fore.MAGENTA + "[" + Fore.YELLOW + "!" + Fore.MAGENTA + "]" + Fore.YELLOW + " Path " + Fore.CYAN + "of" + Fore.YELLOW + " home directory " + Fore.CYAN + "is: " + Back.MAGENTA + Fore.CYAN + str(hubdir) + Style.RESET_ALL)
print("\n")

# build .edgelist filename
ext = ".edgelist"

edgelistname = name + ext
print(Style.BRIGHT + Fore.MAGENTA + "[" + Fore.YELLOW + "!" + Fore.MAGENTA + "]" + Fore.YELLOW + " Name " + Fore.CYAN + "of" + Fore.YELLOW + " .edgelist file " + Fore.CYAN + "is: " + Back.MAGENTA + Fore.CYAN + edgelistname + Style.RESET_ALL)

# build .edgelist file
# nx.write_weighted_edgelist(G, edgelistname)
nx.write_edgelist(G, edgelistname, data=True)

# move .edgelist file into home directory
edgelistpath = pathlib.Path.cwd().joinpath(edgelistname)
newedgelistpath = pathlib.Path.cwd().joinpath('gen').joinpath(name).joinpath(edgelistname)
shutil.move(edgelistpath, newedgelistpath)
print(Style.BRIGHT + Fore.MAGENTA + "[" + Fore.YELLOW + "!" + Fore.MAGENTA + "]" + Fore.CYAN + " Final" + Fore.YELLOW + " .edgelist file path " + Fore.CYAN + "is: " + Back.MAGENTA + Fore.CYAN + str(newedgelistpath) + Style.RESET_ALL)

if graphviz:

	# build .dot filename
	ext2 = ".dot"

	dotname = name + ext2
	print(Style.BRIGHT + Fore.MAGENTA + "[" + Fore.YELLOW + "!" + Fore.MAGENTA + "]" + Fore.YELLOW + " Name " + Fore.CYAN + "of" + Fore.YELLOW + " .dot file " + Fore.CYAN + "is: " + Back.MAGENTA + Fore.CYAN + dotname + Style.RESET_ALL)

	# build .dot file
	nx.nx_pydot.write_dot(G, dotname)

	# move .dot file into home directory
	dotpath = pathlib.Path.cwd().joinpath(dotname)
	newdotpath = pathlib.Path.cwd().joinpath('gen').joinpath(name).joinpath(dotname)
	shutil.move(dotpath, newdotpath)
	print(Style.BRIGHT + Fore.MAGENTA + "[" + Fore.YELLOW + "!" + Fore.MAGENTA + "]" + Fore.CYAN + " Final" + Fore.YELLOW + " .dot file path " + Fore.CYAN + "is: " + Back.MAGENTA + Fore.CYAN + str(newdotpath) + Style.RESET_ALL)
	print("\n")

#################################################################
#################### DRAW BLOCK [ GRAPHVIZ ] ####################
#################################################################

# (works with Graph/DiGraph/MultiGraph/MultiDiGraph)

if graphviz:

	title = 'Do you want to draw(.dot -> .png)/save the graph with Graphviz Library? '

	# ANSWER :
	#
	# yes (draw/show)
	# no (return)
	#

	options = ['yes', 'no']
	option, index = pick(options, title, indicator='>', default_index=1, multi_select=False)

	if option is "yes":

		print(Style.BRIGHT + Fore.MAGENTA + "[" + Fore.YELLOW + "X" + Fore.MAGENTA + "]" + Fore.GREEN + " Graphviz init")

		ext3 = ".png"
		pngname = name + ext3
		print(Style.BRIGHT + Fore.MAGENTA + "[" + Fore.YELLOW + "!" + Fore.MAGENTA + "]" + Fore.YELLOW + " Name " + Fore.CYAN + "of" + Fore.YELLOW + " .png file " + Fore.CYAN + "is: " + Back.MAGENTA + Fore.CYAN + pngname + Style.RESET_ALL)


		# build .png file
		K = nx.nx_pydot.to_pydot(G)
		K.write_png(pngname)

		# move .png file into home directory
		pngpath = pathlib.Path.cwd().joinpath(pngname)
		newpngpath = pathlib.Path.cwd().joinpath('gen').joinpath(name).joinpath(pngname)
		shutil.move(pngpath, newpngpath)
		print(Style.BRIGHT + Fore.MAGENTA + "[" + Fore.YELLOW + "!" + Fore.MAGENTA + "]" + Fore.CYAN + " Final" + Fore.YELLOW + " .png file path " + Fore.CYAN + "is: " + Back.MAGENTA + Fore.CYAN + str(newpngpath) + Style.RESET_ALL)
		print("\n")

	if option is "no":
		print(Style.BRIGHT + Fore.MAGENTA + "[" + Fore.YELLOW + "X" + Fore.MAGENTA + "]" + Fore.RED + " Graphviz terminated")
		print("\n")


#################################################################
#################### DRAW BLOCK [ MATPLOIT ] ####################
#################################################################

#  (works only with Graph/DiGraph)

title = 'Do you want to draw/show the graph with Matplotlib library? '

# ANSWER :
#
# yes (draw/show)
# no (return)
#

options = ['yes', 'no']
option, index = pick(options, title, indicator='>', default_index=1, multi_select=False)

if option is "yes":

	print(Style.BRIGHT + Fore.MAGENTA + "[" + Fore.YELLOW + "X" + Fore.MAGENTA + "]" + Fore.GREEN + " Matplotlib init")
	print("\n")

	title = 'Choose graph layout: '

	# LAYOUTS :
	#
	# circular_layout
	# kamada_kawai_layout *
	# random_layout
	# rescale_layout *
	# shell_layout
	# spring_layout
	# spectral_layout
	#

	options = ['circular_layout', 'random_layout', 'shell_layout', 'spring_layout', 'spectral_layout']
	option, index = pick(options, title, indicator='>', multi_select=False)

	if option is "circular_layout":
		pos=nx.circular_layout(G)
	elif option is "random_layout":
		pos=nx.random_layout(G)
	elif option is "shell_layout":
		pos=nx.shell_layout(G)
	elif option is "spring_layout":
		pos=nx.spring_layout(G)
	elif option is "spectral_layout":
		pos=nx.spectral_layout(G)

	nx.draw_networkx(G, pos, with_labels=True, node_size=400, node_color='black', width=2.0, style='solid', font_color='white', font_weight='bold')

	#edge_labels=dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)])
	edge_labels = nx.get_edge_attributes(G,'weight')

	nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels)

	plt.axis('off')
	plt.show()

if option is "no":
	print(Style.BRIGHT + Fore.MAGENTA + "[" + Fore.YELLOW + "X" + Fore.MAGENTA + "]" + Fore.RED + " Matplotlib terminated")
	print("\n")


print(Style.BRIGHT + Fore.MAGENTA + "[" + Fore.YELLOW + "X" + Fore.MAGENTA + "]" + Fore.GREEN + " Creation completed")
