# ackermann algorithm in python for fun.
import sys  # import sys to change recursion limit

sys.setrecursionlimit(10**6)    # change the recursion limit to a large value or else it won't return

def ack(m, n):
    if m == 0:
        return (n + 1)
    elif n == 0:
        return ack(m - 1, ack(m - 1, 1))
    else:
        return ack(m - 1, ack(m, n - 1))

x = int(input("What is the value for m? "))
print(x)

y = int(input("What is the value for n? "))
print(y)

print("\n The result of your inputs according to the Ackermann function is: ")
print(ack(x, y))
