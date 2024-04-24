"""
Roblox sequences question
- given a set of experiences and max repititions for each
- can the input be organized into a string without repeating experiences?
"""
import heapq

def can_schedule_experiences(experience_map: dict[int, int]) -> bool:
    heap = []
    for exp_id, count in experience_map.items():
        heapq.heappush(heap, (-count, exp_id))
    
    last_exp_id, last_count = None, 0
    
    while heap:
        neg_count, exp_id = heapq.heappop(heap)
        count = -neg_count

        if last_count > 0:
            heapq.heappush(heap, (-last_count, last_exp_id))

        count -= 1

        if count > 0:
            last_exp_id, last_count = exp_id, count
        else:
            last_exp_id, last_count = None, 0

        if last_count > 0 and not heap and exp_id == last_exp_id:
            return False
    
    return True


assert not can_schedule_experiences(experience_map={
    1: 3,
    2: 1
})
assert can_schedule_experiences(experience_map={
    1: 2,
    2: 1
})
assert can_schedule_experiences(experience_map={
    3: 4,
    2: 2,
    1: 1
})