
class Graph(object):
        def __init__(self):
            self.adjacency_list = {}
            self.edge_weights = {}
        #This add a vertex to the adjacency list and gives the vertex its own list of adjacent vertexs initalized to empty. Time complexity O(1)
        def add_vertex(self, new_vertex):
            self.adjacency_list[new_vertex] = []
        #This adds a directed edge to the graph along with a wight, or in this case, a distance. Time complexity O(1)
        def add_directed_edge(self,vertex_from, vertex_to, weight):
            self.edge_weights[(vertex_from, vertex_to)] = weight
            self.adjacency_list[vertex_from].append(vertex_to)
        #This adds an undirected edge by calling the add_directed twice, once in each direction,
        def add_undirected_edge(self, vertex_a, vertex_b, weight):
            self.add_directed_edge(vertex_a, vertex_b, weight)
            self.add_directed_edge(vertex_b, vertex_a, weight)

          # takes in current address and remaining addresses of the packages on the truck and compares distances. Returns the address closest to the current location. Time complexity O(n)
        def closest_address(self, current_location, next_packages):
               next_up = None
               for i in range(len(next_packages)):
                   if next_up == None:
                       next_up = next_packages[i].destination
                   else:# self.edge_weights[int(current_location.destination_id), int(next_up.destination_id)] > str() and self.edge_weights[int(current_location.destination_id), int(next_packages[i].destination.destination_id)] > str() :
                       check_destination = next_packages[i].destination
                       if float(self.edge_weights[int(current_location.destination_id), int(next_up.destination_id)]) > float(self.edge_weights[int(current_location.destination_id), int(check_destination.destination_id)]):
                           next_up = next_packages[i].destination
               return next_up
