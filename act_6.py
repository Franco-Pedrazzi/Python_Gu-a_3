nros=[1,2,3,4,5,6,7,8,9]
def lambaMap():
    print(list(map(lambda x: x + 2,nros)))
    print(list(map(lambda y: y **2,nros)))
lambaMap()