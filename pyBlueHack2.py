#class libraries for the blueetooth applicatio

import time #<---- class library. 1st

from bluetooth.ble import BeaconService  # <--- thried party module 

service = BeaconService() #<--- creating an instance object of the class library 

service.start_advertising("11111111-2222-3333-44444-5555555555555", 1, 1, 1, 200)#<--- advertide the UUID and different ports for spoofing device

time.sleep(15)
sevice.stop_advertise()

print("Done.")