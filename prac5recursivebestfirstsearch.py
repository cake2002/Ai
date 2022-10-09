#NOTE: Give Starting Node as A and Destination Node as D while Running The Code

graph={
    'A':({'B':1,'C':3,'D':7},12),
    'B':({'D':5},1),
    'C':({'D':12},3),
    'D':({'A':3},0),
    }
def greedy_search_rec(graph,prev,dst,path,q):
    print("Connected Nodes with Current Node",prev,"With H(n) Value:")
    for n in graph[prev][0]:
        if n not in path:
            q[n]=graph[n][1]
            print(n,"->",q[n])
    while q:
        mn=min(q,key=q.get)
        print("Taking Minimum H(n) Value: ",mn)
        if dst==mn:
            return path+[dst]
        new_path=greedy_search_rec(graph,mn,dst,path+[mn],q)
        if new_path:
            return new_path
    return[]
source=input("Enter Source Node: ")
dst=input("Enter Destination Node: ")
path=greedy_search_rec(graph,source,dst,[source],{})
if path:
    print(path)
else:
    print("Path Not Found")
