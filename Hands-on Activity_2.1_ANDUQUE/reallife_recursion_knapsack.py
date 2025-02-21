'''
You are living alone in your house, one day you check the stack of your foods and find out that it was empty so
you head to the grocery store with a limited budget and a shopping bag with a limited space. Now your goal is to
buy the most valuable items(nutritious and useful) while considering the three constraints.
'''

# Recursion implementation
def recursion_Knap(bag, budget, Weight, Cost, Value, n):


    if n == 0 or bag == 0 or budget == 0:
        return 0


    if Weight[n - 1] > bag or Cost[n - 1] > budget:
        return recursion_Knap(bag,budget,Weight,Cost,Value, n -1)

    else:
        return max(
            Value[n - 1] + recursion_Knap(bag - Weight[n - 1], budget - Cost[n - 1], Weight,Cost,Value, n - 1),
            recursion_Knap(bag,budget,Weight,Cost,Value,n - 1 )
            )


Item = ['Milk', 'Bread', 'Rice', 'Apples', 'Chicken', 'Cereal', 'Juice']
Value = [80, 50, 90, 70, 100, 60, 55]
Cost = [50, 20, 210, 40, 160, 60, 30]
Weight = [2, 1, 5, 1, 3, 2, 1]
budget = 500
bag = 10

print(f'Max Value: {recursion_Knap(bag,budget,Weight,Cost,Value, len(Value))}')