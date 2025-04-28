from collections import defaultdict

# Heuristic function: estimated cost from current node to goal
def heuristic(n):
    H_dist = {
        'A': 1,
        'B': 1,
        'C': 1,
        'D': 1,
        'E': 1,
        'F': 1,
        'G': 0  # Let's assume goal node 'G' has 0 heuristic
    }
    return H_dist.get(n, float('inf'))  # Return high value if node not found

# Define the graph with neighbors and edge weights
Graph_nodes = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 5)],
    'F': [('G', 2)],
    'G': None
}

# Function to get neighbors
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

# A* Algorithm
def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()
    g = {}               # store distance from starting node
    parents = {}         # parents contains an adjacency map of all nodes
    
    g[start_node] = 0
    parents[start_node] = start_node
    
    while len(open_set) > 0:
        n = None

        # Node with the lowest f() = g() + h() is selected
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        
        if n == None:
            print('Path does not exist!')
            return None

        # If the current node is the stop_node
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path

        # Otherwise, for all the neighbors of the node
        if Graph_nodes.get(n) != None:
            for (m, weight) in get_neighbors(n):
                # If this node is not in both open_list and closed_list
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    # Check if better path exists
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        # Move n from open to closed
        open_set.remove(n)
        closed_set.add(n)
    
    print('Path does not exist!')
    return None

# Example Usage
aStarAlgo('A', 'G')
