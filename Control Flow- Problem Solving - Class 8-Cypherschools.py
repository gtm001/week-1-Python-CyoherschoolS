n=5
for i in range(n):
    for j in range(n):
        print(max(i+1,j+1,n-i,n-j),end= " ")
    print()

    # statements:
    # 'n-j' will give distance from right
    # 'j+1' will give disance from left
    # 'i+1' will give disance from top
    #  'n-1' will give disance from bottom