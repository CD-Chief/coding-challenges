# [383] Ransom Note
"""Solution 1
Loop through ransomnote and check whether each letter exists within magazine
If it does remove the letter from magazine and continue, otherwise its false
Edge:
- Empty Magazine
- Ransomnote is 1 or greater
- Magazine length shorter than ransomnote
Issues I ran into
- Incorrectly placed return False
"""

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote): return False

        newMag = magazine
        found = False

        for ch in ransomNote:
            found = False
            for i in range(len(newMag)):
                if ch == newMag[i]:
                    newMag = newMag[:i] + newMag[i+1:]
                    found = True
                    break
            if not found: return False

        return True 
