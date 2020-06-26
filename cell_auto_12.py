import pygame
import random
import matplotlib.pyplot as plt

SIZE = WIDTH, HEIGHT = 1920, 1080 #the width and height of our screen
BACKGROUND_COLOR = pygame.Color(56, 19, 140) #The background colod of our window
# BACKGROUND_COLOR = pygame.Color(256, 256, 256, 0) #The background colod of our window

BOARDSIZE = 24 # number of tiles on one edge
BOARDMULT = BOARDSIZE / 12

FPS = 60 #Frames per second


class FireSprite(pygame.sprite.Sprite):
    images = []
    images.append(pygame.image.load('images/fire1.png'))
    images.append(pygame.image.load('images/fire2.png'))
    images.append(pygame.image.load('images/fire3.png'))
    images.append(pygame.image.load('images/fire4.png'))
    images.append(pygame.image.load('images/fire5.png'))

    images = [pygame.transform.smoothscale(x, (int(55 / BOARDMULT), int(77 / BOARDMULT))) for x in images]

    def __init__(self, x, y):
        super(FireSprite, self).__init__()
        #adding all the images to sprite array

        #index value to get the image from the array
        #initially it is 0 
        self.index = 0

        #now the image that we will display will be the index from the image array 
        self.image = FireSprite.images[self.index]

        #creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite 
        self.rect = pygame.Rect(13 + x * 80 / BOARDMULT, 5 + y * 80 / BOARDMULT, 77 / BOARDMULT, 77 / BOARDMULT)

    def update(self):
        #when the update method is called, we will increment the index
        self.index += 1

        #if the index is larger than the total images
        if self.index >= len(FireSprite.images) * 6:
            #we will make the index to 0 again
            self.index = 0
        
        #finally we will update the image that will be displayed
        self.image = FireSprite.images[self.index // 6 ]


class TreeSprite(pygame.sprite.Sprite):
    images = []
    for i in range(240):
        images.append(pygame.image.load('images/tree' + '0' * (5 - len(str(i))) + str(i)  +  '.png'))
    images = [pygame.transform.smoothscale(x, (int(77 / BOARDMULT), int(77 / BOARDMULT))) for x in images]
    def __init__(self, x, y):
        super(TreeSprite, self).__init__()
        #adding all the images to sprite array

        #index value to get the image from the array
        #initially it is 0 
        self.index = 0

        #now the image that we will display will be the index from the image array 
        self.image = TreeSprite.images[self.index]

        #creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite 
        self.rect = pygame.Rect(x * 80 / BOARDMULT, 5 + y * 80 / BOARDMULT, 77 / BOARDMULT, 77 / BOARDMULT)

    def update(self):
        #when the update method is called, we will increment the index
        self.index += 1

        #if the index is larger than the total images
        if self.index >= len( TreeSprite.images):
            #we will make the index to 0 again
            self.index = 0
        
        #finally we will update the image that will be displayed
        self.image = TreeSprite.images[self.index]


class PlantSprite(pygame.sprite.Sprite):
    images = []
    for i in range(240):
        images.append(pygame.image.load('images/plant' + '0' * (5 - len(str(i))) + str(i)  +  '.png'))
    images = [pygame.transform.smoothscale(x, (int(77 / BOARDMULT), int(77 / BOARDMULT))) for x in images]
    def __init__(self, x, y):
        super(PlantSprite, self).__init__()
        #adding all the images to sprite array

        #index value to get the image from the array
        #initially it is 0 
        self.index = 0

        #now the image that we will display will be the index from the image array 
        self.image = PlantSprite.images[self.index]

        #creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite 
        self.rect = pygame.Rect(x * 80 / BOARDMULT, 5 + y * 80 / BOARDMULT, 77 / BOARDMULT, 77 / BOARDMULT)

    def update(self):
        #when the update method is called, we will increment the index
        self.index += 1

        #if the index is larger than the total images
        if self.index >= len( PlantSprite.images):
            #we will make the index to 0 again
            self.index = 0
        
        #finally we will update the image that will be displayed
        self.image = PlantSprite.images[self.index]


def main():
    #initializing pygame
    pygame.init()

    tree_pops = []


    treeSprites = [[TreeSprite(x, y) for x in range(BOARDSIZE)] for y in range(BOARDSIZE)]
    treeGroup = pygame.sprite.Group()
    fireSprites = [[FireSprite(x, y) for x in range(BOARDSIZE)] for y in range(BOARDSIZE)]
    fireGroup = pygame.sprite.Group()
    plantSprites = [[PlantSprite(x, y) for x in range(BOARDSIZE)] for y in range(BOARDSIZE)]
    plantGroup = pygame.sprite.Group(plantSprites[0][0])

    #getting the screen of the specified size
    screen = pygame.display.set_mode(SIZE)

    #getting the pygame clock for handling fps
    clock = pygame.time.Clock()

    counter = 0
    click = 0
    draw_fire = False


    while True:
        click += 1
        counter += 1
        tree_pops.append(len(treeGroup))
        # if counter % 2 == 0:
        if True:

            # Fire burning and propogating queueing
            newFires = []
            plantDie = []

            for i in range(BOARDSIZE):
                for j in range(BOARDSIZE):
                    if fireSprites[i][j] in fireGroup:
                        fireGroup.remove(fireSprites[i][j])
                        for a in range(-1, 2, 1):
                            for b in range(-1, 2, 1):
                                if a == b == 0:
                                    pass
                                    # continue
                                if i + a >= 0 and i + a <= BOARDSIZE - 1 and j + b >= 0 and j + b <= BOARDSIZE - 1:
                                    if plantSprites[i+a][j+b] in plantGroup:
                                        newFires.append((i+a, j+b))

                    if treeSprites[i][j] in treeGroup:
                        plantCount = 0
                        for a in range(-1, 2, 1):
                            for b in range(-1, 2, 1):
                                if a == b == 0:
                                    pass
                                    # continue
                                if i + a >= 0 and i + a <= BOARDSIZE - 1 and j + b >= 0 and j + b <= BOARDSIZE - 1:
                                    if plantSprites[i+a][j+b] in plantGroup:
                                        plantCount += 1
                        if plantCount > 3:
                            plantDie.append((i, j))

                    


            # Processing queue
            for fire in newFires:
                fireGroup.add(fireSprites[fire[0]][fire[1]])
                plantGroup.remove(plantSprites[fire[0]][fire[1]])

            for tree in plantDie:
                treeGroup.remove(treeSprites[tree[0]][tree[1]])

            
            # Randomly add tree
            if counter % 2 == 0:
                works = False
                while not works and len(treeGroup) < BOARDSIZE ** 2:
                    rand_x, rand_y = random.randint(0, BOARDSIZE - 1) , random.randint(0, BOARDSIZE - 1)
                    if treeSprites[rand_x][rand_y] in treeGroup or fireSprites[rand_x][rand_y] in fireGroup or plantSprites[rand_x][rand_y] in plantGroup:
                        continue
                    treeGroup.add(treeSprites[rand_x][rand_y])
                    works = True
            
            # Randomly add invasive plant
            if counter % 1 == 0: 
                works = False
                trys = 0
                while not works and trys < 10:
                    rand_x, rand_y = random.randint(0, BOARDSIZE - 1) , random.randint(0, BOARDSIZE - 1)
                    if treeSprites[rand_x][rand_y] in treeGroup or fireSprites[rand_x][rand_y] in fireGroup or plantSprites[rand_x][rand_y] in plantGroup:
                        trys += 1
                        continue
                    plantGroup.add(plantSprites[rand_x][rand_y])
                    works = True

        
        # new Fires every 4 ticks
        if counter % 4 == 0:
            works = False
            while not works and len(treeGroup) < BOARDSIZE ** 2:
                rand_x, rand_y = random.randint(0, BOARDSIZE - 1) , random.randint(0, BOARDSIZE - 1)
                if plantSprites[rand_x][rand_y] in plantGroup:
                    fireGroup.add(fireSprites[rand_x][rand_y])
                    treeGroup.remove(plantSprites[rand_x][rand_y])
                works = True
            

        if draw_fire:
            fireGroup.add(fireSprites[4][4])

        #getting the events
        event = pygame.event.get()

        #if the event is quit means we clicked on the close window button
        for e in event:
            if e.type == pygame.QUIT:
                #quit the game
                plt.plot(tree_pops)
                plt.show()
                pygame.quit()
                quit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                draw_fire = True
            if e.type == pygame.MOUSEBUTTONUP:
                draw_fire = False

        #updating the sprite
        treeGroup.update()
        fireGroup.update()

        #filling the screen with background color
        screen.fill(BACKGROUND_COLOR)

        #drawing the sprite
        treeGroup.draw(screen)
        fireGroup.draw(screen)
        plantGroup.draw(screen)


        #updating the display
        pygame.display.update()


        # pygame.image.save(screen, 'shots/screenshot' + str(click) + '.png')

        #finally delaying the loop to with clock tick for 10fps 
        clock.tick(40 )

if __name__ == '__main__':
    main()