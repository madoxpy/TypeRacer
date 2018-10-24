from pygame import*
from random import choice, randint


def rendertext(text,color,position):
		text = Font.render(text,True,color)
		screen.blit(text, position)

dictionary= ["apple","car","plane","chair","wall",
			 "heart","photo","bus","cup","bucket",
			 "water","taxi","race","bike","mouse",
			 "paper","pen","python","bed","sofa"]
colors=[(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255),(0,255,128),(128,0,255),(255,128,0)]


class Word(object):
	def __init__(self):
		self.speed=5
		self.x = -10
		self.y = randint(10,500)
		self.color = choice(colors)
		self.caption = choice(dictionary)
		
	def update(self):
		self.x=self.x+self.speed

	def draw(self):
		text = Font.render(self.caption,True,self.color)
		screen.blit(text, (self.x,self.y))
    

init()
screen = display.set_mode((1200,600))
display.set_caption("Type racer")
clock=time.Clock()
Font=font.SysFont("Comis Sans",48)


caption=""
level = 0
points = 0
lifes = 5

words=[]
for i in range (level):
	words.append(Word())

end = False
while not end:
	for z in event.get():
		if z.type == QUIT:
			end = True
		if z.type == KEYDOWN:
			for k in range(K_a,K_z+1):
				if z.key==k:
					caption=caption+chr(k)
			if z.key==K_SPACE:
				if lifes > 0:
					caption=caption+" "    
				else:
					caption=""
					level = 0
					points = 0
					lifes = 5
					words=[]
					for i in range (level):
						words.append(Word())
			if z.key==K_RETURN:
				caption=""
			if z.key==K_BACKSPACE:
				caption=caption[0:-1]        
        
	screen.fill((0,0,0))   
	if lifes>0:
		rendertext("Lifes: "+str(lifes),(255,255,255),(600,560))
		rendertext("Level: "+str(level),(255,255,255),(800,560))
		rendertext("Points: "+str(points),(255,255,255),(1000,560))
		rendertext(caption,(255,255,255),(0,560))
		
		
		for word in words:
			word.update()
			word.draw()
			if word.caption==caption:
				caption=""
				words.remove(word)
				points = points + 1
			if word.x>1300:
				lifes=lifes-1
				words.remove(word)


		if len(words)<level:
			words.append(Word())

		if points==10*(level):
			points = points +1
			level = level +1
	else:
		rendertext("Game over",(255,255,255),(510,250))
		rendertext("You got "+str(points)+" points",(255,255,255),(450,300))
		rendertext("Press [space] to start new game",(255,255,255),(360,350))

	clock.tick(20)
	display.flip()