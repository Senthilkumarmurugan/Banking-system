import sys
import random
import pyodbc
class bank:


    bname="Indian Bank"


    @staticmethod
    def deposit():

        deposit=float(input("Enter the amount to deposit:"))
        query="update cus_accountinfo set balance=balance+{} where accountno={}"
        cursor.execute(query.format(deposit,c1.accountno))
        conn.commit()
        print("amount successfully deposited")
        dep="update cus_accountinfo set deposit=? where accountno=?"
        cursor.execute(dep,(deposit,c1.accountno))
        conn.commit()



    @staticmethod
    def withdraw():
        withdraw=float(input("Enter the amount to withdraw:"))
        balance=[]
        query="select balance from cus_accountinfo where accountno={}"
        cursor.execute(query.format(c1.accountno))
        row = cursor.fetchone()
        while row:
            print(balance.append(row[0]))
            row = cursor.fetchone()
        if(withdraw<balance[0]):
            query="update cus_accountinfo set balance=balance-{} where accountno={}"
            cursor.execute(query.format(withdraw,c1.accountno))
            conn.commit()
            print("amount withdrawed successfully")
            withdrawamount="update cus_accountinfo set withdraw=? where accountno=?"
            cursor.execute(withdrawamount,(withdraw,c1.accountno))
            conn.commit()
        else:
            print("insufficient fund")


    @staticmethod
    def showbalance():
        query="select balance from cus_accountinfo where accountno={}"
        cursor.execute(query.format(c1.accountno))
        row = cursor.fetchone()
        while row:
            print("Your balance is:%d" % (row[0]))
            row = cursor.fetchone()

    @staticmethod
    def showpin():
        pin=random.randint(1000,9999)
        query="select pin from cus_accountinfo where accountno=?"
        cursor.execute(query,(c1.accountno))
        row = cursor.fetchone()
        while row:
            print("Your pin is:%d" % (row[0]))
            row = cursor.fetchone()


    def changeATMpin(self):
        self.newpin=int(input("Enter the new pin:"))
        self.conpin=int(input("Re-enter the pin:"))
        if(self.newpin==self.conpin):
            query="update cus_accountinfo set pin={} where accountno={}"
            cursor.execute(query.format(self.newpin,c1.accountno))
            conn.commit()

            print("Pin changed succesfully")
        else:
            print("Pin not match")
    @staticmethod
    def cusinfo():
        query='''select cus_info.accountno,cus_info.name,cus_info.phone,cus_info.address,cus_info.password,
        cus_accountinfo.balance,cus_accountinfo.pin from cus_info inner join cus_accountinfo 
        on cus_info.accountno=cus_accountinfo.accountno 
        where cus_info.accountno=%d and cus_accountinfo.accountno=%d'''
        cursor.execute(query%(c1.accountno,c1.accountno))
        row = cursor.fetchone()
        while row:
            print("Accountno:{} \nName:{}\nPhone:{}\nAddress:{}\nPassword:{}\nBalance:{}\nPin:{}".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
            row = cursor.fetchone()



    def newregistration(self):

        while True:
            self.accountno=random.randint(100000000,999999999)
            # self.accountno=int(input("Enter your account no:"))
            self.name=input("Enter your name:")

            self.phone=int(input("Enter your phone no:"))
            self.address=input("Enter your address:")
            self.password=input("Enter your password:")
            self.conpassword=input("Re-enter your password:")
            if(self.password==self.conpassword):
                query="insert into cus_info values (?,?,?,?,?)"
                cursor.execute(query,(self.accountno,self.name,self.phone,self.address,self.password))
                conn.commit()
                print("your account is successfully added")
                print("your acount number is ",self.accountno)

                print('record insterted successfully')
            else:
                print("Password not matching")

            self.pin=random.randint(1000,9999)
            quer="insert into cus_accountinfo (accountno,pin) values (%d,%d)"
            cursor.execute(quer%(self.accountno,self.pin))
            conn.commit()


            option=input('do you want insert another record--yes/no:')
            if(option=='no'):
                break
            else:
                c1.newregistration()
            return c1

    def existing_user(self):
        # cursor=conn.cursor()
        try:
            self.accountno=int(input("Enter your accountno:"))
            self.password=input("Enter your password:")
            query="select * from cus_info where accountno=? and password=?"
            logincheck = cursor.execute(query ,(self.accountno,self.password))
            # if logincheck == None:
            #     print("Sorry, could not find you in the database\nOr it just isn't working")
            # else:
            #     print("Successfully loaded {} from the database".format(self.accountno))
            result=cursor.fetchall()
            if result:
                for i in result:
                    print("Welcome ",i[1])
                    while True:
                        print("B---->Show balance\nD---->deposit\nW---->Withdraw\nP---->Pin\nCP---->Change ATM pin\nI---->Customer info\nE---->Exit")
                        option=input("Enter the option:")
                        if(option.upper()=='D'):
                            c1.deposit()
                        elif(option.upper()=='W'):
                            c1.withdraw()
                        elif(option.upper()=='E'):
                            print("Thanks for using Indian Bank")
                            sys.exit()
                        elif(option.upper()=='B'):
                            c1.showbalance()
                        elif(option.upper()=='CP'):
                            c1.changeATMpin()
                        elif(option.upper()=='P'):
                            c1.showpin()
                        elif(option.upper()=='I'):
                            c1.cusinfo()
                        else:
                            print("Invalid option")

            else:
                print("Accountno and Password not match Try again....")
        except ValueError:
            print("Accountno must be in numeric")
    # @staticmethod
    # def deposit():
    #     query="select from "
c1=bank()


try:
    conn = pyodbc.connect('''Driver={SQL Server};
                          Server=SENTHILKUMARMUR;
                          Database=bank_database;
                          Trusted_Connection=yes;
                          ''')
    print("connected successfully......")
    cursor = conn.cursor()
    print("Welcome to ",bank.bname)

    while True:
        print("E---->Existing user\nN---->New registration\nC---->Exit")
        option=input("Enter the option:")
        if(option.upper()=='E'):
            c1.existing_user()
        elif(option.upper()=='N'):
            c1.newregistration()
        elif(option.upper()=='c'):
            sys.exit()
        else:
            print("not a valid option")

except pyodbc.OperationalError:
    print("Database connection failed....")
except pyodbc.ProgrammingError:
    print("Database not found....")




