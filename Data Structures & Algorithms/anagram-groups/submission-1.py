class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for i, s in enumerate(strs):
            x = "".join(sorted(s))
            if x in seen:
                seen[x].append(strs[i])
            else:
                seen[x] = [strs[i]]
        return list(seen.values())