

def args_test(*args):

    print(args)
    print(*args)

    for arg in args:
        print(arg)


def kwargs_test(**kwargs):

    print(kwargs)
    print(*kwargs)

    for kwarg in kwargs:
        print(kwarg, kwargs[kwarg])


args_test("메", "렁", 3, 55, 0.7)

kwargs_test(a="메", b="렁", c=3, d=55, e=0.7)