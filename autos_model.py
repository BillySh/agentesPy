## Humberto Ivan Ulloa Cardona
# Desing two agent cars, to simulate a crash between them.


#--------------------------Imports-------------------------------------
from mesa import Agent
from mesa import Model
from mesa.time import RandomActivation
import mesa 
import random
#---------------------------Mapa-----------------------------------------

mapaObs = [(0,0),(1,0),(2,0),(3,0),(0,1),(1,1),(2,1),(3,1),
           (0,2),(1,2),(2,2),(3,2,),(0,3),(1,3),(2,3),(3,3),
           (0,4),(1,4),(2,4),(3,4),(0,5),(1,5),(2,5),(3,5),
           (0,6),(1,6),(2,6),(3,6),(0,9),(1,9),(2,9),(3,9),
           #----------------------------------------------
           (0,9),(1,9),(2,9),(3,9),(0,10),(1,10),(2,10),(3,10),
           (0,19),(1,19),(2,19),(3,19),(0,18),(1,18),(2,18),(3,18),
           (0,4),(1,4),(2,4),(3,4),(0,5),(1,5),(2,5),(3,5),
           (0,6),(1,6),(2,6),(3,6),(0,9),(1,9),(2,9),(3,9),
           #---------------------------
           (6,0),(7,0),(8,0),(9,0),(6,1),(7,1),(8,1),(9,1),
           (6,2),(7,2),(8,2),(9,2),(6,3),(7,3),(8,3),(9,3),
           (6,6),(7,6),(8,6),(9,6),(6,9),(7,9),(8,9),(9,9)]
#---------------------------Agents----------------------------------------

"""
Agents Type glosari:
    agentT == 0 -> Obstacle
    agentT == 1 -> SmoothOperator
    agentT == 2 -> Drunk driver
"""

class CarAgent(Agent): #Car
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.speed = 0  # Initial speed
        self.locationX = 5  # Initial location
        self.locationY = 0  # Initial location
        self.agentT = 2 #DrunkDriver 

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        possible = ((self.locationX + 1, self.locationY),(self.locationX - 1, self.locationY), (self.locationX , self.locationY +1), (self.locationX+1, self.locationY+1))
        if self.locationY >= 19:
            possible = ((self.locationX + 1, self.locationY),(self.locationX - 1, self.locationY), (self.locationX , (self.locationY + 1)%20), (self.locationX+1, (self.locationY + 1)%20))
            #print("Above", possible)
            #print("Modulo de 9:", (self.locationY +1) %10)
        if self.locationX >= 19:
            possible = (((self.locationX + 1)%20, self.locationY),(self.locationX - 1, self.locationY), (self.locationX , self.locationY +1), ((self.locationX+1)%20, self.locationY+1))
            #print("Above", possible)
            #print("Modulo de 9:", (self.locationY +1) %10)
        if self.locationX >=19 and self.locationY >=19:
            possible = (((self.locationX + 1)%20, self.locationY),((self.locationX - 1)%20, self.locationY), (self.locationX , (self.locationY +1)%20), ((self.locationX+1)%20, (self.locationY+1)%20))
        print("posible_New:", possible)
        print(possible_steps)
        for neighbor_cell in possible:
            #print("Neighbor:",neighbor_cell)
            cell_contents = neighbor_cell
            cellmates = self.model.grid.get_cell_list_contents([cell_contents])
            #print("Cellmate:", cellmates)
            if len(cellmates) >=1: 
                #print("Entró")
                value_to_remove = cell_contents
                possible = tuple(value for value in possible if value != value_to_remove)
                print("posible_RemoveDrunk:", possible)

        new_position = self.random.choice(possible)
        self.model.grid.move_agent(self, new_position)
        print("new positionDrunk:", new_position)
        self.locationX, self.locationY = new_position

    def step(self):
        # Implement the logic for the car's behavior in each step
        #This car will only move a designed path, following only its path
        self.move()
        # For example, you can update the speed and location here
        pass
class pavimentoAgent(Agent):
    def __init__(self,unique_id,model):
        super().__init__(unique_id,model)
        self.agentT = 0 #Obstacle
     
    
    def step(self):
        pass

class CoolAgent(Agent):
    """
    Moving upward car agent
    """

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.crashed = False
        self.locationX = 4  # Initial location
        self.locationY = 8
        self.agentT = 1 #SmoothOperator 
    
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        
        possible = ( (self.locationX , self.locationY +1), (self.locationX-1, self.locationY+1),(self.locationX-1, self.locationY))

        if self.locationY >= 19:
            possible = ( (self.locationX , (self.locationY +1) %20), (self.locationX-1, (self.locationY +1) %20),(self.locationX-1, self.locationY))
            #print("Above", possible)
            #print("Modulo de 9:", (self.locationY +1) %10)
        if self.locationX <= -19:
            possible = ( (self.locationX , self.locationY +1), ((self.locationX-1)%20, self.locationY +1),((self.locationX-1) %20, self.locationY))
            #print("Above", possible)
            #print("Modulo de 9:", (self.locationY +1) %10)
        #print("posible_NewOtherCool:", possible)
        #print(possible_steps)
        for neighbor_cell in possible:
            #print("EStoy ya casi por salir--------")
            #print("Neighbor:",neighbor_cell)
            cell_contents = neighbor_cell
            cellmates = self.model.grid.get_cell_list_contents([cell_contents])
            #print("Cellmate:", cellmates)
            if len(cellmates) >=1: 
                print("Entró")
                x,y = neighbor_cell
                value_to_remove = cell_contents
                cell_contents = self.model.grid[x][y]
                #print("cellcon:", cell_contents)
                possible = tuple(value for value in possible if value != value_to_remove)
                print("posible_Remove:", possible)

        new_position = self.random.choice(possible)
        self.model.grid.move_agent(self, new_position)
        print("new positionCool:", new_position)
        self.locationX, self.locationY = new_position


        
    def step(self):
        self.move()
        pass


#-------------------------------------------Model--------------------------------------------------------
class CarModel(Model):
    def __init__(self, width, height, num_agents):
        self.num_agents = num_agents
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        o = 0

        # Create car agents and add them to the schedule
        for i in range(self.num_agents):
            print("Auto")
            car_agent = CarAgent(i, self)
            self.schedule.add(car_agent)
            self.grid.place_agent(car_agent, (car_agent.locationX, car_agent.locationY))
            o +=1 #Contador de ids
        
        #Crete the obstacles
        for i in mapaObs:
            pavA = pavimentoAgent(o,self)
            x, y = i
            self.schedule.add(pavA)
            self.grid.place_agent(pavA,(x,y))
            o += 1

        # Create car agents and add them to the schedule
        for i in range(self.num_agents):
            print("Auto")
            cool_agent = CoolAgent(o, self)
            self.schedule.add(cool_agent)
            self.grid.place_agent(cool_agent, (cool_agent.locationX, cool_agent.locationY))
            o +=1 #Contador de ids

    def step(self):
        self.schedule.step()
