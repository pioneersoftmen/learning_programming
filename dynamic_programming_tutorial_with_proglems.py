# # Python program to Returns the number of arrangements to form 'n'
# def solve(n):
#     # Base case
#     if (n < 0):
#         return 0
#     if (n == 0):
#         return 1

#     return solve(n - 1) + solve(n - 3) + solve(n - 5)

# print(solve(int(input())))



# # Adding memoization or tabulation for the state
# # Initialize to -1
# dp = []
 
# # This function returns the number of
# # arrangements to form 'n'
# def solve(n):
#     # base case
#     if n < 0:
#         return 0
#     if n == 0:
#         return 1
 
# # Checking if already calculated
#     if dp[n] != -1:
#         return dp[n]
 
# # Storing the result and returning
#     dp[n] = solve(n-1) + solve(n-3) + solve(n-5)
#     return dp[n]
 
# print(solve(int(input())))


# # Fibonacci sequence up to the nth term 
# # Naive approach

# def fib(n):
#     if (n <= 1):
#         return n 
    
#     x = fib(n - 1)
#     y = fib(n - 2)
    
#     return x + y

# n = 5

# # Function Call
# print(fib(n))



# # Helper Function
# def fibo_helper(n, ans):
#     # Base case
#     if (n <= 1):
#         return n
    
#     # To check if output already exists
#     if (ans[n] != - 1):
#         return ans[n]
    
#     #  Calculate output 
#     x = fibo_helper(n - 1, ans)
#     y = fibo_helper(n - 2, ans)

#     # Saving the output for future use
#     ans[n] = x + y

#     # Returning the final output
#     return ans[n]

# def fibo(n):
#     ans = [-1] * (n + 1)

#     # Initialize with -1
#     # for (i = 0; i <= n; i++) {
#     for i in range(0, n + 1):
#         ans[i] = -1
#     return fibo_helper(n, ans)

# # Code 
# n = 5

# # Function Call
# print(fibo(n))




# # Function for calculating the nth
# # Fibonacci number
# def fibo(n):
#     ans = [None] * (n + 1)

#     # Storing the independent values in the 
#     # answer array
#     ans[0] = 0
#     ans[1] = 1

#     # Using the bottom - up approach
#     for i in range(2, n + 1):
#         ans[i] = ans[i - 1] + ans[i - 2]

#     # Returning the final index
#     return ans[n]

# # Drivers code
# n = 5

# # Function Call
# print(fibo(n))




# Python code for the above approach

# Function for calculating the nth Fibonacci number
def fibo(n):
    prevPrev, prev, curr = 0, 1, 1
    # Using the bottom-up approach
    for i in range(2, n + 1):
        curr = prev + prevPrev
        prevPrev = prev 
        prev = curr
    # Returning the final answer
    return curr

# Drivers code
n = 5
# Function Call
print(fibo(n))

