import Package
import Destination
import Graph
from datetime import timedelta

class Truck:
    #additional_load = []
    avg_speed = 18
    capacity = 16
    #total_miles = float(0)
    

    def __init__(self, truck_number, start_time, current_location, hub, name):
        self.truck_number = truck_number
        self.start_time = start_time
        self.current_location = current_location
        self.hub = hub
        self.name = name
        self.packages_on_truck = []
        self.next_destination = None
        self.total_miles = float(0)
        self.total_time = timedelta()
        self.additional_load = []


  #This is where the simulation of deliveries takes place. The following block of code will call upon the core algorithm graph.closest_address located in the graph class to set the next destination.
  #Upon arrival the code will check for all packages destined for the current_location and remove them from the load and set the package status as delivered. If a truck is empty, it will return to the hub and check for a second load.
  #The first truck to arrive at the hub will receive the additional load.
    def start_deliveries(self,clock,graph):
        operating_time = clock.time - self.start_time
        timer_minutes= float(operating_time.seconds/60)
        #next_up is assigned to the closest destination that is in the truck's current load. It uses dijkstra's algorithm(located in the Graph Class) to find the closest destination.
        next_up = graph.closest_address(self.current_location, self.packages_on_truck)
        distance = graph.edge_weights[int(self.current_location.destination_id),int(next_up.destination_id)]
        time_for_delivery = timedelta(minutes=float(float(distance)/float(self.avg_speed)*60))
        int_delivery_time = float(time_for_delivery.seconds/60)
        #Checks againt the set time to simulate which deliveries would have completed in the set timeframe. Time complexity O(1)
        while timer_minutes > int_delivery_time:
                self.current_location = next_up
                self.total_miles = self.total_miles + float(distance)
                self.total_time = self.total_time + time_for_delivery
                timer_minutes = timer_minutes - int_delivery_time
                delivery_time = self.start_time + self.total_time
                
                i=0
                #Checks all packages in the current load to see if they belong to the current location. Time complexity O(n)
                while i < len(self.packages_on_truck):
                    if self.packages_on_truck[i].destination.destination_id == self.current_location.destination_id:
                        self.packages_on_truck[i].delivery_status = "delivered at: "+str(delivery_time)+" by "+self.name
                        self.packages_on_truck.pop(i)
                      
                    else:
                     i = i+1
                #Checks if current load has been delivered, if so, it sends the truck back to the hub. Once there, if there is an addition load waiting, it picks it up and starts delivering. TIme complexity O(1)
                if len(self.packages_on_truck) < 1:
                  if self.current_location != self.hub:
                    next_up = self.hub
                    distance = graph.edge_weights[int(self.current_location.destination_id),int(next_up.destination_id)]
                    time_for_delivery = timedelta(minutes=float(distance)/float(self.avg_speed)*60)
                    int_delivery_time = float(time_for_delivery.seconds/60)
                  else:
                      if len(self.additional_load) > 0:
                          self.packages_on_truck = self.additional_load
                         
                      else:
                          timer_minutes = -1
                          break

                else:
                 next_up = graph.closest_address(self.current_location, self.packages_on_truck)
                 distance = graph.edge_weights[int(self.current_location.destination_id),int(next_up.destination_id)]
                 time_for_delivery = timedelta(minutes=float(distance)/float(self.avg_speed)*60)
                 int_delivery_time = float(time_for_delivery.seconds/60)
                 
class TruckNode:

    def __init__(self, truck):

        self.left = None
        self.right = None
        self.truck = truck

# This inserts trucks into the tree by truck number. Time complexity O(n)
    def insert(self, truck):

        if self.truck:
            if truck.truck_number < self.truck.truck_number:
                if self.left is None:
                    self.left = TruckNode(truck)
                else:
                    self.left.insert(truck)
            elif truck.truck_number > self.truck.truck_number:
                if self.right is None:
                    self.right = TruckNode(truck)
                else:
                    self.right.insert(truck)
        else:
            self.truck = truck
# This searches the tree for truck number. Time complexity O(n)
    def findnum(self, number):
        if number < self.truck.truck_number:
            if self.left is None:
                return str(number)+" Not Found"
            return self.left.findnum(number)
        elif number > self.truck.truck_number:
            if self.right is None:
                return str(number)+" Not Found"
            return self.right.findnum(number)
        else:
            print(str(self.truck.truck_number) + ' is found')
# Prints truck tree. time complexity O(n)
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.truck.truck_number),
        if self.right:
            self.right.PrintTree()