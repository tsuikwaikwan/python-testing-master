# def foo_bar(N):
#     for i in range(1, N + 1):
#         if i % 15 == 0:
#         # same logic check as if i % 3 == 0 and i % 5 == 0:
#             print("FooBar")
#         elif i % 3 == 0:
#             print("Foo")
#         elif i % 5 == 0:
#             print("Bar")
#         else:
#             print(i)

# foo_bar(100)
# foo_bar(42)

def foo_bar_extension(N):
    for i in range(1,N+1):
        # 4 ways of counting: 2^n (pick or not); n!;nCr;nPr
        # Add the string to concat. the string
        # Put Empty string instead of string[] because we want to return string
        string = ""
        if i % 3 == 0:
            string += "aaa"
        if i % 5 == 0:
            string += "bbb"
        if i % 7 == 0:
            string += "ccc"
        if i % 11 == 0:
            string += "ddd"
        if string == "":
            print(i)
        else:
            print(string)

#foo_bar_extension(50)
foo_bar_extension(166)
