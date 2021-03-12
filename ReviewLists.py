#LIST PRACTICE
List = ['chelsea', 'brandon', 'ann', 'tim', 'ross','kel', 'tim', 'tim']

#list to string
string= ' '.join(List)
print(string)
string =''
for x in range(len(List)):
    string += List[x] + ' '

print(string,'\n')

#list to tuple
tupleList = tuple(List)
print(tupleList)

tupleList = ()
for x in range (len(List)):
    tupleList += (str(List[x]),)
    
print(tupleList,'\n')

#count occurences
print(List.count('tim'))

count=0
for x in range(len(List)):
    if List[x] == 'tim':
        count +=1
        
print (count,'\n')


#reverse list
reversedList=[]
for x in range (1,len(List)+1):
 
    reversedList.append(List[-x])

print ('Original:\n\t', List)
print ('Reversed List:\n\t', reversedList)

#reverse content and List order
temp=''
FinalList=[]

for x in range (1, len(List)+1): #while the interation value of the is within bounds for list(for loop, 1,len+1)
    for y in range (1,len(List[-x])+1): #   while the new iteration value is within bound for the string(for loop, len)
        temp += List[-x][-y]#concatenate the last alpha varible to the intened reversed string
    FinalList.append(temp)# add the reversed string to the intendend reversed list
    temp='' # wipe temp reverse variable clean for new string
print ('\nOriginal List:\n\t', List)    
print('Reversed List and contents:\n\t',FinalList)
    


#avg List
NumList =[2,3,4,4,4,2,6,6] #31 / 8
num = 0 #set sum counter to 0
for x in range (len(NumList)): # While the iteration is within List range
    num += NumList[x]#add value to the sum counter
avg = num/len(NumList) # divide sum counter by the length of the list

print('\nSum:',num,'\nAvg:',avg)
    
