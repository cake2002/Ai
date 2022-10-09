import collections
def bfs(graph,root):
    seen,queue=set([root]),collections.deque([root])
    while queue:
        vertex=queue.popleft()
        visit(vertex)
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)

def visit(n):
    print(n)


def bfs_shortest_path(grah, source, destination):
    checked=[]
    queue=[[source]]
    if source == destination:
        return "SOURCE IS DESTINATION :"
    while queue:
        path=queue.pop(0)
        node=path[-1]
        if node not in checked:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path=list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == destination:
                    return new_path
            checked.append(node)
    return "PATH DOES NOT EXIST :"
graph={'A': ['B', 'D'],
       'B':['C', 'F'],
       'C': ['E','G','H'],
       'G': ['E', 'H'],
       'E': ['B', 'F'],
       'F': ['A'],
       'D': ['F'],
       'H': ['A']
       
       }

print("GRAPH TRAVERSAL: ")
bfs(graph,'A')
print("\n SHORTERT PATH OF GARPH IS: : ", bfs_shortest_path(graph, 'A','G'))
