#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 14:11:18 2019

@author: paulschwetlick
"""
def read_bills():
    """Reads bills from results.csv"""
    bills = []
    for line in open("results.csv"):
        bill = line.split(',')
        bills.append(bill)
        
    #sorts bills by date
    bills.sort(key=(lambda b: b[4]))
    bills.sort(key=(lambda b: b[3]))
    bills.sort(key=(lambda b: b[2]))
    return bills
    
def write_bills(bills):
     """Writes bills to results.csv"""
     bill_list = open("results.csv", "w")
     for bill in bills:
        bill_list.write(", ".join(bill))
     bill_list.close()
     
def read_bills_text():
    """Reads bills from textfile"""
    bills = []
    for line in open("bills.txt"):
        bill = line.split(',')
        bills.append(bill)
    return bills

def write_bills_text():
    """Writes bills to textfile"""
    bill_list = open("bills.txt", "w")
    for bill in bills:
        bill_list.write(", ".join(bill))
    bill_list.close()
    
def split_bills(bills):
    """gives list of credits and list of debits"""
    
    
def add_bill(bills):
    """adds a new bill to fleet"""
    new_bill = list()
    # get utility company
    company = str(input("Enter the utility company: "))
    new_bill.append(company)    
    
    # get customer name
    name = str(input("Enter the customer name: "))
    new_bill.append(name)
    
    # get date
    date = str(input("Enter the date of the bill (YYYY,MM,DD): "))
    date_ =date.split(',')
    new_bill.extend(date_)
    
    # get amount
    amount = str(input("Enter the amount of the bill (123.45): "))
    new_bill.append(amount)
    
    # get if debit or credit
    print("Please Choose for your bill: \n1. Debit\n2. Credit")
    while True:
        choice = input("Please choose option 1 or 2: ")
        if choice == "1" or choice == "2":
            break
    if choice == "1":
            new_bill.append("debit\n")
    else:
            new_bill.append("credit\n")
    # add new bill to other bills
    bills.append(new_bill)
    return bills
    
    print("Your new bill has been added.")

def provide_report():
    print("Please choose the type of report you want.\n")
    print("1. show total amount of debit and credit for each year\n\n2. show most popular utility company\
          \n\n3. show bills ordered by date\n\n4. show bill with highest debit and credit\n\
          \n5. Check success of a company\n\n6. check average spent\n\n7. show average time between bills\n\n8. back to menu ")

    choice = input("Please choose option: ")
   
    while choice != '8':
        if choice == "1":
            report_1()
        elif choice == "2":
            report_2()
        elif choice == "3":
            report_3()
        elif choice == "4":
            report_4()
        elif choice == "5":
            report_5()
        elif choice == "6":
            report_6()
        elif choice == "7":
            report_7()
            
        else:
            print("Invalid Option")
        print("1. enter new bill\n\n2. provide report\n\n3. text file\n\n4. Quit")
        choice = input("Please choose option: ")
    
#def report_1():
        

def report_2():
    """shows most popular utility company"""
    

def report_3():
    """shows bills in date order"""
    
    print(bills)
def report_4():
    """shows highest debit and credit"""
    
def report_5():
    """checks company performance"""
    
def report_6():
    """checks average spent"""
    
def report_7():
    """shows average time between bills"""
    #newest date
    newest_bill = bills
    
    date_new = bill[0]
    #oldest date
    date_old = 
    #number of bills
    number_bills = len(bills)


def use_textfile():
    print("\nPlease choose:\n\n1. read bills from textfile\n\n2. write bills to textfile")
    while True:
        choice = input("\nPlease choose option 1 or 2: ")
        if choice == "1" or choice == "2":
            break
    if choice == "1":
            bills = read_bills_text()
            return bills
    else: 
            write_bills_text()  
    
    
bills = read_bills()

print("Welcome to the Dublin Bill Management Company's bill management tool.\n")
print("1. enter new bill\n\n2. provide report\n\n3. text file\n\n4. Quit")

choice = input("Please choose option: ")

while choice != '4':
    if choice == "1":
        bills = add_bill(bills)
    elif choice == "2":
        provide_report()
    elif choice == "3":
        use_textfile()
    else:
        print("Invalid Option")
    print("\n1. enter new bill\n\n2. provide report\n\n3. text file\n\n4. Quit")
    choice = input("Please choose option: ")

write_bills(bills)
print("Goodbye")


