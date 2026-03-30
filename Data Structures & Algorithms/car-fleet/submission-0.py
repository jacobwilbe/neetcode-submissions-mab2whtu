class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #positions is a list of positions for the cars
        #speed is the speeds of the cars
        #target is the end position for the cars
        #speeds are constant, once a car reaches another they stay as a fleet
        #each car is its own fleet
        pairs = [(p,s) for p,s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []
        for p,s in pairs:
            time = ((target - p) / s)
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
