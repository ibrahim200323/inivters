inivters=int(input("how many user u wanna to invite"))
if(inivters<10):
    for i in range(inivters):
      username=input(f"enter the {i} invitor")
      print(username)
elif(inivters>=10):
    print("too many  persons")
