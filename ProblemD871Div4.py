# Importing the necessary libraries
from typing import Set

def solve():
    # Reading input for n and m
    n, m = map(int, input().split())

    if n - m == 0:
        print("YES")
        return
    if n % 3 or m > n:
        print("NO")
        return

    # Set to store numbers
    st: Set[int] = set()
    st.add(n)

    while st:
        x = st.pop()

        if x == m:
            print("YES")
            return

        if x % 3 == 0:
            x //= 3
            if x == m or 2 * x == m:
                print("YES")
                return
            if x % 3 == 0:
                st.add(x)
                st.add(2 * x)

    print("NO")


t = int(input())  # Reading the number of test cases
while t > 0:
    solve()  # Calling the solve function for each test case
    t -= 1
