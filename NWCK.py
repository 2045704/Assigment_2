import re
from collections import defaultdict
from math import inf
from heapq import heappop, heappush

def parse_newick(input_str, is_directed=True):
    input_str = re.sub(",,", ",.,", input_str)
    input_str = re.sub(r"\(,", "(.,", input_str)
    input_str = re.sub(r",\)", ",.)", input_str)
    input_str = re.sub(r"\(\)", "(.)", input_str)
    input_str = re.sub(r"^\((.+)\);", r"\1", input_str)
    m = re.finditer(r"(\(|[A-z_.]+|,|\))", input_str)
    tokens = [x.group() for x in m]

    count = 0
    stack = ["0"]
    graph = defaultdict(list)
    i = len(tokens) - 1
    while i >= 0:
        if tokens[i] == "(":
            stack = stack[:-1]
        elif tokens[i] == ")":
            if i + 1 < len(tokens) and tokens[i + 1] not in ",)":
                node = tokens[i + 1]
            else:
                count += 1
                node = str(count)
            graph[stack[-1]].append({"n": node, "w": 1})
            if not is_directed:
                graph[node].append({"n": stack[-1], "w": 1})
            stack += [node]
        elif tokens[i] != "," and (i == 0 or tokens[i - 1] != ")"):
            if tokens[i] == ".":
                count += 1
                tokens[i] = str(count)
            graph[stack[-1]].append({"n": tokens[i], "w": 1})
            if not is_directed:
                graph[tokens[i]].append({"n": stack[-1], "w": 1})
        i -= 1
    return graph

def get_nodes(graph):
    return set(node for node, neighbors in graph.items() for neighbor in neighbors)

def dijkstra(graph, start=1):
    distances = {n: inf for n in get_nodes(graph)}
    distances[start] = 0
    heap_queue = []
    heappush(heap_queue, (0, start))
    processed = set()

    while heap_queue:
        u = heappop(heap_queue)[1]
        processed.add(u)
        for v in graph[u]:
            if v["n"] not in processed:
                distances[v["n"]] = min(distances[u] + v["w"], distances[v["n"]])
                heappush(heap_queue, (distances[v["n"]], v["n"]))

    return distances

def calculate_distance(tree_str, target_nodes):
    parsed_tree = parse_newick(tree_str, is_directed=False)
    return dijkstra(parsed_tree, target_nodes[0])[target_nodes[1]]

# Set the file path
file_path = r'C:\Users\newma\Downloads\rosalind_nwck (2).txt'

with open(file_path, 'r') as file:
    file_contents = file.read().split("\n\n")

if file_contents[-1] == "":
    file_contents = file_contents[:-1]

trees_in_file = [tree_data.split("\n") for tree_data in file_contents]
distances = [calculate_distance(tree_data[0], tree_data[1].split()) for tree_data in trees_in_file]

print(*distances)
