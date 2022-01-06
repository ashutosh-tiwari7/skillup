import os
import sys
from project_skillup import skillup
import json

def check_input(x,y):
    if len(y) == 0:
        print('Please initiate slots first.')
    i = x.split(' ')    
    try :
        if x.startswith('park ') :
            if len(i) != 3:
                print('Invalid Input')
            z = skillup.park_user(i[1],i[2],y)
            y = z[1]
        elif x.startswith('leave ') : 
            if len(i) != 2:
                print('Invalid Input')
            z = skillup.unpark_user(i[1],y)
            y = z[1]
        elif x.startswith('status') :
            z = skillup.get_status(y)
        elif x.startswith('registration_numbers_for_cars_with_colour ') :
            if len(i) != 2:
                print('Invalid Input')
            z = skillup.get_cars_by_color(i[1],y)
        elif x.startswith('slot_numbers_for_cars_with_colour ') :
            if len(i) != 2:
                print('Invalid Input')
            z = skillup.get_cars_by_color(i[1],y)
        elif x.startswith('slot_number_for_registration_number ') :
            if len(i) != 2:
                print('Invalid Input')
            z = skillup.get_slots_by_reg(i[1],y)
        else :
            print('Invalid Command. use --help to see list of commands')
        print(z[0])
    except :
        print('Invalid Input')
    return y

def check_file_input(x,y):
    if len(y) == 0:
        output_file.write('Please initiate slots first.\n')
        print('Please initiate slots first.')
    i = x.split(' ')    
    if x.startswith('park ') :
        if len(i) != 3:
            output_file.write('Invalid Input\n')
            print('Invalid Input')
        z = skillup.park_user(i[1],i[2],y)
        y = z[1]
    elif x.startswith('leave ') : 
        if len(i) != 2:
            output_file.write('Invalid Input\n')
            print('Invalid Input')
        z = skillup.unpark_user(i[1],y)
        y = z[1]
    elif x.startswith('status') :
        z = skillup.get_status(y)
    elif x.startswith('registration_numbers_for_cars_with_colour ') :
        if len(i) != 2:
            output_file.write('Invalid Input\n')
            print('Invalid Input')
        z = skillup.get_cars_by_color(i[1],y)
    elif x.startswith('slot_numbers_for_cars_with_colour ') :
        if len(i) != 2:
            output_file.write('Invalid Input\n')
            print('Invalid Input')
        z = skillup.get_cars_by_color(i[1],y)
    elif x.startswith('slot_number_for_registration_number ') :
        if len(i) != 2:
            output_file.write('Invalid Input\n')
            print('Invalid Input')
        z = skillup.get_slots_by_reg(i[1],y)
    else :
        output_file.write('Invalid Command. use --help to see list of commands\n')
        print('Invalid Command. use --help to see list of commands')
    if type(z[0]) == list :
        if type(z[0][0]) == dict :
            z[0] = json.dumps(z[0]) 
    print(z[0])
    output_file.write(z[0]+'\n')
    return y

if __name__ == '__main__':   
    slots = 0
    slot_array = []
    #Interactive Mode
    if len(sys.argv) == 1:
        while True:
            x = input()
            if x == 'exit':
                break
            else:
                if x.startswith('create_parking_lot ') :
                    i = x.split(' ')
                    try :
                        i = int(i[1])
                        slot_array = skillup.create_slots(i)
                        print('Created a parking lot with '+str(i)+' slots')
                    except :
                        print('Please Input Valid Length for slot')    
                    
                elif x.startswith('--help') :
                    pass
                else :
                    slot_array = check_input(x,slot_array)
    #File Mode
    elif len(sys.argv) == 3:
        try :
            with open(sys.argv[1]) as f:
                lines = f.readlines()
            output_file = open(sys.argv[2], "w")
            for x in lines :
                x = x.strip()
                if x.startswith('create_parking_lot ') :
                    i = x.split(' ')
                    try :
                        i = int(i[1])
                        slot_array = skillup.create_slots(i)
                        output_file.write('Created a parking lot with '+str(i)+' slots\n')
                        print('Created a parking lot with '+str(i)+' slots')
                    except :
                        output_file.write('Please Input Valid Length for slot\n')    
                        print('Please Input Valid Length for slot')    
                    
                elif x.startswith('--help') :
                    pass
                else :
                    slot_array = check_file_input(x,slot_array)
            output_file.close()
        except :
            print('Input File not found')
            slot_array = check_file_input(x,slot_array)
    else :
        print('Invalid Arguments.')