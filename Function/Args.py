# Arguments, when you do not know the no of arguments. General practice is to write 'args' but can be anything. '*' important.
# It is passed as tuple. Like tuple properties, it can be any type list,tuple,int,float etc.


def add(*args):
    print(args)


add(12, 13, 14)  # Print arguments

# use of kwargs ,it is dictionary.Passed with **.  Can be used to pass, multiple data with key values or hwere dict is used
# var can be anything but kwargs is std conevtions
# def (*args,**kwargs) , def(**kwargs)


def add(**kwargs):
    print(kwargs)


add(name="sushant", age=30, gender="Male")

# Named parameter follows sequence, in below example n1 and n2 sequence is important and no of arguments can't be less or more


def add(n1, n2):
    print(n1 + n2)


# default arguments takes default value if not passed


def add(n1, n2=20):
    print(n1 + n2)


add(10)
