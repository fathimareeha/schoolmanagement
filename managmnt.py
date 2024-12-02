class MySchool:
    
    def __init__(self) :
        self.teachers={}
        self.students={}
        self.stdmarks={}
    
    def teacher(self,count,name,subject):
        self.teachers[count]=name,subject
       
        
        
    def addtoteacher(self,count,name,subject):
        self.teachers[count]=name,subject
        
    
    def students(self,count,name,std):
        self.students[count]=name,std
       
    
    def addtostudent(self,count,name,std):
        self.students[count]=name,std
        
        
    def stdmarks(self,count,name,subject,mark):
        self.stdmarks[count]=name,subject,mark
             
        
    def addtomarks(self,count,name,subject,mark):
        self.stdmarks[count]=name,subject,mark
       
    
    def display(self):
        print(self.teachers)
        print(self.students)
        print(self.stdmarks)
        
myobj=MySchool()
myobj.addtoteacher("t1","Reena","Maths")
myobj.addtoteacher("t2","Deepa","Malayalam")
myobj.addtostudent("s1","Reeha",5)
myobj.addtostudent("s2","John","7")
myobj.addtomarks("s1","Ann","English",42)
myobj.addtomarks("s2","John","Science",46)


myobj.display()        
        