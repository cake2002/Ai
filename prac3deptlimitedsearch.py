graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[],
    }
def dls(start,goal,path,level,maxD):
    print("Current Level is ",level)
    print("Goal Testing for Node: ",start)
    path.append(start)
    if start==goal:
        print("Goal Node Found!")
        return path
    else:
        print("Goal Node Test Failed")
    if level==maxD:
        print("Maximum Level Reached!")
    else:
        print("Expanding the Current Node")
        for child in graph[start]:
            if dls(child,goal,path,level+1,maxD):
                return path
            else:
                path.pop()
        return False
start='5'
goal=input("Enter Goal Node: ")
path=list()
result=dls(start,goal,path,0,int(input("Enter Maximum Depth: ")))
if (result):
    print("Path Founded till the Goal Node as Follows: ")
    print("Path: ",path)
else:
    print("Goal Node Not Founded Within the Specified Limit!")
