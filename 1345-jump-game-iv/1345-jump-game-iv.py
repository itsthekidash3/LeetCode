class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        graph = collections.defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
        q = collections.deque([0])
        visited = {0}
        steps = 0
        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                if curr == n - 1:
                    return steps
                for next_idx in (curr - 1, curr + 1):
                    if 0 <= next_idx < n and next_idx not in visited:
                        visited.add(next_idx)
                        q.append(next_idx)
                if arr[curr] in graph:
                    for next_idx in graph[arr[curr]]:
                        if next_idx not in visited:
                            visited.add(next_idx)
                            q.append(next_idx)
                    del graph[arr[curr]] 
            steps += 1
        return -1