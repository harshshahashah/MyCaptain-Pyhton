import csv

def write_into_csv(detail_list):
    with open('Student_Details.csv', 'a', newline = '') as csv_file:
        add = csv.writer(csv_file)

        if csv_file.tell() == 0:
            add.writerow(["Name", "Age" , "Contact Number" , "E-mail ID"])

        add.writerow(detail_list)

if __name__ == '__main__':
    proceed = True
    Sr_No = 1

    while(proceed):
        student_detail = input("Enter details for Student #{} in the following format (Name Age Contact_Number E-mail_ID) : ".format(Sr_No))

        student_detail_list = student_detail.split(" ")

        print("\nThe entered information is -\nName : {}\nAge : {}\nContact Number : {}\nEmail-ID : {}".format(student_detail_list[0], student_detail_list[1], student_detail_list[2], student_detail_list[3]))

        confirm = input("Is the entered information correct? (Yes/No) : ")

        if confirm == "Yes":
            write_into_csv(student_detail_list)

            proceed_check = input("Enter details of another student? (Yes/No) : ")
            if proceed_check == "Yes":
                proceed = True
                Sr_No = Sr_No + 1
            elif proceed_check == "No":
                proceed = False

            elif confirm == "No":
                print("\nPlease re-enter the correct details : ")
