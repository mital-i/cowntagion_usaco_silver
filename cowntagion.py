#start from the first node, multiply until the #of cows is atleast the number of connections of that node
#after spreading to adjacent nodes, start process over from the node that has the most connections
#so on until every node is "visited"

n=4
connections={1:[2, 3, 4],  3:[5], 4:[7, 8], 5:[6]}

def spread(connections): 
    stack=[]+connections[1]
    nDays = 0
    sNode = 1
    #keep repeating that process with the adjacent node with the highest number of adjacent nodes until all the nodes are visited
    while(len(stack) > 0):
        if sNode in connections.keys(): 
            nDays=infect(sNode, connections, nDays)
        sNode = stack.pop()
        if sNode in connections.keys(): 
            stack+=connections[sNode]
    print(nDays)
    
def infect(sNode, connections, nDays): 
    nConnect = len(connections[sNode])
    #double the number of cows until there are atleast as many cows as there are adjacent nodes
    while nConnect > 1: 
        nConnect = nConnect/2
        nDays+=1
    #send one cow to each adjacent node each day until all the adjacent nodes have atleast one cow 
    for i in connections[sNode]:
        nDays+=1
        
    return nDays
    
spread(connections)
