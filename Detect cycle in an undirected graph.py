class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    
	    visited = [False for _ in range(V)]
	    for i in range(V):
	        if visited[i] == False:
	            if self.dfs(visited,adj,i,-1):
	            #if self.bfs(visited,adj,i):
	                return True
	            
	    return False
	
	def dfs(self,visited,adj,node,parent):
	    visited[node]=True
	    for neighbour in adj[node]:
	        if visited[neighbour]==False:
	            cycleDetected = self.dfs(visited,adj,neighbour,node)
	            if cycleDetected:
	                return True
	        elif neighbour!=parent:
	            return True
	    return False
	
	def bfs(self,visited,adj,sv):
	    q = Queue()	    
		parent = {}
		parent[sv]=-1
		q.put(sv)
		visited[sv]=True
		while not q.empty():
		    front = q.get()
		    for ele in adj[front]:
		        if visited[ele]==True and ele!=parent[front]:
		            return True
		        elif visited[ele]==False:
		            q.put(ele)
		            visited[ele] = True
		            parent[ele] = front
        return False
