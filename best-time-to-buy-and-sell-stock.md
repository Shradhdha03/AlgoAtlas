**Article: Best Time to Buy and Sell Stock**

---

**Problem Statement:**  
You are given an array `prices` where `prices[i]` represents the price of a stock on the `i`th day. Your task is to maximize your profit by choosing a single day to buy one stock and a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

**Constraints:**  
- The length of the prices array is between 1 and 10^5, inclusive: `1 <= prices.length <= 10^5`.
- Each stock price is a non-negative integer up to 10^4: `0 <= prices[i] <= 10^4`.

**Test Cases:**  
1. Input: `prices = [7,1,5,3,6,4]`
   Output: `5`
   Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), resulting in a profit of 5.

2. Input: `prices = [7,6,4,3,1]`
   Output: `0`
   Explanation: No profit can be made in this case, hence output is 0.

---

**All Solutions:**  

1. **Brute Force Approach:**  
   - For each stock price, compare it with every other stock price after it to calculate the profit.
   - Keep track of the maximum profit found.
   - This approach checks all possible buy-sell combinations.
   - Time Complexity: O(n^2)
   - Space Complexity: O(1)

2. **One-pass Solution (Greedy Approach):**  
   - Start from the first stock price and consider it as the buying price.
   - Iterate through the list of stock prices, update the buying price if a smaller value is found, else calculate the profit.
   - Keep track of the maximum profit found.
   - Time Complexity: O(n)
   - Space Complexity: O(1)

---

**My Solution Explanation:**  
You have implemented both the brute force and the greedy approach to this problem:

1. The `maxProfit` function implements the one-pass solution. 
   - You initialized `buy` as the first stock price and `maxProfit` to zero.
   - For each subsequent stock price, if it's lower than `buy`, update `buy`. If it's higher, compute the profit and update `maxProfit` if this profit is greater.
   
2. The `maxProfitBruteForce` function implements the brute force approach. 
   - For each stock price, you iterate over the subsequent stock prices to compute the potential profit.
   - You update `maxProfit` only if the computed profit is positive and higher than the current `maxProfit`.

---
```python
from typing import List

class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        # Total number of days for which stock prices are given
        n = len(prices)
        
        # Initialize buying price to the first stock price
        buy = prices[0]
        
        # Initialize maxProfit to 0 since we haven't made any profit yet
        maxProfit = 0
       
        # Start iterating from the second stock price (index 1)
        for i in range(1, n):
            # If the current price is lower than our buying price, 
            # then update our buying price
            if prices[i] < buy:
                buy = prices[i]

            # If the current price is higher than our buying price, 
            # then calculate the potential profit
            elif prices[i] > buy:
                profit = prices[i] - buy
                
                # Update the maxProfit if the current potential profit is higher 
                # than the previously calculated maxProfit
                maxProfit = max(maxProfit, profit)
                
        return maxProfit
    
    def maxProfitBruteForce(self, prices: List[int]) -> int:
        # Total number of days for which stock prices are given
        n = len(prices)
        
        # Initialize maxProfit to 0 since we haven't made any profit yet
        maxProfit = 0
        
        # Brute force approach: Compare every stock price with every other stock price after it
        for i in range(n):
            
            # Compare with stock prices after the ith stock price
            for j in range(i+1, n):
                
                # Calculate the potential profit for these two stock prices
                profit = prices[j] - prices[i]
                
                # If we can make a profit (i.e., sell price is higher than buy price),
                # then update the maxProfit if the calculated profit is higher than 
                # the previously calculated maxProfit
                if profit > 0:
                    maxProfit = max(profit, maxProfit)
                    
        return maxProfit
```

---

**Complexity Analysis:**  
1. `maxProfit` function (One-pass Solution):
   - Time Complexity: O(n) – You pass through the list of stock prices once.
   - Space Complexity: O(1) – You use a constant amount of space.

2. `maxProfitBruteForce` function (Brute Force Approach):
   - Time Complexity: O(n^2) – For each stock price, you potentially compare it with every subsequent stock price.
   - Space Complexity: O(1) – You use a constant amount of space.

---

**Technical Follow-up Questions (with answers):**  
1. *How would your solution change if you had to handle a massive dataset that cannot fit into memory?*
   - Answer: For the one-pass solution, the approach would remain the same, but we might need to employ techniques like external sorting or streaming to process the data in chunks. For the brute force approach, the dataset's size would make it impractical due to the quadratic complexity.

2. *How can we optimize the solution if the stock prices are updated in real-time?*
   - Answer: We can maintain a running minimum (buying price) and compute the profit in real-time as we receive stock price updates. This way, we won't need to re-process the entire dataset, making it efficient for real-time updates.

3. *How would your solution change if we could do at most two transactions?*
   - Answer: The problem becomes more complex, and a dynamic programming approach would be more suitable. We would need to maintain states representing the day, the number of transactions performed, and whether we own a stock.

---

**Real-world Use Cases:**  
1. **Algorithmic Trading:** Algorithms that automatically trigger buying and selling of stocks based on certain predefined criteria use such logic to maximize profit.
   
2. **Stock Market Analysis Tools:** Such tools provide insights and recommendations to stock market investors, leveraging algorithms that consider past stock prices to predict profitable future transactions.

3. **Financial Planning Software:** Software designed to aid personal finance or retirement planning might employ such algorithms to guide users about potential investment opportunities.

4. **Simulation & Backtesting:** Investment banks and hedge funds often use such algorithms in simulations to backtest certain trading strategies against historical stock market data.

