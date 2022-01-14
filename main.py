class hello:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("hello", self.name)
monica=hello("stellah")
monica.display()

class open_gate:
    def __init__(self,name,registeration_number):
        self.name=name
        self.registeration_number=registeration_number
    def choice(self,let_in):
        print("your name is: ",self.name)
        print("\nyour reg no is : ",self.registeration_number)
        print("\n your are allowed in let in id: ",let_in)
student_001=open_gate("stanley",230000)
student_001.choice(1)

#CLASS INHERITANCE
class act_taken(hello):
    def job_allocation(self,name,job):
        print("hello ",name,"your job today is ",job)
worker_001=act_taken(hello)
worker_001.job_allocation("steve","masonry")
worker_001.display()