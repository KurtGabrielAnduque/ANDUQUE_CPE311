'''
You are living alone in your house, one day you check the stack of your foods and find out that it was empty so
you head to the grocery store with a limited budget and a shopping bag with a limited space. Now your goal is to
buy the most valuable items(nutritious and useful) while considering the three constraints.
'''

# Dynamic Programming Implementation
def DP_Knapsack(bag,budget,Weight,Cost,Value,n):

    table = [[[0 for x in range(budget + 1)] for y in range(bag + 1)] for z in range(n + 1)]

    for row in range(n + 1):
        for weight_column in range(bag + 1):
            for cost_column in range(budget + 1):

                if row == 0 or weight_column == 0 or cost_column == 0:
                    table[row][weight_column][cost_column] = 0

                elif Weight[row - 1] <= weight_column and Cost[row - 1] <= cost_column:
                    table[row][weight_column][cost_column] = max(
                        table[row - 1][weight_column][cost_column],
                        table[row - 1][weight_column - Weight[row - 1]][cost_column - Cost[row  - 1]] + Value[row - 1]
                    )
                else: #skip the item the value will be the same as the previous row in the table
                    table[row][weight_column][cost_column] = table[row - 1][weight_column][cost_column]

    return table[n][bag][budget]


Item = ['Milk', 'Bread', 'Rice', 'Apples', 'Chicken', 'Cereal', 'Juice']
Value = [80, 50, 90, 70, 100, 60, 55]
Cost = [50, 20, 210, 40, 160, 60, 30]
Weight = [2, 1, 5, 1, 3, 2, 1]
budget = 500
bag = 10


print(f'Max Value: {DP_Knapsack(bag,budget,Weight,Cost,Value,len(Value))}')