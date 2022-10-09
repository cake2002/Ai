graph={
    'A': ({'B':2},{'E':3},11),
    'B': ({'C':1},{'G':9},6),
    'C': ({'E':2},2),
    'E': ({'D':6},0),
    'D': ({'G':1},7),
    }
def a_star(graph,prev,dst,path,pcost,q):
    print("Connected Nodes with Current Node",prev,"With H(n) Values:")
    for n in graph[prev][0]:
        if n not in path:
            q[n]=(graph[n][1],graph[prev][0][n])
            print(n,"->",q[n])
            add1=sum(q[n])
            path_cost=add1+pcost
            print("A* Value of ",n,"is: ",path_cost)
    while q:
        mn=min(q,key=q.get)
        print("Taking Minimum H(n) Value",mn)
        if dst==mn:
            return path+[dst]
        pc=path_cost+q[mn][1]
        new_path=a_star(graph,mn,dst,path+[mn],pc,q)
        if new_path:
            return new_path
    return []
start=input("Enter Starting Node: ")
dst=input("Enter Destination Node: ")
heuristic=int(input("Enter Heuristic Value For Souce: "))
path=a_star(graph,start,dst,[],0,{start:(heuristic,0)})
if path:
    print(path)
else:
    print("Path Not Found")
