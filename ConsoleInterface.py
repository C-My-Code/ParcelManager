import Package
from Package import PackageHashTable
import Destination
from Destination import DestinationHashTable
import os
import Clock
from datetime import timedelta

class ConsoleInterface:
     def __init__(self, package_table, destination_table, clock,truck1,truck2,map):
          self.package_table = package_table
          self.destination_table = destination_table
          self.current_time = clock
          self.truck1 = truck1
          self.truck2 = truck2
          self.map = map
 #Home screen of console 
     def start_console(self):
        os.system("cls")
        print("                                 WGU")
        print("                     Package Management System\n\n")
        print("1. View/Update existing package ")
        print("2. Status of all packages ")
        print("3. Simulate Time\n")
        print("*No Input or Invalid Input = Exit")
        print("MILEAGE REPORT PRINTS UPON PROPER EXIT")
        selection = input("Select a number followed by ENTER: ")
        if selection == '1':
            self.update_package_ID_request()
        if selection == '2':
            self.status_of_all()
        if selection == '3':
            self.sim_time()


#This load the screen that requests the ID number of the package you wish to view and calls the next screen.
     def update_package_ID_request(self):
            os.system("cls")
            print("                                WGU")
            print("                     Package Management System\n\n")
            print("VIEW/UPDATE PACKAGE \n\n")
            print("*Invalid Input = Back\n\n")
            package_id_input = input("Enter Package ID Number:")
            package = self.package_table.search_table(package_id_input)
            if package != None:
                self.update_package(package)
            else:
                self.start_console()

#This loads the package information view and gives you the options to update the address of the selected package.
     def update_package(self, package):
          os.system("cls")
          print("                                WGU")
          print("                     Package Management System\n\n")
          print(" VIEW/UPDATE PACKAGE\n\n")
          print("Package ID: "+package.id_number)
          print("Package Deadline: "+package.deadline)
          print("Package Status: "+package.delivery_status)
          print("Package Weight: "+package.package_weight)
          print("Special Notes: "+package.special_note)
          print("\nDestination:")
          print("Name: "+package.destination.business_name)
          print("Street Address: "+package.destination.street_address)
          print("City: "+package.destination.city)
          print("Zip: "+package.destination.zip+"\n")
          if package.delivery_status != "delivered":
            selection = input("Enter 1 to Update Destination, or enter any other key to return: ")
            if selection != '1':
                 self.start_console()
            if selection == '1':
                  print("\n\nPlease enter new street address\nInput must be an exact address match")
                  address_input = input("*Example: '410 S State St' :  ")
                  new_destination = self.destination_table.search_table(address_input)
                  if new_destination != None:
                    package.destination = new_destination
                    input("Update successful press any key to return to main screen")
                    self.start_console()
                  if new_destination == None:
                      input("Address not valid, press enter to return")
                      self.update_package(package)
          else:
              selection = input("Press any key to return to main screen")
              self.start_console()

#This loads and prints the status of all packages. Time complexity O(n)
     def status_of_all(self):
          os.system("cls")
          print("                                WGU")
          print("                     Package Management System\n\n")
          print("PACKAGE STATUS REPORT\n\n")
          print("Current Time "+str(self.current_time.time)+"\n")
          for i in range(1,41):
              s = str(i)
              package = self.package_table.search_table(s)
              print("Package ID:"+package.id_number+"  Destination: "+package.destination.street_address+" "+package.destination.city+"  Deadline: "+package.deadline+"  Status: "+package.delivery_status+"\n")
          input("press any key to return")
          self.start_console()


#This loads the screen giving you the option to select which time you would like to simulate to and starts the deliveries. 
     def sim_time(self):
           os.system("cls")
           print("                                WGU")
           print("                     Package Management System\n\n")
           print("Choose time: ")
           print("1. 9:25am")
           print("2. 10:20am")
           print("3. 12:00pm")
           print("4. End of day(5:00pm)")
           selection = input("Enter a number and press enter: ")
           if selection == '1':
               
               self.current_time.time = timedelta(hours=9,minutes=25)
               self.truck1.start_deliveries(self.current_time, self.map)
               self.truck2.start_deliveries(self.current_time, self.map)
               print("Time changed to 9:25am, all reports will now reflect this time")
    
               input("press enter to return")
               self.start_console()
           if selection == '2':
               
               self.current_time.time = timedelta(hours=10,minutes=20)
               self.truck1.start_deliveries(self.current_time, self.map)
               self.truck2.start_deliveries(self.current_time, self.map)
               print("Time changed to 10:20am, all reports will now reflect this time")
               input("press enter to return")
               self.start_console()
           if selection == '3':
               
               self.current_time.time = timedelta(hours=12,minutes=0)
               self.truck1.start_deliveries(self.current_time, self.map)
               self.truck2.start_deliveries(self.current_time, self.map)
               print("Time changed to 12:00pm, all reports will now reflect this time")
               input("press enter to return")
               self.start_console()
           if selection == '4':
               
               self.current_time.time = timedelta(hours=17,minutes=0)
               self.truck1.start_deliveries(self.current_time, self.map)
               self.truck2.start_deliveries(self.current_time, self.map)
               print("Time changed to 5:00pm, all reports will now reflect this time")
               input("press enter to return")
               self.start_console()
           else:
               self.start_console()

