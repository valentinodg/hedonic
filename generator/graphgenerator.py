import os
import shutil
import pathlib
import platform
import random
import networkx as nx
import matplotlib.pyplot as plt
from pick import pick
#import pygraphviz ## import errors on windows


if platform.system() is "Windows":
	os.system("CLS")
elif platform.system() is "Linux":
	os.system("clear")

print("\n")
matplotdraw  = False

######################################################
#################### CHOICE BLOCK ####################
######################################################

title = 'Choose random graph class: '

# CLASSES :
#
# Classic
# Expanders
# Small
# Random
#

options = ['Classics', 'Expanders', 'Small', 'Random']
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

		r = int(input('[*] Branching factor of the tree (int): '))
		h = int(input('[*] Height of the tree (int): '))

		title = 'Choose random graph type: '

		# TYPES :
		#
		# MultiGraph() (grafo non-diretto)
		# MultiDiGraph() (grafo diretto)
		#

		options = ['MultiGraph', 'MultiDiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "MultiGraph":
			G=nx.balanced_tree(r, h, create_using=nx.MultiGraph())
		if option is "MultiDiGraph":
			G=nx.balanced_tree(r, h, create_using=nx.MultiDiGraph())


	elif option is "complete_graph":

		n = int(input('[*] Insert the number of nodes (int): '))

		title = 'Choose random graph type: '

		# TYPES :
		#
		# MultiGraph() (grafo non-diretto)
		# MultiDiGraph() (grafo diretto)
		#

		options = ['MultiGraph', 'MultiDiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "MultiGraph":
			G=nx.complete_graph(n, create_using=nx.MultiGraph())
		if option is "MultiDiGraph":
			G=nx.complete_graph(n, create_using=nx.MultiDiGraph())


	elif option is "circular_ladder_graph":

		n = int(input('[*] Insert length on CLn (int): '))

		title = 'Choose random graph type: '

		# TYPES :
		#
		# MultiGraph() (grafo non-diretto)
		# MultiDiGraph() (grafo diretto)
		#

		options = ['MultiGraph', 'MultiDiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "MultiGraph":
			G=nx.circular_ladder_graph(n, create_using=nx.MultiGraph())
		if option is "MultiDiGraph":
			G=nx.circular_ladder_graph(n, create_using=nx.MultiDiGraph())


	elif option is "cycle_graph":

		n = int(input('[*] Insert the number of nodes (int): '))

		title = 'Choose random graph type: '

		# TYPES :
		#
		# MultiGraph() (grafo non-diretto)
		# MultiDiGraph() (grafo diretto)
		#

		options = ['MultiGraph', 'MultiDiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "MultiGraph":
			G=nx.cycle_graph(n, create_using=nx.MultiGraph())
		if option is "MultiDiGraph":
			G=nx.cycle_graph(n, create_using=nx.MultiDiGraph())


	elif option is "dorogovtsev_goltsev_mendes_graph":

		n = int(input('[*] Insert generation number (int): '))

		# TYPES :
		#
		# Graph() (grafo semplice non-diretto) (only)
		#
		#

		G=nx.dorogovtsev_goltsev_mendes_graph(n, create_using=nx.Graph())


	elif option is "ladder_graph":

		n = int(input('[*] Insert the number of nodes (int): '))

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Graph() (grafo semplice non-diretto)
		# MultiGraph() (grafo non-diretto)
		#

		options = ['Graph', 'MultiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Graph":
			G=nx.ladder_graph(n, create_using=nx.Graph())
		if option is "MultiGraph":
			G=nx.ladder_graph(n, create_using=nx.MultiGraph())


	elif option is "lollipop_graph":

		m = int(input('[*] Insert the number of nodes (int) range(m) - range(m, m+n) -> m: '))
		n = int(input('[*] Insert the number of nodes (int) range(m) - range(m, m+n) -> n: '))

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Graph() (grafo semplice non-diretto)
		# MultiGraph() (grafo non-diretto)
		#

		options = ['Graph', 'MultiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Graph":
			G=nx.lollipop_graph(m, n, create_using=nx.Graph())
		if option is "MultiGraph":
			G=nx.lollipop_graph(m, n, create_using=nx.MultiGraph())


	elif option is "path_graph":

		n = int(input('[*] Insert the number of nodes (int): '))

		title = 'Choose random graph type: '

		# TYPES :
		#
		# MultiGraph() (grafo non-diretto)
		# MultiDiGraph() (grafo diretto)
		#

		options = ['MultiGraph', 'MultiDiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "MultiGraph":
			G=nx.path_graph(n, create_using=nx.MultiGraph())
		if option is "MultiDiGraph":
			G=nx.path_graph(n, create_using=nx.MultiDiGraph())


	elif option is "star_graph":

		n = int(input('[*] Insert the number of nodes (int): '))

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Graph() (grafo semplice non-diretto)
		# MultiGraph() (grafo non-diretto)
		#

		options = ['Graph', 'MultiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Graph":
			G=nx.star_graph(n, create_using=nx.Graph())
		if option is "MultiGraph":
			G=nx.star_graph(n, create_using=nx.MultiGraph())


	elif option is "turan_graph":

		n = int(input('[*] Insert the number of nodes (int): '))
		r = int(input('[*] Insert the number of disjoint subset (partitions) (int): '))

		G=nx.turan_graph(n, r)


	elif option is "wheel_graph":

		n = int(input('[*] Insert the number of nodes (int): '))

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Graph() (grafo semplice non-diretto)
		# MultiGraph() (grafo non-diretto)
		#

		options = ['Graph', 'MultiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Graph":
			G=nx.wheel_graph(n, create_using=nx.Graph())
		if option is "MultiGraph":
			G=nx.wheel_graph(n, create_using=nx.MultiGraph())


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

		p = int(input('[*] Insert the number of nodes [MUST BE A PRIME NUMBER] (int): '))

		G=nx.chordal_cycle_graph(p, create_using=nx.MultiGraph())


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

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Graph() (grafo semplice non-diretto)
		# MultiGraph() (grafo non-diretto)
		#

		options = ['Graph', 'MultiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Graph":
			G=nx.bull_graph(create_using=nx.Graph())
			matplotdraw = True

		if option is "MultiGraph":
			G=nx.bull_graph(create_using=nx.MultiGraph())


	if option is "cubical_graph":

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Graph() (grafo semplice non-diretto)
		# MultiGraph() (grafo non-diretto)
		#

		options = ['Graph', 'MultiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Graph":
			G=nx.cubical_graph(create_using=nx.Graph())
			matplotdraw = True

		if option is "MultiGraph":
			G=nx.cubical_graph(create_using=nx.MultiGraph())


	if option is "desargues_graph":

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Graph() (grafo semplice non-diretto)
		# MultiGraph() (grafo non-diretto)
		#

		options = ['Graph', 'MultiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Graph":
			G=nx.desargues_graph(create_using=nx.Graph())
			matplotdraw = True

		if option is "MultiGraph":
			G=nx.desargues_graph(create_using=nx.MultiGraph())


	if option is "diamond_graph":

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Graph() (grafo semplice non-diretto)
		# MultiGraph() (grafo non-diretto)
		#

		options = ['Graph', 'MultiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Graph":
			G=nx.diamond_graph(create_using=nx.Graph())
			matplotdraw = True

		if option is "MultiGraph":
			G=nx.diamond_graph(create_using=nx.MultiGraph())


	if option is "dodecahedral_graph":

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Graph() (grafo semplice non-diretto)
		# MultiGraph() (grafo non-diretto)
		#

		options = ['Graph', 'MultiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Graph":
			G=nx.dodecahedral_graph(create_using=nx.Graph())
			matplotdraw = True

		if option is "MultiGraph":
			G=nx.dodecahedral_graph(create_using=nx.MultiGraph())


	if option is "frucht_graph":

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Graph() (grafo semplice non-diretto)
		# MultiGraph() (grafo non-diretto)
		#

		options = ['Graph', 'MultiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Graph":
			G=nx.frucht_graph(create_using=nx.Graph())
			matplotdraw = True

		if option is "MultiGraph":
			G=nx.frucht_graph(create_using=nx.MultiGraph())


	if option is "heawood_graph":

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Graph() (grafo semplice non-diretto)
		# MultiGraph() (grafo non-diretto)
		#

		options = ['Graph', 'MultiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Graph":
			G=nx.heawood_graph(create_using=nx.Graph())
			matplotdraw = True

		if option is "MultiGraph":
			G=nx.heawood_graph(create_using=nx.MultiGraph())


	if option is "house_graph":

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Graph() (grafo semplice non-diretto)
		# MultiGraph() (grafo non-diretto)
		#

		options = ['Graph', 'MultiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Graph":
			G=nx.house_graph(create_using=nx.Graph())
			matplotdraw = True

		if option is "MultiGraph":
			G=nx.house_graph(create_using=nx.MultiGraph())


	if option is "house_x_graph":

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Graph() (grafo semplice non-diretto)
		# MultiGraph() (grafo non-diretto)
		#

		options = ['Graph', 'MultiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Graph":
			G=nx.house_x_graph(create_using=nx.Graph())
			matplotdraw = True

		if option is "MultiGraph":
			G=nx.house_x_graph(create_using=nx.MultiGraph())


	if option is "icosahedral_graph":

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Graph() (grafo semplice non-diretto)
		# MultiGraph() (grafo non-diretto)
		#

		options = ['Graph', 'MultiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Graph":
			G=nx.icosahedral_graph(create_using=nx.Graph())
			matplotdraw = True

		if option is "MultiGraph":
			G=nx.icosahedral_graph(create_using=nx.MultiGraph())


	if option is "krackhardt_kite_graph":

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Graph() (grafo semplice non-diretto)
		# MultiGraph() (grafo non-diretto)
		#

		options = ['Graph', 'MultiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Graph":
			G=nx.krackhardt_kite_graph(create_using=nx.Graph())
			matplotdraw = True

		if option is "MultiGraph":
			G=nx.krackhardt_kite_graph(create_using=nx.MultiGraph())


	if option is "moebius_kantor_graph":

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Graph() (grafo semplice non-diretto)
		# MultiGraph() (grafo non-diretto)
		#

		options = ['Graph', 'MultiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Graph":
			G=nx.moebius_kantor_graph(create_using=nx.Graph())
			matplotdraw = True

		if option is "MultiGraph":
			G=nx.moebius_kantor_graph(create_using=nx.MultiGraph())


	if option is "octahedral_graph":

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Graph() (grafo semplice non-diretto)
		# MultiGraph() (grafo non-diretto)
		#

		options = ['Graph', 'MultiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Graph":
			G=nx.octahedral_graph(create_using=nx.Graph())
			matplotdraw = True

		if option is "MultiGraph":
			G=nx.octahedral_graph(create_using=nx.MultiGraph())


	if option is "pappus_graph":
		G=nx.pappus_graph()
		matplotdraw = True


	if option is "petersen_graph":

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Graph() (grafo semplice non-diretto)
		# MultiGraph() (grafo non-diretto)
		#

		options = ['Graph', 'MultiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Graph":
			G=nx.petersen_graph(create_using=nx.Graph())
			matplotdraw = True

		if option is "MultiGraph":
			G=nx.petersen_graph(create_using=nx.MultiGraph())


	if option is "sedgewick_maze_graph":

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Graph() (grafo semplice non-diretto)
		# MultiGraph() (grafo non-diretto)
		#

		options = ['Graph', 'MultiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Graph":
			G=nx.sedgewick_maze_graph(create_using=nx.Graph())
			matplotdraw = True

		if option is "MultiGraph":
			G=nx.sedgewick_maze_graph(create_using=nx.MultiGraph())


	if option is "tetrahedral_graph":

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Graph() (grafo semplice non-diretto)
		# MultiGraph() (grafo non-diretto)
		#

		options = ['Graph', 'MultiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Graph":
			G=nx.tetrahedral_graph(create_using=nx.Graph())
			matplotdraw = True

		if option is "MultiGraph":
			G=nx.tetrahedral_graph(create_using=nx.MultiGraph())


	if option is "truncated_cube_graph":

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Graph() (grafo semplice non-diretto)
		# MultiGraph() (grafo non-diretto)
		#

		options = ['Graph', 'MultiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Graph":
			G=nx.truncated_cube_graph(create_using=nx.Graph())
			matplotdraw = True

		if option is "MultiGraph":
			G=nx.truncated_cube_graph(create_using=nx.MultiGraph())


	if option is "truncated_tetrahedron_graph":

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Graph() (grafo semplice non-diretto)
		# MultiGraph() (grafo non-diretto)
		#

		options = ['Graph', 'MultiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Graph":
			G=nx.truncated_tetrahedron_graph(create_using=nx.Graph())
			matplotdraw = True

		if option is "MultiGraph":
			G=nx.truncated_tetrahedron_graph(create_using=nx.MultiGraph())


	if option is "tutte_graph":

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Graph() (grafo semplice non-diretto)
		# MultiGraph() (grafo non-diretto)
		#

		options = ['Graph', 'MultiGraph']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Graph":
			G=nx.tutte_graph(create_using=nx.Graph())
			matplotdraw = True

		if option is "MultiGraph":
			G=nx.tutte_graph(create_using=nx.MultiGraph())


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
	#
	#

	options = ['fast_gnp_random_graph', 'gnp_random_graph', 'dense_gnm_random_graph', 'gnm_random_graph', 'erdos_renyi_graph', 'binomial_graph', 'newman_watts_strogatz_graph', 'watts_strogatz_graph', 'connected_watts_strogatz_graph']
	option, index = pick(options, title, indicator='>', multi_select=False)

	if option is "fast_gnp_random_graph":

		n = int(input('[*] Insert the number of nodes (int): '))
		p = float(input('[*] Insert the probability of edge creation value (float): '))

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Non-Directed (grafo non-diretto)
		# Directed (grafo diretto)
		#

		options = ['Non-Directed', 'Directed']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Non-Directed":
			G=nx.fast_gnp_random_graph(n, p, directed=False)
		if option is "Directed":
			G=nx.fast_gnp_random_graph(n, p, directed=True)


	if option is "gnp_random_graph":

		n = int(input('[*] Insert the number of nodes (int): '))
		p = float(input('[*] Insert the probability of edge creation value (float): '))

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Non-Directed (grafo non-diretto)
		# Directed (grafo diretto)
		#

		options = ['Non-Directed', 'Directed']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Non-Directed":
			G=nx.gnp_random_graph(n, p, directed=False)
		if option is "Directed":
			G=nx.gnp_random_graph(n, p, directed=True)


	if option is "dense_gnm_random_graph":

		n = int(input('[*] Insert the number of nodes (int): '))
		m = int(input('[*] Insert the number of edges (int): '))

		G=nx.dense_gnm_random_graph(n, m)


	if option is "gnm_random_graph":

		n = int(input('[*] Insert the number of nodes (int): '))
		m = int(input('[*] Insert the number of edges (int): '))

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Non-Directed (grafo non-diretto)
		# Directed (grafo diretto)
		#

		options = ['Non-Directed', 'Directed']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Non-Directed":
			G=nx.gnm_random_graph(n, m, directed=False)
		if option is "Directed":
			G=nx.gnm_random_graph(n, m, directed=True)


	if option is "erdos_renyi_graph":

		n = int(input('[*] Insert the number of nodes (int): '))
		p = float(input('[*] Insert the probability of edge creation value (float): '))

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Non-Directed (grafo non-diretto)
		# Directed (grafo diretto)
		#

		options = ['Non-Directed', 'Directed']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Non-Directed":
			G=nx.erdos_renyi_graph(n, p, directed=False)
		if option is "Directed":
			G=nx.erdos_renyi_graph(n, p, directed=True)


	if option is "binomial_graph":

		n = int(input('[*] Insert the number of nodes (int): '))
		p = float(input('[*] Insert the probability of edge creation value (float): '))

		title = 'Choose random graph type: '

		# TYPES :
		#
		# Non-Directed (grafo non-diretto)
		# Directed (grafo diretto)
		#

		options = ['Non-Directed', 'Directed']
		option, index = pick(options, title, indicator='>', multi_select=False)

		if option is "Non-Directed":
			G=nx.binomial_graph(n, p, directed=False)
		if option is "Directed":
			G=nx.binomial_graph(n, p, directed=True)


	if option is "newman_watts_strogatz_graph":

		n = int(input('[*] Insert the number of nodes (int): '))
		k = int(input('[*] Insert the number of nodes for ring topology (int): '))
		p = float(input('[*] Insert the probability of edge creation value (float): '))

		G=nx.newman_watts_strogatz_graph(n, k, p)


	if option is "watts_strogatz_graph":

		n = int(input('[*] Insert the number of nodes (int): '))
		k = int(input('[*] Insert the number of nodes for ring topology (int): '))
		p = float(input('[*] Insert the probability of edge creation value (float): '))

		G=nx.watts_strogatz_graph(n, k, p)


	if option is "connected_watts_strogatz_graph":

		n = int(input('[*] Insert the number of nodes (int): '))
		k = int(input('[*] Insert the number of nodes for ring topology (int): '))
		p = float(input('[*] Insert the probability of edge creation value (float): '))
		tries = int(input('[*] Insert the number of attempts to generate a connected graph (int): '))

		G=nx.connected_watts_strogatz_graph(n, k, p, tries)


####################################################
#################### MAIN BLOCK ####################
####################################################

title = 'Choose edge weight type: '

# LAYOUTS :
#
# integer
# float
#

options = ['integer', 'float']
option, index = pick(options, title, indicator='>', multi_select=False)

# integer weights
if option is "integer":

	print("\n")
	MinInt = int(input('[*] Insert MinInt range int number: '))
	MaxInt = int(input('[*] Insert MaxInt range int number: '))
	print("\n")

	for (u,v,w) in G.edges(data=True):
	    w['weight'] = random.randint(MinInt, MaxInt)

# float weights
elif option is "float":

	print("\n")
	MinInt = int(input('[*] Insert MinInt range int number: '))
	MaxInt = int(input('[*] Insert MaxInt range int number: '))
	Aprx = int(input('[*] Set approximation (number of decimals): '))
	print("\n")

	for (u,v,w) in G.edges(data=True):
	    w['weight'] = round(random.uniform(MinInt, MaxInt), Aprx)

# set .edgelist filename
name = input('[*] Insert name for file .edgelist: ')
print("\n")

ext = ".edgelist"

filename = name + ext
print("[!] Name of .edgelist file is: " + filename)

# build home directory path
hubdir = pathlib.Path.cwd().joinpath('gen').joinpath(name)
pathlib.Path(hubdir).mkdir(parents=True, exist_ok=True)
print("[!] Path of home directory is: " + str(hubdir))

# build .edgelist file
nx.write_weighted_edgelist(G, filename)

# move .edgelist file into home directory
filepath = pathlib.Path.cwd().joinpath(filename)
newfilepath = pathlib.Path.cwd().joinpath('gen').joinpath(name).joinpath(filename)
shutil.move(filepath, newfilepath)
print("[!] Final .edgelist file path is: " + str(newfilepath))
print("\n")

ext2 = ".dot"
dotpath = name + ext2

# build .dot file
# nx.nx_agraph.write_dot(G, dotpath)

print("[X] Creation completed")

####################################################
#################### DRAW BLOCK ####################
####################################################

if matplotdraw:

	title = 'Do you want to draw the graph? '

	# ANSWER :
	#
	# yes (draw/show)
	# no (return)
	#

	options = ['yes', 'no']
	option, index = pick(options, title, indicator='>', multi_select=False)

	if option is "yes":

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
		print("[X] Creation completed")
