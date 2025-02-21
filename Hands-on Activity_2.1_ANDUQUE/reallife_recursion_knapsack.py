'''
You are living alone in your house, one day you check the stack of your foods and find out that it was empty so
you head to the grocery store with a limited budget and a shopping bag with a limited space. Now your goal is to
buy the most valuable items(nutritious and useful) while considering the three constraints.
'''

# Recursion implementation
def recursion_Knap(bag, budget, Weight, Cost, Value, n):

    # create a base case
    # define  as nth item is empty
    # or bag is empty or 0
    # or there are no budget or 0
    if n == 0 or bag == 0 or budget == 0:
        return 0

    # codition that checks if the weight or the cost of the item is more than the weight capacity of the bag and remaining budget
    # then the this item cannot be included  to the optimal solution or it is going to skip this item
    if Weight[n - 1] > bag or Cost[n - 1] > budget:
        return recursion_Knap(bag,budget,Weight,Cost,Value, n -1)


    # return the highest result among the two cases
    # (1) include the nth item
    # (2) don't include the nth item
    else:
        return max(
            Value[n - 1] + recursion_Knap(bag - Weight[n - 1], budget - Cost[n - 1], Weight,Cost,Value, n - 1),
            recursion_Knap(bag,budget,Weight,Cost,Value,n - 1 )
            )



Value = [80, 50, 90, 70, 100, 60, 55] #Value of products
Cost = [50, 20, 210, 40, 160, 60, 30] #Cost of products
Weight = [2, 1, 5, 1, 3, 2, 1] #weight of products
budget = 500 #budget alloted
bag = 10 #capacity of the bag they bring

print(f'Max Value: {recursion_Knap(bag,budget,Weight,Cost,Value, len(Value))}')