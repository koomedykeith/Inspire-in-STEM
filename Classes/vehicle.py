class vehicle:
    def __init__(car, max_speed, mileage) :
        car.max_speed = max_speed
        car.mileage = mileage

    def v_details(car):
        print('The car has a maximum speed of ' + car.max_speed + ' and its mileage is '+ car.mileage + ' p per mile')
Toyota = vehicle(str(220),str(100))  
Toyota.v_details()
print(Toyota.max_speed,Toyota.mileage)

Mitsubishi = vehicle(str(210),str(80))  
Mitsubishi.v_details()


Suzuki = vehicle(str(180),str(1150))  
Suzuki.v_details()




