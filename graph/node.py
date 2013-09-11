# -*- coding: utf-8 -*-

class Node():

	def __init__(self, value):
		self.value = value
		self.adjacent_nodes = {}

	def add_adj_node(self, node_value, weight):
		self.adjacent_nodes.update({node_value:weight})
	
	def add_dict_adj_nodes(self, nodes):
		self.adjacent_nodes = dict(self.adjacent_nodes.items() + nodes.items())

	def remove_adj_node(self, node_value):
		del self.adjacent_nodes[node_value]

	def qnt_adj_nodes(self):
		return len(self.adjacent_nodes)