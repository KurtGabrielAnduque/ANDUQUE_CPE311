# Dynamic
def DP_K(w_c, v_c, Weight, Volume, Value, n):
    table = [[[0 for x in range(v_c + 1)] for y in range(w_c + 1)] for z in range(n + 1)]

    for i in range(n + 1):
        for W in range(w_c + 1):
            for V in range(v_c + 1):
                if i == 0 or W == 0 or V == 0:
                    table[i][W][V] = 0
                elif Weight[i - 1] <= W and Volume[i - 1] <= V:
                    table[i][W][V] = max(Value[i - 1] + table[i - 1][W - Weight[i - 1]][V - Volume[i - 1]],
                                         table[i - 1][W][V])

                else:
                    table[i][W][V] = table[i - 1][W][V]

    return table[n][w_c][v_c]


Weight_Cap = 50
Volume_Cap = 60
Weight = [15, 25, 30, 40, 35]
Volume = [3, 5, 2, 4, 1]
Value = [100, 150, 250, 120, 80]

print(f'MAX value: {DP_K(Weight_Cap, Volume_Cap, Weight, Volume, Value, len(Value))}')