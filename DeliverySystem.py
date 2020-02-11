import os
import csv
from datetime import timedelta
import Destination
from Destination import DestinationHashTable
from Package import PackageHashTable
import Graph
import Truck
from Truck import TruckNode
import Package
import ConsoleInterface
import Clock




#
#   FIRST: KEVIN   LAST: MILLER
#   STUDENT ID: 001054056
#








#initalizes hash tables, trucks, and console interface
destination_table = DestinationHashTable()
package_table = PackageHashTable()
the_map = Graph.Graph()
current_time = Clock.Clock()


#imports destinations from destinations.csv and stores them in a hash table - time complexity: O(n)
with open('destinations.csv') as destinations_csv:
    csv_read = csv.reader(destinations_csv)
    for row in csv_read:
        dest = [row for row in csv_read]
        for i in range(len(dest)):
            newdestination = Destination.Destination(dest[i][0],dest[i][1],dest[i][2],dest[i][3],dest[i][4])
            destination_table.insert_into_table(newdestination)

#imports package information from packages.csv and matches it with destination information from the csv, then stores the package in a hash table - time complexity: O(n)
with open('packages.csv') as packages_csv:
       csv_reader = csv.reader(packages_csv)
       for row in csv_reader:  
         ent = [row for row in csv_reader]
         for i in range(len(ent)):
          destin = destination_table.existing_destination(ent[i][1])
          if destin == None:
              print("Unable to add address "+ent[i][1])
          else:
           newparcel = Package.Package(ent[i][0],destin,ent[i][5],ent[i][4],ent[i][6])
           package_table.insert_into_table(newparcel)

#Creates Vertex's for Graph and adds them. Time complexity O(n)
for i in range(1,28):
    the_map.add_vertex(i)

#Adds edges and edge weights to graph from csv. Time complexity O(n^3)
with open('distances.csv') as distances_csv:
    csv_read = csv.reader(distances_csv)
    for row in csv_read:
        matrix = [row for row in csv_read]
        for i in range(len(matrix)):
            for b in range(27):
                the_map.add_undirected_edge(i+1,b+1,matrix[i][b])
#Initializes the two trucks and sets their start times and current locations
hub = destination_table.search_table('4001 South 700 East')
truck1 = Truck.Truck(1,timedelta(hours=8,minutes=00),hub,hub,'truck 1')
truck2 = Truck.Truck(2,timedelta(hours=9,minutes=10),hub,hub,'truck 2')

#First load for truck 1 - leaving at 8:00am
truck1.packages_on_truck.append(package_table.search_table('1'))
truck1.packages_on_truck.append(package_table.search_table('4'))
truck1.packages_on_truck.append(package_table.search_table('7'))
truck1.packages_on_truck.append(package_table.search_table('13'))
truck1.packages_on_truck.append(package_table.search_table('14'))
truck1.packages_on_truck.append(package_table.search_table('15'))
truck1.packages_on_truck.append(package_table.search_table('16'))
truck1.packages_on_truck.append(package_table.search_table('19'))
truck1.packages_on_truck.append(package_table.search_table('20'))
truck1.packages_on_truck.append(package_table.search_table('21'))
truck1.packages_on_truck.append(package_table.search_table('29'))
truck1.packages_on_truck.append(package_table.search_table('31'))
truck1.packages_on_truck.append(package_table.search_table('34'))
truck1.packages_on_truck.append(package_table.search_table('37'))
truck1.packages_on_truck.append(package_table.search_table('40'))

#First load for truck 2 - leaving at 9:10am

truck2.packages_on_truck.append(package_table.search_table('3'))
truck2.packages_on_truck.append(package_table.search_table('5'))
truck2.packages_on_truck.append(package_table.search_table('6'))
truck2.packages_on_truck.append(package_table.search_table('8'))
truck2.packages_on_truck.append(package_table.search_table('9'))
truck2.packages_on_truck.append(package_table.search_table('12'))
truck2.packages_on_truck.append(package_table.search_table('17'))
truck2.packages_on_truck.append(package_table.search_table('18'))
truck2.packages_on_truck.append(package_table.search_table('25'))
truck2.packages_on_truck.append(package_table.search_table('26'))
truck2.packages_on_truck.append(package_table.search_table('30'))
truck2.packages_on_truck.append(package_table.search_table('36'))
truck2.packages_on_truck.append(package_table.search_table('38'))



#Second load - Although it says "truck 1", this load is assigned dynamically, the first truck to complete their first load will get this load. With current load it will be truck 1

truck1.additional_load.append(package_table.search_table('10'))
truck1.additional_load.append(package_table.search_table('11'))
truck1.additional_load.append(package_table.search_table('28'))
truck1.additional_load.append(package_table.search_table('32'))
truck1.additional_load.append(package_table.search_table('2'))
truck1.additional_load.append(package_table.search_table('22'))
truck1.additional_load.append(package_table.search_table('23'))
truck1.additional_load.append(package_table.search_table('24'))
truck1.additional_load.append(package_table.search_table('27'))
truck1.additional_load.append(package_table.search_table('33'))
truck1.additional_load.append(package_table.search_table('35'))
truck1.additional_load.append(package_table.search_table('39'))

#Stores trucks in a self-adjusting binary tree
truck_tree = TruckNode(truck1)
truck_tree.insert(truck2)

#Initates and loads console interface functionality
interface = ConsoleInterface.ConsoleInterface(package_table, destination_table,current_time, truck1,truck2,the_map)
interface.start_console()

#Prints report on total time and mileage after program is exited
print("TRUCK REPORT: ")
print("Truck 1 Total Time: "+str(truck1.total_time))
print("Truck 1 Total Mileage: "+str(truck1.total_miles))
print("Truck 2 Total Time: "+str(truck2.total_time))
print("Truck 2 Total Mileage: "+str(truck2.total_miles))
print("Total Time: "+str(truck1.total_time+truck2.total_time))
print("Total Mileage: "+str(truck1.total_miles+truck2.total_miles))




