from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:

        m = len(classroom)
        n = len(classroom[0])

        
        start_r = start_c = 0
        litter_id = [[-1] * n for _ in range(m)]
        litter_count = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start_r, start_c = i, j

                elif classroom[i][j] == 'L':
                    litter_id[i][j] = litter_count
                    litter_count += 1

       
        if litter_count == 0:
            return 0

        
        full_mask = (1 << litter_count) - 1

        
        queue = [
            (start_r, start_c, energy, 0)
        ]

        
        visited = set()
        visited.add((start_r, start_c, energy, 0))

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        moves = 0

        while queue:

            next_queue = []

            for r, c, curr_energy, mask in queue:

                
                if mask == full_mask:
                    return moves

                
                if curr_energy == 0:
                    continue

                
                for dr, dc in directions:

                    nr = r + dr
                    nc = c + dc

                    
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    
                    if classroom[nr][nc] == 'X':
                        continue

                    
                    new_energy = curr_energy - 1

                    new_mask = mask

                    
                    if classroom[nr][nc] == 'L':
                        idx = litter_id[nr][nc]
                        new_mask |= (1 << idx)

                    
                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    state = (nr, nc, new_energy, new_mask)

                    if state not in visited:
                        visited.add(state)
                        next_queue.append(state)

            queue = next_queue
            moves += 1

        return -1