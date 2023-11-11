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
mapaIz = [(4,0), (5,0), (4,1), (5,1),(5,2),(4,2) ,(4,3), (5,3), (4,4), (5,4), (4,5), (5,5), (4,6), (5,6),
          (4,7), (5,7), (4,8), (5,8), (4,9), (5,9), (4,10), (5,10), (4,11), (5,11), (4,12), (5,12),
          (4,13), (5,13), (4,14), (5,14), (4,15), (5,15), (4,16), (5,16), (4,17), (5,17), 
          (4,18), (5,18), (4,19), (5,19),
          #Primera sección carril izquierda 4,5 X
          (12,0),(13,0),(12,1),(13,1),(12,2),(13,2),(12,3),(13,3),(12,4),(13,4),(12,5),(13,5),(12,6),(13,6),
          (12,7),(13,7),(12,8),(13,8),(12,9),(13,9),(12,10),(13,10),(12,11),(13,11),(12,12),(13,12),(12,13),(13,13),(12,14),(13,14),
          (12,15),(13,15),(12,16),(13,16),(12,17),(13,17),(12,18),(13,18),(12,19),(13,19),
          #Segunda columna carril izquierda 12,13 X
          (0,8),(0,7),(1,8),(1,7),(2,8),(2,7),(3,8),(3,7),(4,8),(4,7),(5,8),(5,7),(6,8),(6,7),(7,8),(7,7),(8,8),(8,7),(9,8),(9,7),
          (10,8),(10,7),(11,8),(11,7),(12,8),(12,7),(13,8),(13,7),(14,8),(14,7),(15,8),(15,7),(16,8),(16,7),(17,8),(17,7),(18,8),(18,7),
          (19,8),(19,7),
          #Primer columna carril izquierda Y 8,7
          (0,16),(0,17),(1,16),(1,17),(2,16),(2,17),(3,16),(3,17),(4,16),(4,17),(5,16),(5,17),(6,16),(6,17),(7,16),(7,17),(8,16),(8,17),(9,16),(9,17),
          (10,16),(10,17),(11,16),(11,17),(12,16),(12,17),(13,16),(13,17),(14,16),(14,17),(15,16),(15,17),(16,16),(16,17),(17,16),(17,17),(18,16),(18,17),
          (19,16),(19,17)
          #Segunda coluna del carril izquierdo Y 17,16

           ]
mapaDer = [#Primera fila del carril derecha 6,7 X
    (6,0),(7,0),(6,1),(7,1),(6,2),(7,2),(6,3),(7,3),(6,4),(7,4),(6,5),(7,5),(6,6),(7,6),
    (6,7),(7,7),(6,8),(7,8),(6,9),(7,9),(6,10),(7,10),(6,11),(7,11),(6,12),(7,12),(6,13),(7,13),
    (6,14),(7,14),(6,15),(7,15),(6,16),(7,16),(6,17),(7,17),(6,18),(7,18),(6,19),(7,19),
    #Segunda fila del carril de la derecha 14,15 X
    (14,0),(15,0),(14,1),(15,1),(14,2),(15,2),(14,3),(15,3),(14,4),(15,4),(14,5),(15,5),(14,6),(15,6),
    (14,7),(15,7),(14,8),(15,8),(14,9),(15,9),(14,10),(15,10),(14,11),(15,11),(14,12),(15,12),(14,13),(15,13),
    (14,14),(15,14),(14,15),(15,15),(14,16),(15,16),(14,17),(15,17),(14,18),(15,18),(14,19),(15,19),
    #Primera fila del carril de la derecha 5,6 Y
    (0,5),(0,6),(1,5),(1,6),(2,5),(2,6),(3,5),(3,6),(4,5),(4,6),(5,5),(5,6),(6,5),(6,6),(7,5),(7,6),(8,5),(8,6),
    (9,5),(9,6),(10,5),(10,6),(11,5),(11,6),(12,5),(12,6),(13,5),(13,6),(14,5),(14,6),(15,5),(15,6),(16,5),(16,6),
    (17,5),(17,6),(18,5),(18,6),(19,5),(19,6),
    #Segunda fila del carril de la derecha 14,15 Y
    (0,14),(0,15),(1,14),(1,15),(2,14),(2,15),(3,14),(3,15),(4,14),(4,15),(5,14),(5,15),(6,14),(6,15),(7,14),(7,15),(8,14),(8,15),
    (9,14),(9,15),(10,14),(10,15),(11,14),(11,15),(12,14),(12,15),(13,14),(13,15),(14,14),(14,15),(15,14),(15,15),(16,14),(16,15),
    (17,14),(17,15),(18,14),(18,15),(19,14),(19,15)
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
        self.locationX = 6  # Initial location
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
        #print("posible_New:", possible)
        #print(possible_steps)
        for neighbor_cell in possible:
            #print("Neighbor:",neighbor_cell)
            cell_contents = neighbor_cell
            cellmates = self.model.grid.get_cell_list_contents([cell_contents])
            #print("Cellmate:", cellmates)
            if len(cellmates) >=1: 
                other = cellmates[0]
                #print("Celmates[0]:", other)
                if other.agentT == 0:
                    value_to_remove = cell_contents
                    possible = tuple(value for value in possible if value != value_to_remove)
                    #print("posible_RemoveDrunk:", possible)
                #print("Entró")

        new_position = self.random.choice(possible)
        self.model.grid.move_agent(self, new_position)
        #print("new positionDrunk:", new_position)
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

class carrilizquierdoAgent(Agent):
    def __init__(self,unique_id,model):
        super().__init__(unique_id,model)
        self.agentT = 4 #Obstacle
     
    
    def step(self):
        pass

class CoolAgent(Agent):
    """
    Moving upward car agent
    """

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.crashed = False
        self.locationX, self.locationY = self.random.choice(mapaDer)
        self.agentT = 1 #SmoothOperator 
    
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        
        possible = ( (self.locationX , self.locationY +1),(self.locationX+1, self.locationY))
        #print("LocationX", self.locationX)
        if self.locationY >= 19:
            possible = ( (self.locationX , (self.locationY +1) %20), (self.locationX+1, self.locationY))
            #print("Above", possible)
            #print("Modulo de 9:", (self.locationY +1) %10)
        if self.locationX >= 19:
            possible = ( (self.locationX , self.locationY +1),((self.locationX+1)%20, self.locationY))
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
                
                print("Celmates:", cellmates)
                if other.agentT == 0:
                    #print("0:")
                    value_to_remove = cell_contents
                    possible = tuple(value for value in possible if value != value_to_remove)
                    #print("posible_RemoveCool0:", possible)
                
                if other.agentT == 4:
                    #print("4:")
                    value_to_remove = cell_contents
                    possible = tuple(value for value in possible if value != value_to_remove)
                    #print("posible_RemoveCool4:", possible)

            if len(cellmates) >=2:
                print("Habemos muchos3")
                other2 =  cellmates[1]
                if other2.agentT == 2:
                    print("Choque!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1111111")
                if other2.agentT == 1:
                    print("Choque!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1111111")
            if len(cellmates) >=3:
                print("Habemos muchos3")
                other2 =  cellmates[2]
                if other2.agentT == 2:
                    print("Choque!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1111111")
                if other2.agentT == 1:
                    print("Choque!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1111111")
                    

        #If possible <= 1: Move to same position
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

       
        
        #Crete the obstacles
        for i in mapaObs:
            #print("Mapa")
            pavA = pavimentoAgent(o,self)
            x, y = i
            self.schedule.add(pavA)
            self.grid.place_agent(pavA,(x,y))
            o += 1
        #Create carril derecho
        for i in mapaDer:
            #print("Mapa")
            pavA = carrilDerechoAgent(o,self)
            x, y = i
            self.schedule.add(pavA)
            self.grid.place_agent(pavA,(x,y))
            o += 1
        #Create carril izquierdo
        for i in mapaIz:
            #print("Mapa")
            pavA = carrilizquierdoAgent(o,self)
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
        
        # Create car agents and add them to the schedule
        for i in range(self.num_agents):
            print("Auto")
            car_agent = CarAgent(o, self)
            self.schedule.add(car_agent)
            self.grid.place_agent(car_agent, (car_agent.locationX, car_agent.locationY))
            o +=1 #Contador de ids

    def step(self):
        self.schedule.step()
