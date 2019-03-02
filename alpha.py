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

descendents = {}

# return a list of all descendents in depth-first order; might be repeats.
def in_order(node,edges):
    if descendents.get(node):
        return descendents[node]
    print("finding descendents of: {}".format(node))
    ics = immediate_children_of(node,edges)
    descendents_in_order = [node]
    for child in ics:
        descendents_in_order = descendents_in_order + [child] + in_order(child,edges)
    descendents[node] = descendents_in_order
    return descendents_in_order

def find_position_of_first_difference(word1,word2):
    for i in range(0,len(word1)):
        if (i == len(word2)):
            return -1
        if word1[i] != word2[i]:
            break
    return i

edges = set()

words = open("words.txt").read().split('\n')

for w in range(0,len(words)-1):
    word1 = words[w]
    word2 = words[w+1]
    print("comparing: {} to next: {}".format(word1,word2))
    position = find_position_of_first_difference(word1,word2)
    if (position > -1):
        print("adding edge: {},{}".format(word1[position],word2[position]))
        if (word1[position] != word2[position]):
            edges = add_edge(edges,word1[position],word2[position])
    
all_in_order = []
for r in roots_of(edges):
    all_in_order = all_in_order + in_order(r,edges)

print("done with roots..")
    
seen = set()
all_in_order_unique = []
for node in all_in_order:
    if node not in seen:
        all_in_order_unique = all_in_order_unique + [node]
        seen = seen.union({node})

print(all_in_order_unique)
