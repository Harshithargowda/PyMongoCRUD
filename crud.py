from pymongo import MongoClient

'''Create a client connection to the MongoDb instance running on the local machine,
client connection is needed to communicate with mongodb'''
#client=MongoClient("localhost:27017")
client = MongoClient('localhost', 27017)
db=client.EmployeesData  #creating the database named EmployeeData in mogodb & storing in variable db
#col=db.Employees #creating collections for the EmployeeData  '''


client = MongoClient("localhost:27017")
db = client.EmployeesData


def main():
    while (1):
        selection = int(input("\n Enter 1 for insert,Enter 2 for Read,Enter 3 for update,Enter 4 for delete:"))
        if selection == 1:
            insert()
            #break
        elif selection == 2:
            read()
            #break
        elif selection == 3:
            update()
            #break
        elif selection == 4:
            delete()
            #break
        else:
            print("\n INVALID SELECTION \n")
            print("Choose the proper selection \n ")


def insert():
    try:
        empid = int(input("Enter Emp ID: \n"))
        empname = input("Enter Emp Name: \n")
        empage = int(input("Enter Emp Age: \n"))
        empsalary = int(input("Enter Emp Salary: \n"))
        empcompany = input("Enter Emp Company: \n")

        db.Employee.insert_one(
            {
                'EmployeeID': empid,
                'EmployeeName': empname,
                'EmployeeAge': empage,
                'EmployeeSalary': empsalary,
                'EmployeeCompany': empcompany,
            }
        )
        print("\n INSERTED SUCCESSFULLY.....!!!! ")
    except ValueError:
        print("ooops!, error occured!")


def read():
    empdata = db.Employee.find()
    for emp in empdata:
        print(emp)
    print("\n Successfully fetched data....!!!")


def update():
    try:
        criteria = int(input('\nEnter id to update\n'))
        empname = input("Enter Emp Name to update: \n")
        empage = int(input("Enter Emp Age to update: \n"))
        empsalary = int(input("Enter Emp Salary to update: \n"))
        empcompany = input("Enter Emp Company to update: \n")

        db.Employees.update_one(
            {"EmployeeID": criteria},
            {
                "$set": {
                    "EmployeeName": empname,
                    "EmployeeAge": empage,
                    "EmployeeSalary": empsalary,
                    "EmployeeCompany": empcompany,
                }
            }
        )
        print("\n RECORDS UPDATED SUCCESSFULLY.....!!!")

    except ValueError:
        print("oops!, Error while updating!...")


def delete():
    try:
        criteria = int(input("\n enter the id to delete the record: "))
        db.Employee.delete_many({'EmployeeID': criteria})
        print("\n Deleted SUCCESSFULLY....!!!")

    except ValueError:
        print("oops!, Error while deleting the record")

if __name__=='__main__':
    main()