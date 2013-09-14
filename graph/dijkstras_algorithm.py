# -*- coding: utf-8 -*-

class DijkstrasAlgorithm():

	def __init__(self, graph):
		self.graph = graph
		# self.origin_node = graph.get_random_node()
		# self.end_node = graph.get_random_node()
		self.origin_node = "B"
		self.end_node = "B"
		self.minimum_custom = 0
		self.shortest_path = []
	
	def run(self):
		self.print_header()
		
		if self.origin_node == self.end_node:
			self.shortest_path.append(self.end_node)
		else:
			pass

		self.print_result()

	def print_header(self):
		print "Dijkstra Algorithm:"
		print "  Origin node:", str(self.origin_node)
		print "  End node:", str(self.end_node)

	def print_result(self):
		print "  The shortest path is:", str(self.shortest_path)
		print "  The minimum custom is:", self.minimum_custom
