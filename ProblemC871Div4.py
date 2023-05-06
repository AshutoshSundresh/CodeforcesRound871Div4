def sol():
    n = int(input())  # Read the value of n

    a, b, c, d = [], [], [], []  # Initialize lists to store values
    a_count, b_count, c_count, d_count = 0, 0, 0, 0  # Initialize counters for each category

    for _ in range(n):
        x, s = list(map(int, input().split()))  # Read the values of x and s as integers

        # Categorize the values based on s
        if s == 0:
            a.append(x)
            a_count += 1
        elif s == 10:
            b.append(x)
            b_count += 1
        elif s == 1:
            c.append(x)
            c_count += 1
        else:
            d.append(x)
            d_count += 1

    min_val = float('inf')  # Set initial minimum value to infinity
    found = 0  # Flag to indicate if a valid solution is found

    if d_count != 0:
        x = float('inf')
        for i in range(d_count):
            if d[i] < x:
                x = d[i]
        found = 1
        min_val = x

    if b_count != 0 and c_count != 0:
        x = float('inf')
        y = float('inf')
        for i in range(c_count):
            if c[i] < x:
                x = c[i]
        for i in range(b_count):
            if b[i] < y:
                y = b[i]
        if x + y < min_val:
            min_val = x + y
        found = 1

    if found == 1:
        print(min_val)
    else:
        print(-1)


t = int(input())  # Read the number of test cases

while t > 0:
    sol()
    t -= 1
