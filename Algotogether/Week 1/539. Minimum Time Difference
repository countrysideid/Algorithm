class Solution(object):
    
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        t = sorted ((int(i[:2])*60 + int(i[3:])) for i in timePoints)
        t.append(1440 + t[0])
        
        return min((y-x) for x,y in zip(t[:-1], t[1:]))
