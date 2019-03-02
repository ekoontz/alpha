#!/usr/bin/python

edges = set()

def add_edge(edges,node1,node2):
    edges = edges.union({(node1,node2)})
    return edges

# find all the roots of the graph: those
# nodes with no edges pointing to them.
# 1. get all _from_ nodes from the edges
# 2. remove those that are also at the _to_ of
#    any edge.

def roots_of(edges):
    map(lambda(edge): edge[0], edges)
    
edges2 = add_edge(edges,'a','b')
edges3 = add_edge(edges2,'a','h')

print(edges3)

