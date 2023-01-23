class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        visited = [False]*V
        dfsvisited=[False]*V
        for i in range(V):
            if visited[i]==False:
                if self.dfs(i,visited,dfsvisited,adj):
                    return True
        return False
    
    def dfs(self,node,visited,dfsvisited,adj):
        visited[node]=True
        dfsvisited[node]=True
        for ele in adj[node]:
            if visited[ele]==False:
                if self.dfs(ele,visited,dfsvisited,adj):
                    return True
            elif dfsvisited[ele]:
                return True
        
        dfsvisited[node]=False
        return False
