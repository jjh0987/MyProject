bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

import collections

bridge = collections.deque([0 for _ in range(bridge_length)])
truck_weights = collections.deque(truck_weights)

time = 0
num = 0
while num != 0 or truck_weights:
    try:
        if num <= weight or len(bridge) <= bridge_length:
            if not truck_weights:
                tar = bridge.popleft()
                num -= tar
                if tar > 0:
                    bridge.append(0)
                else:
                    bridge.append(tar)
            else:
                tar = truck_weights.popleft()
                num += tar
                bridge.append(tar)
                tp = bridge.popleft()
                if tp > 0:
                    num -= tp
                if num > weight:
                    tar = bridge.pop()
                    num -= tar
                    truck_weights.appendleft(tar)
                    bridge.append(0)
        else:
            bridge.pop()
            bridge.append(0)
    except:
        bridge.popleft()
        bridge.append(0)
    time += 1












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

