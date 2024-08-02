""" 
Dado 3 números diferentes, evaluar y entregar el orden de mayor a menor
This is a variation of the Bubble Sort algorithm.
Bubble Sort repeatedly steps through the list, compares adjacent elements,
and swaps them if they are in the wrong order.
The process is repeated until the list is sorted.

Bubble Sort requires at most ( n-1 ) passes through the list,
where ( n ) is the number of elements in the list.
"""

number_1=4
number_2=5
number_3=6

decreasing_order = [number_1,number_2,number_3]

for _ in range(len(decreasing_order) - 1):
    for idx in range(len(decreasing_order)):
        if idx==len(decreasing_order)-1:
            continue
        elif decreasing_order[idx] < decreasing_order[idx+1]:
            # Swap the elements
            decreasing_order[idx],decreasing_order[idx+1] = decreasing_order[idx+1],decreasing_order[idx]
        else:
            continue
    # early exit: break the loop if the numbers are in ordered
    if decreasing_order[0] > decreasing_order[1] and decreasing_order[1] > decreasing_order[2]:
        break
            
print(decreasing_order)