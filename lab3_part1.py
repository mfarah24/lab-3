def hello():
    print('Hello World')
    print('Inside a Function')
hello()
hello()
hello()

my_stuff = hello()
print('Stuff returned from hello():', my_stuff)
print('The object my_stuff is of type:', type(my_stuff))

def return_text_value():
    name = 'Terry'
    greeting = 'Good Morning ' + name
    return greeting

text = return_text_value()
print(text)

def return_number_value():
    num1 = 10
    num2 = 5
    num3 = num1 + num2
    return num3

number = return_number_value()
print(number)
print(number + 5)
print(return_number_value() + 10)

print('my number is ' + str(number))
print('my number is ' + str(return_number_value()))
