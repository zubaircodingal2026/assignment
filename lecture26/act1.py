#Encapsulation
class student:
    def __init__(self, name,age,pocketmoney):
        self.name = name
        
        #private variables
        #cant acess directly
        self.__age = age
        self.__pocketmoney = pocketmoney
        
        
    def __printName(self):
        print(self.mame)
        
        
    #getters and setters
    def getAge(self):
        return self.__age
    
    def setAge(self , age):
        self.__age = age
        
    def getPocketMoney(self):
        return self.__PocketMoney
    
    def setPocketMoney(self,pocketmoney):
        self.__pocketmoney = pocketmoney
        
    def getName(self):
        self.__printName
        
if __name__ =="__main__":
    s1 = student("kevin",13,1000)
    print(s1.getName())
    def displayAllDetail():
        print("\nstudent Detail...\n")
        print(s1.getName())
        print(s1.getAge())
        print(s1.getPocketMoney())
        
    displayAllDetail()
    
    
    while True:
        print("\ndo you update the info ?")
        choice = input("Enter yes/no : ")
        if choice not in ['yes','y']:
            break
        
        newAge = int(input("\nEnter new age : "))
        newPocketMoney = newAge = int(input("Enter new PcketMOney : "))
        s1.setAge(newAge)
        s1.setPocketMoney(newPocketMoney)
        displayAllDetail()
        