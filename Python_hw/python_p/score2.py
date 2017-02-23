score = total = 0;
score_data = []
while(True):
    score = int(raw_input("Please enter the student's score, enter -1 to end the function: "))
    if score == -1:
        break
    else:
        score_data.append(score)

for i in range(0,len(score_data)):
    total += score_data[i]

print "The total score in the class is %5d" % total
print "The average score in the class is %5.2f!" % (float(total)/len(score_data))
