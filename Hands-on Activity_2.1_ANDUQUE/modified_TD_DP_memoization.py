Weight_Cap = 50
Volume_Cap = 60
Weight = [15, 25, 30, 40, 35]
Volume = [3, 5, 2, 4, 1]
Value = [100, 150, 250, 120, 80]
n = len(Value)

calc = [[[-1 for x in range(Volume_Cap + 1)] for y in range(Weight_Cap + 1)] for z in range(n + 1)]

def mem_knapsack(w_c,v_c,Weight,Volume,Value,n):
    if n == 0 or w_c == 0 or v_c == 0:
        return 0
    if calc[n][w_c][v_c] != -1:
        return calc[n][w_c][v_c]

    if Weight[n - 1] <= w_c and Volume[n - 1] <= v_c:
        calc[n][w_c][v_c] = max(
            Value[n - 1] + mem_knapsack(w_c - Weight[n - 1]  , v_c - Volume[n -1],Weight,Volume,Value,n-1),
            mem_knapsack(w_c,v_c,Weight,Volume,Value,n-1)
        )
        return calc[n][w_c][v_c]
    elif Weight[n - 1] > w_c:
        calc[n][w_c][v_c] = mem_knapsack(w_c,v_c,Weight,Volume,Value,n-1)
        return calc[n][w_c][v_c]


print(f'Max Value: {mem_knapsack(Weight_Cap,Volume_Cap,Weight,Volume,Value,n)}')