order = []
components = []
adj = [[1], [3, 4], [0], [2], [5, 6], [6], [] ]
adjT = [[2], [0], [3], [1], [1], [4], [5]]
visited = [False]*len(adj)

def dfs(v):
    visited[v] = True
    for u in adj[v]:
        if visited[u] == False:
            dfs(u)
    order.append(v)

def dfsOpposite(v):
    visited[v] = True
    components.append(v)
    for u in adjT[v]:
        if visited[u] == False:
            dfsOpposite(u)

for i in range(len(adj)):
    if visited[i] == False:
        dfs(i)

visited = [False]*len(adj)

for i in range(len(adjT)):
    v = order[len(adjT)-1-i]
    if visited[v] == False:
        dfsOpposite(v)
        print(components)
        components.clear()
