'''
Valid Anagram


Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
 
Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

'''

def ValidAnagram(str1,str2):
    if len(str1) != len(str2):
        return False

    sMap,tMap = {},{}
    for c in str1:
        if c in sMap:
            sMap[c] += 1
        else:
            sMap = 1

    for c in str2:
        if c in tMap:
            tMap[c] += 1
        else:
            tMap = 1
        
    for char in sMap:
        if sMap[char] != tMap.get(char,0):
            return False
    
    return True

    