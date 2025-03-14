class sch:
    que={};i=1000;studet={};stflo={};sfid=2000
    def creatEx(self):
        n=int(input("How many Question To Add:"))
        for i  in range(n):
            ke=input("Enter the Question\n")
            print("Enter the 3 options\n")
            op=[]
            for j in range(3):
                print("Enter the Option:",j+1,end=":")
                op.append(input())
            op.append(input("\nEnter the Answer"))
            self.que[ke]=op
            #print(self.que)
    def stafflog(self):
        while True:
            print("\n\t\t\tSTAFFLOGIN\n\t\t1.signup\n\t\t2.signin\n\t\t3.exit")
            ch=input("Enter Your Option")
            if ch=="1":
                l=[]
                sfname=input("Enter Your Name:")
                sfpas=input("Enter Your Password");l.append(self.sfid);l.append(sfname);l.append(sfpas)
                self.stflo[self.sfid]=l
                print("Your staff Id Is:",self.sfid);self.sfid+=1
                print("\t\t\tSign-Up SuccessFuly")
                #print(self.stflo)
            elif ch=="2":
               try:
                   st=int(input("Enter Your Id:"))
                   pa=input("Enter Your Password:")
                   if st==self.stflo[st][0] and self.stflo[st][2]==pa:
                       print("\t\t\tLogin SuccessFully.....")
                       self.staff()
                   else:
                       print("User Id Or PassWord is Wrong")
               except:
                    print("Invalid Id")
            elif ch=="3":
                break
            else:
                print("enter Correct Option")
    def staff(self):
        while True:
            print("\t\t1.CreateExam\n\t\t2.Approve students\n\t\t3.publish report\n\t\t4.ViewStudents\n\t\t5.exit")
            ch=input("\nEnter the option")
            if(ch=="1"):
              self.creatEx()
            elif ch=="2":
                aid=int(input("Enter the Id for Approve:"))
                try:
                    if aid==self.studet[aid][0]:
                        self.studet[aid][3]=True;self.studet[aid][6]="Approved"
                        print(aid,"Is Approved")
                except:
                    print("Invalid Id")
                    
            elif ch=="3":
                f=True
                for i in self.studet:
                    f=False
                    if len(self.studet)/2<=self.studet[i][5] and self.studet[i][7]=="Not Evaluated":
                        self.studet[i][7]="PASS"
                    elif self.studet[i][7]=="Not Evaluated":
                        self.studet[i][7]="FAIL"
                if(f):
                    print("Exam Not Contect")
                        
            elif ch=="4":
                print("Student Id     StudentName     Approved or Not     Score     Results")
                print("==========     ===========     ===============     =====     ==========")
                with open("studentsdetails.txt",'w') as f1:
                    print("Student Id     StudentName     Approved or Not     Score     Results",file=f1)
                for i in self.studet:
                    print("%-10s     %-11s     %-14s      %-5d     %-7s"%(i,self.studet[i][1],self.studet[i][6],self.studet[i][5],self.studet[i][7]))
                    print("-----------------------------------------------------------------------")
                    with open("studentsdetails.txt",'a') as f:
                        print("%-10s     %-11s     %-14s      %-5d     %-7s"%(i,self.studet[i][1],self.studet[i][6],self.studet[i][5],self.studet[i][7]),file=f)
                print("=======================================================================")
            elif ch=="5":
                break
    def stu(self):
        while True:
            print("\n\t\t\tSTUDENTLOGIN\n\t\t1.signup\n\t\t2.signin\n\t\t3.exit")
            ch=input("enter the Option:")
            if ch=="1":
                l=[]
                stnam=input("Enter your name:")
                stpas=input("Enter Your Password:")
                l.append(self.i);l.append(stnam);l.append(stpas);l.append(False);l.append(False);l.append(0);l.append("Not Approved");l.append("Not attend")
                self.studet[self.i]=l
                print("Your Id is:",self.studet[self.i][0])
                self.i+=1
                #print(self.studet)
            elif ch=="2":
                        
                        id=int(input("Enter Your Id:"))
                        pas=input("Enter Your PassWord:")
                        try:
                           if self.studet[id][2]==pas and self.studet[id][0]==id:
                                 if True==self.studet[id][3]:
                                     print("\t\t\tLogin SuccessFully...")
                                     self.atten(id)
                                     self.studet[id][4]=True
                                 else:
                                     print("Your not Approved")
                           else:
                                print("UserID or PassWord Is Wrong")
                        except:
                            print("Invalid Id")
            elif ch=="3":
                break
    def atten(self,id):
        while True:
                    print("\n\t\t1.AttendExam\n\t\t2.Result\n\t\t3.exit")
                    chs=input("Enter Your Option")
                    if chs=="1":
                        if self.studet[id][7]=="Not attend":
                            c=0
                            print("\n\t\t\ttest started.....\n")
                            self.studet[id][7]="Not Evaluated"
                            for i in self.que:
                                print(i)
                                print("1:",self.que[i][0],"2:",self.que[i][1],"3:",self.que[i][2])
                                ans=input("Enter Your Answer:")
                                if self.que[i][3]==ans:
                                    c+=1
                                    self.studet[id][5]=c
                        else:
                            print("Your Already AttendExam")
                    elif chs=="2":
                        print(self.studet[id][7])
                    elif chs=="3":
                        break
objsch=sch();
print("\t\t\tTHE ")
while True:
    print("\t\t1.Staff\n\t\t2.student\n\t\t3.exit")
    n=input("enter the input:")
    if(n=='1'):
        objsch.stafflog()
    elif n=="2":
        objsch.stu()
    elif n=="3":     
        break
 