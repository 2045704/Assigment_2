'''import networkx as nx

def TREES(dataset):
    E = nx.read_edgelist(dataset,nodetype=int)
    subtrees = list(nx.connected_components(E))
    isolated_nodes = [node for node in E.nodes if E.degree[node] == 0]
    subtrees = [subtree for subtree in subtrees if not any(node in subtree for node in isolated_nodes)]
    result = len(subtrees)
    return result'''
    
def TREES(n,dataset):
    edges = len(dataset)
    trees = n - edges
    missing_edges = trees - 1
    return missing_edges

with open(r'C:\Users\newma\Downloads\rosalind_tree (3).txt','r') as file:
    n = int(file.readline())
    dataset = [list(map(int, line.strip().split())) for line in file]
    A = TREES(n,dataset)
    print(A)