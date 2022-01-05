class Solution:
    def isBipartite(self, graph):    
        part = {} # dictionary to record the node is partitioned or not. 
        
        def dfs(current_node):
            for nxt in graph[current_node]:
                if nxt in part:
                    if part[nxt] == part[current_node]: # means two connected node in the same part
                        return False
                else: # otherwise, set it to a different part of its neighbour
                    part[nxt] = 1 - part[current_node] # if this node is not partitioned before, we put it in alternative part
                    if not dfs(nxt): # and further dfs it next node
                        return False
            return True
        
        for i in range(len(graph)):
            if i not in part:
                part[i] = 0
                if not dfs(i):
                    return False
                
        return True
