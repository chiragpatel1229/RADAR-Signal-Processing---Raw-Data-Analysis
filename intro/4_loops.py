

# %reset -f

group=["Schwerin","Rostock","Wismar","Stralsund"]


for x in group:
    print(x)


for x in group:
    if x=="Rostock":
        continue     # jump to next iteration 
    print(x)         # "if not", loop continues
    
    
for x in group:
    if x=="Wismar":
        break           # break the loop , no further iteration 
    print(x)            # if conditions not true
    
    
for i in range(0,5):
    if i==3:
        continue
    print(i)


i=0 
while i<5:          # while condition
    if not(i==3):
        print(i)
    i +=1
    


    
    
    
# importing a module/library

import numpy as np    
    
ans=np.empty(21)
print(ans)

ans=np.empty(11)     # NOTE: empty is not empty ! BUT, random or previously existent values !!!
print(ans)

time=np.linspace(0,10,21)

ans=np.empty(21)
print(ans)

i=0
for t in time:
    ans[i]=pow(t,2)     # power
    i+=1
    
print(ans)


