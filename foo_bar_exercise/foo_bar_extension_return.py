def string_of_multiple(number):
    multiples = [3,5,7,11,13]
    parts = ["aaa","bbb","ccc","ddd","eee"]
    string = ""
    for i in range(len(multiples)):
        if number % multiples [i] == 0:
            string += parts[i]
        # return is important to output something for other functions to use it
        # also good to break the logic
        return string

def foo_bar_extension(N):
    for i in range(1,N+1):
        string = string_of_multiple(i)
        if string == "":
            print(i)
        else:
            print(string)

#foo_bar_extension(50)
foo_bar_extension(166)
