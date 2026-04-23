import time
from plyer import notification

#water_quantity = int(input("Enter the amount in ml: "))
water_drank = 0
while True:
    print("Water Drink Reminder")
    notification.notify(
        title = "Water Drink Reminder",
        message = "Drink some water",

        timeout = 2
    )
    water_quantity = int(input("Enter the amount in ml: "))
    if water_quantity >= 0:
        #cur_time = time.time()
        #Next_rem =  cur_time + 3
        water_drank += water_quantity
        print(f"water Drank Today: {water_drank}")
        #display_time = time.localtime(Next_rem)
        #Nextsip = time.strftime("%a, %d %b %Y %H:%M:%S", display_time)
        if water_drank >= 1000:
            print("Enough for today you already drank 1000 ml")
            break
        #while cur_time >= Next_rem:
            print("Drink Next sip ")
        time.sleep(5)
            
        
        

    