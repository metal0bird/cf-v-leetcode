class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        queue = deque([(x,0)])
        visited = set()  
        count = 0
        diff = float('inf')
        while queue:
            node , depth = queue.popleft()
            
            if node == y:
                count=depth
                break
            
            visited.add(node)

            if node % 11 == 0:
                child = node // 11
                if child not in visited:
                    queue.append((child,depth+1))
            
            if node % 5 == 0:
                child = node // 5
                if child not in visited:
                    queue.append((child,depth+1))
            
            child = node - 1
            if child not in visited:
                queue.append((child,depth+1))
                
            child = node + 1
            if child not in visited:
                queue.append((child,depth+1))
            
        return count
        