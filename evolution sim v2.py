import turtle
import random

SIM_AREA = 250
MIN_REP_THRESH = 250
animals = []
plants = []
frame = 0

file = open("output.txt", "w")
file.write("Frame Num\tPlant Pop\tPrey Pop\tPred Pop\tPrey Speed\tPred Speed\tPrey Agility\tPred Agility\tPrey Mutation Chance\tPred Mutation Chance\tPrey Reproduction min Hunger\tPred Reproduction min Hunger\n")


paused = False
def pauseSim():
    global paused
    if paused:
        paused = False
        global file
        file = open("output.txt", "a")
    else:
        paused = True
        file.close()

screen = turtle.Screen()
turtle.tracer(0)
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(-350, 0)
turtle.title("Maximilian's Natural Selection Simulation v2")
screen.listen()
screen.onkey(pauseSim, 'space')


class plant():
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.goto(random.randint(-SIM_AREA, SIM_AREA), random.randint(-SIM_AREA, SIM_AREA))
        self.turtle.color("green")
        self.turtle.shape("circle")
        self.turtle.turtlesize(0.05, 0.05, 1)

def spawn_plant():
    plants.append(plant())

class animal:
    def __init__(self, x, y):
        self.predator = False
        self.vision = random.randint(5, 100)
        self.speed = random.randint(1, 10)
        self.mutationProb = random.randint(0, 50)
        self.agility = random.randint(1, 15)
        self.reproductionThreshold = random.randint(MIN_REP_THRESH, 700)
        self.hunger = 80
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.penup()
        self.turtle.goto(x, y)
        #self.turtle.pendown()
        self.turtle.shape("turtle")
        self.turtle.turtlesize(0.2, 0.2, 1)

    def make_predator(self):
        self.predator = True
        self.turtle.color("red")

    def reproduce(self):
        child = animal(self.turtle.xcor() + 5, self.turtle.ycor())
        child.turtle.setheading(self.turtle.heading())
        self.hunger = int(self.hunger / 2)
        child.hunger = self.hunger
        if self.predator:
            child.make_predator()
            
        child.vision = self.vision
        if random.randint(0, 100) > self.mutationProb:
            child.vision += random.randint(-10, 10)
            if child.vision < 0:
                child.vision = 0
            
        child.speed = self.speed
        if random.randint(0, 100) > self.mutationProb:
            child.speed = random.randint(1, 10)

        child.mutationProb = self.mutationProb
        if random.randint(0, 100) > self.mutationProb:
            child.mutationProb = random.randint(0, 50)
            
        child.agility = self.agility
        if random.randint(0, 100) > self.mutationProb:
            child.agility += random.randint(-8, 8)
            if child.agility < 3:
                child.agility = 3
            elif child.agility > 180:
                child.agility = 180
            
        child.reproductionThreshold = self.reproductionThreshold
        if random.randint(0, 100) > self.mutationProb:
            child.reproductionThreshold += random.randint(-10, 10)
            if child.reproductionThreshold < MIN_REP_THRESH:
                child.reproductionThreshold = MIN_REP_THRESH

        animals.append(child)
        


for i in range(200):
    spawn_plant()
for i in range(350):
    animals.append(animal(random.randint(-SIM_AREA, SIM_AREA), random.randint(-SIM_AREA, SIM_AREA)))
for i in range(5):
    p = animal(random.randint(-SIM_AREA, SIM_AREA), random.randint(-SIM_AREA, SIM_AREA))
    p.make_predator()
    animals.append(p)



running = True
while running:
    if paused:
        screen.update()
        continue
    
    frame += 1
    if len(plants) < 2000:
        for i in range(10):
            spawn_plant()

    if len(animals) == 0:
        running = False


    killedAnimals = []
    killedPlants = []

    for i in range(0, len(animals)):
        food = []
        if animals[i].predator:
            food = animals.copy()
            f = 0
            while f < len(food):
                if food[f].predator:
                    food.pop(f)
                else:
                    f += 1
        
        else:
            food = plants.copy()


        targetHeading = animals[i].turtle.towards(0, 0)
        closestFoodDistance = animals[i].vision
        for f in food:
            if animals[i].turtle.distance(f.turtle) < closestFoodDistance:
                closestFoodDistance = animals[i].turtle.distance(f.turtle)
                targetHeading = animals[i].turtle.towards(f.turtle)


        deltaHeading = animals[i].turtle.heading() - targetHeading
        

        if animals[i].predator == False: # prey run away from predators
            closestPredator = animals[i].vision
            for pred in animals:
                if pred.predator and animals[i].turtle.distance(pred.turtle) < closestPredator:
                    closestPredator = animals[i].turtle.distance(pred.turtle)
                    predatorHeading = animals[i].turtle.towards(pred.turtle)

            if closestPredator < animals[i].vision:
                deltaHeading = predatorHeading - animals[i].turtle.heading()

        if deltaHeading > 180:
            deltaHeading -= 360
        if deltaHeading < -180:
            deltaHeading += 360


        if deltaHeading < -animals[i].agility:
            animals[i].turtle.left(animals[i].agility)
        elif deltaHeading > animals[i].agility:
            animals[i].turtle.right(animals[i].agility)
        else:
            animals[i].turtle.right(deltaHeading)

        animals[i].turtle.forward(animals[i].speed)
        animals[i].hunger -= animals[i].speed


        if animals[i].predator: # eating
            for f in range(0, len(animals)):
                if animals[f].predator == False and animals[i].turtle.distance(animals[f].turtle) <= 8:
                    killedAnimals.append(f)
                    animals[i].hunger += 200
        else:
            for f in range(0, len(plants)):
                if animals[i].turtle.distance(plants[f].turtle) <= 8:
                    plants[f].turtle.hideturtle()
                    killedPlants.append(f)
                    animals[i].hunger += 40

        if animals[i].hunger > animals[i].reproductionThreshold:
            animals[i].reproduce()

        if animals[i].hunger <= 0:
            animals[i].turtle.hideturtle()
            killedAnimals.append(i)


    killedAnimals.sort(reverse = True)
    killedPlants.sort(reverse = True)
    
    lastRemoved = -1
    for i in killedAnimals:
        if i != lastRemoved:
            animals[i].turtle.hideturtle()
            animals.pop(i)
            lastRemoved = i

    lastRemoved = -1
    for i in killedPlants:
        if i != lastRemoved:
            plants[i].turtle.hideturtle()
            plants.pop(i)
            lastRemoved = i

    numPredators = 0
    numPrey = 0
    averageSpeedPred = 0
    averageSpeedPrey = 0
    averageAgilityPred = 0
    averageAgilityPrey = 0
    averageVisionPred = 0
    averageVisionPrey = 0
    averageMutationProbPred = 0
    averageMutationProbPrey = 0
    averageReproductionThresholdPred = 0
    averageReproductionThresholdPrey = 0
    for a in animals:
        if a.predator:
            numPredators += 1
            averageSpeedPred += a.speed
            averageAgilityPred += a.agility
            averageVisionPred += a.vision
            averageMutationProbPred += a.mutationProb
            averageReproductionThresholdPred += a.reproductionThreshold
        else:
            numPrey += 1
            averageSpeedPrey += a.speed
            averageAgilityPrey += a.agility
            averageVisionPrey += a.vision
            averageMutationProbPrey += a.mutationProb
            averageReproductionThresholdPrey += a.reproductionThreshold

    if numPredators > 0:
        averageSpeedPred /= numPredators
        averageAgilityPred /= numPredators
        averageVisionPred /= numPredators
        averageMutationProbPred /= numPredators
        averageReproductionThresholdPred /= numPredators

    if numPrey > 0:
        averageSpeedPrey /= numPrey
        averageAgilityPrey /= numPrey
        averageVisionPrey /= numPrey
        averageMutationProbPrey /= numPrey
        averageReproductionThresholdPrey /= numPrey

    file.write(str(int(frame)))
    file.write("\t")
    file.write(str(int(len(plants))))
    file.write("\t")
    file.write(str(int(numPrey)))
    file.write("\t")
    file.write(str(int(numPredators)))
    file.write("\t")
    if numPrey > 0: file.write(str(int(averageSpeedPrey)))
    file.write("\t")
    if numPredators > 0: file.write(str(int(averageSpeedPred)))
    file.write("\t")
    if numPrey > 0: file.write(str(int(averageAgilityPrey)))
    file.write("\t")
    if numPredators > 0: file.write(str(int(averageAgilityPred)))
    file.write("\t")
    if numPrey > 0: file.write(str(int(averageMutationProbPrey)))
    file.write("\t")
    if numPredators > 0: file.write(str(int(averageMutationProbPred)))
    file.write("\t")
    if numPrey > 0: file.write(str(int(averageReproductionThresholdPrey)))
    file.write("\t")
    if numPredators > 0: file.write(str(int(averageReproductionThresholdPred)))
    file.write("\n")

    

    turtle.clear()
    turtle.write("""Frame num: {}
Plant pop: {}
Prey pop: {}
Predator pop: {}
""".format(frame, len(plants), numPrey, numPredators))
    screen.update()

file.close()
print("simulation stopped")
