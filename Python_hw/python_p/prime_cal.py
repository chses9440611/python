import math
num = int(raw_input("Please enter the number: "))
if num == 2 :
    print "2 is a prime."
else:
    for i in range(2, int(math.sqrt(num)) +1 ):
        if num % i == 0:
            print "%d is not prime" % num
            break
    else:
        print "%d is a prime." % num

