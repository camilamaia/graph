# -*- coding: utf-8 -*-

from graph import Graph
from node import Node

class GraphCreator():

	def __init__(self):
		pass

	def get_personalized_graph(self):
		graph = Graph()
		print "Let's create a new graph!"
		number_of_nodes = int(raw_input('Enter the number of nodes (int): '))
		for i in xrange(1,number_of_nodes+1):
			print "###\n" + "Node number " + str(i) + ":"
			node_value = raw_input('Node value: ')
			graph.add_node(node_value)						

		print "The nodes are all created now. Let's make the connections!"

		number_of_connections = int(raw_input('Enter the number of connections you want for the whole graph (int): '))

		for j in xrange(1,number_of_connections+1):
			print "###\n" + "Connection " + str(j) + ":"
			node_value1 = raw_input('First node you want to connect: ')
			node_value2 = raw_input('Second node you want to connect: ')
			weight = int(raw_input('The weight for this connection (int): '))

			graph.connect_nodes(node_value1, node_value2, weight)

		print "Ok, your graph is ready now! Take a look:"
		graph.print_graph()

		return graph

	def get_test_graph(self):
		graph = Graph()

		graph.add_node("A")
		graph.add_node("B")
		graph.add_node("C")
		graph.add_node("D")
		graph.add_node("E")
		graph.add_node("F")
		graph.add_node("G")

		graph.connect_nodes("A", "B", 7)
		graph.connect_nodes("A", "F", 5)
		graph.connect_nodes("A", "G", 3)
		graph.connect_nodes("B", "C", 2)
		graph.connect_nodes("B", "G", 3)
		graph.connect_nodes("C", "D", 5)
		graph.connect_nodes("C", "G", 2)
		graph.connect_nodes("C", "E", 3)
		graph.connect_nodes("D", "E", 4)
		graph.connect_nodes("E", "G", 4)
		graph.connect_nodes("E", "F", 6)
		graph.connect_nodes("F", "G", 3)

		graph.print_graph()

		return graph