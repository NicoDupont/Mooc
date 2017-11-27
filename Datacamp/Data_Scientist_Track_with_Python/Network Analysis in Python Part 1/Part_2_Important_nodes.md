11/2017  
# Datacamp - Network Analysis in Python (Part 1) (Data Scientist Track with Python)  
[Network Analysis in Python (Part 1)](https://www.datacamp.com/courses/network-analysis-in-python-part-1)
---

***Course Description***  

From online social networks such as Facebook and Twitter to transportation networks such as bike sharing systems, networks are everywhere, and knowing how to analyze this type of data will open up a new world of possibilities for you as a Data Scientist. This course will equip you with the skills to analyze, visualize, and make sense of networks. You'll apply the concepts you learn to real-world network data using the powerful NetworkX library. With the knowledge gained in this course, you'll develop your network thinking skills and be able to start looking at your data with a fresh perspective!        

# Part 2 : Important nodes   

Here, you'll learn about ways of identifying nodes that are important in a network. In doing so, you'll be introduced to more advanced concepts in network analysis as well as learn the basics of path-finding algorithms. The chapter concludes with a deep dive into the Twitter network dataset which will reinforce the concepts you've learned, such as degree centrality and betweenness centrality.  

## Compute number of neighbors for each node      

How do you evaluate whether a node is an important one or not? There are a few ways to do so, and here, you're going to look at one metric: the number of neighbors that a node has.  

Every NetworkX graph G exposes a .neighbors(n) method that returns a list of nodes that are the neighbors of the node n. To begin, use this method in the IPython Shell on the Twitter network T to get the neighbors of of node 1. This will get you familiar with how the function works. Then, your job in this exercise is to write a function that returns all nodes that have m neighbors.  

### Instructions

 - Write a function called nodes_with_m_nbrs() that has two parameters - G and m - and returns all nodes that have m neighbors. To do this:
	 - Iterate over all nodes in G (not including the metadata).
	 - Use the len() function together with the .neighbors() method to calculate the total number of neighbors that node n in graph G has.
		- If the number of neighbors of node n is equal to m, add n to the set nodes using the .add() method.
	 - After iterating over all the nodes in G, return the set nodes.
 - Use your nodes_with_m_nbrs() function to retrieve all the nodes that have 6 neighbors in the graph T.

```python
# Define nodes_with_m_nbrs()
def nodes_with_m_nbrs(G,m):
    """
    Returns all nodes in graph G that have m neighbors.
    """
    nodes = set()
    
    # Iterate over all nodes in G
    for n in G.nodes():
    
        # Check if the number of neighbors of n matches m
        if len(G.neighbors(n)) == m:
        
            # Add the node n to the set
            nodes.add(n)
            
    # Return the nodes with m neighbors
    return nodes

# Compute and print all nodes in T that have 6 neighbors
six_nbrs = nodes_with_m_nbrs(T,6)
print(six_nbrs)
```

### Results :  

Great work! The number of neighbors a node has is one way to identify important nodes. It looks like 25 nodes in graph T have 6 neighbors.  

		<script.py> output:
			{22533, 1803, 11276, 11279, 6161, 4261, 10149, 3880, 16681, 5420, 14898, 64, 14539, 6862, 20430, 9689, 475, 1374, 6112, 9186, 17762, 14956, 2927, 11764, 4725}

---


## Compute degree distribution   

The number of neighbors that a node has is called its "degree", and it's possible to compute the degree distribution across the entire graph. In this exercise, your job is to compute the degree distribution across T.  

### Instructions

 - Use a list comprehension along with the .neighbors(n) method to get the degree of every node. The result should be a list of integers.
	 - Use n as your iterator variable.
	 - The output expression of your list comprehension should be the number of neighbors that node n has - that is, its degree. Use the len() function together with the .neighbors() method to compute this.
	 - The iterable in your list comprehension is the all the nodes in T, accessed using the .nodes() method.
 - Print the degrees.

```python
# Compute the degree of every node: degrees
degrees = [len(T.neighbors(n)) for n in T.nodes()]

# Print the degrees
print(degrees)
```

### Results :  

Excellent job! In the next exercise, you're going to visualize this degree distribution as well as the degree centrality distribution.  

---


## Degree centrality distribution    

The degree of a node is the number of neighbors that it has. The degree centrality is the number of neighbors divided by all possible neighbors that it could have. Depending on whether self-loops are allowed, the set of possible neighbors a node could have could also include the node itself.  

The nx.degree_centrality(G) function returns a dictionary, where the keys are the nodes and the values are their degree centrality values.  

The degree distribution degrees you computed in the previous exercise using the list comprehension has been pre-loaded.  

### Instructions

 - Compute the degree centrality of the Twitter network T.
 - Using plt.hist(), plot a histogram of the degree centrality distribution of T. This can be accessed using list(deg_cent.values()).
 - Plot a histogram of the degree distribution degrees of T. This is the same list you computed in the last exercise.
 - Create a scatter plot with degrees on the x-axis and the degree centrality distribution list(deg_cent.values()) on the y-axis.

```python
# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Compute the degree centrality of the Twitter network: deg_cent
deg_cent = nx.degree_centrality(T)

# Plot a histogram of the degree centrality distribution of the graph.
plt.figure()
plt.hist(list(deg_cent.values()))
plt.show()

# Plot a histogram of the degree distribution of the graph
plt.figure()
plt.hist([len(T.neighbors(n)) for n in T.nodes()])
plt.show()

# Plot a scatter plot of the centrality distribution and the degree distribution
plt.figure()
plt.scatter(degrees,list(deg_cent.values()))
plt.show()
```

### Results :  

Great work! Click the 'Next Plot' and 'Previous Plot' buttons to cycle through your 3 plots. Given the similarities of their histograms, it should not surprise you to see a perfect correlation between the centrality distribution and the degree distribution.  

![graph6](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Data_Scientist_Track_with_Python/Network%20Analysis%20in%20Python%20Part%201/img/graph6.svg)
![graph7](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Data_Scientist_Track_with_Python/Network%20Analysis%20in%20Python%20Part%201/img/graph7.svg)
![graph8](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Data_Scientist_Track_with_Python/Network%20Analysis%20in%20Python%20Part%201/img/graph8.svg)

---


## Shortest Path I   

You can leverage what you know about finding neighbors to try finding paths in a network. One algorithm for path-finding between two nodes is the "breadth-first search" (BFS) algorithm. In a BFS algorithm, you start from a particular node and iteratively search through its neighbors and neighbors' neighbors until you find the destination node.  

Pathfinding algorithms are important because they provide another way of assessing node importance; you'll see this in a later exercise.  

In this set of 3 exercises, you're going to build up slowly to get to the final BFS algorithm. The problem has been broken into 3 parts that, if you complete in succession, will get you to a first pass implementation of the BFS algorithm.  

### Instructions

 - Create a function called path_exists() that has 3 parameters - G, node1, and node2 - and returns whether or not a path exists between the two nodes.
 - Initialize the queue of cells to visit with the first node, node1. queue should be a list`.
 - Iterate over the nodes in queue.
 - Get the neighbors of the node using the .neighbors() method of the graph G.
 - Check to see if the destination node node2 is in the set of neighbors. If it is, return True.

```python
# Define path_exists()
def path_exists(G,node1,node2):
    """
    This function checks whether a path exists between two nodes (node1, node2) in graph G.
    """
    visited_nodes = set()
    
    # Initialize the queue of cells to visit with the first node: queue
    queue = [node1] 
    
    # Iterate over the nodes in the queue
    for node in queue:
    
        # Get neighbors of the node
        neighbors = G.neighbors(node) 
        
        # Check to see if the destination node is in the set of neighbors
        if node2 in neighbors:
            print('Path exists between nodes {0} and {1}'.format(node1, node2))
            return True
            break
```

### Results :  

Great! In the next exercise, you'll extend this function by including the condition where the destination node is not present in the neighbors.  

---


## Shortest Path II   

Now that you've got the code for checking whether the destination node is present in neighbors, next up, you're going to extend the same function to write the code for the condition where the destination node is not present in the neighbors.  

All the code you need to write is in the else condition; that is, if node2 is not in neighbors.  

### Instructions

 - Using the .add() method, add the current node node to the set visited_nodes to keep track of what nodes have already been visited.
 - Add the neighbors of the current node node that have not yet been visited to queue. To do this, you'll need to use the .extend() method of queue together with a list comprehension. The .extend() method appends all the items in a given list.
 - The output expression and iterator variable of the list comprehension are both n. The iterable is the list neighbors, and the conditional is if n is not in the visited nodes.

```python
def path_exists(G, node1, node2):
    """
    This function checks whether a path exists between two nodes (node1, node2) in graph G.
    """
    visited_nodes = set()
    queue = [node1]
    
    for node in queue:  
        neighbors = G.neighbors(node)
        if node2 in neighbors:
            print('Path exists between nodes {0} and {1}'.format(node1, node2))
            return True
            break
        
        else:
            # Add current node to visited nodes
            visited_nodes.add(node)
            
            # Add neighbors of current node that have not yet been visited
            queue.extend([n for n in neighbors if n not in visited_nodes])
```

### Results :  

Excellent work, you're almost there! To complete the function, you have to write code for the condition in which there is no path between two nodes.  

---


## How many clusters?    

This is the final exercise of this trio! You're now going to complete the problem by writing the code that returns False if there's no path between two nodes.  

### Instructions

 - Check to see if the queue has been emptied. You can do this by inspecting the last element of queue with [-1].
 - Place the appropriate return statement for indicating whether there's a path between these two nodes.


```python
def path_exists(G, node1, node2):
    """
    This function checks whether a path exists between two nodes (node1, node2) in graph G.
    """
    visited_nodes = set()
    queue = [node1]
    
    for node in queue:  
        neighbors = G.neighbors(node)
        if node2 in neighbors:
            print('Path exists between nodes {0} and {1}'.format(node1, node2))
            return True
            break

        else:
            visited_nodes.add(node)
            queue.extend([n for n in neighbors if n not in visited_nodes])
        
        # Check to see if the final element of the queue has been reached
        if node == queue[-1]:
            print('Path does not exist between nodes {0} and {1}'.format(node1, node2))

            # Place the appropriate return statement
            return False
```

### Results :  

Fantastic! You've just written an implementation of the BFS algorithm!  

---


## NetworkX betweenness centrality on a social network     

Betweenness centrality is a node importance metric that uses information about the shortest paths in a network. It is defined as the fraction of all possible shortest paths between any pair of nodes that pass through the node.  

NetworkX provides the nx.betweenness_centrality(G) function for computing the betweenness centrality of every node in a graph, and it returns a dictionary where the keys are the nodes and the values are their betweenness centrality measures.  

### Instructions

 - Compute the betweenness centrality bet_cen of the nodes in the graph T.
 - Compute the degree centrality deg_cen of the nodes in the graph T.
 - Compare betweenness centrality to degree centrality by creating a scatterplot of the two, with list(bet_cen.values()) on the x-axis and list(deg_cen.values()) on the y-axis.

```python
# Compute the betweenness centrality of T: bet_cen
bet_cen = nx.betweenness_centrality(T)

# Compute the degree centrality of T: deg_cen
deg_cen = nx.degree_centrality(T)

# Create a scatter plot of betweenness centrality and degree centrality
plt.scatter(list(bet_cen.values()),list(deg_cen.values()))

# Display the plot
plt.show()
```

### Results :  

Excellent job! Now that you know how to compute different metrics for node importance, you're going to take a deep dive into the Twitter network.  

![graph9](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Data_Scientist_Track_with_Python/Network%20Analysis%20in%20Python%20Part%201/img/graph9.svg)

---


## Deep dive - Twitter network     

You're going to now take a deep dive into a Twitter network, which will help reinforce what you've learned earlier. First, you're going to find the nodes that can broadcast messages very efficiently to lots of people one degree of separation away.  

NetworkX has been pre-imported for you as nx.  

### Instructions

 - Write a function find_nodes_with_highest_deg_cent(G) that returns the node(s) with the highest degree centrality using the following steps:
	 - Compute the degree centrality of G.
	 - Compute the maximum degree centrality using the max() function on list(deg_cent.values()).
	 - Iterate over the degree centrality dictionary, deg_cen.items().
	 - If the degree centrality value v of the current node k is equal to max_dc, add it to the set of nodes.
 - Use your function to find the node(s) that has the highest degree centrality in T.
 - Write an assertion statement that checks that the node(s) is/are correctly identified. This has been done for you, so hit 'Submit Answer' to see the result!

```python
# Define find_nodes_with_highest_deg_cent()
def find_nodes_with_highest_deg_cent(G):

    # Compute the degree centrality of G: deg_cent
    deg_cent = nx.degree_centrality(G)
    
    # Compute the maximum degree centrality: max_dc
    max_dc = max(list(deg_cent.values()))
    
    nodes = set()
    
    # Iterate over the degree centrality dictionary
    for k, v in deg_cent.items():
    
        # Check if the current value has the maximum degree centrality
        if v == max_dc:
        
            # Add the current node to the set of nodes
            nodes.add(k)
            
    return nodes
    
# Find the node(s) that has the highest degree centrality in T: top_dc
top_dc = find_nodes_with_highest_deg_cent(T)
print(top_dc)

# Write the assertion statement
for node in top_dc:
    assert nx.degree_centrality(T)[node] == max(nx.degree_centrality(T).values())
```

### Results :  

Great work! It looks like node 11824 has the highest degree centrality.

		<script.py> output:
			{11824}

---


## Deep dive - Twitter network part II    

Next, you're going to do an analogous deep dive on betweenness centrality! Just a few hints to help you along: remember that betweenness centrality is computed using nx.betweenness_centrality(G).  

### Instructions

 - Write a function find_node_with_highest_bet_cent(G) that returns the node(s) with the highest betweenness centrality.
	 - Compute the betweenness centrality of G.
	 - Compute the maximum betweenness centrality using the max() function on list(bet_cent.values()).
	 - Iterate over the degree centrality dictionary, bet_cent.items().
	 - If the degree centrality value v of the current node k is equal to max_bc, add it to the set of nodes.
 - Use your function to find the node(s) that has the highest betweenness centrality in T.
 - Write an assertion statement that you've got the right node. This has been done for you, so hit 'Submit Answer' to see the result!

```python
# Define find_node_with_highest_bet_cent()
def find_node_with_highest_bet_cent(G):

    # Compute betweenness centrality: bet_cent
    bet_cent = nx.betweenness_centrality(G)
    
    # Compute maximum betweenness centrality: max_bc
    max_bc = max(list(bet_cent.values()))
    
    nodes = set()
    
    # Iterate over the betweenness centrality dictionary
    for k, v in bet_cent.items():
    
        # Check if the current value has the maximum betweenness centrality
        if v == max_bc:
        
            # Add the current node to the set of nodes
            nodes.add(k)
            
    return nodes

# Use that function to find the node(s) that has the highest betweenness centrality in the network: top_bc
top_bc = find_node_with_highest_bet_cent(T)

# Write an assertion statement that checks that the node(s) is/are correctly identified.
for node in top_bc:
    assert nx.betweenness_centrality(T)[node] == max(nx.betweenness_centrality(T).values())
```

### Results :  

Fantastic, you have correctly identified that node 1 has the highest betweenness centrality!  

---
