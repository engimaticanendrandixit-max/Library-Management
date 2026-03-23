import mysql.connector as sqltor                                                                                       #To establish connection between Python and SQL
import time                                                                                                            #For the purpose of creating effect in home page 
con=sqltor.connect(host='localhost',user='enter user as per SQL',password='enter the password here',charset='utf8')
cursor=con.cursor()                                                                                                    #creating an object so that it can be used to carry forward commands to SQL
cursor.execute('create database if not exists student')                                                                # Checking and Creation of database if not exist
cursor.execute('use student')


# This Particular block deals with the creation of BooK Table within the database as created above
# This Table contains the data of the Books that are present within the library
#BOOK TABLE
cursor.execute('''create table if not exists book
(
bookno int,
bookname char(50),
bookauthor char(50),
bookprice int,
status char(10),
qty int
);''')


# This Particular block deals with the creation of Member Table within the database as created above
# This Table contains the data of the members that are connected with the library
#Member Table
cursor.execute('''create table if not exists member
(
memberno int PRIMARY KEY,
membername char(50),
bookno int,
memberstatus char(5),
username char(10),
passwd char(15)
);''')


# This Particular block deals with the creation of Admin Table within the database as created above 
# This table contains information that is for the use of library official 
#Admin Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS admin (
        username VARCHAR(30) NOT NULL,
        password VARCHAR(30) NOT NULL
    )
""")

def divider():
    print("="*110)
    
def center_text(text):
    print("\n" + text.center(100) + "\n")
def fnmno():
    cursor.execute("SELECT memberno FROM member WHERE username = '{}'".format(lgn_username))
    mno= cursor.fetchone()
    mno = mno[0]
    return mno

#This block have all the functions that can be performed on books i.e Addition, deletion ,modification,deletion and display of records related to books
#Thsi particular section Comes under the Admin Panel and these are to be carried by the official personals only
#Book Management
def bookadd():
    #Execute SQL query to insert records in the table newitems
    while True:
        print("Enter the following data")
        bookno=input("Enter the book number:")
        bookname=input("Enter book name:")
        bookauthor=input("Enter author name:")
        bookprice=float(input("Enter book price:"))
        status=input('book is available or not')
        qty=int(input('Enter Quantity of Book'))
        cursor.execute("insert into book values({},'{}','{}',{},'{}',{})".format (bookno, bookname, bookauthor, bookprice, status,qty))
        con.commit() # Stores the data permanently in the table
        ans=input('Do you want to enter more records( y/n)')
        if ans!='y':
            print("\t\t\t~~~~~~~~~BOOK ADDED~~~~~~~~~")
            divider()
            admin_panel()
        
def bookmodify():
    cursor.execute('select * from book')
    rs=cursor.fetchall()
    print("\t\t\t~~~~~~~~~BOOK DETAILS~~~~~~~~~")
    divider()
    print("S.no".ljust(6),"Book Name".ljust(25),"\tAuthor Name".ljust(20),"Price".ljust(5),"Status".ljust(10),'Quantity'.ljust(5),sep="\t")
    divider()
    for row in rs:
        print(row[0],(row[1].center(50)).lstrip(),(row[2].center(30)).lstrip(),row[3],row[4],row[5],sep='\t')
    con.commit()
    sn=int(input('enter book no. to be modified'))
    cursor.execute('select * from book where bookno ={}'.format(sn))
    r=cursor.fetchall()
    for i in r:
        print(i,sep='\t')
    print('what you want to modify')
    print('1.Book number')
    print('2.Book name')
    print('3.Book author')
    print('4.Book price')
    print('5.Book status')
    print('6. Book Quantity')
    print('7.Exit')
    ch=0
    while ch!=6:
        ch=int(input('ENTER YOUR CHOICE'))
        if ch==1:
            bn=int(input('Enter new book number'))
            cursor.execute('update book set bookno={} where bookno={}'.format(bn,sn))
            admin_panel()
        elif ch==2:
            bn=input('Enter new book name')
            cursor.execute("update book set bookname='{}' where bookno={}".format(bn,sn))
            admin_panel()
        elif ch==3:
            bn=input('Enter new book author')
            cursor.execute("update book set bookauthor='{}' where bookno={}".format(bn,sn))
        elif ch==4:
            bn=int(input('Enter new book price'))
            cursor.execute("update book set bookprice={} where bookno={}".format(bn,sn))
            admin_panel()
        elif ch==5:
            bn=input('Enter new book status')
            cursor.execute("update book set status='{}' where bookno={}".format(bn,sn))
            admin_panel()
        elif ch==6:
            bn=input('Enter new book quantity')            
            cursor.execute("update book set qty={} where bookno={}".format(bn,sn))
            admin_panel()
        elif ch==7:
            print('Exitting Program')
            divider()
            break
        else:
            print('Kindly choose appropiate option')
    con.commit()
    admin_panel()
def bookdisplay():
    cursor.execute('select * from book')
    rs=cursor.fetchall()
    print("\t\t\t~~~~~~~~~BOOK DETAILS~~~~~~~~~")
    divider()
    print("S.no".ljust(6),"Book Name".ljust(25),"\tAuthor Name".ljust(20),"Price".ljust(5),"Status".ljust(10),'Quantity'.ljust(5),sep="\t")
    divider()
    for row in rs:
        print(row[0],(row[1].center(50)).lstrip(),(row[2].center(30)).lstrip(),row[3],row[4],row[5],sep='\t')
    con.commit()
    return

def bookdelete():
    bno=int(input('enter book number to be deleted'))
    cursor.execute('delete from book where bookno={}'.format(bno))
    con.commit()
    divider()
    print("\t\t\t~~~~~~~~~BOOK HAVE BEEN DELETED SUCCESSFULLY~~~~~~~~~")
    divider()
    return


#This function is used to count the total no. of members
def chkmno():
    cursor.execute("SELECT MAX(memberno) FROM member")
    fetchedmno = cursor.fetchone()
    cm_mno = fetchedmno[0]  
    if cm_mno is None:
        cm_mno = 0
    next_mno = cm_mno + 1
    return next_mno


#This block have all the functions that can be performed on members i.e Addition, deletion ,modification,deletion and display of records related to the Members
#MEMBER MANAGEMENT
def Memberadd():
    while True:
        print("Enter the following data")
        mname=input("Enter member name:")
        usn=input("Enter username for login: ")
        pwd=input("Enter password for login: ")
        bookno= 0
        mstatus="no"
        mno = chkmno()
        cursor.execute("insert into member values({},'{}',{},'{}','{}','{}')".format (mno, mname, bookno, mstatus, usn, pwd))
        con.commit() 
        print("\t\t\t~~~~~~~~~User Registered Successfully!~~~~~~~~~")
        divider()
        main()

def Membermodify():
    cursor.execute('select * from member')
    rs=cursor.fetchall()
    print("\t\t\t~~~~~~~~~MEMBER DETAILS~~~~~~~~~")
    divider()
    print("Memberno","Member Name","Book no"," Member Status",sep="\t")
    #to modify records of members
    while True:
        ai=int(input('Enter member to be modified'))
        cursor.execute('Select * from member where memberno={}'.format(ai))
        r=cursor.fetchall()
        for i in r:
            print(i[0],i[1]+"\t",i[2],i[3],sep="\t")
        while True:
            print('What do you want to modify')
            print('1. Member name')
            print('2. Book number')
            print('3. Member status')
            print('4. Exit')
            ch=0
            while ch!=5:
                ch=int(input('ENTER YOUR CHOICE'))
                if ch==1:
                    ia=input('Enter new member name')
                    cursor.execute('update member set membername="{}" where memberno={}'.format(ia,ai))
                    center_text('Member name modified successfully!')
                    Membermodify()
                elif ch==2:
                    ia=int(input('Enter new book num ber'))
                    cursor.execute('update member set bookno={} where memberno={}'.format(ia,ai))
                    Membermodify()
                elif ch==3:
                    ia=input('Enter new member status')
                    cursor.execute('update member set memberstatus="{}" where memberno={}'.format(ia,ai))
                    Membermodify()
                elif ch==4:
                    print('Return Back')
                    admin_panel()
                else:
                    print('Kindly choose appropiate option')
        con.commit()
        print("\t\t\t~~~~~~~~~MEMBER MODIFIED~~~~~~~~~")
    divider()
    Membermodify()

#to delete records of member
def Memberdelete():
    cursor.execute('select * from member')
    rs=cursor.fetchall()
    print("\t\t\t~~~~~~~~~MEMBER DETAILS~~~~~~~~~")
    divider()
    print("Memberno","Member Name","Book no"," Member Status",sep="\t")
    mno=int(input('enter member no. to be deleted'))
    cursor.execute('delete from member where memberno = {}'.format(mno))
    con.commit()
    print("\t\t\t~~~~~~~~~MEMBER HAS BEEN DELETED SUCCESSFULLY~~~~~~~~~")
    Membermodify()

#to display member record
def Memberdisplay():
    cursor.execute('select * from member')
    rs=cursor.fetchall()
    print("\t\t\t~~~~~~~~~MEMBER DETAILS~~~~~~~~~")
    divider()
    print("Memberno","Member Name","Book no"," Member Status",sep="\t")
    divider()
    for row in rs:
        print(row[0],row[1],row[2],row[3],sep='\t')
    print('~~~~~~~~~~~~~~~~MEMBER HAS BEEN DISPLAYED~~~~~~~~~~~~~~~~')
    con.commit()
    Membermodify()



#This block would be there in front of the  Admin so that he/she can work upon these functions

def bookmenu():
    center_text("BOOK MANAGEMENT")
    divider()
    print("1. ADD BOOK ")
    print("2. MODIFY BOOK")
    print("3. DISPLAY BOOK")
    print("4. DELETE BOOK")
    print("5. RETURN BACK ")
    divider()
    ch=int(input('enter your choice'))
    if ch==1:
        bookadd()
    elif  ch==2:
         bookmodify()
    elif ch==3:
        bookdisplay()
    elif ch==4:
        bookdelete()
    elif ch==5:
        admin_panel()
    else:
        print('Kindly choose appropiate option')
   
def membermenu():
    center_text("MEMBER MANAGEMENT")
    divider()
    print("1. ADD MEMBER ")
    print("2.  MODIFY MEMBER ")
    print("3. DELETE MEMBER")
    print("4. DISPLAY MEMBERS")
    print("5. EXIT ")
    divider()
    ch=int(input('enter your choice'))
    if ch==1:
        Memberadd()
    elif ch==2:
        Membermodify()
    elif ch==3:
        Memberdelete()
    elif ch==4:
        Memberdisplay()
    elif ch==5:
        print('Exitting from Member menu')
        main()
    else:
        print('Kindly Choice appropiate option')


#This block is related to issuing of the book and contains various functions in order to maintain uniformity with speed and accuracy 
#Issue Book
def Issuebook():
    mno = fnmno()
    flag=0
    bookdisplay()
    cursor.execute('select * from member where memberno={}'.format(mno))
    memrec=cursor.fetchone()
    if memrec[3].upper()=='NO':
            bno=int(input('Enter Book Number:->'))
            cursor.execute('select * from book where bookno={}'.format(bno))
            bookrec=cursor.fetchone()
            if bookrec[0]==bno:
                flag=1
                if  bookrec[4].capitalize()=='Available':
                    print('The Deatails of Book are:->')
                    divider()
                    print(bookrec)
                    cursor.execute("update member set bookno={}, memberstatus='{}' where memberno={}".format(bno,'YES',mno))
                    cursor.execute("update book set qty=qty-1 where bookno={}".format(bno))
                    con.commit()
                    cursor.execute('select * from book where bookno={}'.format(bno))
                    m1=cursor.fetchone()
                    print(m1)
                    if m1[5]>0:
                        print('Book Successfully issued')
                        print('Return book within 1 week of issue date')
                    else:
                        print('Book already issued to someone else')
    else:
        print('Book Already issued')
        print('Return the book')



#Thsi block is to be used when the user returns the particular book he/she has issued and here there is a feature that automatically calculates the fine 
# RETURN BOOK
def Returnbook():
    mno = fnmno()
    cursor.execute('select * from member where memberno={}'.format(mno))
    mrec=cursor.fetchone()
    bno=mrec[2]
    cursor.execute("update member set bookno={},memberstatus='{}' where memberno={}".format(0,'NO',mno))
    cursor.execute("update book set status='{}' , qty=qty+1 where bookno={}".format('Available',bno))
    con.commit()
    days=int(input('Book returned in no. of days'))
    fine=0
    if (days>10):
        fine=(days-10)*2
        print('Deposit fine amount',fine,'rs')
    print('Book successfully returned')
           


def login():
    divider()
    center_text("LOGIN")
    divider()
    global lgn_username
    lgn_username = input("Username: ".ljust(30))
    lgn_password = input("Password: ".ljust(30))

    cursor.execute("SELECT username, passwd FROM member")
    data = cursor.fetchall()
    for i in data:
        if lgn_username == i[0] and lgn_password == i[1]:
            center_text("Login Success!")
            usr_panel()
            return
    
    center_text("Incorrect Username or Password!")
    login()



def usr_panel():
    divider()
    center_text("DASHBOARD")
    divider()
    cursor.execute("SELECT memberno FROM member WHERE username = '{}'".format(lgn_username))
    mno= cursor.fetchone()
    mno = mno[0]
    while True:
        divider()
        print("1. Issue Book".ljust(30))
        print("2. Return Book".ljust(30))
        print("3. Logout".ljust(30))
        divider()

        choice = input("Enter your choice: ".ljust(30))
        if choice == "1":
            Issuebook()
        elif choice == "2":
            Returnbook()
        elif choice == "3":
            center_text("Logged out successfully!")
            main()


def check_or_create_member():
    cursor.execute("SELECT COUNT(*) FROM member")
    data = cursor.fetchone()
    if data[0] > 0:
        login()
    else:
        center_text("No members account found. Firstly Register!")
        memberadd()


def check_or_create_admin():
    cursor.execute("SELECT COUNT(*) FROM admin")
    data = cursor.fetchone()
    if data[0] > 0:
        admin_login()
    else:
        center_text("No admin account found. Creating default admin...")
        default_admin_username = "a"
        default_admin_password = "a"
        cursor.execute("INSERT INTO admin (username, password) VALUES ('{}', '{}')".format(default_admin_username, default_admin_password))
        con.commit()
        center_text("Default Admin Account created successfully!")
        admin_login()




# Admin Login
def admin_login():
    divider()
    center_text("ADMIN LOGIN")
    divider() 
    cursor.execute("SELECT username, password FROM admin")
    data = cursor.fetchall()
    admin_username = input("Admin Username: ".ljust(30))
    admin_password = input("Admin Password: ".ljust(30))
    for i in data:
        if admin_username == i[0] and admin_password == i[1]:  
            center_text("Admin Login Successful!")
            admin_panel()
        else:
            center_text("Invalid Username or password!")
            admin_login()



def admin_panel():
    center_text("ADMIN LIBRARY MANAGEMENT")
    divider()
    print("""
1. BOOK MANAGEMENT
2. MEMBER MANAGEMENT 
3. LOGOUT
    """)
    divider()
    choice = input("Enter your choice: ".ljust(30))
    if choice == "1":
        bookmenu()
    elif choice == "2":
        membermenu()
    elif choice == "3":
        main()
    else:
        print("Invalid choice!!")
        admin_panel()
    

# HomePage

def main():
    divider()
    center_text("HOMEPAGE")
    divider()
    print("""
1. Login 
2. Register Member
3. Admin Login
9. Exit
    """)
    divider()
    choice = input("Enter your choice: ".ljust(30))
    while  choice in ["1","2","3","9"]:
        if choice == "1":
            check_or_create_member()
        elif choice == "2":
            Memberadd()
        elif choice == "3":
            check_or_create_admin()
        elif choice == "9":
            print()
            msg = 'Thanks for using the software'
            for i in msg:  
                print(i,end='',flush=True)
                time.sleep(0.04)
            input("\n\nPress ENTER to exit.".ljust(30))
            exit()
        else:
            print("\nInvalid choice Entered!\n".ljust(30))
            main()



main()
