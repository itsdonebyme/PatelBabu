username=input("What's your username ")

j=0
if username=='admin':
    password=input("What's your password ")
    if password=="abhishek":
        j=1
    else:
        print("Your username or password is incorrect")

print(j)

list_of_clients=[]
n=len(list_of_clients)

if j==1: 
    while n>=0:
        list_of_clients.append(input("Give username and password of principal or exit ").split(" "))
        if list_of_clients[n]=="exitit":
            n=-3
            exit
        else:
            n=n+1

print(list_of_clients)
   
    
    
