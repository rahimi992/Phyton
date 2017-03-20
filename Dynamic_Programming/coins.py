# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 21:45:07 2017

@author: Amin
"""
"""
Write a function to compute the number of combinations that make up that amount. 
You may assume that you have infinite number of each kind of coin.
"""

def change(amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(1, amount + 1):
               if j >= i:
                   dp[j] += dp[j - i]
        return dp[amount]
    
    
value = 10
coins = [1, 2, 5]

print change(value, coins)