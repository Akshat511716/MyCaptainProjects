import csv

def file_into_csv(Student_info):
    csv_file = open("Student_data.csv", mode = 'a', newline = '')
    
    csv_file_write = csv.writer(csv_file)

    if csv_file.tell() == 0:
        csv_file_write = csv_file_write.writerow(["NAME","AGE","CONTACT NUMBER","EMAIL ID"])

    csv_file_write.writerow(Student_info)

    csv_file.close()    

if __name__ == "__main__":

    condition = True

    while(condition):
        Student_info = input("\nENTER THE STUDENT DETAILS (Name  Age  Contact Number  Email Id) : \n\t")

        Student_data = Student_info.split()
        print(f"THE STUDENT DATA : \nNAME : {Student_data[0]} \nAGE : {Student_data[1]} \nCONTACT NUMBER : {Student_data[2]} \nEMAIL ID : {Student_data[3]}")

        conf = input("DO YOU CONFIRM THE STUDENT DATA (yes/no) : " )

        if conf == 'yes':
              file_into_csv(Student_data)
              choice = input("DO YOU WANT TO ENTER ANOTHER STUDENT's DATA (yes/no) : ")
              if choice == 'yes':
                  condition = True
              else:
                  condition = False
        else:
            print("\n!!!ENTER THE STUDENT DATA AGAIN!!!\n ") 
    
    
