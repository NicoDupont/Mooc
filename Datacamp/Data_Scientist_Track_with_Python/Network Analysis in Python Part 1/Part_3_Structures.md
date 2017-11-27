11/2017  
# Datacamp - Network Analysis in Python (Part 1) (Data Scientist Track with Python)  
[Network Analysis in Python (Part 1)](https://www.datacamp.com/courses/network-analysis-in-python-part-1)
---

***Course Description***  

From online social networks such as Facebook and Twitter to transportation networks such as bike sharing systems, networks are everywhere, and knowing how to analyze this type of data will open up a new world of possibilities for you as a Data Scientist. This course will equip you with the skills to analyze, visualize, and make sense of networks. You'll apply the concepts you learn to real-world network data using the powerful NetworkX library. With the knowledge gained in this course, you'll develop your network thinking skills and be able to start looking at your data with a fresh perspective!        

# Part 3 : Structures   

This chapter is all about finding interesting structures within network data. You'll learn about essential concepts such as cliques, communities, and subgraphs, which will leverage all of the skills you acquired in Chapter 2. By the end of this chapter, you'll be ready to apply the concepts you've learned to a real-world case study.   

## Identifying triangle relationships   

Now that you've learned about cliques, it's time to try leveraging what you know to find structures in a network. Triangles are what you'll go for first. We may be interested in triangles because they're the simplest complex clique. Let's write a few functions; these exercises will bring you through the fundamental logic behind network algorithms.  

In the Twitter network, each node has an 'occupation' label associated with it, in which the Twitter user's work occupation is divided into celebrity, politician and scientist. One potential application of triangle-finding algorithms is to find out whether users that have similar occupations are more likely to be in a clique with one another.  

### Instructions

 - Import combinations from itertools.
 - Write a function is_in_triangle() that has two parameters - G and n - and checks whether a given node is in a triangle relationship or not.
	 - combinations(iterable, n) returns combinations of size n from iterable. This will be useful here, as you want combinations of size 2 from G.neighbors(n).
	 - To check whether an edge exists between two nodes, use the .has_edge(node1, node2) method. If an edge exists, then the given node is in a triangle relationship, and you should return True.

```python
from itertools import combinations

# Define is_in_triangle() 
def is_in_triangle(G, n):
    """
    Checks whether a node `n` in graph `G` is in a triangle relationship or not. 
    
    Returns a boolean.
    """
    in_triangle = False
    
    # Iterate over all possible triangle relationship combinations
    for n1, n2 in combinations(G.neighbors(n),2):
    
        # Check if an edge exists between n1 and n2
        if G.has_edge(n1, n2):
            in_triangle = True
            break
    return in_triangle
```

### Results :  

Excellent! You're going to modify this function in the next exercise to extract all nodes involved in a triangle relationship with a given node.  

---


## How many clusters?    

NetworkX provides an API for counting the number of triangles that every node is involved in: nx.triangles(G). It returns a dictionary of nodes as the keys and number of triangles as the values. Your job in this exercise is to modify the function defined earlier to extract all of the nodes involved in a triangle relationship with a given node.  

### Instructions

 - Write a function nodes_in_triangle() that has two parameters - G and n - and identifies all nodes in a triangle relationship with a given node.
	 - In the for loop, iterate over all possible triangle relationship combinations.
	 - Check whether the nodes n1 and n2 have an edge between them. If they do, add both nodes to the set triangle_nodes.
 - Use your function in an assert statement to check that the number of nodes involved in a triangle relationship with node 1 of graph T is equal to 35.

```python
from itertools import combinations

# Write a function that identifies all nodes in a triangle relationship with a given node.
def nodes_in_triangle(G, n):
    """
    Returns the nodes in a graph `G` that are involved in a triangle relationship with the node `n`.
    """
    triangle_nodes = set([n])
    
    # Iterate over all possible triangle relationship combinations
    for n1, n2 in combinations(G.neighbors(n),2):
    
        # Check if n1 and n2 have an edge between them
        if G.has_edge(n1, n2):
        
            # Add n1 to triangle_nodes
            triangle_nodes.add(n1)
            
            # Add n2 to triangle_nodes
            triangle_nodes.add(n2)
            
    return triangle_nodes
    
# Write the assertion statement
assert len(nodes_in_triangle(T, 1)) == 35
```

### Results :  

Great work! Your function correctly identified that node 1 is in a triangle relationship with 35 other nodes.  

---


## Finding open triangles      

Let us now move on to finding open triangles! Recall that they form the basis of friend recommendation systems; if "A" knows "B" and "A" knows "C", then it's probable that "B" also knows "C".  

### Instructions

 - Write a function node_in_open_triangle() that has two parameters - G and n - and identifies whether a node is present in an open triangle with its neighbors.
	 - In the for loop, iterate over all possible triangle relationship combinations.
	 - If the nodes n1 and n2 do not have an edge between them, set in_open_triangle to True, break out from the if statement and return in_open_triangle.
 - Use this function to count the number of open triangles that exist in T.
	 - In the for loop, iterate over all the nodes in T.
	 - If the current node n is in an open triangle, increment num_open_triangles.

```python
from itertools import combinations

# Define node_in_open_triangle()
def node_in_open_triangle(G, n):
    """
    Checks whether pairs of neighbors of node `n` in graph `G` are in an 'open triangle' relationship with node `n`.
    """
    in_open_triangle = False
    
    # Iterate over all possible triangle relationship combinations
    for n1, n2 in combinations(G.neighbors(n),2):
    
        # Check if n1 and n2 do NOT have an edge between them
        if not G.has_edge(n1, n2):
        
            in_open_triangle = True
            
            break
            
    return in_open_triangle

# Compute the number of open triangles in T
num_open_triangles = 0

# Iterate over all the nodes in T
for n in T.nodes():

    # Check if the current node is in an open triangle
    if node_in_open_triangle(T, n):
    
        # Increment num_open_triangles
        num_open_triangles += 1
        
print(num_open_triangles)
```

### Results :  

Excellent job! It looks like 22 nodes in graph T are in open triangles!  

		<script.py> output:
			22

---


## How many clusters?    

Now that you've explored triangles (and open triangles), let's move on to the concept of maximal cliques. Maximal cliques are cliques that cannot be extended by adding an adjacent edge, and are a useful property of the graph when finding communities. NetworkX provides a function that allows you to identify the nodes involved in each maximal clique in a graph: nx.find_cliques(G). Play around with the function by using it on T in the IPython Shell, and then try answering the exercise.  

### Instructions

 - Write a function maximal_cliques() that has two parameters - G and size - and finds all maximal cliques of size n.
	 - In the for loop, iterate over all the cliques in G using the nx.find_cliques() function.
	 - If the current clique is of size size, append it to the list mcs.
 - Use an assert statement and your maximal_cliques() function to check that there are 33 maximal cliques of size 3 in the graph T.

```python
# Define maximal_cliques()
def maximal_cliques(G,size):
    """
    Finds all maximal cliques in graph `G` that are of size `size`.
    """
    mcs = []
    for clique in nx.find_cliques(G):
        if len(clique) == size:
            mcs.append(clique)
    return mcs

# Check that there are 33 maximal cliques of size 3 in the graph T
assert len(maximal_cliques(T,3)) == 33
```

### Results :  

Great work! There are 33 maximal cliques of size 3 in T.  

---


## Subgraphs I    

There may be times when you just want to analyze a subset of nodes in a network. To do so, you can copy them out into another graph object using G.subgraph(nodes), which returns a new graph object (of the same type as the original graph) that is comprised of the iterable of nodes that was passed in.  

matplotlib.pyplot has been imported for you as plt.  

### Instructions

 - Write a function get_nodes_and_nbrs(G, nodes_of_interest) that extracts the subgraph from graph G comprised of the nodes_of_interest and their neighbors.
	 - In the first for loop, iterate over nodes_of_interest and append the current node n to nodes_to_draw.
	 - In the second for loop, iterate over the neighbors of n, and append all the neighbors nbr to nodes_to_draw.
 - Use the function to extract the subgraph from T comprised of nodes 29, 38, and 42 (contained in the pre-defined list nodes_of_interest) and their neighbors. Save the result as T_draw.
 - Draw the subgraph T_draw to the screen.

```python
nodes_of_interest = [29, 38, 42]

# Define get_nodes_and_nbrs()
def get_nodes_and_nbrs(G, nodes_of_interest):
    """
    Returns a subgraph of the graph `G` with only the `nodes_of_interest` and their neighbors.
    """
    nodes_to_draw = []
    
    # Iterate over the nodes of interest
    for n in nodes_of_interest:
    
        # Append the nodes of interest to nodes_to_draw
        nodes_to_draw.append(n)
        
        # Iterate over all the neighbors of node n
        for nbr in G.neighbors(n):
        
            # Append the neighbors of n to nodes_to_draw
            nodes_to_draw.append(nbr)
            
    return G.subgraph(nodes_to_draw)

# Extract the subgraph with the nodes of interest: T_draw
T_draw = T.subgraph(get_nodes_and_nbrs(T, nodes_of_interest))

# Draw the subgraph to the screen
nx.draw(T_draw, with_labels=True)
plt.show()
```

### Results :  

Great work! The subgraph consisting of the nodes of interest and their neighbors has 7 nodes.   

![graph10](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Data_Scientist_Track_with_Python/Network%20Analysis%20in%20Python%20Part%201/img/graph10.svg)

---


## Subgraphs II      

In the previous exercise, we gave you a list of nodes whose neighbors we asked you to extract.  

Let's try one more exercise in which you extract nodes that have a particular metadata property and their neighbors. This should hark back to what you've learned about using list comprehensions to find nodes. The exercise will also build your capacity to compose functions that you've already written before.  

### Instructions

 - Using a list comprehension, extract nodes that have the metadata 'occupation' as 'celebrity' alongside their neighbors:
 - The output expression of the list comprehension is n, and there are two iterator variables: n and d. The iterable is the list of nodes of T (including the metadata, which you can specify using data=True) and the conditional expression is if the 'occupation' key of the metadata dictionary d equals 'celebrity'.
 - Place them in a new subgraph called T_sub. To do this:
 - Iterate over the nodes, compute the neighbors of each node, and add them to the set of nodes nodeset by using the .union() method. This last part has been done for you.
 - Use nodeset along with the T.subgraph() method to calculate T_sub.
 - Draw T_sub to the screen.

```python
# Extract the nodes of interest: nodes
nodes = [n for n, d in T.nodes(data=True) if d['occupation'] == 'celebrity']

# Create the set of nodes: nodeset
nodeset = set(nodes)

# Iterate over nodes
for n in nodes:

    # Compute the neighbors of n: nbrs
    nbrs = T.neighbors(n)
    
    # Compute the union of nodeset and nbrs: nodeset
    nodeset = nodeset.union(nbrs)

# Compute the subgraph using nodeset: T_sub
T_sub = T.subgraph(nodeset)

# Draw T_sub to the screen
nx.draw(T_sub)
plt.show()
```

### Results :  


Excellent job! You're now ready to bring together all of the concepts you've learned and apply them to a case study!  

![graph11](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Data_Scientist_Track_with_Python/Network%20Analysis%20in%20Python%20Part%201/img/graph11.svg)

---
