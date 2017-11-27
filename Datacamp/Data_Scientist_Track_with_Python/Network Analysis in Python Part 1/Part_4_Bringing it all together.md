11/2017  
# Datacamp - Network Analysis in Python (Part 1) (Data Scientist Track with Python)  
[Network Analysis in Python (Part 1)](https://www.datacamp.com/courses/network-analysis-in-python-part-1)
---

***Course Description***  

From online social networks such as Facebook and Twitter to transportation networks such as bike sharing systems, networks are everywhere, and knowing how to analyze this type of data will open up a new world of possibilities for you as a Data Scientist. This course will equip you with the skills to analyze, visualize, and make sense of networks. You'll apply the concepts you learn to real-world network data using the powerful NetworkX library. With the knowledge gained in this course, you'll develop your network thinking skills and be able to start looking at your data with a fresh perspective!        

# Part 4 : Bringing it all together   

In this final chapter of the course, you'll consolidate everything you've learned by diving into an in-depth case study of GitHub collaborator network data. This is a great example of real-world social network data, and your newly acquired skills will be fully tested. By the end of this chapter, you'll have developed your very own recommendation system which suggests GitHub users who should collaborate together. Enjoy!.  

## How many clusters?    

To start out, let's do some basic characterization of the network, by looking at the number of nodes and number of edges in a network. It has been pre-loaded as G and is available for exploration in the IPython Shell. Your job in this exercise is to identify how many nodes and edges are present in the network. You can use the functions len(G.nodes()) and len(G.edges()) to calculate the number of nodes and edges respectively.  

### Possible Answers => 

 - 74095 nodes, 56519 edges.
 - 56519 nodes, 74095 edges.
 - 47095 nodes, 65789 edges.
 - 63762 nodes, 71318 edges.


```python
len(G.nodes())
len(G.edges())
```

### Results :  

Great work! G does indeed have 56519 nodes and 74095 edges.  

		In [1]: len(G.nodes())
		Out[1]: 56519

		In [2]: len(G.edges())
		Out[2]: 74095

---


## Characterizing the network (II)     

Let's continue recalling what you've learned before about node importances, by plotting the degree distribution of a network. This is the distribution of node degrees computed across all nodes in a network.  

### Instructions

 - Plot the degree distribution of the GitHub collaboration network G. Recall that there are four steps involved here:
	 - Calculating the degree centrality of G.
	 - Using the .values() method of G and converting it into a list.
	 - Passing the list of degree distributions to plt.hist().
	 - Displaying the histogram with plt.show().

```python
# Import necessary modules
import matplotlib.pyplot as plt
import networkx as nx 

# Plot the degree distribution of the GitHub collaboration network
plt.hist(list(nx.degree_centrality(G).values()))
plt.show()
```

### Results :  

Excellent job! The next step in characterizing the network is to explore its betweenness centrality distribution.  

![graph12](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Data_Scientist_Track_with_Python/Network%20Analysis%20in%20Python%20Part%201/img/graph12.svg)

---


## Characterizing the network (III)      

The last exercise was on degree centrality; this time round, let's recall betweenness centrality!  

A small note: if executed correctly, this exercise may need about 5 seconds to execute.  

### Instructions

 - Plot the betweenness centrality distribution of the GitHub collaboration network. You have to follow exactly the same four steps as in the previous exercise, substituting nx.betweenness_centrality() in place of nx.degree_centrality().

```python
# Import necessary modules
import matplotlib.pyplot as plt
import networkx as nx

# Plot the degree distribution of the GitHub collaboration network
plt.hist(list(nx.betweenness_centrality(G).values()))
plt.show()
```

### Results :  

Fantastic! You'll now move on to visualizing the network using MatrixPlots, ArcPlots, and CircosPlots.  

![graph13](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Data_Scientist_Track_with_Python/Network%20Analysis%20in%20Python%20Part%201/img/graph13.svg)

---


## MatrixPlot  

Let's now practice making some visualizations. The first one will be the MatrixPlot. In a MatrixPlot, the matrix is the representation of the edges.  

### Instructions

 - Make a MatrixPlot visualization of the largest connected component subgraph, with authors grouped by their user group number.
	 - First, calculate the largest connected component subgraph by using the nx.connected_component_subgraphs(G) inside the provided sorted() function. Python's built-in sorted() function takes an iterable and returns a sorted list (in ascending order, by default). Therefore, to access the largest connected component subgraph, the statement is sliced with [-1].
	 - Create the MatrixPlot object h. You have to specify the parameters graph and node_grouping to be the largest connected component subgraph and 'grouping', respectively.
	 - Draw the MatrixPlot object to the screen and display the plot.

```python
# Import necessary modules
from nxviz import MatrixPlot
import matplotlib.pyplot as plt

# Calculate the largest connected component subgraph: largest_ccs
largest_ccs = sorted(nx.connected_component_subgraphs(G), key=lambda x: len(x))[-1]

# Create the customized MatrixPlot object: h
h = MatrixPlot(largest_ccs,'grouping')

# Draw the MatrixPlot to the screen
h.draw()
plt.show()
```

### Results :  

Great work! Recall that in a MatrixPlot, nodes are the rows and columns of the matrix, and cells are filled in according to whether an edge exists between the pairs of nodes.  

![graph14](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Data_Scientist_Track_with_Python/Network%20Analysis%20in%20Python%20Part%201/img/graph14.svg)

---


## ArcPlot    

Next up, let's use the ArcPlot to visualize the network. You're going to practice sorting the nodes in the graph as well.  

Note: this exercise may take about 4-7 seconds to execute if done correctly.  

### Instructions

 - Make an ArcPlot of the GitHub collaboration network, with authors sorted by degree. To do this:
 - Iterate over all the nodes in G, including the metadata (by specifying data=True).
 - In each iteration of the loop, calculate the degree of each node n with nx.degree() and set its 'degree' attribute. nx.degree() accepts two arguments: A graph and a node.
 - Create the ArcPlot object a by specifying two parameters: the graph, which is G, and the node_order, which is 'degree', so that the nodes are sorted.
 - Draw the ArcPlot object to the screen.

```python
# Import necessary modules
from nxviz.plots import ArcPlot
import matplotlib.pyplot as plt

# Iterate over all the nodes in G, including the metadata
for n, d in G.nodes(data=True):

    # Calculate the degree of each node: G.node[n]['degree']
    G.node[n]['degree'] = nx.degree(G,n)
    
# Create the ArcPlot object: a
a = ArcPlot(graph=G,node_order='degree')

# Draw the ArcPlot to the screen
a.draw()
plt.show()
```

### Results :  

Excellent! You'll now transform this ArcPlot into a CircosPlot in the next exercise.  

![graph15](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Data_Scientist_Track_with_Python/Network%20Analysis%20in%20Python%20Part%201/img/graph15.svg)

---


## CircosPlot   

Finally, you're going to make a CircosPlot of the network!  

### Instructions

 - Make a CircosPlot of the network, again, with GitHub users sorted by their degree, and grouped and coloured by their 'grouping' key. To do this:
 - Iterate over all the nodes in G, including the metadata (by specifying data=True).
 - In each iteration of the loop, calculate the degree of each node n with nx.degree() and set its 'degree' attribute.
 - Create the CircosPlot object c by specifying three parameters in addition to the graph G: the node_order, which is 'degree', the node_grouping and the node_color, which are both 'grouping'.
 - Draw the CircosPlot object to the screen.

```python
# Import necessary modules
from nxviz import CircosPlot
import matplotlib.pyplot as plt 
 
# Iterate over all the nodes, including the metadata
for n, d in G.nodes(data=True):

    # Calculate the degree of each node: G.node[n]['degree']
    G.node[n]['degree'] = nx.degree(G,n)

# Create the CircosPlot object: c
c = CircosPlot(graph=G,node_order='degree',node_grouping='grouping',node_color='grouping')

# Draw the CircosPlot object to the screen
c.draw()
plt.show()
```

### Results :  

Fantastic! This CircosPlot provides a compact alternative to the ArcPlot. It is easy to see in this plot that most users belong to one group.  

![graph16](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Data_Scientist_Track_with_Python/Network%20Analysis%20in%20Python%20Part%201/img/graph16.svg)

---


## Finding cliques (I)   

You're now going to practice finding cliques in G. Recall that cliques are "groups of nodes that are fully connected to one another", while a maximal clique is a clique that cannot be extended by adding another node in the graph.  

### Instructions

 - Count the number of maximal cliques present in the graph and print it.
	 - Use the nx.find_cliques() function of G to find the maximal cliques.
	 - The nx.find_cliques() function returns a generator object. To count the number of maximal cliques, you need to first convert it to a list with list() and then use the len() function. Place this inside a print() function to print it.

```python
# Calculate the maximal cliques in G: cliques
cliques = nx.find_cliques(G)

# Count and print the number of maximal cliques in G
print(len(list(cliques)))
```

### Results :  

Fantastic! This Github network has 8 maximal cliques.  

---


## Finding cliques (II)   

Great work! Let's continue by finding a particular maximal clique, and then plotting that clique.  

### Instructions

 - Find the author(s) that are part of the largest maximal clique, and plot the subgraph of that/one of those clique(s) using a CircosPlot. To do this:
	 - Use the nx.find_cliques() function to calculate the maximal cliques in G. Place this within the provided sorted() function to calculate the largest maximal clique.
	 - Create the subgraph consisting of the largest maximal clique using the .subgraph() method and largest_clique.
	 - Create the CircosPlot object using the subgraph G_lc (without any other arguments) and plot it.

```python
# Import necessary modules
import networkx as nx
from nxviz import CircosPlot
import matplotlib.pyplot as plt

# Find the author(s) that are part of the largest maximal clique: largest_clique
largest_clique = sorted(nx.find_cliques(G), key=lambda x:len(x))[-1]

# Create the subgraph of the largest_clique: G_lc
G_lc = G.subgraph(largest_clique)

# Create the CircosPlot object: c
c = CircosPlot(G_lc)

# Draw the CircosPlot to the screen
c.draw()
plt.show()
```

### Results :  

Great work! The subgraph consisting of the largest maximal clique has 38 users. It's time to move on towards building the recommendation system!  

![graph17](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Data_Scientist_Track_with_Python/Network%20Analysis%20in%20Python%20Part%201/img/graph17.svg)

---


## Finding important collaborators     

Almost there! You'll now look at important nodes once more. Here, you'll make use of the degree_centrality() and betweenness_centrality() functions in NetworkX to compute each of the respective centrality scores, and then use that information to find the "important nodes". In other words, your job in this exercise is to find the user(s) that have collaborated with the most number of users.  

### Instructions

 - Compute the degree centralities of G. Store the result as deg_cent.
 - Compute the maximum degree centrality. Since deg_cent is a dictionary, you'll have to use the .values() method to get a list of its values before computing the maximum degree centrality with max().
 - Identify the most prolific collaborators using a list comprehension:
	- Iterate over the degree centrality dictionary deg_cent that was computed earlier using its .items() method. What condition should be satisfied if you are seeking to find user(s) that have collaborated with the most number of users? Hint: It has do to with the maximum degree centrality.
 - Hit 'Submit Answer' to see who the most prolific collaborator(s) is/are!

```python
# Compute the degree centralities of G: deg_cent
deg_cent = nx.degree_centrality(G)

# Compute the maximum degree centrality: max_dc
max_dc = max(deg_cent.values())

# Find the user(s) that have collaborated the most: prolific_collaborators
prolific_collaborators = [n for n, dc in deg_cent.items() if dc == max_dc]

# Print the most prolific collaborator(s)
print(prolific_collaborators)
```

### Results :  

Great work! It looks like 'u89' is the most prolific collaborator.  

		<script.py> output:
			['u89']

---


## Characterizing editing communities    

You're now going to combine what you've learned about the BFS algorithm and concept of maximal cliques to visualize the network with an ArcPlot.  

The largest maximal clique in the Github user collaboration network has been assigned to the subgraph G_lmc.  

### Instructions

 - Go out 1 degree of separation from the clique, and add those users to the subgraph. Inside the first for loop:
 - Add nodes to G_lmc from the neighbors of G using the .add_nodes_from() method and .neighbors() methods.
 - Using the .add_edges_from(), method, add edges to G_lmc between the current node and all its neighbors. To do this, you'll have create a list of tuples using the zip() function consisting of the current node and each of its neighbors. The first argument to zip() should be [node]*len(G.neighbors(node)), and the second argument should be the neighbors of node.
 - Record each node's degree centrality score in its node metadata.
 - Do this by assigning nx.degree_centrality(G_lmc)[n] to G_lmc.node[n]['degree centrality'] in the second for loop.
 - Visualize this network with an ArcPlot sorting the nodes by degree centrality (you can do this using the keyword argument node_order='degree centrality').

```python
# Import necessary modules
from nxviz import ArcPlot
import matplotlib.pyplot as plt
 
# Identify the largest maximal clique: largest_max_clique
largest_max_clique = set(sorted(nx.find_cliques(G), key=lambda x: len(x))[-1])

# Create a subgraph from the largest_max_clique: G_lmc
G_lmc = G.subgraph(largest_max_clique)

# Go out 1 degree of separation
for node in G_lmc.nodes():
    G_lmc.add_nodes_from(G.neighbors(node))
    G_lmc.add_edges_from(zip([node]*len(G.neighbors(node)), G.neighbors(node)))

# Record each node's degree centrality score
for n in G_lmc.nodes():
    G_lmc.node[n]['degree centrality'] = nx.degree_centrality(G_lmc)[n]
        
# Create the ArcPlot object: a
a = ArcPlot(G_lmc,node_order='degree centrality')

# Draw the ArcPlot to the screen
a.draw()
plt.show()
```

### Results :  

Great work! The final step that remains is to recommend collaborators who have not yet collaborated together.  

![graph18](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Data_Scientist_Track_with_Python/Network%20Analysis%20in%20Python%20Part%201/img/graph18.svg)

---


## Recommending co-editors who have yet to edit together      

Finally, you're going to leverage the concept of open triangles to recommend users on GitHub to collaborate!  

### Instructions

 - Compile a list of GitHub users that should be recommended to collaborate with one another. To do this:
	 - In the first for loop, iterate over all the nodes in G, including the metadata (by specifying data=True).
	 - In the second for loop, iterate over all the possible triangle combinations, which can be identified using the combinations() function with a size of 2.
	 - If n1 and n2 do not have an edge between them, a collaboration between these two nodes (users) should be recommended, so increment the (n1), (n2) value of the recommended dictionary in this case. You can check whether or not n1 and n2 have an edge between them using the .has_edge() method.
 - Using a list comprehension, identify the top 10 pairs of users that should be recommended to collaborate. The iterable should be the key-value pairs of the recommended dictionary (which can be accessed with the .items() method), while the conditional should be satisfied if count is greater than the top 10 in all_counts. Note that all_counts is sorted in ascending order, so you can access the top 10 with all_counts[-10].

```python
# Import necessary modules
from itertools import combinations
from collections import defaultdict

# Initialize the defaultdict: recommended
recommended = defaultdict(int)

# Iterate over all the nodes in G
for n, d in G.nodes(data=True):

    # Iterate over all possible triangle relationship combinations
    for n1, n2 in combinations(G.neighbors(n), 2):
    
        # Check whether n1 and n2 do not have an edge
        if not G.has_edge(n1, n2):
        
            # Increment recommended
            recommended[(n1, n2)] += 1

# Identify the top 10 pairs of users
all_counts = sorted(recommended.values())
top10_pairs = [pair for pair, count in recommended.items() if count > all_counts[-10]]
print(top10_pairs)
```

### Results :  

Fantastic job! You've identified pairs of users who should collaborate together, and in doing so, built your very own recommendation system!  

		<script.py> output:
			[('u37', 'u2159'), ('u534', 'u322')]

---