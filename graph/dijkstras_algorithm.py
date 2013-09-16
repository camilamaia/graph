# -*- coding: utf-8 -*-

class DijkstrasAlgorithm():

	def __init__(self, graph):
		self.graph = graph
		# self.origin_node = graph.get_random_node()
		# self.end_node = graph.get_random_node()
		self.origin_node = "A"
		self.end_node = "D"
		self.minimum_custom = 0
	
	def run(self):
		self.print_header()
		
		if self.origin_node != self.end_node:
			nodes = self.graph.get_nodes()
			nodes_unvisted = set()
			minimum_customs = {}

			for i in xrange(0,self.graph.order()):
				node = nodes.pop()
				nodes_unvisted.update(node)
				minimum_customs.update({node:-1})

			minimum_customs[self.origin_node] = 0
			current_node = self.origin_node

			


			print minimum_customs
			print nodes_unvisted



		self.print_result()

	def print_header(self):
		print "Dijkstra Algorithm:"
		print "  Origin node:", str(self.origin_node)
		print "  End node:", str(self.end_node)

	def print_result(self):
		print "  The minimum custom is:", self.minimum_custom
