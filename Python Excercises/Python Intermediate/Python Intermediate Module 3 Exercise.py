f = open("pythonessay.txt", "w")
f.write("I like Python because it's very interesting.")
f = open("pythonessay.txt", "a")
f.write("\nI plan to lear data visualization.")
f.write("\ni want to work in the field of data science.")
f.write("\nI plan to make a beeter world for the furture geneeration.")
f = open("pythonessay.txt", "r")
f.close()


f = open("pythonessay.txt", "r")
print(f.read())
print(f.readline())
f = open("pythonessay.txt", "r")
for x in f:
    print(x)
import os
if os.path.exists("pythonessay.txt"):
  os.remove("pythonessay.txt")
else:
  print("the file does not exist")

x = 500
if x > 100:
  raise Exception("This code will result in an error if x is bigger than 100.")

try:
  print(variable_1)

except:
  print("variable_1 is not yet defined")

for i in range(6):
  print("I'm so happy!")

try:
  print(12 * 6)
except:
  print("this operation can't be performed.")
else:
  print("This operation can be performed.")

best_burger = "Burger King"
number_2_burger = "McDonald's"

assert best_burger == "Burger King"
assert best_burger == "McDonald's"