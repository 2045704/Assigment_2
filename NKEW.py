import re
from collections import defaultdict, deque

def parse_newick(newick):
    newick = re.sub(",,", ",.,", newick)
    newick = re.sub(r"\(,", "(.,", newick)
    newick = re.sub(r",\)", ",.)", newick)
    newick = re.sub(r"\(\)", "(.)", newick)
    newick = re.sub(r"^\((.+)\);", r"\1", newick)
    m = re.finditer(r"(\(|([A-z_.]*:\d+)|,|\))", newick)
    tokens = [x.groups()[0] for x in m]

    count = 0
    node_stack = ["0"]
    graph = defaultdict(list)
    i = len(tokens) - 1
    while i >= 0:
        if tokens[i] == "(":
            node_stack = node_stack[:-1]
        elif tokens[i] == ")":
            if i + 1 < len(tokens) and tokens[i + 1] not in ",)":
                if tokens[i + 1][0] == ":":
                    weight = tokens[i + 1][1:]
                    count += 1
                    node = str(count)
                else:
                    node, weight = tokens[i + 1].split(":")
            graph[node_stack[-1]].append({"neighbor": node, "weight": int(weight)})
            graph[node].append({"neighbor": node_stack[-1], "weight": int(weight)})
            node_stack += [node]
        elif tokens[i] != "," and (i == 0 or tokens[i - 1] != ")"):
            if tokens[i] == ".":
                count += 1
                tokens[i] = str(count)
            node, weight = tokens[i].split(":")
            graph[node_stack[-1]].append({"neighbor": node, "weight": int(weight)})
            graph[node].append({"neighbor": node_stack[-1], "weight": int(weight)})
        i -= 1
    return graph

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = deque([(start, 0)])

    while priority_queue:
        current_node, current_distance = priority_queue.popleft()

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph[current_node]:
            distance = current_distance + neighbor["weight"]

            if distance < distances[neighbor["neighbor"]]:
                distances[neighbor["neighbor"]] = distance
                priority_queue.append((neighbor["neighbor"], distance))

    return distances[end]

with open(r'C:\Users\newma\Downloads\rosalind_nkew.txt','r') as file:
    contents = file.read().split("\n\n")
if contents[-1] == "":
    contents = contents[:-1]
trees = [x.split("\n") for x in contents]

for tree in trees:
    tree_structure = parse_newick(tree[0])
    nodes = tree[1].split()
    distance = dijkstra(tree_structure, nodes[0], nodes[1])
    print(distance, end=" ")


