from typing import List
from collections import defaultdict, deque



class Solution:
    def one_step(self, word1, word2):
        ok = False
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                if ok:
                    return False
                else:
                    ok = True

        return True

    def add_edge(self, word1, word2, graph):
        graph[word1].add(word2)
        graph[word2].add(word1)

    def bfs(self, graph, begin_word, end_word, all_words):
        queue = deque()
        queue.append(begin_word)
        visited = {w: False for w in all_words}
        visited[begin_word] = True
        d = 0
        while queue:
            l = len(queue)
            d += 1
            while l > 0:
                n = queue.popleft()
                if n == end_word:
                    return d
                for el in graph[n]:
                    if not visited[el]:

                        queue.append(el)
                        visited[el] = True
                l -= 1
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(set)
        all_words = [beginWord] + wordList

        for i in range(len(all_words)):
            for j in range(i+1, len(all_words)):
                if self.one_step(all_words[i], all_words[j]):
                    self.add_edge(all_words[i], all_words[j], graph)
        d = self.bfs(graph, beginWord, endWord, all_words)
        # print(graph)
        return d





def main():
    sol = Solution()
    beginWord = "leet"
    endWord = "code"
    wordList = ["lest","leet","lose","code","lode","robe","lost"]

    print(sol.ladderLength(beginWord, endWord, wordList))


if __name__ == "__main__":
    main()