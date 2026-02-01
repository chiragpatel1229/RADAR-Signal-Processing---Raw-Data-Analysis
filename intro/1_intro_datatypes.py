

# > datatypes

# int, float 
x= 42

y=53.223

x= 1_000_000

x=2 
x=4/2     # float !!!
x=int(4/2)

# what kind of data type is x ?
type(x)



# strings 

str1="helllooooo"
print(str1)
str1="Hello 'guys'"
print(str1)
print(x)

# formatted string
str2="""hello,
all"""

print(str2)


# strings are sequences

len(str2)    # length of a string

str2[0]     # data selection, index starts at 0 !
str2[2]
str2[6]
str2[2:5]   # : slicing operator position "3" to "5"

str1[:]
str1[:4]

str2[::2]   # steps

str2[::-1]   # index order reversed
str2[::-2]

str2[10:2:-1]  # pos 10...2


# reset -f 

# integer + string

x=2             # integer
y=2.02          # float
z='3'           # string


print(str(x)+z) # 23
type(str(x)+z)

print(x+int(z)) # 5







# string injection - string.format

kk=20
'select * from tbl where y == {}'.format(kk)

'select * from {} where y == {}'.format('clients',42)

'select * from {1} where y == {0}'.format(42,'clients')


# f-strings

table='clients'
value=42

f'select * from {table} where y == {value}'




# number injection
'lucky number is: {0}'.format(0.24363645)

'lucky number is: {0:5.4f}'.format(160.24363645)



# string methods

x ='ABc'

x.capitalize()   # first letter of string in capital
x.lower()        # all in lower case 
x.upper()       # all in upper case
x
x2=x.split('B')




# bool 
x=False    # bools are stored as logical 0, 1 -> num!
y=True

            # how may we "proof" this ?
sum([x])
sum([y])

type(x)
type(y)
type(x+y)    # bool + bool = int -> math. operation


# none 

x=None    # only exists ones! though different variable names
y=None    # ~= NaN !    nan -> math, numpy


        # where is the data stored?
id(x)     
id(y)   
        # -> same physical location for x and y !
x=2
y=128
id(x)     
id(y)   


# list  [container-objects]
# literal initiation
x=[1,2,3]
y=['A','B','C']
z=[1,'b',[1,2,4]]

z2=z[2]


# vectorization

x=[34,20,15]
2019-x      # not allowed in pure python -> numpy !

2019-x[0]  # but, possible with sequencial calcualtion by e.g. for-loop


x =[1,2,3]

y=x*2   # multiplication? 


#    copying lists 

# reset -f

x=5         # integer
id(x)
y=x
id(y)

x =[1,2,3]  # list

id(x)
y=x
id(y)


x.append(99)    #  x & y are modified - list is not copied, 
                #  just name added to the same physical space
                #  x and y are ONE object
                #  memory efficient - to avoid multiple equal lists! 

id(x)
id(y)

# handling CBR

x =[1,2,3]    

y=x

y= x.copy()     #  copy list into new physical space
id(x)
id(y)

x.append(99)

# or

# reset -f

x =[1,2,3]

x 
x[:]

y=x[:]

id(x)
id(y)           # different spaces !



# attribute functions   

x=[1,2,3]

x.count(3)      # number of "3" presence

x.append(3)

x.count(3)


# tuple 

x=(1,2,3)

x=('A','B','C')

x=(1,'A',(1,2,3,))     # tuple - immutable object - cannot be changed, needs to be copied

x[1]='Z'

x[2]


# reset -f

# dictionary :  ->   key/name - value - pair

x={'Paul':3,'Klaus':5,'Finn':4}
x['Klaus']

# generate a dictionary from list/tuple

lonlat=[9.453,23.432]   # geographic coordinates 
x={lonlat: 42}      # measurement value    
                    # not allowed - unhashable - list not an tuple


lonlat=(9.453,23.432)   # geographic coordinates 
x={lonlat: 42}         # measurement value    
                    #  allowed for tuple - hashable

# -- clear()

# set 

x={1,1,2,2,3,3}  # NOTE:  sets are not shown in older Spyder, eventually PyCharm or others...
                # Python 3.7 / Spyder v4 does show it now!
type(x)

y={2,2,3,3,4,4}


x.intersection(y)

x.union(y)

x.difference(y)  # difference of one set to the other - single perspective
y.difference(x)

x.symmetric_difference(y)  # symmetric - "total" difference of one set to the other



# frozenset   - compare  list - tuple    set - frozenset

x=frozenset([1,2,2,1,4,5,3])      # it's like a function used to genereate a frozen list...

type(x)

print(x)

# does x exist, is it defined?
'x' in globals()




# type conversion

x='42'

int('42')
type(int(x))

str(42)

bool(0)

x=(1,2,3)
y=list(x)
type(list(x))

tuple([1,2,3])
x=[('A',1),('B',2),('C',3)]
y=dict(x)

x=[1,2,3,4,4]
y=set(x)




# assign new values
# list , tuple

x=[1,2,3]

x[0]=42

x[0:2]=[9,77]


# dictionary
x={'Paul':3,'Klaus':5,'Finn':4}
x['Lucia']=6                        # adding of a new key-value-pair (=item) as key does not exist
x['Paul']=4                         # modifying of an existing key

x.update({'Lucia':7})               # modifying

y= x.keys()

type(y)

x.values()
x.items()

list(y)



c={'m':7,'n':8} # dictionary
print(c['m'])   # 7




t=[1,3,"car",4,6.7]
t[2]

t[2][1]

t[2][1:3]
t[2][1:]
t[1:]



