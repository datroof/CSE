import random
honey = 0
holl = 0
my_money = 15
roll_count = 0
while my_money != 0:
   if honey < my_money:
       honey = my_money
       holl = roll_count
   D1 = random.randint(1, 6)
   D2 = random.randint(1, 6)
   Roll = D1 + D2
   #input("Roll the dice.")
   if Roll == 7:
       roll_count += 1
       my_money += 4
       print("You rolled a %s" % Roll)
       print("You have %s dollars." % my_money)
       print("You rolled %s times." % roll_count)
   if Roll != 7:
       roll_count += 1
       my_money -= 1
       print("You rolled a %s" %Roll)
       print("You have %s dollars." %my_money)
       print("You rolled %s times." % roll_count)
print("You lost.")
print("Your highest money was %d" %honey)
print("You earned that on round %d" %holl)






