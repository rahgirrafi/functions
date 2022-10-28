#input row number of your matrix. Then enter 1 row at a time and press Enter.
def matrix_input(row_number):
    arr = []
    for i in range(row_number):
        r1 = list(map(int, input().split()))
        arr.append(r1)

    arr = np.array(arr)
'''
Input:
1 2 3
1 2 3

Output:
[[1 2 3]
 [1 2 3]]
 
'''
