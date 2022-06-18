class Customers:
    greeting = "Welcome to Coffee Palace!"

    def __init__(self, name, beverage, food, total):
        self.name = name
        self.beverage = beverage
        self.food = food
        self.total = total

c_1 = Customers("Haze", "Espresso", "Pastrami on rye", 220)
c_2 = Customers("Hayden", "Latte", "Donnut", 300)
c_3 = Customers("Hedrick", "Ice coffee", "Pizza", 400)
c_4 = Customers("Hanna", "Caramel", "Lasagna", 500)
c_5 = Customers("Honey", "Iced Tea", "Blueberry pie", 600)

print(Customers.greeting)
print(c_2.name)
print(c_2.beverage)
print(c_2.food)
print(c_2.total)
print(c_5.name)
print(c_5.beverage)
print(c_5.food)
print(c_5.total)


class ClubMembers:
    def __init__(self, name, birthday, age, favorite_food, goal):
      self.name = name
      self.birthday = birthday
      self.age = age
      self.favorite_food = favorite_food
      self.goal = goal

    def display1(self):
          print("Name:", self.name)
          print("Birthday:", self.birthday)
          print("Age:", self.age)
          print("Favorite food:", self.favorite_food)
          print("Goal:", self.goal)

class ClubOfficers(ClubMembers):
# __init__ method of Admin subclass overrides __init___method of User base class

    def __init__(self, name, birthday, age, favorite_food, goal, position):
          self.position = position
          ClubMembers.__init__(self, name, birthday, age, favorite_food, goal)

    def display2(self):
          print("Name:", self.name)
          print("Birthday:", self.birthday)
          print("Age:", self.age)
          print("Favorite food:", self.favorite_food)
          print("Position:", self.position)

m_1 = ClubMembers("Tom", "January 16", 14, "Ice cream", "to be happy")
o_4 = ClubOfficers("Vera", "June 22", 16, "Beef stroganoff", "to be the world's greates chef", "Treasurer")

m_1.display1()
o_4.display2()


