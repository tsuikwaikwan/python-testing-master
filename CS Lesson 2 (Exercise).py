def what_type_is_this(variable):
    # Let's try debugger
    # print( end='\n') '' is including a default value \n
    print(f'{variable} is ', end='')
    print(f'{type(variable).__name__}')

#Ctrl + / can change the code <> comments
what_type_is_this(42)
what_type_is_this(3.14)
what_type_is_this(42.)
what_type_is_this(1/3)
# // is the floor division - getting the quotient or lower integer, e.g. 12//5 = 2
what_type_is_this(1//3)
what_type_is_this('Coding')
# We need the \ to indicate the special character is not ' of function but is a variable
what_type_is_this('Don\'t panic')
what_type_is_this(1/3*3 == 1)
what_type_is_this(True)
what_type_is_this(1 == 1 + 3 or True)
#Comparing 2 floating point numbers would be problematic due to rounding error in floating format, so usually use <= or >= for comparison
what_type_is_this(0.1 + 0.2 == 0.3)
what_type_is_this(1 < 3 < 4)
# "2==2" and "2 is True"
what_type_is_this(2 == 2 is True)
#It breaks into 2 arguement: 1==2 and 2!=3
what_type_is_this(1 == 2 != 3)
#(1==2) is false and false default value is 0, so 0!=3 returns true
what_type_is_this((1 == 2 )!= 3)
what_type_is_this(1 == (2 != 3))
# False default value is zero and True default value is 1
what_type_is_this(1 == False)
#The "plus" would gives the calculation not an argument
what_type_is_this(1 + True)
#The equal sign would give a statement and the interpretation flows from priority list (+ sign > == > or) and "1 or True" = "bool(num) or True". Shrt
what_type_is_this(-1 + True == True)
a = -1
what_type_is_this(a)
what_type_is_this(abs(a))
a = 'Haha'
what_type_is_this(a)
a = ['Haha', 1]
what_type_is_this(a)
what_type_is_this(abs(a))