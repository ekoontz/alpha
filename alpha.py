#!/usr/bin/python

edges = set()

def add_edge(edges,node1,node2):
    edges = edges.union({(node1,node2)})
    return edges

# find all the roots of the graph: those
# nodes with no edges pointing to them.
def roots_of(edges):
    from_nodes = set(map(lambda edge: edge[0], edges))
    to_nodes = set(map(lambda edge: edge[1], edges))
    return from_nodes.difference(to_nodes)

# find all children of the node given the edges.
def immediate_children_of(node,edges):
    return map(lambda edge: edge[1],filter(lambda edge: edge[0] == node, list(edges)))

# return a list of all descendents in depth-first order; might be repeats.
def in_order(node,edges):
    ics = immediate_children_of(node,edges)
    descendents_in_order = [node]
    for child in ics:
        descendents_in_order = descendents_in_order + [child] + in_order(child,edges)
    return descendents_in_order

edges = add_edge(edges,'a','m')
edges = add_edge(edges,'c','m')
edges = add_edge(edges,'b','c')

all_in_order = []
for r in roots_of(edges):
    all_in_order = all_in_order + in_order(r,edges)

seen = set()
all_in_order_unique = []
for node in all_in_order:
    if node not in seen:
        all_in_order_unique = all_in_order_unique + [node]
        seen = seen.union({node})

print(all_in_order_unique)





