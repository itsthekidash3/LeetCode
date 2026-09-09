class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        gate, obstacle, empty_room = 0, -1, 2147483647

        m, n = len(rooms), len(rooms[0])

        empty_rooms = set()
        queue = collections.deque([])

        for x in range(m):
            for y in range(n):
                if rooms[x][y] == gate:
                    queue.append((x,y, 0))
                    empty_rooms.add((x,y))
                if rooms[x][y] == empty_room:
                    empty_rooms.add((x,y))


        while queue:
            x, y, dist = queue.popleft()
            if (x, y) in empty_rooms:
                rooms[x][y] = dist
                empty_rooms.remove((x,y))
                queue.append((x+1, y, dist+1))
                queue.append((x-1, y, dist+1))
                queue.append((x, y-1, dist+1))
                queue.append((x, y+1, dist+1))




 