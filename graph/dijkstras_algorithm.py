# -*- coding: utf-8 -*-

import sys

class DijkstrasAlgorithm():

	def __init__(self, graph):
		self.graph = graph
		self.get_origin_and_end_node()
		self.minimum_cost = 0
		self.unvisted_nodes = set()
		self.minimum_costs = {}
		
	def get_origin_and_end_node(self):
		self.origin_node = raw_input('Origin node: ')
		self.end_node = raw_input('End node: ')
		if self.origin_node not in self.graph.nodes or self.end_node not in self.graph.nodes:
			raise Exception("The origin and end nodes must be on graph")

	def run(self):
		self.print_header()
		
		if self.origin_node != self.end_node:
			self.calculate_minimum_cost()

		self.print_result()

	def calculate_minimum_cost(self):
		self.set_initial_unvisited_nodes_and_min_costs()
		current_node = self.origin_node

		while self.end_node in self.unvisted_nodes:
			unvisted_neighbors = self.get_unvisted_neighbors(current_node)
			
			for neighbor in unvisted_neighbors:
				self.updete_min_distances(neighbor, current_node)				
			
			self.unvisted_nodes.remove(current_node)
			current_node = self.get_current_node()
			
		self.minimum_cost = self.minimum_costs[self.end_node]

	def set_initial_unvisited_nodes_and_min_costs(self):
		nodes = self.graph.get_nodes()

		for i in xrange(0,self.graph.order()):
			node = nodes.pop()
			self.unvisted_nodes.update(node)
			self.minimum_costs.update({node:sys.maxint})

		self.minimum_costs[self.origin_node] = 0

	def get_unvisted_neighbors(self, current_node):
		neighbors = self.graph.get_adj_nodes(current_node)
		return neighbors.intersection(self.unvisted_nodes)

	def updete_min_distances(self, neighbor, current_node):
		distance = self.minimum_costs[current_node] + self.graph.get_weight(current_node, neighbor)
		if distance < self.minimum_costs[neighbor]:
			self.minimum_costs.update({neighbor:distance})

	def get_current_node(self):
		if len(self.unvisted_nodes) != 0:
			return min(self.unvisted_nodes, key=lambda j:self.minimum_costs[j])

	def print_header(self):
		print "Dijkstra Algorithm:"
		print "  Origin node:", str(self.origin_node)
		print "  End node:", str(self.end_node)

	def print_result(self):
		print "  The minimum cost is:", self.minimum_cost
