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


#####################################################
#################### INIT BLOCK #####################
#####################################################

if platform.system() is "Windows":
	os.system("cls")
else :
	os.system("clear")


# colorama init
init()
matplotdraw  = False


#####################################################
#################### MAIN BLOCK #####################
#####################################################

n = int(input(Style.BRIGHT + Fore.CYAN + '[' + Fore.YELLOW + '*' + Fore.CYAN + ']' + Fore.MAGENTA + ' Insert the number of nodes' + Fore.CYAN + '(' + Fore.YELLOW + 'int' + Fore.CYAN + ')' + Fore.MAGENTA + ': ' + Style.RESET_ALL))

G=nx.complete_graph(n,create_using=nx.Graph())

print("\nnodes:  " + str(list(G.nodes)))
print("edges:  " + str(list(G.edges)))

print("\n")
MinInt = int(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' MIN EDGE VALUE ' + Fore.CYAN + 'range int number: ' + Style.RESET_ALL))
MaxInt = int(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' MAX EDGE VALUE ' + Fore.CYAN + 'range int number: ' + Style.RESET_ALL))
print("\n")

while(True):
    maxc = int(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' MAX COLOR ' + Fore.CYAN + 'range int number [ 0 <= colors <= MAX COLOR ]: ' + Style.RESET_ALL))
    if(maxc <= n):
        break
    else:
        print("INVALID VALUE --> NUMBER OF COLORS MUST BE <= NUMBER OF NODES\n")
        continue

print("\n")
maxp = int(input(Style.BRIGHT + Fore.MAGENTA + '[' + Fore.YELLOW + '*' + Fore.MAGENTA + '] ' + Fore.CYAN + 'Insert' + Fore.YELLOW + ' MAX COLOR PROFIT ' + Fore.CYAN + 'range int number: ' + Style.RESET_ALL))

print("\n")

################################################################################

for (u,v,w) in G.edges(data=True):
    w['weight'] = random.randint(MinInt, MaxInt)

print(Style.BRIGHT + Fore.RED + "COLORS (LIST)\n" + Style.RESET_ALL)
colors = list(range(maxc))
print(colors)
print("\n")

################################################################################

for (n,c) in G.nodes(data=True):
    c['color'] = random.choice(colors)

print(Style.BRIGHT + Fore.RED + "NODE -- COLOR (DICTIONARY) == INITIAL COLOURING\n" + Style.RESET_ALL)
for (node,data) in G.nodes(data=True):
    print(node,data)

print("\nnumber of nodes:  " + str(G.number_of_nodes()))
print("\n")

################################################################################

print(Style.BRIGHT + Fore.RED + "NODE -- COLORS -- PROFITS (NESTED DICTIONARY)\n" + Style.RESET_ALL)

result = {node:{color:random.randint(0,maxp) for color in colors} for node in G.nodes()}

pprint(result)
print("\n")

################################################################################

print(Style.BRIGHT + Fore.RED + "NODE -- NODE -- EDGE WEIGHT (LIST OF LIST OF DICTIONARY)\n" + Style.RESET_ALL)
for (u,v,w) in G.edges(data=True):
    print(u,v,w)

print("\nnumber of edges:  " + str(G.number_of_edges()))
print("\n")

################################################################################
################################################################################

plt.figure("INITIAL NODE COLORS")

nx.draw_networkx(G, nx.circular_layout(G), with_labels=False, node_size=400, node_color='yellow', width=2.0, style='solid', font_color='black', font_weight='bold')

edge_labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, nx.circular_layout(G), edge_labels = edge_labels)

node_labels = nx.get_node_attributes(G,'color')
nx.draw_networkx_labels(G, nx.circular_layout(G), labels = node_labels, font_color = 'black', font_weight = 'bold')

plt.axis('off')

################################################################################

print(Style.BRIGHT + Fore.MAGENTA + "### PROFITS FOR NODE IN COLOURING C BASED ON CURRENT COLORS ##\n" + Style.RESET_ALL)

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



sys.exit()

################################################################################

print(Style.BRIGHT + Fore.MAGENTA + "### PROFITS FOR NODE IN COLOURING C BASED ON CURRENT COLORS ##\n" + Style.RESET_ALL)

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

################################################################################

plt.figure("NODE VALUES")

nx.draw_networkx(G, nx.circular_layout(G), with_labels=True, node_size=400, node_color='black', width=2.0, style='solid', font_color='white', font_weight='bold')

edge_labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, nx.circular_layout(G), edge_labels = edge_labels)

plt.axis('off')

plt.figure("NODE COLORS")

nx.draw_networkx(G, nx.circular_layout(G), with_labels=False, node_size=400, node_color='orange', width=2.0, style='solid', font_color='black', font_weight='bold')

edge_labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, nx.circular_layout(G), edge_labels = edge_labels)

node_labels = nx.get_node_attributes(G,'color')
nx.draw_networkx_labels(G, nx.circular_layout(G), labels = node_labels, font_color = 'black', font_weight = 'bold')

plt.axis('off')

plt.show()
