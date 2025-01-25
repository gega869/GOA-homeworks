#name = "gega"
#name არის ცვლადი
surname = "Dolidze"
# = არის ცვლადისთვის მნიშვნელობის მიმნიჭებელი სიმბოლო
# "gega" არის ცვლადისთვის მნიშვნელობა
# print(name)

#პრინტ ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი
name = "Gega" #ეს არის str (sting) ტიპის ცვლადი
age = 11 #ეს არის int (integer) მთელი რიცხვი 
height = 150.5 #ეს არის float ტიპის ცვლადი
#boolean (bool) ტიპი ცვლადი


knows_programming = False #True ან False
is_ugly = False #snakecase(უბრალოდ წერის სტილი სტანდარტულად)
isUgly = False #ჯავასკრიპტული сamelcase
print(name + " " + surname)
#სტრინგი არის ბრჭყალებში მოქცეული სიმბოლოები
#print(name + age)

#print(type(age))
#print(type(name))
#print(type(surname))
#print(type(height))
#print(type(knows_programming))

print(name + " " + str(age))
print(name + " " + surname + " " + str(age) + " " + str(height) + " " + str(knows_programming))
print("Hello, my name is" + " " + name + " " + surname + "." + " " + "I am" + " " + str(age) + " " + "years old" + "." + " " + "I am" + " " + str(height) + " " + "cm in height" + "." + " " + "It is" + " " + str(knows_programming) + " " + "that I know programming" + ".")
print("Hello world")