def recurssion_K(w_c, v_c, Weight, Volume, Value, n):

    # create a base case
    # define  as nth item is empty
    # or weight capacity is 0
    # or volume capacity is 0
    if n == 0 or w_c == 0 or v_c == 0:
        return 0

    # codition that checks if the weight or the volume of the item is more than the weight capacity and volume capacity
    #then the this item cannot be included  to the optimal solution or it is going to skip this item
    if (Weight[n - 1] > w_c or Volume[n - 1] > v_c):
        return recurssion_K(w_c, v_c, Weight, Volume, Value, n - 1)

    # return the highest result among the two cases
    # (1) include the nth item
    # (2) don't include the nth item
    else:
        return max(
            Value[n - 1] + recurssion_K(w_c - Weight[n - 1], v_c - Volume[n - 1], Weight, Volume, Value, n - 1),
            recurssion_K(w_c, v_c, Weight, Volume, Value, n - 1)
        )


#testing
Weight_Cap = 50 #constraint 1
Volume_Cap = 60 #constraint 2
Weight = [15, 25, 30, 40, 35] #weight of every items
Volume = [3, 5, 2, 4, 1] #volume of every itenms
Value = [100, 150, 250, 120, 80]# value of every items

#testing
print(f'MAX value: {recurssion_K(Weight_Cap, Volume_Cap, Weight, Volume, Value, len(Value))}')
