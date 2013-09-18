# -*- coding: utf-8 -*-

from graph import Graph
from node import Node

class GraphCreator():

	def __init__(self):
		self.graph = Graph()

	def get_test_graph(self):
		self.graph.add_node("A")
		self.graph.add_node("B")
		self.graph.add_node("C")
		self.graph.add_node("D")
		self.graph.add_node("E")
		self.graph.add_node("F")
		self.graph.add_node("G")

		self.graph.connect_nodes("A", "B", 7)
		self.graph.connect_nodes("A", "F", 5)
		self.graph.connect_nodes("A", "G", 3)
		self.graph.connect_nodes("B", "C", 2)
		self.graph.connect_nodes("B", "G", 3)
		self.graph.connect_nodes("C", "D", 5)
		self.graph.connect_nodes("C", "G", 2)
		self.graph.connect_nodes("C", "E", 3)
		self.graph.connect_nodes("D", "E", 4)
		self.graph.connect_nodes("E", "G", 4)
		self.graph.connect_nodes("E", "F", 6)
		self.graph.connect_nodes("F", "G", 3)

		self.graph.print_graph()

		return self.graph

	def get_personalized_graph(self):
		print "Let's create a new graph!"
		self.create_nodes()
		self.create_connections()
		print "Ok, your graph is ready now! Take a look:"
		self.graph.print_graph()

		return self.graph

	def create_nodes(self):
		number_of_nodes = self.get_number_of_nodes()

		for i in xrange(1,number_of_nodes+1):
			print "###\n" + "Node number " + str(i) + ":"
			node_value = raw_input('Node value: ')
			self.graph.add_node(node_value)						

		print "The nodes are all created now. Let's make the connections!"

	def get_number_of_nodes(self):
		try:
			return int(raw_input('Enter the number of nodes (int): '))
		except:
			raise TypeError("Number of nodes must be an integer!")

	def create_connections(self):
		number_of_connections = self.get_number_of_connections()

		for j in xrange(1,number_of_connections+1):
			print "###\n" + "Connection " + str(j) + ":"
			node_value1 = raw_input('First node you want to connect: ')
			node_value2 = raw_input('Second node you want to connect: ')
			weight = self.get_weight_connections()
			self.graph.connect_nodes(node_value1, node_value2, weight)	

	def get_number_of_connections(self):
		try:
			return int(raw_input('Enter the number of connections you want for the whole graph (int): '))
		except:
			raise TypeError("Number of connectios must be an integer!")

	def get_weight_connections(self):
		try:
			return int(raw_input('The weight for this connection (int): '))
		except:
			raise TypeError("Weight must be an integer!")