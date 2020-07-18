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

def foo_bar_2(N):
    for i in range(1,N+1):
        rule = [i % 3 == 0,i % 5 == 0]
        if all(rule):
            print("FooBar")
        elif rule[0]:
            print("Foo")
        elif rule[1]:
            print("Bar")
        else:
            print(i)

# foo_bar_2(100)
foo_bar_2(42)