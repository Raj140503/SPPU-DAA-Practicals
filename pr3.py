# Write a program to solve a fractional Knapsack problem using a greedy method.

class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractionalKnapsack(w, arr):
    arr.sort(key=lambda x: x.profit/x.weight, reverse = True)
    finalValue = 0.0
    for item in arr:
        if w > item.weight:
            finalValue += item.profit
            w -= item.weight
        else:
            finalValue += item.profit * (w/item.weight)
            break
    return finalValue

if __name__ == '__main__':
    n = int(input('Enter number of items-\n'))
    arr = []
    for i in range(n):
        profit = int(input('Enter profit of item ' + str(i+1) + '-\n'))
        weight = int(input('Enter weight of item ' + str(i+1) + '-\n'))
        arr.append(Item(profit, weight))
    w = int(input("Enter capacity of knapsack-\n"))
    print("Maximum value in knapsack: ", fractionalKnapsack(w,arr))


#Output 

'''
Enter number of items-
3
Enter profit of item 1-
60
Enter weight of item 1-
10
Enter profit of item 2-
100
Enter weight of item 2-
20
Enter profit of item 3-
120
Enter weight of item 3-
30
Enter capacity of knapsack-
50
Maximum value in knapsack:  240.0
'''