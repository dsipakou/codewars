class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            cur = trie
            for lett in word:
                if lett not in cur:
                    cur[lett] = {}
                cur = cur[lett]
            cur['*'] = word
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        output = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.explore(i, j, board, visited, trie, output)
        return output.keys()
        
    def explore(self, i, j, board, visited, node, output):
        if visited[i][j]:
            return
        ch = board[i][j]
        if ch not in node:
            return
        visited[i][j] = True
        node = node[ch]
        if '*' in node:
            output[node['*']] = True
        nb = self.neighbors(i, j, board)
        for nn in nb: 
            self.explore(nn[0], nn[1], board, visited, node, output)
        visited[i][j] = False
    
    def neighbors(self, i, j, board):
        output = []
        if i > 0:
            output.append([i - 1, j])
        if i < len(board) - 1:
            output.append([i + 1, j])
        if j > 0:
            output.append([i, j - 1])
        if j < len(board[0]) - 1:
            output.append([i, j + 1])
        return output
