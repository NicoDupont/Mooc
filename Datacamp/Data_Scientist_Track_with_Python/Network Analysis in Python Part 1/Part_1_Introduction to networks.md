11/2017  
# Datacamp - Network Analysis in Python (Part 1) (Data Scientist Track with Python)  
[Network Analysis in Python (Part 1)](https://www.datacamp.com/courses/network-analysis-in-python-part-1)
---

***Course Description***  

From online social networks such as Facebook and Twitter to transportation networks such as bike sharing systems, networks are everywhere, and knowing how to analyze this type of data will open up a new world of possibilities for you as a Data Scientist. This course will equip you with the skills to analyze, visualize, and make sense of networks. You'll apply the concepts you learn to real-world network data using the powerful NetworkX library. With the knowledge gained in this course, you'll develop your network thinking skills and be able to start looking at your data with a fresh perspective!        

# Part 1 : Introduction to networks   

In this chapter, you'll be introduced to fundamental concepts in network analytics while becoming acquainted with a real-world Twitter network dataset that you will explore throughout the course. In addition, you'll learn about NetworkX, a library that allows you to manipulate, analyze, and model graph data. You'll learn about different types of graphs as well as how to rationally visualize them.  

## What is a network?   

Let's think again about examples of networks. Which of the following data is least easily modeled as a network?  

### Possible Answers  => 1

 - Airplane transportation.
 - Phone numbers in a telephone directory.
 - Co-authorship of papers.
 - Atoms in a molecule.

```python

```

### Results :  

Correct! Compared to the other options, it would not be as easy to model phone numbers in a telephone directory as a network.  

---


## Basics of NetworkX API, using Twitter network      

To get you up and running with the NetworkX API, we will run through some basic functions that let you query a Twitter network that has been pre-loaded for you and is available in the IPython Shell as T. The Twitter network comes from KONECT, and shows a snapshot of a subset of Twitter users. It is an anonymized Twitter network with metadata.  

You're now going to use the NetworkX API to explore some basic properties of the network, and are encouraged to experiment with the data in the IPython Shell.  

Wait for the IPython shell to indicate that the graph that has been preloaded under the variable name T (representing a Twitter network), and then answer the following question:  

What is the size of the graph T, the type of T.nodes(), and the data structure of the third element of the last entry of T.edges(data=True)? The len() and type() functions will be useful here. To access the last entry of T.edges(data=True), you can use T.edges(data=True)[-1].  

### Possible Answers => 1

 - 23369, list, dict.
 - 32369, tuple, datetime.
 - 23369, list, datetime.
 - 22339, dict, dict.

```python

```

### Results :  

Correct! Now that you've explored the graph quantitatively, you'll explore NetworkX's drawing functionalities in the next exercise.  

    In [2]: type(T)
    Out[2]: networkx.classes.digraph.DiGraph
    In [3]: len(T)
    Out[3]: 23369
    In [4]: T.edges(data=True)
    Out[4]:
    [(1, 3, {'date': datetime.date(2012, 11, 17)}),
     (1, 4, {'date': datetime.date(2007, 6, 19)}),
     (1, 5, {'date': datetime.date(2014, 3, 18)}),
     (1, 6, {'date': datetime.date(2007, 3, 18)}),
     (1, 7, {'date': datetime.date(2011, 12, 19)}),
    In [5]: type(T.nodes())
    Out[5]: list

---


## Basic drawing of a network using NetworkX      

NetworkX provides some basic drawing functionality that works for small graphs. We have selected a subset of nodes from the graph for you to practice using NetworkX's drawing facilities. It has been pre-loaded as T_sub.  

### Instructions

 - Import matplotlib.pyplot as plt and networkx as nx.
 - Draw T_sub to the screen by using the nx.draw() function, and don't forget to also use plt.show() to display it.

```python
# Import necessary modules
import networkx as nx
import matplotlib.pyplot as plt

# Draw the graph to screen
nx.draw(T_sub)
plt.show()
```

### Results :  

![graph1](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Data_Scientist_Track_with_Python/Network%20Analysis%20in%20Python%20Part%201/img/graph1.svg)

Great work! Next, you'll learn how to perform basic queries on a graph.

---


## Queries on a graph    

Now that you know some basic properties of the graph and have practiced using NetworkX's drawing facilities to visualize components of it, it's time to explore how you can query it for nodes and edges. Specifically, you're going to look for "nodes of interest" and "edges of interest". To achieve this, you'll make use of the .nodes() and .edges() methods that Eric went over in the video. The .nodes() method returns a list of nodes, while the .edges() method returns a list of tuples, in which each tuple shows the nodes that are present on that edge. Recall that passing in the keyword argument data=True in these methods retrieves the corresponding metadata associated with the nodes and edges as well.  

You'll write list comprehensions to effectively build these queries in one line. For a refresher on list comprehensions, refer to Part 2 of DataCamp's Python Data Science Toolbox course. Here's the recipe for a list comprehension:  

[ output expression for iterator variable in iterable if predicate expression ].  

You have to fill in the _iterable_ and the _predicate expression_. Feel free to prototype your answer by exploring the graph in the IPython Shell before submitting your solution.  

### Instructions

 - Use a list comprehension to get a list of nodes from the graph T that have the 'occupation' label of 'scientist'.
   - The output expression n has been specified for you, along with the iterator variables n and d. Your task is to fill in the iterable and the conditional expression.
   - Use the .nodes() method of T access its nodes, and be sure to specify data=True to obtain the metadata for the nodes.
   - The iterator variable d is a dictionary. The key of interest here is 'occupation' and value of interest is 'scientist'.
 - Use a list comprehension to get a list of edges from the graph T that were formed for at least 6 years, i.e., from before 1 Jan 2010.
   - Your task once again is to fill in the iterable and conditional expression.
   - Use the .edges() method of T to access its edges. Be sure to obtain the metadata for the edges as well.
   - The dates are stored as datetime.date objects in the metadata dictionary d, under the key 'date'. To access the date 1 Jan 2009, for example, the dictionary value would be date(2009, 1, 1).

```python
# Use a list comprehension to get the nodes of interest: noi
noi = [n for n, d in T.nodes(data=True) if d['occupation'] == 'scientist']

# Use a list comprehension to get the edges of interest: eoi
eoi = [(u, v) for u, v, d in T.edges(data=True) if d['date'] < date(2010, 1, 1)]

print(T.edges(data=True)[:5])
print('---------------------------')
print(T.nodes(data=True)[:5])
```

### Results :  

Well done! Now that you know how to perform basic queries on a graph, you're ready to learn about different types of graphs.  

    In [3]: T.edges(data=True)[:5]
    Out[3]:
    [(1, 3, {'date': datetime.date(2012, 11, 17)}),
     (1, 4, {'date': datetime.date(2007, 6, 19)}),
     (1, 5, {'date': datetime.date(2014, 3, 18)}),
     (1, 6, {'date': datetime.date(2007, 3, 18)}),
     (1, 7, {'date': datetime.date(2011, 12, 19)})]

    In [4]: T.nodes(data=True)[:5]
    Out[4]:
    [(1, {'category': 'I', 'occupation': 'scientist'}),
     (3, {'category': 'P', 'occupation': 'politician'}),
     (4, {'category': 'D', 'occupation': 'celebrity'}),
     (5, {'category': 'I', 'occupation': 'politician'}),
     (6, {'category': 'D', 'occupation': 'politician'})]

---


## Checking the un/directed status of a graph    

In the video, Eric described to you different types of graphs. Which type of graph do you think the Twitter network data you have been working with corresponds to? Use Python's built-in type() function in the IPython Shell to find out. The network, as before, has been pre-loaded as T.  

Of the four below choices below, which one corresponds to the type of graph that T is?  

### Possible Answers => 2

 - Undirected Graph.
 - Directed Graph.
 - Undirected Multi-Edge Graph.
 - Directed Multi-Edge Graph.

```python
type(T)
```

### Results :  

    In [1]: type(T)
    Out[1]: networkx.classes.digraph.DiGraph

Correct! The graph is indeed a Directed Graph.

---


## Specifying a weight on edges       

Weights can be added to edges in a graph, typically indicating the "strength" of an edge. In NetworkX, the weight is indicated by the 'weight' key in the metadata dictionary.  

Before attempting the exercise, use the IPython Shell to access the dictionary metadata of T and explore it, for instance by running the commands T.edge[1][10] and then T.edge[10][1]. Note how there's only one field, and now you're going to add another field, called 'weight'.  

### Instructions

 - Set the 'weight' attribute of the edge between node 1 and 10 of T to be equal to 2. Refer to the following template to set an attribute of an edge: network_name.edge[node1][node2]['attribute'] = value. Here, the 'attribute' is 'weight'.
 - Set the weight of every edge involving node 293 to be equal to 1.1. To do this:
   - Using a for loop, iterate over all the edges of T, including the metadata.
   - If 293 is involved in the list of nodes [u, v]:
     - Set the weight of the edge between u and v to be 1.1.

```python
# Set the weight of the edge
T.edge[1][10]['weight'] = 2

# Iterate over all the edges (with metadata)
for u, v, d in T.edges(data=True):

    # Check if node 293 is involved
    if 293 in [u, v]:
    
        # Set the weight to 1.1
        T.edge[u][v]['weight'] = 1.1
```

### Results :  

Excellent job! Being able to iterate over graphs like this to explore and alter their metadata is an important skill.  

---


## Checking whether there are self-loops in the graph      

As Eric discussed, NetworkX also allows edges that begin and end on the same node; while this would be non-intuitive for a social network graph, it is useful to model data such as trip networks, in which individuals begin at one location and end in another.  

It is useful to check for this before proceeding with further analyses, and NetworkX graphs provide a method for this purpose: .number_of_selfloops().  

In this exercise as well as later ones, you'll find the assert statement useful. An assert-ions checks whether the statement placed after it evaluates to True, otherwise it will return an AssertionError.  

To begin, use the .number_of_selfloops() method on T in the IPython Shell to get the number of edges that begin and end on the same node. A number of self-loops have been synthetically added to the graph. Your job in this exercise is to write a function that returns these edges.  

### Instructions

 - Define a function called find_selfloop_nodes() which takes one argument: G.
	 - Using a for loop, iterate over all the edges in G (excluding the metadata).
	 - If node u is equal to node v:
		 - Append u to the list nodes_in_selfloops.
		 - Return the list nodes_in_selfloops.
 - Check that the number of self loops in the graph equals the number of nodes in self loops. This has been done for you, so hit 'Submit Answer' to see the result!

```python
# Define find_selfloop_nodes()
def find_selfloop_nodes(G):
    """
    Finds all nodes that have self-loops in the graph G.
    """
    nodes_in_selfloops = []
    
    # Iterate over all the edges of G
    for u, v in G.edges():
    
    # Check if node u and node v are the same
        if u == v:
        
            # Append node u to nodes_in_selfloops
            nodes_in_selfloops.append(u)
            
    return nodes_in_selfloops

# Check whether number of self loops equals the number of nodes in self loops
assert T.number_of_selfloops() == len(find_selfloop_nodes(T))
```

### Results :  

Great work! There are 42 nodes in T that have self-loops.  

---


## Visualizing using Matrix plots      

It is time to try your first "fancy" graph visualization method: a matrix plot. To do this, nxviz provides a MatrixPlot object.  

nxviz is a package for visualizing graphs in a rational fashion. Under the hood, the MatrixPlot utilizes nx.to_numpy_matrix(G), which returns the matrix form of the graph. Here, each node is one column and one row, and an edge between the two nodes is indicated by the value 1. In doing so, however, only the weight metadata is preserved; all other metadata is lost, as you'll verify using an assert statement.  

A corresponding nx.from_numpy_matrix(A) allows one to quickly create a graph from a NumPy matrix. The default graph type is Graph(); if you want to make it a DiGraph(), that has to be specified using the create_using keyword argument, e.g. (nx.from_numpy_matrix(A, create_using=nx.DiGraph)).  

One final note, matplotlib.pyplot and networkx have already been imported as plt and nx, respectively, and the graph T has been pre-loaded. For simplicity and speed, we have sub-sampled only 100 edges from the network.  

### Instructions

 - Import nxviz as nv.
 - Plot the graph T as a matrix plot. To do this:
	 - Create the MatrixPlot object called m using the nv.MatrixPlot() function with T passed in as an argument.
	 - Draw the m to the screen using the .draw() method.
	 - Display the plot using plt.show().
 - Convert the graph to a matrix format, and then convert the graph to back to the NetworkX form from the matrix as a directed graph. This has been done for you.
 - Check that the category metadata field is lost from each node. This has also been done for you, so hit 'Submit Answer' to see the results!

```python
# Import nxviz
import nxviz as nv

# Create the MatrixPlot object: m
m = nv.MatrixPlot(T)

# Draw m to the screen
m.draw()

# Display the plot
plt.show()

# Convert T to a matrix format: A
A = nx.to_numpy_matrix(T)

# Convert A back to the NetworkX form as a directed graph: T_conv
T_conv = nx.from_numpy_matrix(A, create_using=nx.DiGraph())

# Check that the `category` metadata field is lost from each node
for n, d in T_conv.nodes(data=True):
    assert 'category' not in d.keys()
```

### Results :  

![graph2](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Data_Scientist_Track_with_Python/Network%20Analysis%20in%20Python%20Part%201/img/graph2.svg)

---


## Visualizing using Circos plots      

Circos plots are a rational, non-cluttered way of visualizing graph data, in which nodes are ordered around the circumference in some fashion, and the edges are drawn within the circle that results, giving a beautiful as well as informative visualization about the structure of the network.  

In this exercise, you'll continue getting practice with the nxviz API, this time with the CircosPlot object. matplotlib.pyplot has been imported for you as plt.  

### Instructions

 - Import CircosPlot from nxviz.
 - Plot the Twitter network T as a Circos plot without any styling. Use the CircosPlot() function to do this. Don't forget to draw it to the screen using .draw() and then display it using plt.show().

```python
# Import necessary modules
import matplotlib.pyplot as plt
from nxviz import CircosPlot

# Create the CircosPlot object: c
c = CircosPlot(T)

# Draw c to the screen
c.draw()

# Display the plot
plt.show()
```

### Results :  

Fantastic! In the Chapter 4 Case Study, you'll learn how to customize CircosPlots to make them more informative.

![graph3](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Data_Scientist_Track_with_Python/Network%20Analysis%20in%20Python%20Part%201/img/graph3.svg)

---


## Visualizing using Arc plots    

Following on what you've learned about the nxviz API, now try making an ArcPlot of the network. Two keyword arguments that you will try here are node_order='keyX' and node_color='keyX', in which you specify a key in the node metadata dictionary to color and order the nodes by.

matplotlib.pyplot has been imported for you as plt.

### Instructions

 - Import ArcPlot from nxviz.
 - Create an un-customized ArcPlot of T. To do this, use the ArcPlot() function with just T as the argument.
 - Create another ArcPlot of T in which the nodes are ordered and colored by the 'category' keyword. You'll have to specify the node_order and node_color parameters to do this. For both plots, be sure to draw them to the screen and display them with plt.show().

```python
# Import necessary modules
import matplotlib.pyplot as plt
from nxviz import ArcPlot

# Create the un-customized ArcPlot object: a
a = ArcPlot(T)

# Draw a to the screen
a.draw()

# Display the plot
plt.show()

# Create the customized ArcPlot object: a2
a2 = ArcPlot(T,node_order='category',node_color='category')

# Draw a2 to the screen
a2.draw()

# Display the plot
plt.show()
```

### Results :  

Excellent job! Notice the node coloring in the customized ArcPlot compared to the uncustomized version. In the customized ArcPlot, the nodes in each of the categories - 'I', 'D', and 'P' - have their own color. If it's difficult to see on your screen, you can expand the plot into a new window by clicking on the pop-out icon on the top-left next to 'Plots'.

![graph4](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Data_Scientist_Track_with_Python/Network%20Analysis%20in%20Python%20Part%201/img/graph4.svg)
![graph5](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Data_Scientist_Track_with_Python/Network%20Analysis%20in%20Python%20Part%201/img/graph5.svg)

---