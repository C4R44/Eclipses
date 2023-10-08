import pygame
import os
import sys

pygame.init()

#pygame.draw.circle(WIN, (255, 255, 0), (WIDTH // 2, HEIGHT // 2), SUN_DIAMETER // 2) #sun
#WIN.blit(EARTH, (EARTH_WIDTH, EARTH_HEIGHT)) #earth
#pygame.draw.circle(WIN, (200, 200, 200), MOON.center, MOON.width // 2) #moon

WIDTH, HEIGHT = 1000, 800
FPS = 60

MOON_DIAMETER = 10
SUN_DIAMETER = 40
EARTH_DIAMETER = 100

MOON_HEIGHT = HEIGHT / 2 - MOON_DIAMETER / 2
MOON_WIDTH = WIDTH / 2 - MOON_DIAMETER / 2

SUN_HEIGHT = HEIGHT / 2 - SUN_DIAMETER / 2
SUN_WIDTH = WIDTH / 2 - SUN_DIAMETER / 2

EARTH_HEIGHT = HEIGHT/2 - EARTH_DIAMETER/2 
EARTH_WIDTH = WIDTH/2 - EARTH_DIAMETER/2 

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Eclipse")

MOON = pygame.Rect(MOON_WIDTH - 200, MOON_HEIGHT, MOON_DIAMETER, MOON_DIAMETER)

EARTH = pygame.image.load(os.path.join('assets', 'earth.png'))
EARTH = pygame.transform.scale(EARTH, (100, 100))

TOTAL = pygame.image.load(os.path.join('assets', 'total.png'))
TOTAL = pygame.transform.scale(TOTAL, (200, 200))

BACKGROUND = pygame.image.load(os.path.join('assets', 'background.jpeg'))
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))



def movement(gets_pressed):
    if gets_pressed[pygame.K_LEFT]:
        MOON.x -= 5
    if gets_pressed[pygame.K_RIGHT]:
        MOON.x += 5


def intro():
    font = pygame.font.Font(None, 100)
    text = font.render("ECLIPSES", True, (200, 200, 200))
    WIN.blit(text, (WIDTH // 2 - 165, HEIGHT // 2 - 200))

    text = pygame.font.Font(None, 50).render("[Press space to continue]", True, (200, 200, 200))
    WIN.blit(text, (WIDTH // 2 - 200, HEIGHT // 2))



def page1():
    MOON = pygame.Rect(300, MOON_HEIGHT, MOON_DIAMETER, MOON_DIAMETER)

    pygame.draw.circle(WIN, (255, 255, 0), (WIDTH + 3510, HEIGHT // 2), 4000) #sun

    pygame.draw.circle(WIN, (200, 200, 200), MOON.center, 10) #moon
    font = pygame.font.Font(None, 25)
    text = font.render("Why does the moon and sun appear to be the same size? ", True, (200, 200, 200))
    WIN.blit(text, (15, 50))
    text = font.render("Why does the moon and sun appear to be the same size? ", True, (200, 200, 200))
    WIN.blit(text, (15, 50))
    text = font.render("Why does the moon and sun appear to be the same size? ", True, (200, 200, 200))
    WIN.blit(text, (15, 50))
    text = font.render("Why does the moon and sun appear to be the same size? ", True, (200, 200, 200))
    WIN.blit(text, (15, 50))

    text = font.render("This is because the moon is 400 times smaller than the sun,  ", True, (200, 200, 200))
    WIN.blit(text, (15, 80))
    text = font.render("but it is 400 times closer to the earth than the sun. ", True, (200, 200, 200))
    WIN.blit(text, (15, 100))
    text = font.render("Therefore, the moon and the sun appear to be the same size, ", True, (200, 200, 200))
    WIN.blit(text, (15, 120))
    text = font.render("so will result in a total annular eclipse.  ", True, (200, 200, 200))
    WIN.blit(text, (15, 140))
    text = font.render("However, the moon is obviously much smaller than the sun,", True, (200, 200, 200))
    WIN.blit(text, (15, 160))
    text = font.render("so it doesn’t completely cover the sun when  ", True, (200, 200, 200))
    WIN.blit(text, (15, 180))
    text = font.render("the eclipse occurs. This results in an annular solar eclipse. ", True, (200, 200, 200))
    WIN.blit(text, (15, 200))
    text = font.render("This makes the eclipse look as if there is a  ", True, (200, 200, 200))
    WIN.blit(text, (15, 220))
    text = font.render("shiny fire ring in the sky. ", True, (200, 200, 200))
    WIN.blit(text, (15, 240))

    
    font = pygame.font.Font(None, 25)
    text = font.render("[Press space to continue]", True, (200, 200, 200))
    WIN.blit(text, (150, HEIGHT // 2 + 300))



def page2():
    pygame.draw.circle(WIN, (255, 255, 0), (300, HEIGHT // 2), 40) #sun
    WIN.blit(EARTH, (650, EARTH_HEIGHT)) #earth
    pygame.draw.circle(WIN, (200, 200, 200), (MOON_WIDTH, HEIGHT//2), 40) #moon

    font = pygame.font.Font(None, 25)
    text = font.render("Why does the sun, earth and moon align in the first place? ", True, (200, 200, 200))
    WIN.blit(text, (250, 100))
    text = font.render("Why does the sun, earth and moon align in the first place? ", True, (200, 200, 200))
    WIN.blit(text, (250, 100))
    text = font.render("Why does the sun, earth and moon align in the first place? ", True, (200, 200, 200))
    WIN.blit(text, (250, 100))
    text = font.render("Why does the sun, earth and moon align in the first place? ", True, (200, 200, 200))
    WIN.blit(text, (250, 100))


    text = font.render("The sun orbits the sun in a slightly elliptical way and the moon orbits the earth in a slightly ", True, (200, 200, 200))
    WIN.blit(text, (130, 130))
    text = font.render("elliptical way as well. When the moon spins around the earth, at some point it will block the", True, (200, 200, 200))
    WIN.blit(text, (130, 150))
    text = font.render("sun and since the sun is staying still, the three planets create a ‘row’ of planets which gives ", True, (200, 200, 200))
    WIN.blit(text, (130, 170))
    text = font.render("rise to an eclipse.", True, (200, 200, 200))
    WIN.blit(text, (430, 190))

    font = pygame.font.Font(None, 25)
    text = font.render("[Press space to continue]", True, (200, 200, 200))
    WIN.blit(text, (WIDTH// 2 - 110, HEIGHT - 100))

def page3():
    font = pygame.font.Font(None, 25)
    text = font.render("Did you know that when the moon casts a shadow on the earth there are 2 types of shadows?", True, (200, 200, 200))
    WIN.blit(text, (40, 250))
    text = font.render("Did you know that when the moon casts a shadow on the earth there are 2 types of shadows?", True, (200, 200, 200))
    WIN.blit(text, (40, 250))
    text = font.render("Did you know that when the moon casts a shadow on the earth there are 2 types of shadows?", True, (200, 200, 200))
    WIN.blit(text, (40, 250))
    text = font.render("Did you know that when the moon casts a shadow on the earth there are 2 types of shadows?", True, (200, 200, 200))
    WIN.blit(text, (40, 250))


    text = font.render("If you put your hand over a surface, there will be areas which are darker and others which", True, (200, 200, 200))
    WIN.blit(text, (40, 280))
    text = font.render("are lighter. The darker, smaller shadow is called an umbra. If you are in a location that is ", True, (200, 200, 200))
    WIN.blit(text, (40, 300))
    text = font.render("covered by this umbra, then the sun will be blocked out from your perspective, so the sky will ", True, (200, 200, 200))
    WIN.blit(text, (40, 320))
    text = font.render("be dark! The umbral shadow doesn’t stay at one point on earth, it actually moves because ", True, (200, 200, 200))
    WIN.blit(text, (40, 340))
    text = font.render("the earth itself moves and this causes a ‘path of totality’. What is fascinating, is that in this ", True, (200, 200, 200))
    WIN.blit(text, (40, 360))
    text = font.render("path, the sun is completely blocked out as the total solar eclipse occurs.", True, (200, 200, 200))
    WIN.blit(text, (40, 380))
    text = font.render("(!DO NOT WATCH THIS WITH A NAKED EYE AS THE RADIATION FROM SUN WILL DAMAGE YOUR EYES!)", True, (200, 200, 200))
    WIN.blit(text, (40, 410))
    text = font.render("The second type is called the penumbra which is a larger and lighter shadow. This type of ", True, (200, 200, 200))
    WIN.blit(text, (40, 440))
    text = font.render("shadow only partially blocks out the sun, so it will not completely block out the sun. This type ", True, (200, 200, 200))
    WIN.blit(text, (40, 460))
    text = font.render("of shadow causes a partial solar eclipse.", True, (200, 200, 200))
    WIN.blit(text, (40, 480))

    font = pygame.font.Font(None, 25)
    text = font.render("[Press space to continue]", True, (200, 200, 200))
    WIN.blit(text, (WIDTH// 2 - 110, HEIGHT - 100))


def page4():
    #total solar eclipse
    pygame.draw.circle(WIN, (255, 255, 0), (MOON_WIDTH, MOON_HEIGHT+5), 80) #sun
    pygame.draw.circle(WIN, (200, 200, 200), MOON.center, 80) #moon


    font = pygame.font.Font(None, 50)
    text = font.render("Total Solar Eclipse", True, (200, 200, 200))
    WIN.blit(text, (WIDTH//2 - 150, HEIGHT // 2 - 300))

    font = pygame.font.Font(None, 25)
    text = font.render("[Use arrow keys to move the moon]", True, (200, 200, 200))
    WIN.blit(text, (WIDTH // 2 - 140, HEIGHT // 2 + 200))

    font = pygame.font.Font(None, 25)
    text = font.render("The moon is closest to the earth at a point called the perigee, which is around ¼ way of the ", True, (200, 200, 200))
    WIN.blit(text, (150, HEIGHT // 2 - 250))
    text = font.render("orbit from the left, which gives rise to a total solar eclipse, the coolest and most mesmerising ", True, (200, 200, 200))
    WIN.blit(text, (150, HEIGHT // 2 - 230))
    text = font.render("of them all!", True, (200, 200, 200))
    WIN.blit(text, (450, HEIGHT // 2 - 210))


    font = pygame.font.Font(None, 25)
    text = font.render("[Press space to continue]", True, (200, 200, 200))
    WIN.blit(text, (WIDTH// 2 - 110, HEIGHT - 100))

def page5():
    #annular solar eclipse
    
    pygame.draw.circle(WIN, (255, 255, 0), (MOON_WIDTH, MOON_HEIGHT+5), 80) #sun
    pygame.draw.circle(WIN, (200, 200, 200), MOON.center, 70) #moon


    font = pygame.font.Font(None, 50)
    text = font.render("Annular Solar Eclipse", True, (200, 200, 200))
    WIN.blit(text, (WIDTH//2 - 170, HEIGHT // 2 - 300))

    font = pygame.font.Font(None, 25)
    text = font.render("[Use arrow keys to move the moon]", True, (200, 200, 200))
    WIN.blit(text, (WIDTH // 2 - 140, HEIGHT // 2 + 200))

    font = pygame.font.Font(None, 25)
    text = font.render("An annular eclipse occurs when the moon is further from earth so that it isn't seen to be covering ", True, (200, 200, 200))
    WIN.blit(text, (100, HEIGHT // 2 - 250))
    text = font.render("the sun completely ", True, (200, 200, 200))
    WIN.blit(text, (420, HEIGHT // 2 - 230))

    font = pygame.font.Font(None, 25)
    text = font.render("[Press space to continue]", True, (200, 200, 200))
    WIN.blit(text, (WIDTH// 2 - 110, HEIGHT - 100))

def page6():
    font = pygame.font.Font(None, 25)
    text = font.render("Annular Total Solar Eclipse:", True, (200, 200, 200))
    WIN.blit(text, (40, 350))
    text = font.render("Annular Total Solar Eclipse:", True, (200, 200, 200))
    WIN.blit(text, (40, 350))
    text = font.render("Annular Total Solar Eclipse:", True, (200, 200, 200))
    WIN.blit(text, (40, 350))
    text = font.render("Annular Total Solar Eclipse:", True, (200, 200, 200))
    WIN.blit(text, (40, 350))

    text = font.render("The rarest of them all … is the annular total solar eclipse (sometimes referred to as the ", True, (200, 200, 200))
    WIN.blit(text, (40, 380))
    text = font.render("hybrid solar eclipse). This is when some parts experience a total solar eclipse while the ", True, (200, 200, 200))
    WIN.blit(text, (40, 400))
    text = font.render("others experience an annual solar eclipse.", True, (200, 200, 200))
    WIN.blit(text, (40, 420))

    font = pygame.font.Font(None, 25)
    text = font.render("[Press space to continue]", True, (200, 200, 200))
    WIN.blit(text, (WIDTH// 2 - 110, HEIGHT - 100))



def page7():
    font = pygame.font.Font(None, 25)
    text = font.render("Why do only some people see these eclipses?", True, (200, 200, 200))
    WIN.blit(text, (40, 350))
    text = font.render("Why do only some people see these eclipses?", True, (200, 200, 200))
    WIN.blit(text, (40, 350))
    text = font.render("Why do only some people see these eclipses?:", True, (200, 200, 200))
    WIN.blit(text, (40, 350))
    text = font.render("Why do only some people see these eclipses?", True, (200, 200, 200))
    WIN.blit(text, (40, 350))

    text = font.render("The reason behind this is because the moon’s size is so much smaller than the size of the ", True, (200, 200, 200))
    WIN.blit(text, (40, 380))
    text = font.render("sun, meaning that at times the moon covers only a small fraction of the sun’s rays. This ", True, (200, 200, 200))
    WIN.blit(text, (40, 400))
    text = font.render("therefore means that a small shadow is created on the earth, so the umbra shadow for ", True, (200, 200, 200))
    WIN.blit(text, (40, 420))
    text = font.render("example will only some places on the planet will witness the phenomenon.", True, (200, 200, 200))
    WIN.blit(text, (40, 440))

    font = pygame.font.Font(None, 25)
    text = font.render("[Press space to continue]", True, (200, 200, 200))
    WIN.blit(text, (WIDTH// 2 - 110, HEIGHT - 100))

def page8():
    font = pygame.font.Font(None, 25)
    text = font.render("What is an eclipse season?", True, (200, 200, 200))
    WIN.blit(text, (40, 350))
    text = font.render("What is an eclipse season?", True, (200, 200, 200))
    WIN.blit(text, (40, 350))
    text = font.render("What is an eclipse season?", True, (200, 200, 200))
    WIN.blit(text, (40, 350))
    text = font.render("What is an eclipse season?", True, (200, 200, 200))
    WIN.blit(text, (40, 350))


    text = font.render("Every 173 days, for between 31 and 37 days, the Moon is lined-up perfectly to intersect the ", True, (200, 200, 200))
    WIN.blit(text, (40, 380))
    text = font.render("ecliptic (the great circle representing the sun’s apparent path). There is a short season", True, (200, 200, 200))
    WIN.blit(text, (40, 400))
    text = font.render("during which two—and occasionally three—Solar and lunar eclipses can occur. These ", True, (200, 200, 200))
    WIN.blit(text, (40, 420))
    text = font.render("eclipses don’t happen every month as the Moon’s orbit isn’t horizontally located. Imagine a .", True, (200, 200, 200))
    WIN.blit(text, (40, 440))
    text = font.render("ring held horizontally. This is exactly how the Moon’s orbit looks like. Therefore, the Moon ", True, (200, 200, 200))
    WIN.blit(text, (40, 460))
    text = font.render("sometimes rises above and below the Earth, not casting a shadow on it, therefore there is no ", True, (200, 200, 200))
    WIN.blit(text, (40, 480))
    text = font.render("eclipse at these times. The Moon’s orbit is raised at around 5 degrees from the ecliptic and it ", True, (200, 200, 200))
    WIN.blit(text, (40, 500))
    text = font.render("takes 34.5 days ( which is an ecliptic season) for the Sun, Earth and Moon to come to that ", True, (200, 200, 200))
    WIN.blit(text, (40, 520))
    text = font.render("perfect alignment which causes an eclipse.", True, (200, 200, 200))
    WIN.blit(text, (40, 540))

    font = pygame.font.Font(None, 25)
    text = font.render("[Press space to continue]", True, (200, 200, 200))
    WIN.blit(text, (WIDTH// 2 - 110, HEIGHT - 100))


def page9():
    pygame.draw.circle(WIN, (255, 255, 0), (300, HEIGHT // 2), 40) #sun
    WIN.blit(EARTH, (EARTH_WIDTH, EARTH_HEIGHT)) #earth
    pygame.draw.circle(WIN, (200, 200, 200), (700, HEIGHT//2), 40) #moon



    font = pygame.font.Font(None, 50)
    text = font.render("Lunar Eclipses", True, (200, 200, 200))
    WIN.blit(text, (WIDTH//2 - 130, HEIGHT // 2 - 300))


    font = pygame.font.Font(None, 25)
    text = font.render("This is just the same thing as before, however it is now the Earth that casts a shadow on the ", True, (200, 200, 200))
    WIN.blit(text, (150, HEIGHT // 2 - 250))
    text = font.render("Moon when the Earth is covering the Moon from the Sun. In a solar eclipse, the Sun gets ", True, (200, 200, 200))
    WIN.blit(text, (150, HEIGHT // 2 - 230))
    text = font.render("darker. In a lunar eclipse, the Moon gets darker. There are also 2 types of eclipses, which", True, (200, 200, 200))
    WIN.blit(text, (150, HEIGHT // 2 - 210))
    text = font.render("are the same from before: umbra and penumbra, the only difference being that the shadows", True, (200, 200, 200))
    WIN.blit(text, (150, HEIGHT // 2 - 190))
    text = font.render("are now on the Moon instead of the Sun.", True, (200, 200, 200))
    WIN.blit(text, (350, HEIGHT // 2 - 170))


    font = pygame.font.Font(None, 25)
    text = font.render("[Press space to continue]", True, (200, 200, 200))
    WIN.blit(text, (WIDTH// 2 - 110, HEIGHT - 100))



def page10():
    font = pygame.font.Font(None, 50)
    text = font.render("Total Lunar Eclipse", True, (200, 200, 200))
    WIN.blit(text, (WIDTH//2 - 160, HEIGHT // 2 - 300))


    font = pygame.font.Font(None, 25)
    text = font.render(" when the Moon falls under the umbral shadow of Earth, and the Sun, Earth and Moon are ", True, (200, 200, 200))
    WIN.blit(text, (150, HEIGHT // 2 - 250))
    text = font.render("perfectly aligned. This creates a shadow over the Moon giving it an unexpected red colour. ", True, (200, 200, 200))
    WIN.blit(text, (150, HEIGHT // 2 - 230))
    text = font.render("This is because the Earth completely blocks out all of the sunlight from reaching the Moon, ", True, (200, 200, 200))
    WIN.blit(text, (148, HEIGHT // 2 - 210))
    text = font.render("which makes the Moon lose its signature white-greyish colour. Earth’s atmosphere absorbs ", True, (200, 200, 200))
    WIN.blit(text, (145, HEIGHT // 2 - 190))
    text = font.render("the other colours but it bends some sunlight toward the Moon.The longest wavelength colour ", True, (200, 200, 200))
    WIN.blit(text, (145, HEIGHT // 2 - 170))
    text = font.render("is red (looking at the Electromagnetic spectrum, red has a longer wavelength of 700nm while ", True, (200, 200, 200))
    WIN.blit(text, (148, HEIGHT // 2 - 150))
    text = font.render("purple has the shortest wavelength of 400nm) , which is inward towards the moon, giving it ", True, (200, 200, 200))
    WIN.blit(text, (150, HEIGHT // 2 - 130))
    text = font.render("that red colour! .", True, (200, 200, 200))
    WIN.blit(text, (430, HEIGHT // 2 - 110))

    WIN.blit(TOTAL, (WIDTH//2 -110, HEIGHT//2)) #total

    font = pygame.font.Font(None, 25)
    text = font.render("[Press space to continue]", True, (200, 200, 200))
    WIN.blit(text, (WIDTH// 2 - 110, HEIGHT - 100))




def page11():

    font = pygame.font.Font(None, 50)
    text = font.render("Partial Lunar Eclipse", True, (200, 200, 200))
    WIN.blit(text, (WIDTH//2 - 175, HEIGHT // 2 - 300))


    font = pygame.font.Font(None, 25)
    text = font.render("This happens when the Sun, Earth and Moon align in a way where only ½ of the Moon is ", True, (200, 200, 200))
    WIN.blit(text, (150, HEIGHT // 2 - 250))
    text = font.render("located in the umbral shadow. How to spot this lunar eclipse? You will see the Earth cover  ", True, (200, 200, 200))
    WIN.blit(text, (150, HEIGHT // 2 - 230))
    text = font.render("only a small part of the Moon, so only a small shadow will be seen.", True, (200, 200, 200))
    WIN.blit(text, (220, HEIGHT // 2 - 210))

    font = pygame.font.Font(None, 25)
    text = font.render("[Press space to continue]", True, (200, 200, 200))
    WIN.blit(text, (WIDTH// 2 - 110, HEIGHT - 100))
    
   

def page12():
    font = pygame.font.Font(None, 50)
    text = font.render("Prenumbral Lunar Eclipse", True, (200, 200, 200))
    WIN.blit(text, (WIDTH//2 - 200, HEIGHT // 2 - 300))


    font = pygame.font.Font(None, 25)
    text = font.render("The penumbral lunar eclipse is when the three planets arrange in such a way where the ", True, (200, 200, 200))
    WIN.blit(text, (150, HEIGHT // 2 - 250))
    text = font.render("Moon is located in the penumbral shadow, which causes the Moon to be completely covered ", True, (200, 200, 200))
    WIN.blit(text, (150, HEIGHT // 2 - 230))
    text = font.render("by a light shadow from Earth. This is very easy to miss!!", True, (200, 200, 200))
    WIN.blit(text, (300, HEIGHT // 2 - 210))

    font = pygame.font.Font(None, 25)
    text = font.render("[Press space to continue]", True, (200, 200, 200))
    WIN.blit(text, (WIDTH// 2 - 110, HEIGHT - 100))

def page13():
    font = pygame.font.Font(None, 25)
    text = font.render("More about the sun:", True, (200, 200, 200))
    WIN.blit(text, (40, 250))


    text = font.render("The sun’s outer layer is called the corona, which is too faint to see except when the light of ", True, (200, 200, 200))
    WIN.blit(text, (40, 275))
    text = font.render("the Sun is blocked. We use instruments called coronagraphs to block the Sun’s light and ", True, (200, 200, 200))
    WIN.blit(text, (40, 300))
    text = font.render("actually see the corona. These instruments however cannot do this properly which limits  ", True, (200, 200, 200))
    WIN.blit(text, (40, 320))
    text = font.render("scientists’ ability to view essential processes in the Sun. The Sun spurs a constant stream of  ", True, (200, 200, 200))
    WIN.blit(text, (40, 340))
    text = font.render("particles which reaches the Earth allowing us to see. It’s crazy that a star can provide so ", True, (200, 200, 200))
    WIN.blit(text, (40, 360))
    text = font.render("much light, and life! The Sun’s energy created a layer called the ionosphere which contains  ", True, (200, 200, 200))
    WIN.blit(text, (40, 380))
    text = font.render("many ions. (the word ion means a particle that has lost or gained electrons to become ", True, (200, 200, 200))
    WIN.blit(text, (40, 400))
    text = font.render("charged). This region contains many low-Earth orbit satellites. ", True, (200, 200, 200))
    WIN.blit(text, (40, 420))

    font = pygame.font.Font(None, 25)
    text = font.render("[Press space to continue]", True, (200, 200, 200))
    WIN.blit(text, (WIDTH// 2 - 110, HEIGHT - 100))


def page14():

    font = pygame.font.Font(None, 25)
    text = font.render("You can use this website to check when the next ellipses in your areas are! ", True, (200, 200, 200))
    WIN.blit(text, (40, 250))


    text = font.render("https://www.timeanddate.com/eclipse/list-total-solar.html", True, (200, 200, 200))
    WIN.blit(text, (40, 275))
    text = font.render("These are spectacular events, so make sure to see them if you can! ", True, (200, 200, 200))
    WIN.blit(text, (40, 300))
    text = font.render("If you live in the US, you can view the 2023 annular solar eclipse on October 14. It will also ", True, (200, 200, 200))
    WIN.blit(text, (40, 320))
    text = font.render("be visible to people who are situated in the Western Hemisphere. The 2024 total solar ", True, (200, 200, 200))
    WIN.blit(text, (40, 340))
    text = font.render("eclipse will happen on April 8th which will also happen in the Western Hemisphere.", True, (200, 200, 200))
    WIN.blit(text, (40, 360))

    font = pygame.font.Font(None, 25)
    text = font.render("[Press space to end]", True, (200, 200, 200))
    WIN.blit(text, (WIDTH// 2 - 90, HEIGHT - 100))


def main():
    page = 0
    run = True
    clock = pygame.time.Clock()

    while run:
        #WIN.fill((0, 0, 0))
        WIN.blit(BACKGROUND, (0, 0))
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        gets_pressed = pygame.key.get_pressed()
        movement(gets_pressed)

        if page == 0:
            
            intro()

            if gets_pressed[pygame.K_SPACE]:
                page += 1
                pygame.time.delay(100)

        elif page == 1:
            page1()
            
            if gets_pressed[pygame.K_SPACE]:
                page += 1
                pygame.time.delay(100)

        elif page == 2:
            page2()
            if gets_pressed[pygame.K_SPACE]:
                page += 1
                pygame.time.delay(100)

        elif page == 3:
            page3()
            if gets_pressed[pygame.K_SPACE]:
                page += 1
                pygame.time.delay(100)

        elif page == 4:
            page4()
            if gets_pressed[pygame.K_SPACE]:
                page += 1
                MOON.x = MOON_WIDTH - 200
                pygame.time.delay(100)

        elif page == 5:
            page5()
            if gets_pressed[pygame.K_SPACE]:
                page += 1

                pygame.time.delay(100)

        elif page == 6:
            page6()
            if gets_pressed[pygame.K_SPACE]:
                page += 1

                pygame.time.delay(100)

        elif page == 7:
            page7()
            if gets_pressed[pygame.K_SPACE]:
                page += 1

                pygame.time.delay(100)

        elif page == 8:
            page8()
            if gets_pressed[pygame.K_SPACE]:
                page += 1

                pygame.time.delay(100)

        elif page == 9:
            page9()
            if gets_pressed[pygame.K_SPACE]:
                page += 1

                pygame.time.delay(100)

        elif page == 10:
            page10()
            if gets_pressed[pygame.K_SPACE]:
                page += 1

                pygame.time.delay(100)


        elif page == 11:
            page11()
            if gets_pressed[pygame.K_SPACE]:
                page += 1

                pygame.time.delay(100)

        elif page == 12:
            page12()
            if gets_pressed[pygame.K_SPACE]:
                page += 1

                pygame.time.delay(100)

        elif page == 13:
            page13()
            if gets_pressed[pygame.K_SPACE]:
                page += 1

                pygame.time.delay(100)


        elif page == 14:
            page14()
            if gets_pressed[pygame.K_SPACE]:
                run = False


        
                


        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
