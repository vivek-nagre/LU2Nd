# # file handling
# writing=open("w.txt",'w')
# writing.write("hello letsupgrader")
# print("file saved")
# writing.close()


# reading=open("w.txt",'r')
# content=reading.read()
# print(content)
# reading.close()

# both=open("w.txt",'r+')
# print(both.read())
# both.write("\ni am good what about you ")
# print(both.read())
# both.close()


# function assignment
lst=[]
def myFunc(fact):
    if fact==0:
        return 1
    else:
        m=fact*fact
        lst.append(m)
        fact-=1
        return lst
print(myFunc(5))
 