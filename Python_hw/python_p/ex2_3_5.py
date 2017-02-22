money = raw_input("Pleae input the shopping money: ")

money = int(money)
#in python the logic unit is "words"
if money >= 100000:
    cost = 0.8
elif (money >= 50000) and (money < 100000):
    cost = 0.85
elif money >= 30000 and money < 50000:
    cost = 0.9
elif money >= 10000 and money < 30000:
    cost = 0.95
else:
    cost = 1
print "The total payment is NT$ %.1f" % (cost * money)
