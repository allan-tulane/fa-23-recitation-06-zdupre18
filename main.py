def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1
    ###TODO
    counts[n] += 1
    
    # Base case
    if n <= 1:
        return n
    
    # Recursive case
    return fib_recursive(n - 1, counts) + fib_recursive(n - 2, counts)
    

    
def fib_top_down(n, fibs):
    ###TODO
    if fibs[n] is not None:
        return fibs[n]

    # Base case
    if n <= 1:
        fibs[n] = n
    else:
        # Recursive case
        fibs[n] = fib_top_down(n - 1, fibs) + fib_top_down(n - 2, fibs)

    return fibs[n]


def fib_bottom_up(n):
    ###TODO
     if n <= 1:
        return n

    fibs = [0] * (n + 1)
    fibs[1] = 1

    for i in range(2, n + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]

    return fibs[n]




def fib_bottom_up_better(n):
    ###TODO
    if n <= 1:
        return n

    prev, curr = 0, 1

    for i in range(2, n + 1):
        next_fib = prev + curr
        prev, curr = curr, next_fib

    return curr
