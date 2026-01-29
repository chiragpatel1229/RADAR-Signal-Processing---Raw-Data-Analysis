

# %reset -f
 
# operators

# assignment operator

x=43        # integer
x+=1  # x= x+1
x-=1  # x= x-1

# mathematical operator

x=7
y=3

x+y       # add.
x-y       # subtr.
x*y       # multiplication
x/y       # division
x**2      # square
9%2       # modulo (9,2)
9//2      # integer remains  ~ floor(9/2)

x.__add__(2)       # methods to the variable!



# relational operator

3==2
x==7
3!=2    #  ~=
1>2
1>=2
1<2
1<=2


# logical operator

(3==2) or (3==3)
(3==2) and (3==3)

not(False)

# & -> bitwise comparson !!! 


# identity operator
x=42001
y=42004

id(x) == id(y)
x is y 

# in-operator

42 in [1,4,42,52]

# set-operator      pdf s.61

x={1,1,2,2,3,3}
y={2,2,3,3,4,4} 

type(x)

x|y     # included in both
x-y     # subtr. 
x^y     # not within x and y - symmetric difference
x&y     # within x and y - intersection




# string

text='hello'
text2="hello"

'A'+'B'

x=12
y='ABC'

y=y+'D'

type(x)

type(y)




# Function and Methods  (global vs. local) - attributes

# method:
y=y.lower()    # ABC -> Kleinbuchstaben

y=y.upper()

# functions:
print(x)

# attributes



type(y)

y.__class__   # ~ type    -> __ __   "dunder"  "permanent" attributes

y=y.lower     # new assignment of y 

print(y)

# objects

x =42  # name: x, value: 42

id(x)   # location in memory
id(y)

type(x) # type

# > Duck typing   -> type is assumed (int, float,...)






