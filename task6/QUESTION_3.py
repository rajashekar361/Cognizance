import re                                          
with open('about.txt','r') as file:
    contents =file.read()
    string = re.sub('[^a-zA-Z\d\s]', '', contents)                                                    
    x=string.split()                               #string to list
    print("the words with atleast 6 letters : ") #printing words with len>=6
    for i in range(len(x)):                     
        if len(x[i]) >= 6:                         
            print(x[i])
    
    ans = max(x,key=x.count)                       
    print("Most frequently used word is :",ans) # most frequently used word
    print("frequency : ",x.count(ans))