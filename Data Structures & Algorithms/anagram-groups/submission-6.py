class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for letter in word:
                key[ord(letter) - ord('a')] += 1
            hash[tuple(key)].append(word)
        return list(hash.values())
