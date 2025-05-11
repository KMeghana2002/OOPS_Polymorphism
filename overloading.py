class sample():
    def m1(self,num1,num2):
        print(num1*num2)
    def m1(self,num1,num2,num3):
        print(num1*num2*num3)
    def m1(self,num1,num2,num3,num4):
        print(num1*num2*num3*num4)
obj=sample()
obj.m1(2,2,2,2)
obj.m1(2,2,2)#it will give error because it will take lateset one
