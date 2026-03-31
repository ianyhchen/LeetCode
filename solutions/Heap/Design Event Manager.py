import heapq
class EventManager:

    def __init__(self, events: list[list[int]]):
        # pri_queue stores: (-priority, eventId)
        self.pri_queue = []
        # event_pri_map stores: eventId -> -current_priority
        self.event_pri_map = {}
        for event in events:
            if event[0] not in self.event_pri_map:
                self.event_pri_map[event[0]] = event[1]
                
            heapq.heappush(self.pri_queue, (-1 * event[1], event[0]))
        
    def updatePriority(self, eventId: int, newPriority: int) -> None:
        # Add the new state into the heap (Lazy Update)
        heapq.heappush(self.pri_queue, (-1 * newPriority, eventId))
        if eventId in self.event_pri_map:
            self.event_pri_map[eventId] = newPriority            

    def pollHighest(self) -> int:
        while self.pri_queue:
            # Extract the element with highest priority (min -pri) 
            # and smallest eventId if priorities are tied.            
            curr_pri, curr_id =  heapq.heappop(self.pri_queue)

            # Check if this event is still "active" and the priority is up-to-date
            if curr_id in self.event_pri_map and self.event_pri_map[curr_id] == curr_pri:
                # Remove from map to mark it as no longer active
                del self.event_pri_map[curr_id]
                return curr_id
        return -1
            
                    
        


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()©leetcode