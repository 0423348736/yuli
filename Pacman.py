import re
class Pacman:
    # PX is position on x-axis (WEST and EAST),PY is position on y-axis(North and South)
    PX = 0 
    PY = 0
    Face = "NORTH"
    # Give an initial position with PX, PY, and Face (with position in Grid range)
    def PLACE(self, px, py, face):
        if px>=0 and px<=4 and py>=0 and py<=4 and (face=="NORTH" or face=="SOUTH" or face=="WEST" or face=="EAST"):
            self.PX = px
            self.PY = py
            self.Face = face

    # Move Pacman 1 unit on Grid on its current facing direction
    def MOVE(self):
        if self.Face == "NORTH" and (self.PY + 1)<=4:
            self.PY = self.PY + 1
        if self.Face == "SOUTH" and 0<=(self.PY - 1):
            self.PY = self.PY - 1
        if self.Face == "WEST" and 0<=(self.PX - 1):
            self.PX = self.PX - 1
        if self.Face == "EAST" and (self.PX + 1)<=4:
            self.PX = self.PX + 1
            
    # Print current position and facing direction
    def REPORT(self):
        print("Output: "+str(self.PX)+", "+str(self.PY)+", "+self.Face)
        
    # Rotate Pacman left 90 degrees in the specified direction without changing the position of Pacman
    def LEFT(self):
        if self.Face == "NORTH":
            self.Face = "WEST"
            return
        if self.Face == "WEST":
            self.Face = "SOUTH"
            return
        if self.Face == "SOUTH":
            self.Face = "EAST"
            return
        if self.Face == "EAST":
            self.Face = "NORTH"
            return
    # Rotate Pacman right 90 degrees in the specified direction without changing the position of Pacman
    def RIGHT(self):
        if self.Face == "NORTH":
            self.Face = "EAST"
            return
        if self.Face == "WEST":
            self.Face = "NORTH"
            return
        if self.Face == "SOUTH":
            self.Face = "WEST"
            return
        if self.Face == "EAST":
            self.Face = "SOUTH"            
            return

p = Pacman()
print(" ---Enter command and type return to exit---")

while True:
    inp = raw_input("")
    matchObj = re.match( r'PLACE ([0-4]),([0-4]),(NORTH|WEST|SOUTH|EAST)', inp, re.M|re.I)

    if inp == "":
        # Exit when return
        break    
    if matchObj:
        p.PLACE(int(matchObj.group(1)),int(matchObj.group(2)),matchObj.group(3))
    if inp == "MOVE":
        p.MOVE()
    if inp == "REPORT":
        p.REPORT()
    if inp == "RIGHT":
        p.RIGHT()
    if inp == "LEFT":
        p.LEFT()

