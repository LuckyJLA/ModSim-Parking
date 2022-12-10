import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from colorama import *
import datetime as dt

def init_csv():
    # Function that receives the content of the csv to the global variables
    # After updating the content of csv, calling this function will update the content of the global variables
    # If the function is not called after an update, it will print the values prior to update

    # Make the variables global
    global parkMonitor, lotNum, status
    global parkLogs,prkCount
    
    # Receives the values of the csv
    parkMonitor = pd.read_csv('C:\\Users\\alama\\OneDrive\\Desktop\\ModSim Parking\\Park-Monitor.csv')
    parkLogs = pd.read_csv("C:\\Users\\alama\\OneDrive\\Desktop\\ModSim Parking\\ParkingLogs.csv")

    # np.array(<variable['column name']>) converts to column values to numpy array
    lotNum = np.array(parkMonitor['lot_num']); status = np.array(parkMonitor['available'])
    prkCount = np.array(parkLogs['parked_counter']); 

'''def init_log():
    
    itime = dt.datetime(2022,12,10,6,0,00)
    newLog = pd.DataFrame({'timestamp':[itime],
                                   'lot_num':[None],
                                   'in_out':[None],
                                   'parked_counter':[0]})
    newLog.to_csv("C:\\Users\\alama\\OneDrive\\Desktop\\ModSim Parking\\ParkingLogs.csv", index=False)'''

# Displays the parking lots
def display():
    print("\n                           PARKING LOTS\n")
    for i in range(15):
        # True means available
        if status[i] == True: 
            print(Fore.GREEN,"[",lotNum[i],"]",Fore.RESET, end="     ")
        
        # False means someone already parked    
        elif status[i] == False: 
             print(Fore.RED,"[",lotNum[i],"]",Fore.RESET, end="     ")

        #Creates a new line every 5 values
        if (i+1) % 5 == 0:
            print("\n")
    input() #waits for the the enter key 
    return

#parks a car in the available lot (picks the number by ascending order)        
def park():
    display()
    currentTime = dt.datetime.now()
    
    # There are 15 parking lots
    for i in range(15):

        if status[i] == True:
            # Prints the parking lot number to be given
            print("Parking Lot Number: ", lotNum[i])

            newCount = prkCount[-1]+1
            # Changes the value inside the variable to False
            parkMonitor.iloc[i,1]=False 
            newLog = pd.DataFrame({'timestamp':[currentTime],
                                   'lot_num':[lotNum[i]],
                                   'in_out':[True],
                                   'parked_counter':[newCount]})

            # Updates the values of the csv 
            parkMonitor.to_csv('C:\\Users\\alama\\OneDrive\\Desktop\\ModSim Parking\\Park-Monitor.csv', index=False)

            # mode='a' is append a row
            newLog.to_csv("C:\\Users\\alama\\OneDrive\\Desktop\\ModSim Parking\\ParkingLogs.csv", mode='a', index=False, header=False)
            
            input()
            mainMenu()
    print("No available parking")
    mainMenu()

def unpark():
    display()
    currentTime = dt.datetime.now()
    nprk = input("Parking Lot: ")
    newCount = prkCount[-1]-1
    nprk=int(nprk)

    for i in range(15):
        if lotNum[i] == nprk:
            print("Thank you for parking!!!")
            parkMonitor.iloc[i,1]=True
            newLog = pd.DataFrame({'timestamp':[currentTime],
                                   'lot_num':[lotNum[i]],
                                   'in_out':[False],
                                   'parked_counter':[newCount]})
            parkMonitor.to_csv('C:\\Users\\alama\\OneDrive\\Desktop\\ModSim Parking\\Park-Monitor.csv', index=False)
            newLog.to_csv("C:\\Users\\alama\\OneDrive\\Desktop\\ModSim Parking\\ParkingLogs.csv", mode='a', index=False, header=False)
            input()
            mainMenu()
    print("Parking Lot does not exist")
    mainMenu()

def logs():
    print(parkLogs)
    
    # Just a receiver of input. If not used, another log will be added even there shouldn't be
    x = input()

    mainMenu()


def mainMenu():
    init_csv()
    print(
        "\nMAIN MENU\n"
        "(M) Parking Monitor\n"
        "(P) Park\n"
        "(U) Unpark\n"
        "(L) Parking Logs\n"
        "(E) Exit"
            )
    print("Enter Choice:", end=" "); choice = input()
    
    match choice:
        case 'M':
            display()
            mainMenu()
        case 'P':
            park()
        case 'U':
            unpark()
        case 'L':
            logs()
        case 'E':
            exit()

init_csv()
#init_log()
'''if gagawa ka ulit ng bago or gagawin mong empty yung csv, use this para magkalaman agad
nakacomment sa may taas yung def nito'''
mainMenu()
print(parkLogs)