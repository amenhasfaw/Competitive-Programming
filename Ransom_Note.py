'''
Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

 

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

'''


def canConstruct(RansomNote, Magazine):
    ransom, mag = {}, {}
    for i in RansomNote:
        if i in ransom:
            ransom[i] += 1
        else:
            ransom = 1

    for i in Magazine:
        if i in mag:
            mag[i] += 1
        else:
            mag = 1

    for char in ransom:
        if mag.get(char,0) >= ransom[char]:
            continue
        else:
            return False
    return True