class Customers:
    greeting = "Welcome to Coffee House!!"


c_1 = Customers()
c_1.name = "Harold"
c_1.beverage = "Mocha"
c_1.food = "Pizza"
c_1.power = 300

print(Customers.greeting)
print(c_1.beverage)
print(c_1.food)

print(217 * 6)
print(600 + 35234)
print(67 // 12)
print(56329 % 982)
print(34 ** 5)

my_age = 24
mom_age = 61
dad_age = 63

print(mom_age < dad_age and my_age == 24)
print(mom_age == 61)
print(mom_age > 34 or dad_age == 63)
print(mom_age >= 61)
print(not(dad_age <= 400 and my_age == 24))