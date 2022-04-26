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
