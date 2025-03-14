import sqlite3
import pandas as pd

connection = sqlite3.connect('Hospital.db')

cursor = connection.cursor()

while True:
    print('Welcome to J.G Hospital DataBase')
    print('1: Display Patients')
    print('2: Display Doctors')
    print('3: Display Appointments')
    print('4: Display Bills')
    print('5: Display Medial Records')
    print('6: Enter A Patient')
    print('7: Search Patient By ID')
    print('8: Delete Patient')
    print('9: Create Appointment')
    print('10: Create Bill')


    choice = int(input('Please select your choice: '))

    if choice == 1:
        sql = "SELECT * FROM patients"
        cursor.execute(sql)
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns = ['ID','First Name','Last Name','Age','Gender','Contact'])
        print()
        print(df)
        print()


    elif choice == 2:
        sql = "SELECT * FROM doctors"
        cursor.execute(sql)
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns = ['ID','First Name','Last Name','Speciality','Contact'])
        print()
        print(df)
        print()


    elif choice == 3:
        sql = "SELECT * FROM appointments"
        cursor.execute(sql)
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns = ['Appointment ID','Patient ID','Doctor ID','Date','Time'])
        print()
        print(df)
        print()


    elif choice == 4:
        sql = "SELECT * FROM bills"
        cursor.execute(sql)
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns = ['Bill ID','Patient ID','Service','Total Amount','Bill Date'])
        print()
        print(df)
        print()


    elif choice == 5:
        sql = "SELECT * FROM medicalrecords"
        cursor.execute(sql)
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns = ['Record ID','Patient ID','Doctor ID','Diagnosis','Prescription','Date'])
        print()
        print(df)
        print()


    elif choice == 6:
        try:
            print()
            print('Enter Patient Information')
            pat_id = input('Enter ID: ')
            pat_first = input('Enter First Name: ')
            pat_last = input('Enter Last Name: ')
            pat_age = input('Enter Age: ')
            pat_sex = input('Enter Sex: ')
            pat_contact = input('Enter Phone Number: ')
            sql = 'INSERT INTO patients(patient_id, first_name, last_name, age, gender, contact) VALUES (?,?,?,?,?,?)'
            cursor.execute(sql,(pat_id,pat_first,pat_last,pat_age,pat_sex,pat_contact))
            connection.commit()
            print('Patient Added Successfully')
            print()
        except sqlite3.IntegrityError:
             print("Error: This ID already exists. Try Again")
             print()
        except Exception as e:
            print('Error Occured')
            print()

    elif choice == 7:
        print()
        print('Search patient by ID')
        pat_id = input('Enter patients ID: ')
        sql = 'SELECT * FROM patients WHERE patient_id = ?'
        cursor.execute(sql,(pat_id,))
        rows = cursor.fetchall()
        if len(rows) > 0:
            df = pd.DataFrame(rows, columns = ['ID','First Name','Last Name','Age','Gender','Contact'])
            print()
            print(df)
            print()
        else:
            print()
            print('No Patient With ID Found')
            print()


    elif choice == 8:
        print()
        pat_id = input('Enter Patient ID To Delete: ')
        sql = 'DELETE FROM patients WHERE patient_id = ?'
        cursor.execute(sql,(pat_id,))
        connection.commit()
        print('Pateint Has Been Deleted')
        print()

    elif choice == 9:
        try:
            print()
            print('Make an Appointment')
            app_id = input('Enter Appointment ID: ')
            pat_id = input('Enter Patient ID: ')
            doc_id = input('Enter Doctor ID: ')
            date = input('Enter Date (MM/DD/YYYY): ')
            time = input('Enter Time (HH:MM): ')
            pat_contact = input('Enter Phone Number: ')
            sql = 'INSERT INTO appointments(appointment_id,patient_id,doctor_id,appointment_date,appointment_time) VALUES (?,?,?,?,?)'
            cursor.execute(sql,(app_id,pat_id,doc_id,date,time))
            connection.commit()
            print('Appointment Created Successfully')
            print()
        except sqlite3.IntegrityError:
            print("Error: This ID already exists. Try Again")
            print()
        except Exception as e:
            print('Error Occured')
            print()

    elif choice == 10:
        try:
            print()
            print('Make Bill')
            bill_id = input('Enter Bill ID: ')
            pat_id = input('Enter Patient ID: ')
            service = input('Enter Service: ')
            amount = input('Enter Total Amount: ')
            date = input('Enter Bill Date: ')
            sql = 'INSERT INTO bills(bill_id,patient_id,service,total_amount,bill_date) VALUES (?,?,?,?,?)'
            cursor.execute(sql,(bill_id,pat_id,service,amount,date))
            connection.commit()
            print('Billed Added Successfully')
            print()
        except sqlite3.IntegrityError:
             print("Error: This ID already exists. Try Again")
             print()
        except Exception as e:
            print('Error Occured')
            print()


    else:
        print('Invalid Input Entered. Try Again')
        print()

