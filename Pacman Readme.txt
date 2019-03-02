1. Pacman program is required to run in python environment with verion >= python 2.7
2. To run Pacman program, please download "Pacman.py" to local directory with corresponding python environment. 
3. One way to run it is: (On Mac) Open Terminal, cd to directory where "Pacman.py" is saved, type "python Pacman.py"
4. When test this program, please note:
	4.1 Use correct command (PLACE X(int),Y(int),F(str) / MOVE / LEFT / RIGHT / REPORT)
	4.2 Please test it with following inputs:
		4.2.1  PLACE 0,0,NORTH 		(expected position: 0,0,NORTH)
		4.2.2  REPORT				(expected position: 0,0,NORTH)
		4.2.3  MOVE					(expected position: 0,1,NORTH)
		4.2.4  REPORT				(expected position: 0,1,NORTH)
		4.2.5  RIGHT				(expected position: 0,1,EAST)
		4.2.6  REPORT				(expected position: 0,1,EAST)
		4.2.7  LEFT					(expected position: 0,1,NORTH)
		4.2.8  LEFT					(expected position: 0,1,WEST)
		4.2.9  REPORT				(expected position: 0,1,WEST)
		4.2.10 MOVE					(expected position: 0,1,WEST)
		4.2.11 REPORT				(expected position: 0,1,WEST)
		4.2.12 return				(exit program)