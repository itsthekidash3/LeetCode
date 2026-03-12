class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        # PROBLEM: Build a spanning tree with n-1 edges from n nodes
        # - Some edges are mandatory (must=1), others optional (must=0)
        # - Can upgrade k edges to double their strength (si *= 2)
        # - GOAL: Maximize the minimum strength in the spanning tree
        
        # APPROACH: Greedy MST construction + Strategic upgrades
        # 1. Add all mandatory edges first (no choice)
        # 2. Greedily add strongest optional edges to complete spanning tree
        # 3. Upgrade the k weakest edges in our final tree to boost minimum
        
        # Initialize Union-Find for cycle detection
        parents = [x for x in range(n)]
        
        # Find root with path compression - flattens tree for O(α(n)) amortized time
        def ufind(x):
            if parents[x] != x:
                parents[x] = ufind(parents[x])  # Path compression
            return parents[x]
        
        # Try to union two nodes - returns True if they were in different components
        def uunion(a, b):
            root_a = ufind(a)
            root_b = ufind(b)
            
            if root_a != root_b:
                parents[root_a] = root_b  # Union operation
                return True
            return False  # Already connected (would create cycle)
        
        weights = []  # Track all edge strengths in our spanning tree
        used = 0      # Count edges added to spanning tree
        
        # Helper: attempt to add edge to spanning tree
        def add(u, v, s):
            if uunion(u, v):  # Only add if it doesn't create a cycle
                nonlocal used
                used += 1
                return True
            return False
        
        # STEP 1: Process mandatory edges first
        consider = []  # Will hold optional edges for later
        
        for u, v, s, m in edges:
            if m == 1:  # Mandatory edge
                if not add(u, v, s):  # If it creates a cycle
                    return -1  # Impossible - mandatory edges form cycle
                weights.append(s)
            else:
                consider.append((u, v, s))  # Save optional edges
        
        # STEP 2: Greedily add strongest optional edges
        consider.sort(key=lambda x: -x[2])  # Sort by strength descending
        
        upgrade_weights = []  # Track which edges we added (can be upgraded)
        
        for u, v, s in consider:
            if add(u, v, s):
                upgrade_weights.append(s)
        
        # STEP 3: Validate we have a spanning tree
        if used != n - 1:  # Spanning tree needs exactly n-1 edges
            return -1  # Graph is disconnected
        
        # STEP 4: Upgrade the k weakest edges to maximize minimum
        # (Upgrading weak edges raises the floor more than upgrading strong ones)
        upgrade_weights.sort()  # Sort to find weakest
        
        for i in range(min(k, len(upgrade_weights))):
            # Find and upgrade in weights array
            upgrade_weights[i] *= 2
        
        weights.extend(upgrade_weights)
        return min(weights)  # Return minimum strength after upgrades