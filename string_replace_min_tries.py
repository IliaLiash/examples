s = input()
a = input()
b = input()

count = 0

while a in s:
    s = s.replace(a,b)
    count += 1
    
    if count > 1000:
        break
    
if count <= 1000:
    print(count)
else:
    print('Over 1000')     
    
    
    #Find out what is the minimum number of operations in string s there will be no occurrences of string a. 
    #If more than 1000 operations are required, output 'Over 1000'.
