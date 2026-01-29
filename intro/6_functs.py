
# reset -f

# functions

def myFunction():        # dummy function, just doing nothing
    pass

myFunction()



def myFunction(x,y):
    out = x+y
    return out

x=myFunction(4,8)       # mathematically sum

myFunction('F','A')     # adding strings



def myFunction(x,y):    
    return x,y

z=myFunction(4,8)       # generation of a tupel as only one variable (z) is requested/defined
x=z[0];
y=z[1];


a,b = myFunction(1,2)   # results are stored in individual variables 


# pre-definition

def myFunction(x=1,y=0):    # x and y are pre-defined
    out=x+y
    return out

z=myFunction()              # function may be called without parameters/values handed over to the function

z=myFunction(x=23,y=11)




# not allowed:

#def myFunction(x=0,y):
#    out=x+y
#    return out

# allowed:

def myFunction(y,x=10):      # predefined variables/values always at the end!
    out=x+y
    return out

z=myFunction(12)

z=myFunction(12,11)


x=42;

def myFunction():
    print(x)
    
myFunction()



#  ->  global variable is used - function is not isolated in the memory -> beware of similar variable names


def myFunction():
    x=21
    print(x)
    
myFunction()

#  ->  local variable is used

# ???

def myFunction():
    global x
    print(x)
    
myFunction()
#

locals()

globals()      #-> dict
dir()      

globals().keys()


# %reset -f

#    args   kwargs

def myFunction(x,y):
    out=x+y
    return out

myFunction(3,4)


# unknown number of input values


def myFunction(x):
    out=sum(x)
    return out

myFunction([1,2,3])


# or ->   args     arguments

# 1. provide a list instead of keyword argument
# 2. process a flexible number of values


def myFunction(x,*args):   # all elements assigned to args are as   a tuple
    print(x)
    print(args)            # tupel args
    print(*args)           # tupel > list
    out=sum([x, *args])    #  sum need the list
    return out


myFunction(42)

myFunction(1,2,7,5)

myFunction(*(1,2,3))       # submit values as tuple


#    kwargs   
# 1. higher flexibility than   args
# 2. specify the function by a dictionary

def myFunction(x,y):
    out=x**y   
    return out


myFunction(*(4,2))

myFunction(**{'y':2,'x':3})    # kwargs


# reset -f

def myFunction(x=[1,2,3],y=0):
    x.append(y)
    return x

z=myFunction(y=20)

# y will be added to x with every iteration/ function call



def myFunction(x=None,y=0):
    if x == None:
        x=[1,2,3]
    x.append(y)
    return x

myFunction(y=42)

# x is not growing


def myFunction(x):
    if isinstance(x,str):
        raise TypeError('Do provide an int - not a string')
    if x==42:
        raise ValueError('ok')
    out=x**2
    return out

myFunction('A')

myFunction(40)

myFunction(42)



def myFunction(x):
    try:
        if isinstance(x,str):
            raise TypeError('Do provide an int - not a string')

        if x==42:
            raise ValueError('ok')

        out=x**2
        return out
    
    except TypeError:
        return('there was a type error')

    except ValueError:
        return('there was a value error')

myFunction('A')

myFunction(42)

myFunction(40)




