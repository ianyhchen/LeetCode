class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sort boxes by the number of units per box in descending order
        boxTypes.sort(key = lambda x:x[1], reverse=True)
        
        total_units = 0
        
        for num_boxes, units_per_box in boxTypes:
            # If the truck is already full, break immediately
            if truckSize == 0:
                break

            # Take as many boxes as possible (either all available boxes or up to the remaining truck capacity)            
            boxes_to_take = min(num_boxes, truckSize)

            # Add the total units of the chosen boxes
            total_units += units_per_box * boxes_to_take

            # Deduct the count of boxes taken from the truck's remaining capacity
            truckSize -= boxes_to_take
            
        return total_units