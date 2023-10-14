#Database and Table Creation
from mysql.connector import *
c=connect(host="localhost",user="root",passwd="flemin12032005")
cur=c.cursor()
cur.execute("create database HMS")
cur.execute("use HMS")

cur.execute("create table Doctor(D_ID int primary key,D_Name varchar(20),Age int,\
                        Gender char(1),DOB date,DOJ date,Department varchar(20),\
                        PhoneNo char(10) unique,Salary int)")
#In Doctor,
#D_ID-->Doctor ID  ,    D_Name-->Doctor Name , DOJ-->Date of Join

cur.execute("create table Staff(S_ID int primary Key,S_Name varchar(30),Age int,\
                       Gender char(1),DOB date,DOJ date,Designation varchar(20),\
                       PhoneNo char(10) unique,Salary int)")
#In Staff,
#S_ID-->Staff ID  ,  S_Name-->Staff Name, DOJ-->Date of Join

cur.execute("create table Patient(P_ID int primary key,P_Name varchar(30),Age int,\
                       Gender char(1),DOB date,CanFee int,WardFee int,\
                       PhoneNo char(10) unique,Registered_Date date)")
                        
#In Patient,
#P_ID-->Patient ID  ,  P_Name-->Patient Name

cur.execute("create table Appointments(P_ID int primary key,D_ID int,Appoint_Date date)")
            
c.commit()
c.close()
print("System Created Successfully!!")
