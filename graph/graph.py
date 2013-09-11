# -*- coding: utf-8 -*-

from node import Node

class Graph():
	
    def __init__(self):
    	self.nodes = set()
    	pass

    def success_method(self):
    	# self.test_node()    
    	self.add_node(5)
    	self.print_nodes()

    def add_node(self, node_value):
    	node = Node(node_value)
    	self.nodes.add(node)

    def remove_node(self, node_value):
    	pass

    def print_nodes(self):
    	for node in self.nodes:
    		print node.value

    def test_node(self):
        node = Node(5)
    	print node.adjacent_nodes, "length: ", node.qnt_adj_nodes()
    	node.add_adj_node(2,3)
    	print node.adjacent_nodes, "length: ", node.qnt_adj_nodes()
    	node.add_dict_adj_nodes({6:9,7:1})
    	print node.adjacent_nodes, "length: ", node.qnt_adj_nodes()
    	node.remove_adj_node(6)
    	print node.adjacent_nodes, "length: ", node.qnt_adj_nodes()