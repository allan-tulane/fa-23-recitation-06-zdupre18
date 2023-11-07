# CMPS 2200 Recitation 06
## Answers

**Name:**_____zoe cdupre ____________________
**Name:**_________________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**
For n <= 1, we have the base cases:
W(0) = 1
W(1) = 1

W(n) = W(n - 1) + W(n - 2) + 1

work is O(2^n) since it grows exponentially 
- **3)**
For n <= 1 (base cases):
S(0) = 1
S(1) = 1

S(n) = S(n - 1) + S(n - 2) + O(1)

since the span is determined by the fib num span is O(n)

- **4)**
for count the pattern follows as a small number like 0-3 the count lists how many retirees with a count of 1 saying the fib number is computed once through recursion. The fib numb that is further from the beginning of life will be lower because of less frecency of computing. The pattern shows the recursion nature of the fib sequence in coding and in life and shows the problems leading to repeated calculation numbers, especially for small values in N/
- **6)**

  max time I am called is 2
work - O(n) = because of the number of recursive calls the work is proportional to num of Fibonacci calculated since its linear
span - the span is focused on the recursive call in the tree since the max is 2 for i the span would be O(1) since the tree depth would be n
- **8)**
