def foo_1():
    print('Hello from foo_1()!')
    def foo_2():
        print('Hello from foo_2()!')

    foo_2()

foo_1()