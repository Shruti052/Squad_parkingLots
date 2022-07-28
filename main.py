
def assign_slot(parking_lots=[],vdata={},next_empty=0):
    '''assing slot to car & find next empty slot'''
    if next_empty > len(parking_lots):
        print("Parking Slots are FULL")
        return next_empty
    vdata['slot_no'] = next_empty
    parking_lots[next_empty-1] = vdata
    print(f"Car with vehicle registration number {vdata['vno']} has been parked at slot number {next_empty}")
    # find next empty slot & save it in variable next_empty
    while next_empty <= len(parking_lots):
        # if empty slot found then return 
        if parking_lots[next_empty-1] == 0:
            return next_empty
        # else keep finding next slot
        next_empty +=1
    return next_empty

def leave_slot(slot_no=0,parking_lots=[],next_empty=0):
    if slot_no > len(parking_lots):
        print("Wrong Slot no. Entered :/   ...This Slot is not Present, ")
        return next_empty
    cdata = parking_lots[slot_no-1]
    parking_lots[slot_no-1] = 0
    print(f"Slot number {slot_no} vacated, the car with vehicle registration number {cdata['vno']} left the space, the driver of the car was of age {cdata['age']}")
    # if this slot(empty) is found to be smaller, update next_empty variable
    if slot_no < next_empty:
        next_empty = slot_no
    return next_empty

def print_commands(command='',parking_lots=[]):
    '''reads commands, gets what to find & for what & prints required data'''

    find = command.split('for')[0][0:-1].upper()
    where = (command.split('for')[1]).split(' ')[0][1::].upper()
    value = command.split(' ')[1]
    # dict created for types for commands that could be received 
    sdict = {'VEHICLE_REGISTRATION_NUMBER':'vno','VEHICLE_REGISTRATION_NUMBERS':'vno','CAR_WITH_NUMBER':'vno','CAR_WITH_NUMBERS':'vno','CAR_NUMBER':'vno','CAR_NUMBERS':'vno',
                'SLOT_NUMBER':'slot_no','SLOT_NUMBERS':'slot_no','SLOT_WITH_NUMBER':'slot_no',
                'DRIVER_OF_AGE':'age','DRIVER_AGE':'age','DRIVER_WITH_AGE':'age','AGE':'age'
            }
    # variables for which we need to find data
    try:
        find = sdict[find]
        where = sdict[where]
    except:
        print("Request Not Found :/   ..Please Enter Valid Command")
        return
    result_list = []
    for slot in parking_lots:
        if slot == 0:
            continue
        if str(slot[where]) == str(value):
            result_list.append(str(slot[find]))
    print(','.join(result_list))
    return 


def main():
    '''reads input from txt file & runs commands present in txt file'''

    file_data = open("input.txt","r+")
    parking_lots=[]
    next_empty = 0
    for line in file_data.readlines():
        line = line.strip('\n') 
        commands = line.split(' ')
        if commands[0].upper() == 'CREATE_PARKING_LOT':
            parking_lots = [0]*(int(commands[1]))
            next_empty = 1
            print(f"Created parking of {int(commands[1])} slots..")
        elif commands[0].upper() == 'PARK':
            next_empty = assign_slot(parking_lots=parking_lots,vdata={"vno":commands[1],"age":commands[3]},next_empty=next_empty)
        elif commands[0].upper() == 'LEAVE':
            next_empty = leave_slot(slot_no = int(commands[1]),parking_lots = parking_lots,next_empty=next_empty)
        else:
            print_commands(command=line,parking_lots=parking_lots)

main()