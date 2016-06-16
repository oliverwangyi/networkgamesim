#Require NetworkX, matplotlib
#create_degree_sequence has been sunset
#pesudo_power_sequence_alt gives a alternative way to generate degree sequence

import networkx as nx
from networkx.utils import powerlaw_sequence
import matplotlib.pyplot as plt

degree_sequence_collection = []
network_collection = []
edgelist_collection = []

#Generate a single degree sequence

def pesudo_power_sequence(n, gamma):
    current_degree_sequence = nx.utils.create_degree_sequence(n, powerlaw_sequence, max_tries=50, exponent=gamma)
    return sorted(current_degree_sequence)

#Alternative implementations of above function

def pesudo_power_sequence_alt(n, gamma):
    unround_sequence = powerlaw_sequence(n, exponent=gamma)
    current_degree_sequence=[min(n, max( int(round(unround_sequence)),0)) for s in unround_sequence]
    return sorted(current_degree_sequence)

#Generate all sequence at a specific gamma

def sequence_collection_builder(n, k, gamma):
    count = 0
    while count < k:
        current_degree_sequence = pesudo_power_sequence(n, gamma)
        if current_degree_sequence not in degree_sequence_collection:
            degree_sequence_collection.append(current_degree_sequence)
            count = count+1

#generate 10 instances of sequence of the sepcific gamma
#sequence_collection_builder(100, 10, 2.6)

#Generate the graphs
#Note that configuration model may lead to self-loop and parallel if the there is too many nodes (>10,000)
#nx.Graph() removes parallel edges

def network_builder():
    count = 0
    while count < len(degree_sequence_collection):
        temp_graph = nx.configuration_model(degree_sequence_collection[count])
        network_collection.append(nx.Graph(temp_graph))

#Build edgelist from the configuration model for simulation

def build_edgelist():
    for item in network_collection:
        temp_edgelist = nx.to_edgelist(item)
        edgelist_collection.append(temp_edgelist)

#In case you want to see the visualization of the graphs
#Use "plt.save()" if you want to save the picture

def graph_visual(network_collection):
    for i in range(0, len(network_collection)):
        nx.draw(network_collection[i])
        plt.show()# Requires NetworkX
