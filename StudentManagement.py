import mysql.connector

# mydb =mysql.connector.connect(
#     host ="localhost",
#     user="root",
#     password=""
    
# )
# cursor =mydb.cursor()
# cursor.execute("create database studentmanagement")



mydb =mysql.connector.connect(
    host ="localhost",
    user ="root",
    password="",
    db ="studentmanagement"
)

cursor =mydb.cursor()

cursor.execute("create table info(roll int ,name varchar(50),address varchar(80),branch varchar(20),division varchar(10),mob int(15))")



# INSERT STUDENT DATA
def insert(roll,name,address,branch,division,mob):
    sql="insert into info(roll,name,address,branch,division,mob) values(%s,%s,%s,%s,%s,%s)"
    value =(roll,name,address,branch,division,mob)
    cursor.execute(sql,value)
    mydb.commit()

# DISPLAY STUDENT DATA
def display():
    sql ="select * from info"
    cursor.execute(sql)
    for x in cursor:
        print("|{:>10}|{:>20}|{:>20}|{:>10}|{:>20}|{:>20}|".format(x[0],x[1],x[2],x[3],x[4],x[5]))

# UPDATE FUNCTION
def update():    
    while(True):
        print("_"*55)
        print("*"*55)
        print("1.Roll")
        print("2.Name")
        print("3.Branch")
        print("4.Division")
        print("5.Address")
        print("6.Mobile Number")
        print("7.Exit")
        print("_"*55)
        print("*"*55)
        ch =input("What do you want to Update:")


        if(ch=="1"):
            roll_O =input("Enter the old roll")
            roll_U =input("Enter the new roll")
            sql ="update info SET roll = %s  where roll =%s"
            # value =(roll_O,roll_U)
            cursor.execute(sql,(roll_U,roll_O))
            mydb.commit()

        elif(ch=="2"):
            name_n= input("Enter The New name :")
            roll =input("Enter the Roll :")
            sql ="update info SET name = %s  where roll =%s"
            cursor.execute(sql,(name_n,roll))
            mydb.commit()
            print("Name successfully change ",name_n)

        elif(ch=="3"):
            branch_n =input("Enter The Branch")
            roll =input("Enter the Roll :")
            sql ="update info SET branch = %s  where roll =%s"
            cursor.execute(sql,(branch_n,roll))
            mydb.commit()
            print("Name successfully change ",branch_n)
        elif(ch=="4"):
            div =input("Enter The Division")
            roll =input("Enter the Roll :")
            sql ="update info SET division = %s  where roll =%s"
            cursor.execute(sql,(div,roll))
            mydb.commit()
            print("Name successfully change ",div)
            
        elif(ch=="5"):
            address =input("Enter The Adress")
            roll =input("Enter the Roll :")
            sql ="update info SET address = %s  where roll =%s"
            cursor.execute(sql,(address,roll))
            mydb.commit()
            print("Name successfully change ",address)
        elif(ch=="6"):
            Mob =input("Enter The Mobile NO")
            roll =input("Enter the Roll :")
            sql ="update info SET mob = %s  where roll =%s"
            cursor.execute(sql,(Mob,roll))
            mydb.commit()
            print("Name successfully change ",Mob)
        elif(ch=="7"):
            break

# DELETE FUNCTION
def delete():
    roll_n = input("Enter the roll")
    sql = "DELETE FROM info WHERE roll = %s"
    val = (roll_n,)
    cursor.execute(sql, val)
    mydb.commit()
    print("Record deleted successfully.")

# SEARCH FUNCTION
def search():
    while True:
        
        print("_"*55)
        print("1. Search by Roll Number :")
        print("2. Search by Name :")
        print("3. Search by Branch :")
        print("4. Search by Mobile :")
        print("5. Exit")
        print("_"*55)
        print("*"*55)
        ch = input("Choose a search option: ")

        if ch == "1":
            roll_to_search = input("Enter the Roll Number to search: ")
            sql = "SELECT * FROM info WHERE roll = %s"
            cursor.execute(sql, (roll_to_search,))
            result = cursor.fetchone()
            if result:
                print("Student found:")
                print("|{:>10}|{:>20}|{:>20}|{:>10}|{:>20}|{:>20}|".format("Roll", "Name", "Address", "Branch", "Division", "Mobile No"))
                print("|{:>10}|{:>20}|{:>20}|{:>10}|{:>20}|{:>20}|".format(result[0], result[1], result[2], result[3], result[4], result[5]))
            else:
                print("Student with Roll Number {} not found.".format(roll_to_search))

        elif ch == "2":
            name_to_search = input("Enter the Roll Number to search: ")
            sql = "SELECT * FROM info WHERE name = %s"
            cursor.execute(sql, (name_to_search,))
            result = cursor.fetchone()
            if result:
                print("Student found:")
                print("|{:>10}|{:>20}|{:>20}|{:>10}|{:>20}|{:>20}|".format("Roll", "Name", "Address", "Branch", "Division", "Mobile No"))
                print("|{:>10}|{:>20}|{:>20}|{:>10}|{:>20}|{:>20}|".format(result[0], result[1], result[2], result[3], result[4], result[5]))
            else:
                print("Student with N   ame {} not found.".format(name_to_search))
            
            
        elif ch == "3":
            branch_to_search = input("Enter the branch  to search: ")
            sql = "SELECT * FROM info WHERE branch = %s"
            cursor.execute(sql, (branch_to_search,))
            result = cursor.fetchone()
            if result:
                print("Student found:")
                print("|{:>10}|{:>20}|{:>20}|{:>10}|{:>20}|{:>20}|".format("Roll", "Name", "Address", "Branch", "Division", "Mobile No"))
                print("|{:>10}|{:>20}|{:>20}|{:>10}|{:>20}|{:>20}|".format(result[0], result[1], result[2], result[3], result[4], result[5]))
            else:
                print("Student with Branch {} not found.".format(branch_to_search))

        elif ch == "4":
            mobile_to_search = input("Enter the Mobile Number  to search: ")
            sql = "SELECT * FROM info WHERE mob = %s"
            cursor.execute(sql, (mobile_to_search,))
            result = cursor.fetchone()
            if result:
                print("Student found:")
                print("|{:>10}|{:>20}|{:>20}|{:>10}|{:>20}|{:>20}|".format("Roll", "Name", "Address", "Branch", "Division", "Mobile No"))
                print("|{:>10}|{:>20}|{:>20}|{:>10}|{:>20}|{:>20}|".format(result[0], result[1], result[2], result[3], result[4], result[5]))
            else:
                print("Student with Mobile Number {} not found.".format(mobile_to_search))
        elif ch == "5":
            break


# MAIN PROGRAM
while(True):
    print("_"*100)
    print("\n\t\t\t\tSTUDENT MANAGEMENT SYSTEM")
    print("_"*100)
    print("1.Add Student")
    print("2.Display Student List")
    print("3.Update Student details")
    print("4.Delete student")
    print("5.Search student ")
    print("6.EXIT")
    print("__"*55)
    ch =input("Enter the choice :")
    if(ch=="1"):
        roll=int(input("Enter the Roll Number"))
        name=input("Enter The Name :")
        branch=input("Enter the Branch :")
        division=input("Enter the Division :")
        mob =input("Enter the Mobile N0 :")
        address=input("Enter the address :")
        insert(roll,name,address,branch,division,mob)
    
    elif(ch=="2"):
        print("__"*55)
        print("{:>10}{:>20}{:>20}{:>10}{:>20}{:>20}".format("Roll","Name","Address","Branch","Division","Mobile No"))
        # print("**"*55)
        print("**"*55)
        display()
        # print("\n\n")
        print("**"*55)
    elif(ch=="3"):
        update()
    
    elif(ch=="4"):
        delete()
    
    elif(ch=="5"):
        search()
    elif(ch=="6"):
        break

mydb.close()

    


