#!/usr/bin/python

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

# take a list and return the elements of the list except without duplicates.
def remove_duplicates(input):
    seen = set()
    retval = []
    for element in input:
        if element not in seen:
            seen = seen.union(set([element]))
            retval = retval + [element]
    return retval

# return a list of all descendents in depth-first order.
def in_order(node,edges):
    print("finding descendents of: {}".format(node))
    ics = immediate_children_of(node,edges)
    descendents_in_order = [node]
    for child in ics:
        descendents_in_order = descendents_in_order + [child] + in_order(child,edges)
    descendents_in_order = remove_duplicates(descendents_in_order)
    return descendents_in_order

def find_position_of_first_difference(word1,word2):
    for i in range(0,len(word1)):
        if (i == len(word2)):
            return -1
        if word1[i] != word2[i]:
            break
    return i

def get_edges(words):
    edges = set()
    for w in range(0,len(words)-2):
        word1 = words[w]
        word2 = words[w+1]
        print("comparing: {} to next: {}".format(word1,word2))
        position = find_position_of_first_difference(word1,word2)
        if (position > -1):
            if (word1[position] != word2[position]):
                print("adding edge: {},{}".format(word1[position],word2[position]))
                edges = add_edge(edges,word1[position],word2[position])
    return edges

def ordering():
    words = open("words.txt").read().split('\n')
    edges = get_edges(words)

    all_in_order = []
    while(len(edges) > 0):
        for r in roots_of(edges):
            print("root: {}".format(r))
            all_in_order = all_in_order + [r]
            new_edges = edges.difference(filter(lambda edge: edge[0] == r, edges))
            if len(new_edges) == 0:
                # no more new edges left: we've printed out every letter located
                # at the 'from' of any edge.
                # last thing to do is print the 'to' for the last remaining edges.
                for edge in edges:
                    all_in_order = all_in_order + [edge[1]]
            edges = new_edges

    print(all_in_order)
