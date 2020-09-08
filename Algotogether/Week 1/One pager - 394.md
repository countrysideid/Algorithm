# Decode String

LeetCode 394: https://leetcode.com/problems/decode-string/

## Thinking Process

In order to return a decoded string while an encoded string is given, we need to spit char strings inside brackets ('[', and ']') and outside bracket.
Only strings inside brackets are replicated, so we can store strings and the number of times they should be repliated into the stack. Do the replication and
concatenate with the previous string.

## Solutions

### Stack

To return a decoded string while an encoded string is given, we first need to identify numeric integer, character, and brackets ('[', and ']').
Then we need to use a stack to store the single char or char string, and the numeric integer into a stack. Based on the numeric integer before brackets '[',
we need to replicate the single char or char string inside '[' and ']' the numeric integer number of times, and concatenated the replicated char string to the previous 
char string. Once the stack is empty, the concatenated string char is the decoded string.

## Code

### Decode String using a stack

```python
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # corner case
        if len(s) == 0 or '[' not in s:
            return s
        current_str = ''
        num = 0
        # length = len(s)
        # p1= 0
        q = []
        for c in s:
            if c == '[':
                q.append((current_str, num))
                current_str = ''
                num = 0
            elif c == ']':
                previous_str, times = q.pop()
                current_str =  previous_str + times * current_str
            elif c.isdigit():
                num = num*10 + int(c)
            else:
                current_str += c
        return current_str
```

## My Weakness /Bugs

1. [Weakness-1] Can’t figure out how to use 1 stack.

This problem is intuitive with stack. However, some people may use multiple stacks to store stings inside brackets and outside brackets, which may take extrac space.

2. [Bug-1] Not familiar with stack, so that write too many conditions, and got lost in the loop.

## My Similar Problems

LeetCode 271: https://leetcode.com/problems/encode-and-decode-strings/
LeetCode 880: https://leetcode.com/problems/decoded-string-at-index/
