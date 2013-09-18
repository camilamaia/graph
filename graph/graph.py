# -*- coding: utf-8 -*-

from node import Node
import random

class Graph():
	
    def __init__(self):
    	self.nodes = {}

    def add_node(self, node_value):
        if node_value not in self.nodes:
        	node = Node(node_value)
        	self.nodes.update({node.value:node})
        else:
            raise Exception("Error adding: The node " + str(node_value) + " is already on graph")

    def remove_node(self, node_value):
    	if node_value in self.nodes:
            del self.nodes[node_value]
            for node in self.nodes.values():
                if node_value in node.adjacent_nodes:
                    node.remove_adj_node(node_value)
        else:
            raise Exception("Error removing: There is no node " + str(node_value) + " on Graph")

    def connect_nodes(self, node_value1, node_value2, weight) :
        if node_value1 in self.nodes and node_value2 in self.nodes:
            node1 = self.nodes[node_value1]
            node2 = self.nodes[node_value2]

            node1.add_adj_node(node_value2,weight)
            node2.add_adj_node(node_value1,weight)
        else:
            raise Exception("Error connecting: The two nodes must be on graph")

    def disconnect_nodes(self, node_value1, node_value2) :
        if node_value1 in self.nodes and node_value2 in self.nodes:
            node1 = self.nodes[node_value1]
            node2 = self.nodes[node_value2]

            node1.remove_adj_node(node_value2)
            node2.remove_adj_node(node_value1)
        else:
            raise Exception("Error disconnecting: The two nodes must be on graph")

    def order(self):
        return len(self.nodes)

    def get_nodes(self):
        return set(self.nodes.keys())        

    def get_random_node(self):
        return random.choice(self.nodes.keys())

    def get_adj_nodes(self, node_value):
        if node_value in self.nodes:
            node = self.nodes[node_value]
            return set(node.adjacent_nodes.keys())
        raise Exception("Error getting adjacent nodes: There is no node " + str(node_value) + " on Graph")

    def size(self, node_value):
        if node_value in self.nodes:
            node = self.nodes[node_value]
            return node.qnt_adj_nodes()
        raise Exception("Error getting size: There is no node " + str(node_value) + " on Graph")

    def get_weight(self, node_value1, node_value2):
        if node_value1 in self.nodes and node_value2 in self.nodes:
            node1 = self.nodes[node_value1]
            return node1.get_weight(node_value2)
        else:
            raise Exception("Error getting weight: The two nodes must be on graph")

    def print_graph(self):
        print "Graph: \n  {"
        for node_value in self.nodes:
    		print '    ', node_value, self.nodes[node_value].adjacent_nodes
        print "  }"
        print "  order:", str(self.order()), "\n"     