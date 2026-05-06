class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        # Collision only happens when stack top is moving right (positive) 
        # and current asteroid is moving left (negative)
        for curr in asteroids:
            alive = True
            while alive and curr < 0 and stack and stack[-1] > 0:
                if stack[-1] < abs(curr):
                    # Stack top asteroid is smaller, it explodes
                    stack.pop()
                    # Current asteroid continues to collide with the next stack top
                    continue
                elif stack[-1] == abs(curr):
                    # Both asteroids are the same size, both explode
                    stack.pop()
                # Current asteroid explodes or both explode
                alive = False
                
            # If current asteroid survived all collisions or no collision occurred
            if alive:
                stack.append(curr)
        
        return stack
