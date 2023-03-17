#Program by: Leanna Gutierrez & Marco Lee-Shi
#CIS 284-1 Final Project
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from datetime import date
import mysql.connector

#connect to database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="usbw",
  database="driverslicense")

#create cursor to execute sql commands
cursor = db.cursor()

#root creation and also images/icons
root = Tk()
root.title("Belize City Council")
root.geometry("640x800")
root.iconbitmap('C:\\Users\\Marco\\Downloads\\city.ico')
logo = PhotoImage(file = "C:\\Users\\Marco\\Downloads\\council.png")
logolabel = Label(root, image = logo).place(x=30, y=10)


#approve and deny functions
def deny():
    messagebox.showerror("Application Denied", "Your application has been denied")
def approve():
    nam = namebx.get()
    addr = address.get()
    ag = age.get()
    dob = dateobirth.get()
    vehicle = vehiclelist.get(vehiclelist.curselection())
    heit = height.get()
    gen = gender.get()
    licen = license.get()
    countr = country.get()
    pas = passed.get()
    susp = suspend.get()
    passd = passed.get()
    med = medical.get()
    lioff = licenoff.get()
    govoff = governoff.get()
    
    licensestuff = "None"
    countrystuff = "None"
    dateplace = "None"
    
    if gen == 1:
       Sex = "Male"
    elif gen == 2:
       Sex =  "Female"
    elif gen == 3:
       Sex =  "Other"
       
    if licen == TRUE:
        licensestuff = licensebx.get()
        
    if countr == TRUE:
        countrystuff = countrybx.get()
        
    if pas == TRUE:
        dateplace = dptestbx.get()

    
    messagebox.showinfo("Application Approved", message=
                        "Please check if the information below is correct:                                                              \n" +
                        "\nName of Applicant: " + str(nam) + "\nAddress: " + str(addr) + "\nAge: " + str(ag) +
                        "\nDate of Birth: " + str(dob) + "\nHeight: " + str(heit) + "\nGender: " + str(Sex) +                        
                        "\nType of vehicle: " + str(vehicle) + "\n\nLicense issued in Belize: " + str(licen) +
                        "\nNumber, date, office of Issue: " + str(licensestuff) + "\n\nLicense issued in other country: " + str(countr) + 
                        "\nCountry and dateo of license issue: " + str(countrystuff) + "\n\nEver suspended: " + str(susp) + 
                        "\n\nEver Passed driving test: " + str(passd) +  "\nDate and place of test: " + str(dateplace) +
                        "\n\nLast medical check: " + str(med) + "\n\n\nLicensing officer: " + str(lioff) + "\nGovernment Medical Officer: " + str(govoff))
    
    #sql execution part
    cursor.execute("INSERT INTO drivers (name, address, age, DoB, height, vehicle) VALUES('"+ nam +"', '"+ addr +"', '"+ ag +"', '"+ dob +"', '"+ heit +"', '"+ vehicle +"')")
    db.commit()
    print("1 record inserted, ID:", cursor.lastrowid)
    db.disconnect()
    

#functions that enable entry boxes once the check box is ticked
def checkLicense():
    if licensebx['state'] == 'normal':
        licensebx['state'] = 'disabled'
    else:
        licensebx['state'] = 'normal'
def checkCountry():
    if countrybx['state'] == 'normal':
        countrybx['state'] = 'disabled'
    else:
        countrybx['state'] = 'normal'
def checkTest():
    if dptestbx['state'] == 'normal':
        dptestbx['state'] = 'disabled'
    else:
        dptestbx['state'] = 'normal'


#labels for displaying words
today = date.today()
date = today.strftime("%b-%d-%Y")
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
labels = Label(root, text="CITY OF BELIZE", font=("Times New Roman", 15, "bold")).place(x=230, y=25)
labels = Label(root, text="DEPARTMENT OF ENFORCEMENT & TRAFFIC", font=("Times New Roman", 15, "bold")).place(x=100,y=50)
labels = Label(root, text="Application for Drivers License Learners Permit", font=("Times New Roman", 12, "bold")).place(x=150,y=75)
labels = Label(root, text= "Sec. Ref:", font=("Times New Roman", 7)).place(x=500,y=5)
labels = Label(root, text= "Dated:", font=("Times New Roman", 7)).place(x=500,y=20)
labels = Label(root, text= "Document No:", font=("Times New Roman", 7)).place(x=500,y=35)
labels = Label(root, text="Full name of applicant:", font=("Times New Roman", 10)).place(x=30,y=100)
labels = Label(root, text="Address:", font=("Times New Roman", 10)).place(x=30,y=120)
labels = Label(root, text="Age:", font=("Times New Roman", 10)).place(x=125,y=140)
labels = Label(root, text="Date of Birth:", font=("Times New Roman", 10)).place(x=250,y=140)
labels = Label(root, text="Gender:", font=("Times New Roman", 10)).place(x=30,y=190)
labels = Label(root, text="Height:", font=("Times New Roman", 10)).place(x=30,y=160)
labels = Label(root, text="State type of vehicle it is intended to drive", font=("Times New Roman", 10)).place(x=30,y=220)
labels = Label(root, text="Have you ever held a driver's license issued in Belize?", font=("Times New Roman", 10)).place(x=30,y=325)
labels = Label(root, text="If so, state number, date and office of issue:", font=("Times New Roman", 10)).place(x=30,y=350)
labels = Label(root, text="Have you ever held a driver's license issued in any other country?", font=("Times New Roman", 10)).place(x=30,y=400)
labels = Label(root, text="If so, state which country and date of issue of license:", font=("Times New Roman", 10)).place(x=30,y=420)
labels = Label(root, text="Are you, at the time of this application, suspended from driving or disqualified from obtaining a driver's license?", font=("Times New Roman", 10)).place(x=30,y=460)
labels = Label(root, text="Have you ever passed a driving test?", font=("Times New Roman", 10)).place(x=30,y=515)
labels = Label(root, text="If so, state date and place of test:", font=("Times New Roman", 10)).place(x=30,y=535)
labels = Label(root, text="When were you last medically examined for a driver's license?", font=("Times New Roman", 10)).place(x=30,y=580)
labels = Label(root, text="Signature of Applicant", font=("Times New Roman", 10)).place(x=250,y=650)
labels = Label(root, text="Date/Time", font=("Times New Roman", 9)).place(x=100,y=630)
labels = Label(root, text=date + "\n" + str(dt_string), font=("Times New Roman", 9)).place(x=75,y=645)
labels = Label(root, text="Please examine applicant as to his or her \n fitness to hold a driver's license", font=("Times New Roman", 9)).place(x=30,y=680)
labels = Label(root, text="I certify that the physique, vision, hearing and \n bodily and mental fitness of", font=("Times New Roman", 9)).place(x=410,y=630)
labels = Label(root, text="are such as to qualify him/her to hold a driver's license.", font=("Times New Roman", 7)).place(x=420,y=680)
labels = Label(root, text="Licensing Officer", font=("Times New Roman italic", 8)).place(x=80,y=731)
labels = Label(root, text="Government Medical Officer", font=("Times New Roman italic", 8)).place(x=453,y=715)

#entry boxes
namebx = Entry(root)
address = Entry(root)
age = Entry(root)
dateobirth = Entry(root)
height = Entry(root)
secref = Entry(root, font=("Times New Roman", 7))
officedate = Entry(root, font=("Times New Roman", 7))
docnum = Entry(root, font=("Times New Roman", 7))
licensebx = Entry(root, state=DISABLED)
countrybx = Entry(root, state=DISABLED)
dptestbx = Entry(root, state=DISABLED)
medical = Entry(root)
applicant = Entry(root)
licenoff = Entry(root)
driver = Entry(root)
governoff = Entry(root)

#entry box .place()
namebx.place(x=160, y=100, width=300)
address.place(x=160, y=120, width=300)
age.place(x=160, y=140, width=50)
dateobirth.place(x=335, y=140, width=125)
height.place(x=160, y=160)
secref.place(x=560, y=5, height=15, width=75)
officedate.place(x=560, y=20, height=15, width=75)
docnum.place(x=560, y=35, height=15, width=75)
licensebx.place(x=30, y=370, width=450)
countrybx.place(x=30, y=440, width=450)
dptestbx.place(x=30, y=555, width=450)
medical.place(x=30, y=600, width = 450)
applicant.place(x=460, y=665)
licenoff.place(x=65, y=715)
driver.place(x=250, y=670)
governoff.place(x=460, y=700)

#radio buttons for gender
gender = IntVar()
male = Radiobutton(root, text="Male", variable=gender, value=1).place(x=75, y=190)
female = Radiobutton(root, text="Female", variable=gender, value=2).place(x=125, y=190)
other = Radiobutton(root, text="Other", variable=gender, value=3).place(x=190, y=190)
gender.set(3) #preselected to other

#listbox for types of vehicles
vehiclelist = Listbox(root, exportselection=0, height=4)
for carlist in [ "Private Motor Vehicle", "Motorcycle", "Public Service", "Goods Vehicle"]:
    vehiclelist.insert(END, carlist)
vehiclelist.place(x=30, y=240)
vehiclelist.select_set(0) #preselected to Private Motor Vehicle

#checkbuttons for yes no options
license = BooleanVar()
country = BooleanVar()
suspend = BooleanVar()
passed = BooleanVar()
licenseck = Checkbutton(root, text="Tick for Yes",variable=license, onvalue=TRUE, offvalue=FALSE, command=checkLicense).place(x=325, y=324)
countryck = Checkbutton(root, text="Tick for Yes",variable=country, onvalue=TRUE, offvalue=FALSE, command=checkCountry).place(x=390, y=399)
suspendck = Checkbutton(root, text="Tick for Yes",variable=suspend, onvalue=TRUE, offvalue=FALSE,).place(x=30, y=479)
passedck = Checkbutton(root, text="Tick for Yes",variable=passed, onvalue=TRUE, offvalue=FALSE, command=checkTest).place(x=225, y=514)

#buttons to approve or deny
approve = Button(root, text="Approve", command=approve) .place(x=250, y=750)
deny = Button(root, text="Deny", command=deny) .place(x=310, y=750)

root.mainloop()