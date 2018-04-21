import os
import random
import networkx as nx
import matplotlib.pyplot as plt
from pick import pick

os.system("CLS")

matploitdraw  = False

######################################################
#################### CHOICE BLOCK ####################
######################################################

title = 'Choose random graph class: '

# CLASSES :
#
# Classic
# Expanders
# Lattice
#

options = ['Classic', 'Expanders', 'Lattice']
option, index = pick(options, title, indicator='>', multi_select=False)

if option is "Classic":

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

	# insert draw block
	if option is "chordal_cycle_graph":

		p = int(input('[*] Insert the number of nodes [MUST BE A PRIME NUMBER] (int): '))

		G=nx.chordal_cycle_graph(p, create_using=nx.MultiGraph())




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

if option is "integer":

	MinInt = int(input('[*] Insert MinInt range int number: '))
	MaxInt = int(input('[*] Insert MaxInt range int number: '))

	for (u,v,w) in G.edges(data=True):
	    w['weight'] = random.randint(MinInt, MaxInt)

elif option is "float":

	MinInt = int(input('[*] Insert MinInt range int number: '))
	MaxInt = int(input('[*] Insert MaxInt range int number: '))
	Aprx = int(input('[*] Set approximation (number of decimals): '))

	for (u,v,w) in G.edges(data=True):
	    w['weight'] = round(random.uniform(MinInt, MaxInt), Aprx)

name = input('[*] Insert name for file .edgelist: ')
ext = ".edgelist"

filename = name + ext

nx.write_weighted_edgelist(G, filename)


####################################################
#################### DRAW BLOCK ####################
####################################################

if matploitdraw :

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
		print("[*] Creation completed")
