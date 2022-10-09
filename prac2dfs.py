graph={'A': ['B', 'D'],
       'B':['C', 'F'],
       'C': ['E','G','H'],
       'G': ['E', 'H'],
       'E': ['B', 'F'],
       'F': ['A'],
       'D': ['F'],
       'H': ['A']
       }

start=input("Enter Source Node:")
des=input("Enter Destination Node:")
def dfs(g,start,li,des):
    if start not in li:
        li.append(start)
        for i in g[start]:
            if li[-1] is des:
                break

        dfs(g,i,li,des)
        return li
print(dfs(graph,start,[],des))
