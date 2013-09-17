# -*- coding: utf-8 -*-

import sys

class DijkstrasAlgorithm():

	def __init__(self, graph):
		self.graph = graph
		self.origin_node = graph.get_random_node()
		self.end_node = graph.get_random_node()
		self.minimum_custom = 0
	
	def run(self):
		self.print_header()
		
		if self.origin_node != self.end_node:
			nodes = self.graph.get_nodes()
			unvisted_nodes = set()
			minimum_customs = {}

			for i in xrange(0,self.graph.order()):
				node = nodes.pop()
				unvisted_nodes.update(node)
				minimum_customs.update({node:sys.maxint})

			minimum_customs[self.origin_node] = 0
			current_node = self.origin_node

			while self.end_node in unvisted_nodes:
				neighbors = self.graph.get_adj_nodes(current_node)
				unvisted_neighbors = neighbors.intersection(unvisted_nodes)
				
				for neighbor in unvisted_neighbors:
					distance = minimum_customs[current_node] + self.graph.get_weight(current_node, neighbor)
					if distance < minimum_customs[neighbor]:
						minimum_customs.update({neighbor:distance})

				unvisted_nodes.remove(current_node)
				if len(unvisted_nodes) != 0:
					current_node = min(unvisted_nodes, key=lambda j:minimum_customs[j])
				
			self.minimum_custom = minimum_customs[self.end_node]

		self.print_result()

	def print_header(self):
		print "Dijkstra Algorithm:"
		print "  Origin node:", str(self.origin_node)
		print "  End node:", str(self.end_node)

	def print_result(self):
		print "  The minimum custom is:", self.minimum_custom
