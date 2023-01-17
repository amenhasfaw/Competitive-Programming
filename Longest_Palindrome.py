'''
Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

Constraints:
1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.

'''

def longestPalindrome(string):
    SMap = {}
    for i in SMap:
        if i in SMap:
            SMap[i] += 1
        else:
            SMap = 1
    
    res = 0
    odd = 0

    for i in SMap.values():
        if i > 1:
            if i%2 == 0:
                res += i
            else:
                res += i - 1
                odd += 1
        else:
            odd += 1

    if odd > 1:
        res += 1

    return res