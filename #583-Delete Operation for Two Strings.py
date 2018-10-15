class Solution:
    def minDistance(self, word1, word2):
        row = len(word1)+1
        col = len(word2)+1
        if word1 == "" and word2 == "":
            return 0
        if word1 == "" and word2:
            return col-1
        if word2 == "" and word1:
            return row-1
        dp = []
        for i in range(0,row):
            temp = []
            for j in range(0,col):
                temp.append(0)
            dp.append(temp)
        
        for i in range(0,row):
            dp[i][0] = i
        
        for j in range(0,col):
            dp[0][j] = j
        
        for i in range(1,row):
            for j in range(1,col):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+ min(dp[i-1][j], dp[i][j-1])
        return dp[row-1][col-1]


def main():
    word1 = "prajwal"
    word2 = "raj"
    obj = Solution()
    print (obj.minDistance(word1,word2))

if __name__ == '__main__':
    main()