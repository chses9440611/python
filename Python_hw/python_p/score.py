total = person = score = 0
while(True):
    person += 1
    score = int(raw_input("Please enter the %d student's score, enter -1 to end the function: " % person))
    if score == -1:
        break
    total += score
person -= 1
average = float(total) / person
print "The total score in the class is %5d" % total
print "The average score in the class is %5.2f!" % average
