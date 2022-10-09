graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[],
    }
def iddfs(graph,n,seen,dst,dep,lim):
    if n not in seen:
        seen.append(n)
        if dep<=lim:
            for i in graph[n]:
                if seen[-1] is dst:
                    return seen
                iddfs(graph,i,seen,dst,dep+1,lim)
        else:
            print("Maximum Level Reached")
    return None
print(iddfs(graph,'5',[],'8',0,int(input("Enter Maximum Limit:"))))
