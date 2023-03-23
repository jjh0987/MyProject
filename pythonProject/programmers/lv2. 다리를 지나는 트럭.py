bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

import collections

bridge = []
truck_weights = collections.deque(truck_weights)

time = 0
while bridge or truck_weights:
    if not bridge:
        while truck_weights:
            bridge.append(truck_weights.popleft())
            if sum(bridge) > weight:
                truck_weights.appendleft(bridge.pop())
                break
            time += 1
    else:
        while bridge:
            bridge.pop()
            time += 1

