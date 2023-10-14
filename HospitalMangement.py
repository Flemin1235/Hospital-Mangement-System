from mysql.connector import *
con=connect(host="localhost",user="root",passwd="flemin12032005",database="HMS")
cur=con.cursor()
#Note:
#ID,Name,Age,Gender,DOB and PhoneNo is indexed same for Doctor,Staff and Patient
def operations(entity): #entity can be Doctor,Staff or Patient as shown in Main Loop
    global d
    print("\n\t==========%s's Data=========="%(entity,))
    print("\tChoose the Desired Option")
    print("\t1.Add A New %s"%(entity,))
    print("\t2.Search For An Existing %s"%(entity,))
    print("\t3.Update Existing %s's Details"%(entity,))
    print("\t4.Remove Existing %s's Details"%(entity,))
    print("\t5.Display All %s of the Hospital"%(entity,))
    print("\t6.Back to Menu")
    d=int(input("Enter Option Number:"))

def update(entity):#used to update details in Doctor or Staff
    i=int(input("Enter %s ID to update his/her details: "%(entity,)))
    cur.execute("SELECT * FROM %s"%(entity,))
    data=cur.fetchall()
    yes=0
    for record in data:
        if record[0]==i:
            yes=1
            print("\tWhat do you want to update?")
            print("\t1.Age")
            print("\t2.Salary")
            k=int(input("Enter Choice Number: "))
            if k==1:
                rn=int(input("\tEnter New Age: "))
                cur.execute("UPDATE %s Set Age=%s WHERE %s_ID=%s"%(entity,rn,entity[0],i))
                print("\t============Age Updated Successfully!!============")
            elif k==2:
                sal=float(input("\tEnter Revised Salary: "))
                cur.execute("UPDATE %s Set Salary=%s WHERE %s_ID=%s"%(entity,sal,entity[0],i))
                print("\t============Salary Updated Successfully!!============")        
            else:
                print("\t============Invalid Choice.Try Again!!============")
            con.commit()
    if yes!=1:
        print("============No %s Registered in Hospital with ID %d"%(entity,i),"!!============")
            
def delete(entity): #entity can be Doctor,Staff or Patient as shown in Main Loop
    t=(entity,entity)
    di=int(input("Enter %s ID to delete %s's Details: "%t))
    cur.execute("SELECT * FROM %s"%(entity,))
    data=cur.fetchall()# collects all records in an entity
    yes=0
    for rec in data:
        if rec[0]==di:
            yes=1
            t=(entity,entity[0],di)
            cur.execute("DELETE FROM %s where %s_ID=%s"%t)
            print("\t============Details Deleted Successfully!!============")
    if yes!=1:
        print("\t============No %s Registered in Hospital with ID %d"%(entity,di),"!!============")

def searchall(entity): #entity can be Doctor,Staff or Patient as shown in Main Loop
    cur.execute("SELECT * FROM %s"%(entity,))
    rec=cur.fetchall()
    if len(rec)==0:
        print("\t============No %s (s)"%(entity,),"!!============")
    else:
        for data in rec:
            print("\tID:",data[0],"\tName:",data[1],"\tGender:",data[3],"\tPhoneNo:",data[7])

#Doctor Table
def doctor():
   while True:
        yes=found=0
        operations("Doctor")
        if d==1:
            i=int(input("Enter Doctor ID: "))
            cur.execute("SELECT * FROM Doctor")
            rec=cur.fetchall()
            for doc in rec:
                if doc[0]==i:
                    found=1
                    print("\t============A Doctor Already Registered with ID",i,"!!============")
            if found!=1:
                name=str(input("Enter Doctor Name: "))
                age=int(input("Enter Age: "))
                gen=str(input("Enter Gender(M/F): "))
                dob=str(input("Enter Date Of Birth(in yyyy-mm-dd): "))
                doj=str(input("Enter Date Of Join(in yyyy-mm-dd): "))
                dept=str(input("Enter Department: "))
                ph=str(input("Enter Phone No(10 digit):  "))
                sal=float(input("Enter Salary: "))
                t=(i,name,age,gen,dob,doj,dept,ph,sal)
                cur.execute("INSERT INTO Doctor values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",t)
                print("\t============Doctor Added Successfully!!============")
                con.commit()
        elif d==2:
            n=int(input("Enter Doctor ID to seacrh his/her details: "))
            cur.execute("SELECT * FROM Doctor")
            found=0
            for doctor in cur:
                if doctor[0]==n:
                    found=1
                    print("\t==========Doctor Found!!==========")
                    print("\tName: ",doctor[1])
                    print("\tAge: ",doctor[2])
                    print("\tGender: ",doctor[3])
                    print("\tDOJ: ",doctor[5])
                    print("\tDepartment: ",doctor[6])
                    print("\tPhoneNo: ",doctor[7])
                    print("\tSalary: ",doctor[8])
            if found!=1:
                print("\t==========No Doctor Registered with ID",n,"!!==========")
        elif d==3:
            update("Doctor")
        elif d==4:
            delete("Doctor")
            con.commit()
        elif d==5:
            searchall("Doctor")
        elif d==6:
            break
        else:
            print("\t==========Invalid Option.Please Try Again!!==========")
        
#Staff Table
def staff():
    while True:
        yes=found=0
        operations("Staff")
        if d==1:
            i=int(input("Enter Staff ID: "))
            cur.execute("SELECT * FROM Staff")
            rec=cur.fetchall()
            for doc in rec:
                if doc[0]==i:
                    found=1
                    print("\t============A Staff Already Registered with ID",i,"!!============")
            if found!=1:
                name=str(input("Enter Staff Name: "))
                age=int(input("Enter Age: "))
                gen=str(input("Enter Gender(M/F): "))
                dob=str(input("Enter Date of Birth(in yyyy-mm-dd): "))
                doj=str(input("Enter Date of Join(in yyyy-mm-dd): "))
                des=str(input("Enter Designation: "))
                ph=str(input("Enter PhoneNo: "))
                sal=float(input("Enter Salary: "))
                t=(i,name,age,gen,dob,doj,des,ph,sal)
                cur.execute("INSERT INTO Staff values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",t)
                print("\t============Staff Added Successfully!!============")
                con.commit()
        elif d==2:
            n=int(input("Enter Staff ID to seacrh his/her details: "))
            cur.execute("SELECT * FROM Staff")
            found=0
            for staff in cur:
                if staff[0]==n:
                       found=1
                       print("\t============Staff Found!!============")
                       print("\tName: ",staff[1])
                       print("\tAge: ",staff[2])
                       print("\tGender: ",staff[3])
                       print("\tDOJ: ",staff[5])
                       print("\tDesignation: ",staff[6])
                       print("\tPhoneNo: ",staff[7])
                       print("\tSalary: ",staff[8])
            if found!=1:
                print("\t============No Staff Registered with ID",n,"!!============")
        elif d==3:
            update("Staff")
        elif d==4:
            delete("Staff")
            con.commit()
        elif d==5:
            searchall("Staff")
        elif d==6:
            break
        else:
            print("\t============Invalid Option.Please Try Again!!============")
        
#Patient Table
def patient():
    while True:
        yes=found=0
        operations("Patient")
        if d==1:
            i=int(input("Enter Patient ID: "))
            cur.execute("SELECT * FROM Patient")
            rec=cur.fetchall()
            for doc in rec:
                if doc[0]==i:
                    found=1
                    print("\t============A Patient Already Registered with ID",i,"!!============")
            if found!=1:
                name=str(input("Enter Patient Name: "))
                age=int(input("Enter Age: "))
                gen=str(input("Enter Gender(M/F): "))
                dob=input("Enter Date Of Birth(in yyyy-mm-dd): ")
                can=float(input("Enter Canteen Fee(if any otherwise 0): "))
                ward=float(input("Enter Ward Fee(if any otherwise 0): "))
                ph=int(input("Enter Phone No(10 digit):  "))
                r=input("Enter Date Registered(in yyyy-mm-dd): ")
                t=(i,name,age,gen,dob,can,ward,ph,r)
                cur.execute("INSERT INTO Patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",t)
                print("\t============Patient Added Successfully!!============")
                con.commit()
        elif d==2:
            n=int(input("Enter Patient ID to seacrh his/her details: "))
            cur.execute("SELECT * FROM Patient")
            found=0
            for patient in cur:
                if patient[0]==n:
                   found=1
                   print("\t============Patient Found!!============")
                   print("\tName: ",patient[1])
                   print("\tAge: ",patient[2])
                   print("\tGender: ",patient[3])
                   print("\tCanteen Fee: ",patient[5])
                   print("\tWard Fee: ",patient[6])
                   print("\tPhoneNo: ",patient[7])
                   print("\tDate Registered: ",patient[8])
            if found!=1:
                print("\t============No Patient Registered with ID",n,"!!============")
        elif d==3:
            i=int(input("Enter Patient ID to update his/her details: "))
            cur.execute("SELECT * FROM Patient")
            data=cur.fetchall()
            found=0
            for rec in data:
                if rec[0]==i:
                    found=1
                    print("What do you want to update?")
                    print("\t1.Age")
                    print("\t2.Canteen Fee")
                    print("\t3.Ward Fee")
                    k=int(input("Enter Choice Number: "))
                    if k==1:
                        age=int(input("\tEnter New Age: "))
                        cur.execute("UPDATE Patient Set Age=%s WHERE P_ID=%s"%(age,i))
                        print("============Age Updated Successfully!!============")
                    elif k==2:
                        can=int(input("\tEnter Revised Canteen Fee: "))
                        cur.execute("UPDATE Patient Set CanFee=%s WHERE P_ID=%s"%(can,i))
                        print("============Canteen Fee Updated Successfully!!============")
                    elif k==3:
                        ward=int(input("\tEnter Revised Ward Fee: "))
                        cur.execute("UPDATE Patient Set WardFee=%s WHERE P_ID=%s"%(ward,i))
                        print("============Ward Fee Updated Successfully!!============")
                    else:
                        print("\t============Invalid Choice.Try Again!!============")
            if found!=1:
                print("\t============No Patient Registered with ID",i,"!!============")
            con.commit()
        elif d==4:
            delete("Patient")
            con.commit()
        elif d==5:
            searchall("Patient")
        elif d==6:
            break
        else:
            print("\t============Invalid Option.Please Try Again!!============")

#Appointments Table
def appointment():
    #Note: A Patient can only make one appointment at a time.
    while True:
        print("\nChoose the Desired Option")
        print("\t1.Schedule Appointment")
        print("\t2.Check Appointment")
        print("\t3.Display All Appointments")
        print("\t4.Cancel Appointment")
        print("\t5.Back to Menu")
        c=int(input("Enter Option Number: "))
        yes=found=present=0
        if c==1:
            i=int(input("Enter Patient ID to Issue Appointment: "))
            cur.execute("SELECT * FROM Appointments")
            data=cur.fetchall()
            for rec in data:
                if rec[0]==i:
                    yes=1
                    print("\t============Patient Already Has An Appointment!!============")
            if yes!=1:
                cur.execute("SELECT * FROM Patient")
                data=cur.fetchall()
                for p in data:
                    if p[0]==i:
                        found=1
                        d=int(input("Enter Doctor ID of Doctor whom Patient wants to meet: "))
                        cur.execute("SELECT * FROM Doctor")
                        data=cur.fetchall()
                        for doc in data:
                            if doc[0]==d:
                                present=1
                                date=str(input("Enter Appointment Date: "))
                                t=(i,d,date)
                                cur.execute("INSERT INTO Appointments  values(%s,%s,%s)",t)
                                print("\t============Appointment Scheduled Successfully!!============")
                        if present!=1:
                            print("\t============No Doctor Registered in Hospital with ID",d,"!!============")
                if found!=1:
                    print("\t============No Patient Registered in Hospital with ID",i,"!!============")
                con.commit()
        elif c==2:
            i=int(input("Enter Patient ID to Check Appointment: "))
            cur.execute("SELECT * FROM Appointments")
            data=cur.fetchall()
            for apt in data:
                if apt[0]==i:
                    yes=1
                    print("\t============Appointment Found!!============")
                    cur.execute("SELECT B.P_ID,B.P_Name,A.D_ID,A.D_Name,C.Appoint_Date FROM Doctor A,\
                                Patient B,Appointments C  where B.P_ID=C.P_ID and A.D_ID=C.D_ID")
                    appoint=cur.fetchall()
                    for rec in appoint:
                        if rec[0]==i:
                            print("\tPatient:",rec[1],"\tDoctor:",rec[3],"\tAppointDate:",rec[4])
                            break
            if yes!=1:
                print("\t============Appointment Not Found!!============")
        elif c==3:
            cur.execute("SELECT * FROM Appointments")
            rec=cur.fetchall()
            if len(rec)==0:
                print("\t============No Appointment(s)!!============")
            else:
                #Using SQL Join
                cur.execute("SELECT B.P_ID,B.P_Name,A.D_ID,A.D_Name,C.Appoint_Date FROM Doctor A,\
                                Patient B,Appointments C where B.P_ID=C.P_ID and A.D_ID=C.D_ID")
                data=cur.fetchall()
                for apt in data:
                    print("\tPatient:",apt[1],"\tDoctor:",apt[3],"\tAppointment:",apt[4])
        elif c==4:
            yes=0
            i=int(input("Enter Patient ID to Cancel Appointment: "))
            cur.execute("SELECT * FROM Appointments")
            data=cur.fetchall()
            for p in data:
                if p[0]==i:
                    yes=1
                    cur.execute("DELETE FROM Appointments where P_ID=%s"%(i,))
                    print("\t============Appointment Cancelled Successfully!!============")
            if yes!=1:
                print("\t============Appointment Not Found!!============")
            con.commit()
        elif c==5:
            break
        else:
            print("\t============Invalid Choice.Please Try Again!!============")
        
#Main Loop

while True:
    doctor()
       

