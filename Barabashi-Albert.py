#!/usr/bin/env python
# coding: utf-8

# In[44]:


from matplotlib.pyplot import *
import networkx as nx


def startGraph(m0):
    g = nx.Graph()
    nodes = [i for i in range(m0)]
    
    edges_count = int((m0*(m0-1))/2)
    
    for node in nodes:
        g.add_node(node)
    for edge in range(edges_count):
        g.add_edge(nodes[edge-1], nodes[edge])
        
    nx.draw_circular(g,
             node_color='red',
             node_size=500,
             with_labels=True)
    return len(g.nodes)




def barabashiAlbert(n,m0):
    
    #StartGraph
    g = nx.Graph()
    nodes = [i for i in range(m0)]
    
    edges_count = int((m0*(m0-1))/2)
    #print(nodes)
    for node in nodes:
        g.add_node(node)
    for edge in range(edges_count):
        g.add_edge(nodes[edge-1], nodes[edge])
        
    
    new_nodes = []
    
    #print(len(pk), len(K))
    
    for node in range(m0,n):
        new_nodes.append(node)
    
    sumDegree = 0
    
    
    K = []
    pk = []
    iMV = [] #список индексов максимальных значений pk
    
    
    for i in range(n-m0):
        
        for node in range(len(g.nodes)):
            sumDegree += g.degree[node]
        
        maxValue = 0
        indexMaxValue = 0
        
        nodeNewValue = new_nodes[i]
        #print(nodeNewValue)
        
        
        nodes.append(nodeNewValue)
        g.add_node(nodeNewValue)
        
        
        
        #print(sumDegree)    
        #print(nodes)
        
        for j in range(m0):
            p = g.degree[j]/sumDegree
            pk.append(p)
            K.append(g.degree[j])
        #print(K)
        
        
        for m in range(m0):
            #for value in range(len(pk)):
            if (pk[m] >= maxValue):
                maxValue = pk[m]
                indexMaxValue = m
            iMV.append(indexMaxValue)
            g.add_edge(nodeNewValue, nodes[iMV[m]])
        
        
       
        #m0 += 1
        
    graph_image = nx.draw_circular(g,
                     node_color='red',
                     node_size=500,
                     with_labels=True)
    fig = figure()
    ax = fig.add_subplot(111)
    scatter(K, pk)
    show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




