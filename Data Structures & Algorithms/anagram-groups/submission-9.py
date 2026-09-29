class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_words = {}
        grouped_anagrams = []

        for word in strs:
            if str("".join(sorted(word))) in hash_words:
                hash_words[str("".join(sorted(word)))].append(word)
            else:
                hash_words[str("".join(sorted(word)))] = [word]

        for lst in hash_words.values():
            grouped_anagrams.append(lst)

        return grouped_anagrams