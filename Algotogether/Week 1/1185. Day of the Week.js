class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        # corner case year less than 1971 or year > 2100
        if year < 1971 or year > 2100:
            return -1
        
        t = [ 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 ] 
        y = year
        m = month
        d = day
        y -= m < 3

        ret = str(( y + int(y / 4) - int(y / 100) + int(y / 400) + t[m - 1] + d) % 7) 

        daycode = {"0":"Sunday", "1":"Monday","2": "Tuesday","3": "Wednesday","4": "Thursday","5": "Friday", "6":"Saturday"}
        for key, value in daycode.items():
            if ret == key:
                return value
