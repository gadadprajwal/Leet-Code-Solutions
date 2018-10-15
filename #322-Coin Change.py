import math
class Solution:
    def coinChange(self, coins, amount):
        # Table for storing previous results
        dp = []
        # Append the table initially with infinity
        for i in range(amount+1):
            dp.append(math.inf)
        # Initialize the first index with 0 as it is the base case for our problem
        dp[0] = 0
        
        # Find the minimum number of coins that could be used to get to the amount remaining and add that to your dp table
        for i in range(1,amount+1):
            min_ = math.inf
            for j in range(len(coins)):
                if i-coins[j] >= 0:
                    if min_ > dp[i-coins[j]]:
                        min_ = dp[i-coins[j]]
            if min_ != math.inf:
                dp[i] = min_+1
        # If no combination is possible then the value is remained as infinity as it does not change and we return -1
        if dp[amount] == math.inf:
            return -1
        else:
            return dp[amount]


def main():
    coins = [1,5,10]
    amount = 10
    obj = Solution()
    print(obj.coinChange(coins, amount))

if __name__ == '__main__':
    main()