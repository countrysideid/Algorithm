
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        # corner case
        heaters.sort()
        houses.sort()
        heaters=[float('-inf')]+heaters+[float('inf')] # add 2 fake heaters
        ans,i = 0,0
        for house in houses:
            while house > heaters[i+1]:
                i+=1
            dis = min(house - heaters[i], heaters[i+1] - house)
            ans = max(dis, ans)
        return ans
        
