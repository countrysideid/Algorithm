class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        # corner case
        if not IP:
            return 'Neither'
#         def isIPV4(x):
#             try: return (x == str(int(x))) and (0 <= x <= 255)
#             except: return False
        
#         def isIPV6(x):
#             try: return (0 <= len(x) <= 4) and int(s, 16) >= 0
#             except: return False

#         if IP.count(".") == 3 and all(isIPV4(i) for i in IP.split(".")):
#             return "IPv4"
#         if IP.count(":") == 7 and all(isIPV6(i) for i in IP.split(":")):
#             return "IPv6"
#         return "Neither"
        
        def is_ip4(x):
            
            x_list= x.split('.')
            
            if  len(x_list) != 4 :
                return False
            
            for i in x_list:
                if len(i) == 0:
                    return False
                for j in i:
                    if not j.isdigit():
                        return False
                if i != str(int(i)):
                    return False
             
            new_x = [int(i) for i in x_list]
            if min(new_x) <0 or max(new_x) > 255:
                return False
            return True
        
        def is_ip6(x):
            hexadecimal  = 'abcdefABCDEF'
            x_list= x.split(':')
            
            if len(x_list) != 8 :
                return False
            for i in x_list:
                if len(i) == 0:
                    return False
                if len(i) > 4 or len(i) ==0:
                    return False
                
                for j in i:
                    if (not j.isdigit()) and (not j in hexadecimal):
                        return False
            return True
        
        if is_ip4(IP):
            return "IPv4"
        elif is_ip6(IP):
            return "IPv6"
        else :
            return "Neither"
