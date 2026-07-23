from collections import defaultdict
class DetectSquares:

    def __init__(self):
        # Nested hash map: x_coordinate -> y_coordinate -> count
        self.point_map = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        # Increment the frequency count of the given point (x, y)
        x, y = point[0], point[1]
        self.point_map[x][y] += 1
        

    def count(self, point: List[int]) -> int:
        x1, y1 = point[0], point[1]        
        total_count = 0

        # Get all points that share the same X-coordinate as the query point
        y_map = self.point_map[x1]

        # Iterate through all available y2 coordinates on the same vertical line
        for y2, y2_count in y_map.items():
            # Skip if it is the query point itself (side length must be greater than 0)
            if y2 == y1:
                continue

            # Calculate the side length of the square    
            d = abs(y1 - y2)

            # Case 1: Check the square on the right side (x1 + d)
            # Use 'in' to prevent defaultdict from automatically creating empty sub-dicts
            if x1 + d in self.point_map:
                right_map = self.point_map[x1 + d]
                # Multiply the counts of the other 3 vertices based on the multiplication principle
                total_count += y2_count * right_map[y1] * right_map[y2]
            # Case 2: Check the square on the left side (x1 - d)
            if x1 - d in self.point_map:
                left_map = self.point_map[x1 - d]
                # Multiply the counts of the other 3 vertices based on the multiplication principle
                total_count += y2_count * left_map[y1] * left_map[y2]
        return total_count


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)