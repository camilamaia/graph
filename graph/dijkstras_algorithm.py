# -*- coding: utf-8 -*-

import sys

class DijkstrasAlgorithm():

	def __init__(self, graph):
		self.graph = graph
		self.origin_node = graph.get_random_node()
		self.end_node = graph.get_random_node()
		self.minimum_custom = 0
		self.unvisted_nodes = set()
		self.minimum_customs = {}
	
	def run(self):
		self.print_header()
		
		if self.origin_node != self.end_node:
			self.calculate_minimum_custom()

		self.print_result()

	def calculate_minimum_custom(self):
		self.set_initial_unvisited_nodes_and_min_customs()
		current_node = self.origin_node

		while self.end_node in self.unvisted_nodes:
			unvisted_neighbors = self.get_unvisted_neighbors(current_node)
			
			for neighbor in unvisted_neighbors:
				self.updete_min_distances(neighbor, current_node)				
			
			self.unvisted_nodes.remove(current_node)
			current_node = self.get_current_node()
			
		self.minimum_custom = self.minimum_customs[self.end_node]

	def set_initial_unvisited_nodes_and_min_customs(self):
		nodes = self.graph.get_nodes()

		for i in xrange(0,self.graph.order()):
			node = nodes.pop()
			self.unvisted_nodes.update(node)
			self.minimum_customs.update({node:sys.maxint})

		self.minimum_customs[self.origin_node] = 0

	def get_unvisted_neighbors(self, current_node):
		neighbors = self.graph.get_adj_nodes(current_node)
		return neighbors.intersection(self.unvisted_nodes)

	def updete_min_distances(self, neighbor, current_node):
		distance = self.minimum_customs[current_node] + self.graph.get_weight(current_node, neighbor)
		if distance < self.minimum_customs[neighbor]:
			self.minimum_customs.update({neighbor:distance})

	def get_current_node(self):
		if len(self.unvisted_nodes) != 0:
			return min(self.unvisted_nodes, key=lambda j:self.minimum_customs[j])

	def print_header(self):
		print "Dijkstra Algorithm:"
		print "  Origin node:", str(self.origin_node)
		print "  End node:", str(self.end_node)

	def print_result(self):
		print "  The minimum custom is:", self.minimum_custom
