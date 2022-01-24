class room():
    def __init__(self, d, w, h, n_door): # Constructor
        self.depth = d
        self.width = w
        self.height = h
        self.num_door = n_door
   
    def get_room_info(self):
        print('Room depth: ', self.depth,
        'width: ', self.width,
        'height: ', self.height,
        'number of doors: ', self.num_door)
    
class office(room): #
    def __init__(self, room_num, occ, name_occupant, wb, pb, d, w, h, n_door):
        self.room_number = room_num
        self.occupied = occ
        self.person = None
        if self.occupied:
            self.person = name_occupant
        self.whiteboard_installed = wb
        self.pinboard_installed = pb
        room.__init__(self, d, w, h, n_door) #
    
    def print_office_info(self):
        print('Room Number: ', self.room_number, 
            'Occupation status: ', self.occupied,
            'Occupied by: ', self.person,
            'Whiteboard Installed:', self.whiteboard_installed, 
            'Pinboard Installed:', self.pinboard_installed)

room_1 = room(50, 50, 13, 2)  # object of room
room_1.get_room_info()

office_1 = office(1215, True, 'Sukrit', 1, 1, 10, 12, 13, 1) # object of office
office_1.print_office_info()
office_1.get_room_info()