class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        # corner case
        if len(secret) != len(guess):
            return -1
        count_A, count_B = 0, 0
        dict_s, dict_g, dict_A = {}, {}, {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                count_A += 1
                if secret[i] in dict_A:
                    dict_A[secret[i]] += 1
                else:
                    dict_A[secret[i]] = 1
                    
            if secret[i] in dict_s:
                dict_s[secret[i]] += 1
            else:
                dict_s[secret[i]] = 1
                
            if guess[i] in dict_g:
                dict_g[guess[i]] += 1
            else:
                dict_g[guess[i]] = 1
                
        for i in dict_s:
            if i in dict_g:
                if i in dict_A:
                    count_B += (min(dict_s[i], dict_g[i]) - dict_A[i])
                else:
                    count_B += min(dict_s[i], dict_g[i])
        return '{}A{}B'.format(count_A, count_B)
