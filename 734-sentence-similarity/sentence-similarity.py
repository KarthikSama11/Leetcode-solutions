class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        N1, N2 = len(sentence1), len(sentence2)
        if N1 != N2:
            return False
        pairs = defaultdict(set)
        for v, w in similarPairs:
            pairs[v].add(w)
            pairs[w].add(v)
        for i, word in enumerate(sentence1):
            if word == sentence2[i]:
                continue
            if word in pairs and sentence2[i] in pairs[word]:
                continue
            return False

            
        return True

        