

# %reset -f

# control structures

age=17

if age <16:
    print("you're not allowed to drive here unless you're drugged up!")
    print('a')
elif(age>=16) and (age<18):
    print("you're allowed to drive with companion")
else:
    print("have a good ride...")
    

# conditional expression

num=31
if(num % 2)==0:     # modulo , division remainder
    print('div')
else:
    print("not div")
    
# ->
    
'div' if (num % 2) == 0 else 'not div'


