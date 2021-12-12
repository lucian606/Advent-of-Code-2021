from collections import defaultdict

def traverseNode(graph, source, dest, visited, path, paths):
    visited[source] = True
    path.append(source)

    if source == dest:
        paths.append(path)
    else:
        for neighbour in graph[source]:
            if neighbour == "start":
                continue
            if neighbour.isupper() or visited[neighbour] == False:
                traverseNode(graph, neighbour, dest, visited, path, paths)

    path.remove(source)
    visited[source] = False

def getAllPathsDFS(graph):
    visited = defaultdict(lambda: False)
    path = []
    paths = []
    traverseNode(graph, "start", "end", visited, path, paths)
    return len(paths)

def getAllPathsBFS(graph):
    path = ["start"]
    q = [(path, True)]
    path_count = 0
    while q:
        curr_path, canVisitTwice = q.pop()
        last = curr_path[-1]
        
        if last == "end":
            path_count += 1

        else:
            for node in graph[last]:
                if node.isupper() or node not in curr_path:
                    newpath = curr_path.copy()
                    newpath.append(node)
                    q.append((newpath, canVisitTwice))
                elif canVisitTwice and node != "start":
                    newpath = curr_path.copy()
                    newpath.append(node)
                    q.append((newpath, False))     

    return path_count

with open('inputs/day12.in') as f:
    lines = f.readlines()
    graph = defaultdict(lambda: [])
    for line in lines:
        line = line.split('\n')[0]
        (source, dest) = line.split('-')
        graph[source].append(dest)
        graph[dest].append(source)
    print(getAllPathsDFS(graph))
    print(getAllPathsBFS(graph))