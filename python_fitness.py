#################################################################################################################
################## Fitness Tracker - V2 - Patrick Arthur #########################################################



import math
import datetime

from datetime import date, timedelta


today=datetime.date.today()
Lastwk=date.today()-timedelta(days=7)
Week3=date.today()+timedelta(days=7)
Week4=Week3+timedelta(days=7)


###### Measurement variables used for BF,BMI,bmr########

print ("Welcome to the Monthly Fitness Goal Tracker\n")

##### user inputs the change they want to see in a few weeks as goal ######

print ("Add in how much change in body composition in a month in percent\n")
wt_per=input("Weight Percentage: \n")
wt_per2=((int(wt_per)*.01)/4)


### User inputs weight and height for BMI calculations####

sx =input("Select your Sex: M or F\n")
age=input("What is your age in years\n")
wt=input("What is your weight in lbs as of "+str(today)+"\n")
ht=input("What is your height in inches as of "+str(today)+"\n")
wst=input("What is your waist measurement in inches as of "+str(today)+"\n")
nk=input("What is your neck measurement in inches as of "+str(today)+"\n")
hp=input("For Females, what is your hip measurement in inches as of "+str(today)+"\n")

#### creates BMI, BMR and BF and goal per week based on user inputs ######


BMI=(float(wt)/(float(ht)*float(ht)))*703
BMI2=abs((BMI*wt_per2)-BMI)
BMI3=abs((BMI2*wt_per2)-BMI2)
print ("Your BMI is "+str(BMI)+" as of "+str(today)+"\n")
print ("Your BMI is goal is "+str(BMI2)+" as of "+str(Week3)+"\n")
print ("Your BMI is goal is "+str(BMI3)+" as of "+str(Week4)+"\n")

if sx=='M':
    bmr=((66+6.23)*float(wt)+(4.7*float(ht))-(4.7*float(age)))
    bmr2=abs((bmr*wt_per2)-bmr)
    bmr3=abs((bmr2*wt_per2)-bmr2)
    bf=86.010*math.log(float(wst) - float(nk)) - 70.041*math.log(float(ht)) + 36.76
    bf2=abs((bf*wt_per2)-bf)
    bf3=abs((bf2*wt_per2)-bf2)
    print ("Your Daily Caloric Intake is "+str(bmr)+" as of "+str(today)+"\n")
    print ("Your Daily Caloric Intake is "+str(bmr2)+" as of "+str(Week3)+"\n")
    print ("Your Daily Caloric Intake is "+str(bmr3)+" as of "+str(Week4)+"\n")
    print ("Your Body Fat Percentage is "+str(bf)+" as of "+str(today)+"\n")
    print ("Your Body Fat Percentage is "+str(bf2)+" as of "+str(Week3)+"\n")
    print ("Your Body Fat Percentage is "+str(bf3)+" as of "+str(Week4)+"\n")
elif sx=='F':
    bmr=((655+4.35)*float(wt)+(4.7*float(ht))-(4.7*float(age)))
    bmr2=abs((bmr*wt_per2)-bmr)
    bmr3=abs((bmr2*wt_per2)-bmr2)
    bf=163.205*math.log(float(wst) - float(hp) + float(nk)) - 97.684*math.log(float(ht)) - 78.387
    bf2=abs((bf*wt_per2)-bf)
    bf3=abs((bf2*wt_per2)-bf2)
    print ("Your Daily Caloric Intake is "+str(bmr)+" as of "+str(today)+"\n")
    print ("Your Daily Caloric Intake is "+str(bmr2)+" as of "+str(Week3)+"\n")
    print ("Your Daily Caloric Intake is "+str(bmr3)+" as of "+str(Week4)+"\n")
    print ("Your Body Fat Percentage is "+str(bf)+" as of "+str(today)+"\n")
    print ("Your Body Fat Percentage is "+str(bf2)+" as of "+str(Week3)+"\n")
    print ("Your Body Fat Percentage is "+str(bf3)+" as of "+str(Week4)+"\n")
else:
    print ("User did not put in correct information")


##### user adds in exercises for week and program creates goals and inputs in list ######

print ("Please input exercised and performance for week\n")

print ("Add in how much strength and speed you want to increase by end of month\n")

wt_per_ft=input("PR Percentage: \n")
wt_per2_ft=((int(wt_per)*.01)/4)

lis=[]
lis2=[]

def workout(exer,exer2,ls):
         excty=input("Please add "+exer+str(Lastwk)+"\n")
         excty2=input("Please add "+exer2+" as of "+str(Lastwk)+"\n")
         while (excty != ""):
                 ls.append([excty,excty2])
                 input("Press <ENTER> to exit\n")
                 excty=input("Please add "+exer+str(Lastwk)+"\n")
                 excty2=input("Please add "+exer2+" as of "+str(Lastwk)+"\n")
workout("exercises performed as of ","lbs lifted",lis)
workout("miles ran ","time in mins/sec",lis2)

def bodycomp(lss,ex1,ex2):
    for i in lss:
        var3=float(i[1])
        var4=float(i[1])*wt_per2_ft+float(i[1])
        var5=var4*wt_per2+var4
        var6=var5*wt_per2+var5
        var7=i[0]
        print (var7+" Personal Record as of "+str(Lastwk)+" is "+str(var3)+" lbs")
        print ("Your "+var7+" goal for this week is to "+ex1+str(var4)+ex2+str(today))
        print ("Your "+var7+" goal for this week is to "+ex1+str(var5)+ex2+str(Week3))
        print ("Your "+var7+" goal for this week is to "+ex1+str(var6)+ex2+str(Week4))
bodycomp(lis,"lift "," lbs as of ")
bodycomp(lis2,"run "," in min/sec as of")
