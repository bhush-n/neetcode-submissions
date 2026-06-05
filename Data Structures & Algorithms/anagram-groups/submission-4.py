from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)

        for ch in strs:
            n = "".join(sorted(ch))
            anagrams[n].append(ch)
        return list(anagrams.values())
