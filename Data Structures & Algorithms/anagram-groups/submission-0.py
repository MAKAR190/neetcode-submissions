class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for string in strs:
            key = sorted(string)
            groups.setdefault("".join(key),[]).append(string)
        
        return list(groups.values())