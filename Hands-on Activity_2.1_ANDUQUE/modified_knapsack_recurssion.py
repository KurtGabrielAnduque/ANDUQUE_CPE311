
def recurssion_K(w_c,v_c,Weight,Volume,Value,n):

    if n == 0 or w_c == 0 or v_c == 0:
        return 0


    if(Weight[n - 1] > w_c or Volume[n - 1] > v_c):
        return recurssion_K(w_c,v_c,Weight,Volume,Value,n - 1)

    else:
        return max(
            Value[n - 1] + recurssion_K(w_c - Weight[n - 1]  , v_c - Volume[n -1],Weight,Volume,Value,n-1),
            recurssion_K(w_c,v_c,Weight,Volume,Value,n-1)
        )

items = []
Weight_Cap = 8
Volume_Cap = 60
item = ['Bottled Water','Food Pack','First Aid Kit','Blanket','Flashlight']
Weight = [10,15,25,12,8]
Volume = [3,5,2,4,1]
Value = [10,15,25,12,8]

print(f'MAX value: {recurssion_K(Weight_Cap,Volume_Cap,Weight,Volume,Value,len(Value))}')
