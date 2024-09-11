## Fractional Knapsack Problem
> [!NOTE]
> To implement this greedy strategy, each item in the problem should be able to be divided into **fractions**

## How it works?
1. Calculate the ratio of the profit for each single kilo of the item.
2. Sort the item by ratio from the largest to the smallest.
3. While knapsack if not full: for each item, if item weight is less than the current knapsack capacity then add it as is in the knapsack, else add a fraction of it.

![Fractional Knapsack problem](https://github.com/Mohammed-Abdelmoneim/Algorithms-Analysis-and-Design-from-scratch/blob/main/greedy_algorithm/fractional_knapsack_problem/Fractional%20Knapsack.png)
