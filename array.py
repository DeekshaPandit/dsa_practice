1) Write a program to print maximum and minimum elements of the input array A of size N where you have to take integer N and other N elements as input from the user.

def main():
   min = None
   max = None
   arr = []
   val = input()
   numbers = val.split(' ')
   for i in numbers:
       val = int(i)
       if min == None or min > val:
           min = val
       if max == None or max < val:
           max = val

   print("{0} {1}".format(max, min))
   return 0

if __name__ == '__main__':
    main()
      
      
 2) You are given an integer T (number of test cases). You are given array A and an integer B for each test case. You have to tell whether B is present in array A or not.

contraints:
   
1 <= T <= 10
1 <= |A| <= 105
1 <= A[i], B <= 109

example input 1:
 1 
 5 4 1 5 9 1
 5
      
      def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    testcases = int(input())
    for i in range(testcases):
       arr = list(map(int,input().split()))

       val = int(input())
       output = 0
       if arr:
           for j in arr:
               if(val==j):
                   output = 1
            
           print(output)
       else:
           print(output)


if __name__ == '__main__':
    main()
