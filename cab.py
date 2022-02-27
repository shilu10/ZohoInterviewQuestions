# creating a separate class for the taxi's .

class Taxi :
    def __init__(self, name, end_time = 0, cash_earned = 0) :
        
        self.cash_earned = cash_earned
        self.pickedspot = []
        self.customerid = []
        self.droppedspot = []
        self.name = name
        self.end_time = end_time
           
class TaxiBooking :
    
    def __init__(self) :
        self.avaiable_taxis = [ ]
        self.taxi()
        self.points()
               
    # initializing the taxis
    def taxi(self) :
        self.taxi1 = Taxi(name = 'taxi-1', cash_earned = 0)
        self.taxi2 = Taxi(name = 'taxi-2', cash_earned = 0)
        self.taxi3 = Taxi(name = 'taxi-3', cash_earned = 0)
        self.taxi4 = Taxi(name = 'taxi-4', cash_earned = 0)
        self.avaiable_taxis.append(self.taxi1)
        self.avaiable_taxis.append(self.taxi2)
        self.avaiable_taxis.append(self.taxi3)
        self.avaiable_taxis.append(self.taxi4)
        
    # taking care of taxis at the points
    def points(self) :
        self.points_dict = {
            'A' : [self.taxi1, self.taxi2, self.taxi3, self.taxi4],
            'B' : [],
            'C' : [],
            'D' : []
        }
         
    def helperfunction(self, points) :
        does_booked = False
        for point in points :             
            taxis = [i for i in self.points_dict[point]]   
            if len(taxis) >= 1 and does_booked == False :                       
                if taxis[0].end_time <= self.timing :
                    taxis[0].end_time = 0
                    money1 = taxis[0].cash_earned
                    taxiname = taxis[0].name
                    taxi_obj = taxis[0]
                    for taxi in taxis :
                        if (taxi.cash_earned <= money1 and taxi.end_time == 0) :
                            taxi_obj = taxi
                            taxiname = taxi.name
                            booked_at = point
                            does_booked = True
                        else :
                            break
        return does_booked, taxi_obj, booked_at
                      
    # this function is for taxi booking
    def booking(self, customerid,  pickupspot, droppingspot , timing = 11) :
        self.pickupspot = pickupspot 
        self.droppingspot = droppingspot
        self.timing = timing
        self.customerid = customerid     
        if self.pickupspot in self.points_dict :
            if self.pickupspot == 'A' :
                points = ['A', 'B', 'C', 'D']
                does_booked, taxi_obj, booked_at = self.helperfunction(points)
                
            # for point B
            elif self.pickupspot == 'B' :                
                points = ['B', 'A', 'C', 'D']
                does_booked, taxi_obj, booked_at = self.helperfunction(points)            
                    
            # for point C            
            elif self.pickupspot == 'C' :            
                points = ['C', 'B', 'A', 'D']
                does_booked, taxi_obj, booked_at = self.helperfunction(points) 
                              
            # for point D           
            elif self.pickupspot == 'D' :
                points = ['D', 'C', 'B', 'A']            
                does_booked, taxi_obj, booked_at = self.helperfunction(points)
                                 
            if does_booked :
                cash = self.cash_calculation()
                taxi_obj.cash_earned += cash           
                taxi_obj.customerid.append(self.customerid)
                taxi_obj.droppedspot.append(self.droppingspot)
                taxi_obj.pickedspot.append(self.pickupspot)
                taxi_obj.end_time = self.time_to_travel( )+ self.timing                
                self.points_dict[booked_at].remove(taxi_obj)
                self.points_dict[self.droppingspot].append(taxi_obj)
                print(taxi_obj.name, "is been booked")
                print()

            else :
                print("booking rejected")
                print()
               
    #calculating the time to travel   
    def time_to_travel(self) :
        distance = abs(ord(self.pickupspot) - ord(self.droppingspot))
        self.time = distance * 1
        return self.time
        
    # this is for calcaluting cash earned by taxis in a ride   
    def cash_calculation(self) :
        distance = abs(ord(self.pickupspot) - ord(self.droppingspot))
        distance = distance * 15
        self.cash = 100 + ((distance - 5) * 10 )
        return self.cash
      
    def logs(self) :  
        for taxi in self.avaiable_taxis :          
            print(f"-------------{taxi.name}----------------")
            print("CustomerId " + "  " + "TaxiName" + "  " + "PickedSpot" + "  " + "DroppedSpot" + "  " + "TotalCash Earned")
            for i in range(len(taxi.customerid)) :
                print(taxi.customerid[0], "      ",  taxi.name , "     " , taxi.pickedspot[i] , "     " , taxi.droppedspot[i] ,"     " , taxi.cash_earned)
            print()
            print()

   # Running the code 
  taxi = TaxiBooking()
  while True :
    print("1 . booking   2 . details   3. exit")
    choice = int(input("enter your choice : "))
    print()

    if choice == 1 :      
        customerid = int(input("enter your id : "))
        pickupspot = input("enter the pickup spot : ")
        droppingspot = input("enter the drop spot : ")
        timing = int(input("enter the timing : "))
        print()
        taxi.booking(customerid, pickupspot, droppingspot, timing)

    if choice == 2 :
        taxi.logs()
        print()

    if choice == 3 :
        print("ThankYou !!!")
        break
            
