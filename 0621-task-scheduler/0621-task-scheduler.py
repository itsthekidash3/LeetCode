from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Goal: Schedule tasks with cooldown period n, minimize total time
        # Rules: Same task cannot run within n intervals of each other
        # Approach: Max heap for most frequent tasks + queue to track cooldowns
        # Strategy: Always process most frequent task available (greedy)
        
        # Step 1: Count frequency of each task type
        count = Counter(tasks)
        
        # Step 2: Create max heap with task frequencies (negate for max heap)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)  # Fixed typo: was 'hapify'
        
        time = 0  # Track total time elapsed
        q = deque()  # Queue stores [remaining_count, available_time] for cooling tasks
        
        # Step 3: Process tasks until heap and queue are empty
        while maxHeap or q:
            time += 1  # Increment time (either process task or idle)
            
            if maxHeap:
                # Pop most frequent task and process it
                cnt = 1 + heapq.heappop(maxHeap)  # cnt is negative, so adding 1 reduces magnitude
                
                # If task has remaining occurrences, add to cooldown queue
                if cnt:  # cnt != 0 means more instances of this task remain
                    q.append([cnt, time + n])  # Can't run again until time + n
            
            # Check if any task in queue has finished cooling down
            if q and q[0][1] == time:  # Fixed: should compare to time, not just check truthiness
                heapq.heappush(maxHeap, q.popleft()[0])  # Fixed typo: was 'maxheap'
        
        return time  # Fixed: should return time, not 0