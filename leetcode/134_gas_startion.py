from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # return immediately if impossible
        print(f'{sum(gas)=} {sum(cost)=}')
        if sum(gas) < sum(cost):
            return -1

        # now know there is a solution

        tank = 0
        start_i = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:
                tank = 0
                start_i = i + 1

            # print(f'{start_i} {i=} : {gas[i]} - {cost[i]} += {tank=} ')

        return start_i
