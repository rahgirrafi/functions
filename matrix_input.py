def matrix_input(row_number):
    arr = []
    for i in range(row_number):
        r1 = list(map(int, input().split()))
        arr.append(r1)

    arr = np.array(arr)
