# -*- coding: utf-8 -*-

from node import Node

class Graph():
	
    def __init__(self):
    	self.nodes = {}
    	pass

    def success_method(self):
    	self.test_node()    
    	self.add_node(5)
        self.print_graph()
        self.remove_node(10)
        self.print_graph()

    def add_node(self, node_value):
        if node_value not in self.nodes:
        	node = Node(node_value)
        	self.nodes.update({node.value:node})
        else:
            print "Error adding: The node " + str(node_value) + " is already on graph."

    def remove_node(self, node_value):
    	if node_value in self.nodes:
            del self.nodes[node_value]
            for node in self.nodes.values():
                if node_value in node.adjacent_nodes:
                    node.remove_adj_node(node_value)
        else:
            print "Error removing: There is no node " + str(node_value) + " on Graph"

    def conect_nodes(self, node_value1, node_value2) :
        pass

    def print_graph(self):
        print "Graph: \n{"
        for node_value in self.nodes:
    		print '  ', node_value, self.nodes[node_value].adjacent_nodes
        print "}"

    def test_node(self):
        node = Node(10)
        self.nodes.update({node.value:node})
        self.print_graph()
        node.add_adj_node(2,3)
        self.print_graph()
        node.add_dict_adj_nodes({6:9,5:1})
        self.print_graph()
        node.remove_adj_node(6)
        self.print_graph()