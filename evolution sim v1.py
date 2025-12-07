import random
import turtle

turtle.title("Maximilian's evolution simulation")

turtle.hideturtle()
turtle.penup()
turtle.speed(0)
turtle.setup(800, 800)
turtle.tracer(0)


turtles = []
species = []
foodStorage = []
hunger = []
sight=[]
speed = []
cloneSpacing = []
timeToClone = []
agility = []
direction = []
mutationProbability = []

plants = []


def init(numPlants, numAnimals, numPredators):
    global turtles
    global foodStorage
    global hunger
    global sight
    global speed
    global cloneSpacing
    global timeToClone
    global agility
    global direction
    global plants
    global mutationProbability
    global species
    turtles = []
    foodStorage = []
    hunger = []
    sight=[]
    speed = []
    cloneSpacing = []
    timeToClone = []
    agility = []
    direction = []

    plants = []
    
    for i in range(numAnimals):
        new_direction = random.randint(0, 359)
        direction.append(new_direction)
        
        t = turtle.Turtle()
        t.penup()
        t.speed(0)
        t.shape("turtle")
        t.goto(random.randint(-200, 200), random.randint(-200, 200))
        t.turtlesize(0.7, 0.7, 0.7)
        t.setheading(new_direction)
        turtles.append(t)

        sight.append(random.randint(20, 180))
        new_foodStorage = random.randint(50, 600)
        foodStorage.append(new_foodStorage)
        hunger.append(new_foodStorage)
        speed.append(random.randint(1, 10))
        new_cloneSpacing = random.randint(15, 100)
        cloneSpacing.append(new_cloneSpacing)
        timeToClone.append(new_cloneSpacing)
        agility.append(random.randint(5, 15))
        mutationProbability.append(random.randint(0, 50))
        species.append("herbivore")
    
    for i in range(numPredators):
        new_direction = random.randint(0, 359)
        direction.append(new_direction)
        
        t = turtle.Turtle()
        t.penup()
        t.speed(0)
        t.shape("turtle")
        t.color("red")
        t.goto(random.randint(-200, 200), random.randint(-200, 200))
        t.turtlesize(0.7, 0.7, 0.7)
        t.setheading(new_direction)
        turtles.append(t)

        sight.append(random.randint(20, 180))
        new_foodStorage = random.randint(50, 600)
        foodStorage.append(new_foodStorage)
        hunger.append(new_foodStorage)
        speed.append(random.randint(1, 10))
        new_cloneSpacing = random.randint(15, 100)
        cloneSpacing.append(new_cloneSpacing)
        timeToClone.append(new_cloneSpacing)
        agility.append(random.randint(5, 15))
        mutationProbability.append(random.randint(0, 50))
        species.append("carnivore")



    for i in range(numPlants):
        t = turtle.Turtle()
        t.shape("circle")
        t.speed(0)
        t.penup()
        t.turtlesize(0.4, 0.4, 0.4)
        t.goto(random.randint(-400, 400), random.randint(-400, 400))
        t.color("light green")
        plants.append(t)

def get_average(values, s):
    total = 0
    length = 0
    for i in range(len(values)):
        if species[i] == s:
            total += values[i]
            length += 1
    
    return round(total/length, 1)

def print_report():
    global turtles
    global foodStorage
    global hunger
    global sight
    global speed
    global cloneSpacing
    global timeToClone
    global agility
    global direction
    global mutationProbability
    global species

    print()
    print()
    print()
    print("Herbivores:")
    print()
    print("Population: " + str(species.count("herbivore")))
    if species.count("herbivore") > 0:
        print("Average foodStorage: " + str(get_average(foodStorage, "herbivore")))
        print("Average hunger: " + str(get_average(hunger, "herbivore")))
        print("Average sight: " + str(get_average(sight, "herbivore")))
        print("Average speed: " + str(get_average(speed, "herbivore")))
        print("Average cloneSpacing: " + str(get_average(cloneSpacing, "herbivore")))
        print("Average timeToClone: " + str(get_average(timeToClone, "herbivore")))
        print("Average agility: " + str(get_average(agility, "herbivore")))
        print("Average mutationProbability: " + str(get_average(mutationProbability, "herbivore")))
    print()
    print()
    print("Carnivores:")
    print()
    print("Population: " + str(species.count("carnivore")))
    if species.count("carnivore") > 0:
        print("Average foodStorage: " + str(get_average(foodStorage, "carnivore")))
        print("Average hunger: " + str(get_average(hunger, "carnivore")))
        print("Average sight: " + str(get_average(sight, "carnivore")))
        print("Average speed: " + str(get_average(speed, "carnivore")))
        print("Average cloneSpacing: " + str(get_average(cloneSpacing, "carnivore")))
        print("Average timeToClone: " + str(get_average(timeToClone, "carnivore")))
        print("Average agility: " + str(get_average(agility, "carnivore")))
        print("Average mutationProbability: " + str(get_average(mutationProbability, "carnivore")))
    print()
    print()
    print()

def killAnimal(num):
    global turtles
    global foodStorage
    global hunger
    global sight
    global speed
    global cloneSpacing
    global timeToClone
    global agility
    global direction
    global plants
    global mutationProbability
    global species
    
    turtles[num].hideturtle()
    turtles.pop(num)
    foodStorage.pop(num)
    hunger.pop(num)
    sight.pop(num)
    speed.pop(num)
    cloneSpacing.pop(num)
    timeToClone.pop(num)
    agility.pop(num)
    direction.pop(num)
    mutationProbability.pop(num)
    species.pop(num)

def simulate():
    global turtles
    global foodStorage
    global hunger
    global sight
    global speed
    global cloneSpacing
    global timeToClone
    global agility
    global direction
    global plants
    global mutationProbability
    global species

    i=0
    while i < len(turtles):
        hunger[i] -= speed[i]
        timeToClone[i] -= 1
        distanceToNearestPlant = 9999999
        headingToNearestPlant = turtles[i].heading()
        if species[i] == "herbivore":
            for p in plants:
                if turtles[i].distance(p) < distanceToNearestPlant:
                    distanceToNearestPlant = turtles[i].distance(p)
                    headingToNearestPlant = turtles[i].towards(p)

            distanceToNearestPred = 9999999
            for t in turtles:
                if turtles[i].distance(t) < distanceToNearestPred and species[turtles.index(t)] == "carnivore" and turtles[i].distance(t) < sight[i]: # run away from nearest carnivore
                    distanceToNearestPred = turtles[i].distance(t)
                    headingToNearestPlant = turtles[i].towards(t) + 180
            
        elif species[i] == "carnivore":
            for t in turtles:
                if turtles[i].distance(t) < distanceToNearestPlant and species[turtles.index(t)] == "herbivore":
                    distanceToNearestPlant = turtles[i].distance(t)
                    headingToNearestPlant = turtles[i].towards(t)


        if distanceToNearestPlant > sight[i]:
            headingToNearestPlant = turtles[i].towards(random.choice([0, 200, -200]), random.choice([0, 200, -200])) # can't see anymore if out of range, and wanders randomly on the map

        if turtles[i].heading() - headingToNearestPlant < agility[i] and turtles[i].heading() - headingToNearestPlant > - agility[i]:
            turtles[i].setheading(headingToNearestPlant)
        elif turtles[i].heading() - headingToNearestPlant > 0 and turtles[i].heading() - headingToNearestPlant < 180:
            turtles[i].right(agility[i])
        else:
            turtles[i].left(agility[i])

        if distanceToNearestPlant < speed[i]:
            turtles[i].forward(distanceToNearestPlant)
        else:
            turtles[i].forward(speed[i])

        if species[i] == "herbivore": # eating
            p = 0
            while p < len(plants):
                if turtles[i].distance(plants[p]) < 5:
                    plants[p].hideturtle()
                    plants.pop(p)
                    hunger[i] += 60
                    if hunger[i] > foodStorage[i]:
                        hunger[i] = foodStorage[i]

                else:
                    p += 1

        elif species[i] == "carnivore": # eating
            a = 0
            while a < len(turtles):
                if turtles[i].distance(turtles[a]) < 10 and species[a] == "herbivore":
                    hunger[i] += hunger[a] * 2
                    if hunger[i] > foodStorage[i]:
                        hunger[i] = foodStorage[i]
                    killAnimal(a)
                    if a < i:
                        i-= 1

                else:
                    a += 1

        if timeToClone[i] <= 0 and hunger[i] >= foodStorage[i] * 1/2: # clone animal 
            timeToClone[i] = cloneSpacing[i]
            
            turtles.append(turtles[i].clone())
            if random.randint(0, 100) > mutationProbability[i]:
                foodStorage.append(foodStorage[i])
            else:
                foodStorage.append(random.randint(50, 600))

            if random.randint(0, 100) > mutationProbability[i]:
                sight.append(sight[i])
            else:
                sight.append(random.randint(20, 180))

            if random.randint(0, 100) > mutationProbability[i]:
                speed.append(speed[i])
            else:
                speed.append(random.randint(1, 10))

            if random.randint(0, 100) > mutationProbability[i]:
                new_cloneSpacing = cloneSpacing[i]
            else:
                new_cloneSpacing = random.randint(15, 100)
            cloneSpacing.append(new_cloneSpacing)
            timeToClone.append(new_cloneSpacing)

            if random.randint(0, 100) > mutationProbability[i]:
                agility.append(agility[i])
            else:
                agility.append(agility[i] + random.randint(-5, 5))

            if random.randint(0, 100) > mutationProbability[i]:
                mutationProbability.append(mutationProbability[i])
            else:
                mutationProbability.append(random.randint(0, 50))

            direction.append(random.randint(0, 359))
            species.append(species[i])
            hunger.append(hunger[i])
        
        if hunger[i] > 0:
            i += 1
        else:
            killAnimal(i) # died from starvation

        
turtle.Screen().listen()

init(200, 20, 3)

genNum = 0
while len(turtles) > 0:

    if genNum/2 == int(genNum/2): # add a new plant every 2 iterations
        t = turtle.Turtle()
        t.shape("circle")
        t.speed(0)
        t.penup()
        t.turtlesize(0.4, 0.4, 0.4)
        t.goto(random.randint(-400, 400), random.randint(-400, 400))
        t.color("light green")
        plants.append(t)

    
    if genNum/5 == int(genNum/5):
        print_report()
    
    simulate()
    turtle.Screen().update()
    
    genNum += 1
    print("Generations: "+ str(genNum))
    
print()
print("Your ecosystem is extinct")
