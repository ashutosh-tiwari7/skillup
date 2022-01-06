class skillup():
    def create_slots(x):
        if type(x) == int :
            slot_array = [0] * x
            return slot_array
        else :
            return False 

    def park_user(x,y,z):
        for a in range(0,len(z)):
            if z[a] == 0:
                z[a] = {'reg': x, 'color':y}
                return ['Allocated slot number: '+str(a+1),z]
            else :
                pass
        return ['Sorry, parking lot is full',z]

    def unpark_user(x,y):
        try :
            y[int(x)-1] = 0
            return ['Slot number ' + str(x) + ' is free',y]
        except :
            return ['Invalid Slot Value',y]

    def get_status(x):
        status_dict = []
        i = 0
        for a in range(0,len(x)):
            if x[a] != 0 :
                status_dict.append({'slot_no':a+1,'registration_no':x[a]['reg'],'colour':x[a]['color']})
                i += 1
        return [status_dict,]

    def get_cars_by_color(c,x):
        car_dict = []
        i = 0
        for a in range(0,len(x)):
            if x[a]['color'] == c :
                car_dict.append({'slot_no': a+1, 'registration_no': x[a]['reg']})
                i += 1
        if len(car_dict) == 0:
            car_dict = 'Not Found'                
        return [car_dict,]

    def get_slots_by_reg(c,x):
        car_dict = []
        i = 0
        for a in range(0,len(x)):
            if x[a]['reg'] == c :
                car_dict.append({'slot_no': a+1, 'color': x[a]['color']})
                i += 1
        if len(car_dict) == 0:
            car_dict = 'Not Found'        
        return [car_dict,]

