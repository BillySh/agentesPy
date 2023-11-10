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
           (0,4),(1,4),(2,4),(3,4),
           (0,9),(1,9),(2,9),(3,9),
           #----------------------------------------------
           (0,9),(1,9),(2,9),(3,9),(0,10),(1,10),(2,10),(3,10),
           (0,19),(1,19),(2,19),(3,19),(0,18),(1,18),(2,18),(3,18),
           (0,4),(1,4),(2,4),(3,4),
           (0,9),(1,9),(2,9),(3,9),
           #---------------------------
           (8,0),(9,0),(8,1),(9,1),(9,2),(8,4),(9,4),
           (8,2),(9,2),(8,3),(9,3),(9,9),(8,9),(10,0),(11,0),(10,1),(11,1),
           (10,2),(11,2),(10,3),(11,3),(10,4),(11,4),
           (19,0),(18,0),(17,0),(16,0),
           (19,1),(18,1),(17,1),(16,1), (19,2),(18,2),(17,2),(16,2), (19,3),(18,3),(17,3),(16,3),
           (19,4),(18,4),(17,4),(16,4),
           (9,10),(8,10),(10,10),(11,10), (10,9), (11,9), (9,11),(8,11),(10,11),(11,11),
           (9,12),(8,12),(10,12),(11,12), (9,13),(8,13),(10,13),(11,13), (0,13),(2,13),(3,13),(1,13),
            (0,12),(2,12),(3,12),(1,12),  (0,11),(2,11),(3,11),(1,11), (9,19),(8,19),(10,19),(11,19), 
            (9,18),(8,18),(10,18),(11,18), (19,9),(18,9),(17,9),(16,9), (19,10),(18,10),(17,10),(16,10),
            (19,11),(18,11),(17,11),(16,11), (19,12),(18,12),(17,12),(16,12), (19,13),(18,13),(17,13),(16,13),
            (19,19),(18,19),(17,19),(16,19), (19,18),(18,18),(17,18),(16,18)
           ]
#---------------------------Agents----------------------------------------

"""
Agents Type glosari:
    agentT == 0 -> Obstacle
    agentT == 1 -> SmoothOperator
    agentT == 2 -> Drunk driver
    agetnT == 3 -> Carril derecho
    agetnT == 4 -> Carril izquierdo
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
                other = cellmates[0]
                print("Celmates[0]:", other)
                if other.agentT == 0:
                    value_to_remove = cell_contents
                    possible = tuple(value for value in possible if value != value_to_remove)
                    print("posible_RemoveDrunk:", possible)
                #print("Entró")

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

class carrilDerechoAgent(Agent):
    def __init__(self,unique_id,model):
        super().__init__(unique_id,model)
        self.agentT = 3 #Obstacle
     
    
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
                other = cellmates[0]
                print("Celmates[0]:", other)
                if other.agentT == 0:
                    value_to_remove = cell_contents
                    possible = tuple(value for value in possible if value != value_to_remove)
                    print("posible_RemoveDrunk:", possible)

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
            #print("Mapa")
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
