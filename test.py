from abc import ABC,abstractmethod

class ToDolist(ABC):

    @abstractmethod
    def addtask(self):
        print("task add successfully")

    @abstractmethod
    def viewtask(self):
        print()

    @abstractmethod
    def removetask(self):
        print("task remove successfully")

class SimpleToDolist(ToDolist):
    def addtask(self):
        self.task_list=[]
        count=int(input("how many task you want add?"))
        for name in range(count):
            ToDolist=input("enter task:")
            self.task_list.append(ToDolist)
        return super().addtask()

    def viewtask(self):
        print("\ntasklist")
        for s_no,name in enumerate(self.task_list,1):
            print("{}.{}".format(s_no,name))
        return super().viewtask()

    def removetask(self):
        data=input("which task you want remove?")
        if data in self.task_list:
            self.task_list.remove(data)
            return super().removetask()
        else:
            print("Invaild task")
ToDolist=SimpleToDolist()

while True:
    print("\n")
    print("1.addtask")
    print("2.viewtask")
    print("3.removetask")
    print("4.quit")

    print()
    option=int(input("please enter your option:"))

    if(option==1):
        ToDolist.addtask()
    elif(option==2):
        ToDolist.viewtask()
    elif(option==3):
        ToDolist.removetask()
    else:
        quit()

























