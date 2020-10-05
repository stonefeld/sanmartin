import pygame as pg
import pandas as pd
import time
import math

pg.init()


class Sound(object):
    def __init__(self, location):
        self.sound = pg.mixer.Sound(location)
        self.sound.set_volume(0.5)
        return

    def play(self):
        self.sound.play()
        return

class Music(object):
    def __init__(self, location):
        self.music = pg.mixer.music.load(location)
        pg.mixer.music.set_volume(0.25)
        return

    def play(self):
        pg.mixer.music.play(-1)
        return

    def stop(self):
        pg.mixer.music.stop()
        return

class Personajes(object):
    def __init__(self):
        resize = 4
        self.sprites = [
            [pg.transform.scale(pg.image.load("./sprites/sm bb 27x25.png"), (27 * resize, 25 * resize))],
            [pg.transform.scale(pg.image.load("./sprites/sm nene 23x29.png"), (23 * resize, 29 * resize)), pg.transform.scale(pg.image.load("./sprites/sm nene boca abierta.png"), (23 * resize, 29 * resize)), pg.transform.scale(pg.image.load("./sprites/sm nene oojos cerrados.png"), (23 * resize, 29 * resize))],
            [pg.transform.scale(pg.image.load("./sprites/sm adulto 27x43.png"), (27 * resize, 43 * resize)), pg.transform.scale(pg.image.load("./sprites/sm adulto boca abierta.png"), (27 * resize, 43 * resize)), pg.transform.scale(pg.image.load("./sprites/sm adulto ojos cerrados.png"), (27 * resize, 43 * resize))],
            [pg.transform.scale(pg.image.load("./sprites/sm viejo.png"), (23 * resize, 33 * resize)), pg.transform.scale(pg.image.load("./sprites/sm viejo boca abierta.png"), (23 * resize, 33 * resize)), pg.transform.scale(pg.image.load("./sprites/sm viejo ojos cerrados.png"), (23 * resize, 33 * resize))],
            [pg.transform.scale(pg.image.load("./sprites/sargentom kabral.png"), (24 * resize, 49 * resize)), pg.transform.scale(pg.image.load("./sprites/sargentom kabral boca abierta.png"), (24 * resize, 49 * resize)), pg.transform.scale(pg.image.load("./sprites/sargentom kabral ojos cerrados.png"), (24 * resize, 49 * resize))],
            [pg.transform.scale(pg.image.load("./sprites/remedios 14años 22x38.png"), (22 * resize, 38 * resize)), pg.transform.scale(pg.image.load("./sprites/remedios 14años boca abierta.png"), (22 * resize, 38 * resize)), pg.transform.scale(pg.image.load("./sprites/remedios 14años ojos cerrados.png"), (22 * resize, 38 * resize))],
            [pg.transform.scale(pg.image.load("./sprites/remedios embarazada 14años  ._..png"), (23 * resize, 45 * resize)), pg.transform.scale(pg.image.load("./sprites/remedios embarazada 14años  ._. boca abierta.png"), (23 * resize, 45 * resize)), pg.transform.scale(pg.image.load("./sprites/remedios embarazada 14años  ._. ojos cerrados.png"), (23 * resize, 45 * resize))],
            [pg.transform.scale(pg.image.load("./sprites/granaderos sin caballo.png"), (800, 200))],
            [pg.transform.scale(pg.image.load("./sprites/remedios 25años.png"), (22 * resize, 35 * resize)), pg.transform.scale(pg.image.load("./sprites/remedios 25años boca abierta.png"), (22 * resize, 35 * resize)), pg.transform.scale(pg.image.load("./sprites/remedios 25años ojos cerrados.png"), (22 * resize, 35 * resize))],
            [pg.transform.scale(pg.image.load("./sprites/hija 7años 18x28.png"), (18 * resize, 28 * resize)), pg.transform.scale(pg.image.load("./sprites/hija 7años boca abierta.png"), (18 * resize, 28 * resize)), pg.transform.scale(pg.image.load("./sprites/hija 7años ojos cerrados.png"), (18 * resize, 28 * resize))],
            [pg.transform.scale(pg.image.load("./sprites/game over.png"), (45 * resize, 46 * resize))],
            [pg.transform.scale(pg.image.load("./sprites/martillom.png"), (31 * resize, 32 * resize))],
            [pg.transform.scale(pg.image.load("./sprites/plantita wall-e.png"), (19 * resize, 25 * resize))],
            [pg.transform.scale(pg.image.load("./sprites/guitarra de lolo.png"), (35 * resize, 32 * resize))],
            [pg.transform.scale(pg.image.load("./sprites/peon ajedrezz.png"), (90 * resize, 29 * resize))],
            [pg.transform.scale(pg.image.load("./sprites/good ending.png"), (45 * resize, 34 * resize))]
        ]
        self.spriteCountPrimer = 0
        self.spriteCountSegundo = 0
        return

    def render(self, screen, spritesList):
        o = 10
        primerSprite = 0
        segundoSprite = 0
        primer = True
        posK = 0
        for i in range(len(spritesList)):
            if spritesList[i] != 'k':
                if primer:
                    primerSprite += int(spritesList[i]) * o
                    o /= 10

                else:
                    segundoSprite += int(spritesList[i]) * o
                    o /= 10

            else:
                if i == 1:
                    primerSprite /= 10

                primer = False
                posK = i + 1
                o = 10

        if not primer:
            if len(spritesList) - posK == 1:
                segundoSprite /= 10

            segundoSprite -= 1
            if self.spriteCountSegundo >= len(self.sprites[int(segundoSprite)]):
                self.spriteCountSegundo = 0

            if segundoSprite == 7:
                spriteRect = self.sprites[int(segundoSprite)][self.spriteCountSegundo].get_rect()
                screen.blit(pg.transform.flip(self.sprites[int(segundoSprite)][self.spriteCountSegundo], True, False), (1, 200 - spriteRect.height - 3))
                self.spriteCountSegundo += 1
            else:
                spriteRect = self.sprites[int(segundoSprite)][self.spriteCountSegundo].get_rect()
                screen.blit(pg.transform.flip(self.sprites[int(segundoSprite)][self.spriteCountSegundo], True, False), (10, 200 - spriteRect.height - 3))
                self.spriteCountSegundo += 1

        else:
            if i == 0:
                primerSprite /= 10

        primerSprite -= 1
        if self.spriteCountPrimer >= len(self.sprites[int(primerSprite)]):
            self.spriteCountPrimer = 0

        spriteRect = self.sprites[int(primerSprite)][self.spriteCountPrimer].get_rect()
        screen.blit(self.sprites[int(primerSprite)][self.spriteCountPrimer], (screen.get_width() - spriteRect.width -  10, 200 - spriteRect.height - 3))
        self.spriteCountPrimer += 1

        return

class Script(object):
    def __init__(self, xPos, yPos, width, height, scriptLocation, font):
        self.width = width
        self.height = height
        self.x = xPos
        self.y = yPos

        self.script = pd.read_csv(scriptLocation, delimiter=";", encoding='unicode_escape')
        self.dfIndex = 0
        self.font = font

        self.lineWidth = 3
        self.offset = int(self.lineWidth + self.lineWidth / 2)

        self.textReady = False
        self.readyForOptions = False
        self.optionReady = False

        self.printing = False
        return

    def parseText(self):
        self.textScript = str(self.script["texto"][self.dfIndex])
        self.optionA = str(self.script["At"][self.dfIndex])
        self.indexA = int(self.script["Ao"][self.dfIndex]) - 1
        self.optionB = str(self.script["Bt"][self.dfIndex])
        self.indexB = int(self.script["Bo"][self.dfIndex]) - 1
        self.optionC = str(self.script["Ct"][self.dfIndex])
        self.indexC = int(self.script["Co"][self.dfIndex]) - 1
        self.sprites = str(self.script["sprites"][self.dfIndex])
        return

    def initRender(self, text):
        self.times = 1
        self.textIndex = 0
        self.textIndexColumn = self.textIndex
        self.textRow = 0
        self.text = text
        self.textLength = len(text)

        self.optionA = False
        self.optionB = False
        self.optionC = False
        self.textReady = False
        self.readyForOptions = False
        self.optionReady = False
        return

    def renderText(self, screen):
        if not self.textReady and not self.readyForOptions and not self.optionReady:
            renderText = self.font.render(self.text[self.textIndex], False, (255, 255, 255))
            screen.blit(renderText, ((5 + self.x + self.offset * 2) + self.textIndexColumn * 18, self.y + (self.offset * 2) + self.textRow * 27))

            self.textIndex += 1
            self.textIndexColumn += 1

            if self.textIndex == 42 * self.times:
                self.times += 1
                self.textIndexColumn = 0
                self.textRow += 1

            if self.textRow >= 14:
                self.textIndexColumn = 0
                self.textRow = 0
                self.textReady = True
                self.readyForOptions = False
                self.optionReady = False

            if self.textIndex >= len(self.text):
                self.times = 1
                self.textIndex = 0
                self.textIndexColumn = 0
                self.textRow = 0
                self.renderA = True
                self.renderB = False
                self.renderC = False
                self.textReady = True
                self.readyForOptions = True
                self.optionReady = False

        return

    def renderOptions(self, screen):
        if self.textReady and self.readyForOptions and not self.optionReady:
            if self.renderA and not self.renderB and not self.renderC:
                renderText = self.font.render(self.optionA[self.textIndex], False, (255, 255, 255))
                screen.blit(renderText, ((5 + self.x + self.offset * 2) + self.textIndexColumn * 18, self.y + (self.offset * 2) + self.textRow * 27))
                self.textIndex += 1
                self.textIndexColumn += 1

                if self.textIndex == 42 * self.times:
                    self.times += 1
                    self.textIndexColumn = 0
                    self.textRow += 1

                if self.textRow >= 14:
                    self.textIndexColumn = 0
                    self.textRow = 0

                if self.textIndex >= len(self.optionA):
                    self.times = 1
                    self.textIndex = 0
                    self.textIndexColumn = self.textIndex
                    self.textRow += 1
                    self.renderA = False
                    self.renderB = True
                    self.renderC = False
                    self.optionReady = False

            if not self.renderA and self.renderB and not self.renderC:
                renderText = self.font.render(self.optionB[self.textIndex], False, (255, 255, 255))
                screen.blit(renderText, ((5 + self.x + self.offset * 2) + self.textIndexColumn * 18, self.y + (self.offset * 2) + self.textRow * 27))
                self.textIndex += 1
                self.textIndexColumn += 1

                if self.textIndex == 42 * self.times:
                    self.times += 1
                    self.textIndexColumn = 0
                    self.textRow += 1

                if self.textRow >= 14:
                    self.textIndexColumn = 0
                    self.textRow = 0

                if self.textIndex >= len(self.optionB):
                    self.times = 1
                    self.textIndex = 0
                    self.textIndexColumn = self.textIndex
                    self.textRow += 1
                    self.renderA = False
                    self.renderB = False
                    self.renderC = True
                    self.optionReady = False

            if not self.renderA and not self.renderB and self.renderC:
                if self.optionC != "nan":
                    renderText = self.font.render(self.optionC[self.textIndex], False, (255, 255, 255))
                    screen.blit(renderText, ((5 + self.x + self.offset * 2) + self.textIndexColumn * 18, self.y + (self.offset * 2) + self.textRow * 27))
                    self.textIndex += 1
                    self.textIndexColumn += 1

                    if self.textIndex == 42 * self.times:
                        self.times += 1
                        self.textIndexColumn = 0
                        self.textRow += 1

                    if self.textRow >= 14:
                        self.textIndexColumn = 0
                        self.textRow = 0

                    if self.textIndex >= len(self.optionC):
                        self.times = 1
                        self.textIndex = 0
                        self.textIndexColumn = self.textIndex
                        self.textRow = 0
                        self.renderA = False
                        self.renderB = False
                        self.renderC = False
                        self.textReady = True
                        self.readyForOptions = True
                        self.optionReady = True
                        self.printing = False

                else:
                    self.times = 1
                    self.textIndex = 0
                    self.textIndexColumn = self.textIndex
                    self.textRow = 0
                    self.renderA = False
                    self.renderB = False
                    self.renderC = False
                    self.textReady = True
                    self.readyForOptions = True
                    self.optionReady = True
                    self.printing = False

        return

    def renderBox(self, screen):
        pg.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width - self.lineWidth, self.height - self.lineWidth), self.lineWidth)
        pg.draw.rect(screen, (255, 255, 255), (self.x + self.offset, self.y + self.offset, self.width - self.lineWidth - self.offset * 2, self.height - self.lineWidth - self.offset * 2), self.lineWidth)
        return

class Game(object):
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.screenTitle = title
        self.gameRunning = True
        self.elapsedTime = int(round(time.time() * 1000))
        self.text = None

        self.speed = 100

        textBoxY = 200
        scriptLocation = "./scripts/Guion.csv"
        font = pg.font.Font("./font/FNAF.ttf", 24)
        self.script = Script(1, textBoxY, 800, self.height - textBoxY, scriptLocation, font)

        self.sprites = Personajes()

        self.textSound = Sound("./sounds/text.wav")
        self.marchaSanLorenzo = Music("./music/marcha de San Lorenzo 8-bit.wav")

        self.screen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption(self.screenTitle)
        icon = pg.image.load("./sprites/logo.png")
        pg.display.set_icon(icon)

        self.clock = pg.time.Clock()
        return

    def update(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.gameRunning = False

        keys = pg.key.get_pressed()
        if keys[pg.K_RETURN]:
            if self.script.textReady and not self.script.readyForOptions and not self.script.optionReady:
                self.script.textReady = False
                self.screen.fill((0, 0, 0))
                pg.draw.rect(self.screen, (50, 50, 50), (1, 1, 800, 197))
                self.script.renderBox(self.screen)

            if not self.script.printing:
                if self.script.textReady and self.script.readyForOptions and not self.script.optionReady:
                    self.script.printing = True
                    self.screen.fill((0, 0, 0))
                    pg.draw.rect(self.screen, (50, 50, 50), (1, 1, 800, 197))
                    self.script.renderBox(self.screen)

        if keys[pg.K_SPACE]:
            self.speed = 10

        else:
            self.speed = 100

        if keys[pg.K_1]:
            if self.script.textReady and self.script.readyForOptions and self.script.optionReady:
                if self.script.indexA == -2:
                    gameOver(self)
                    self.gameRunning = False

                else:
                    self.script.dfIndex = self.script.indexA
                    self.screen.fill((0, 0, 0))
                    pg.draw.rect(self.screen, (50, 50, 50), (1, 1, 800, 197))
                    self.script.renderBox(self.screen)

        if keys[pg.K_2]:
            if self.script.textReady and self.script.readyForOptions and self.script.optionReady:
                if self.script.indexB == -2:
                    gameOver(self)
                    self.gameRunning = False

                else:
                    self.script.dfIndex = self.script.indexB
                    self.screen.fill((0, 0, 0))
                    pg.draw.rect(self.screen, (50, 50, 50), (1, 1, 800, 197))
                    self.script.renderBox(self.screen)

        if keys[pg.K_3]:
            if self.script.textReady and self.script.readyForOptions and self.script.optionReady:
                if self.script.indexC == -2:
                    gameOver(self)
                    self.gameRunning = False

                else:
                    if self.script.optionC != "null":
                        self.script.dfIndex = self.script.indexC
                        self.screen.fill((0, 0, 0))
                        pg.draw.rect(self.screen, (50, 50, 50), (1, 1, 800, 197))
                        self.script.renderBox(self.screen)

        self.script.parseText()
        return

    def render(self, actualTime):
        if self.text != self.script.textScript:
            self.text = self.script.textScript
            self.script.initRender(self.text)

        if not self.script.textReady and not self.script.readyForOptions:
            dif = actualTime - self.elapsedTime
            if dif > self.speed:
                self.elapsedTime = actualTime
                self.script.renderText(self.screen)
                if self.script.text[self.script.textIndex] != " ":
                    self.textSound.play()

                self.sprites.render(self.screen, self.script.sprites)

        if self.script.printing:
            dif = actualTime - self.elapsedTime
            if dif > self.speed:
                self.elapsedTime = actualTime
                self.script.renderOptions(self.screen)
                if self.script.text[self.script.textIndex] != " ":
                    self.textSound.play()

                self.sprites.render(self.screen, self.script.sprites)

        pg.display.update()
        return

def mainMenu(game):
    mainMenuScreen = pg.transform.scale(pg.image.load("./sprites/título.png"), (800, 400))
    game.screen.fill((0, 0, 0))
    game.screen.blit(mainMenuScreen, (1, 100))
    pg.mixer.music.load("./music/marcha de San Lorenzo 8-bit.wav")
    pg.mixer.music.set_volume(0.25)
    pg.mixer.music.play(-1)
    pg.display.set_caption("Presione ENTER para ver las instrucciones")
    pg.display.update()
    mainScreen = True
    while mainScreen:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                mainScreen = False
                game.gameRunning = False

        keys = pg.key.get_pressed()
        if keys[pg.K_RETURN]:
            mainScreen = False

    game.screen.fill((0, 0, 0))
    return

def reglas(game):
    reglasMenuScreen = pg.transform.scale(pg.image.load("./sprites/Sin título.png"), (800, 500))
    game.screen.fill((0, 0, 0))
    game.screen.blit(reglasMenuScreen, (1, 50))
    pg.display.set_caption("Presione ENTER para jugar")
    pg.display.update()
    reglasScreen = True
    listo = False
    o = 0
    while reglasScreen:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                reglasScreen = False
                game.gameRunning = False

        keys = pg.key.get_pressed()
        if keys[pg.K_RETURN] and listo:
            reglasScreen = False

        o += 1
        if o >= 10000:
            listo = True

    game.screen.fill((0, 0, 0))
    return

def gameOver(game):
    gameOverMenuScreen = pg.transform.scale(pg.image.load("./sprites/aaaaa.png"), (800, 500))
    game.screen.fill((0, 0, 0))
    game.screen.blit(gameOverMenuScreen, (1, 50))
    pg.display.set_caption("Presione ENTER para jugar")
    pg.display.update()
    gameOverScreen = True
    while gameOverScreen:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameOverScreen = False

        keys = pg.key.get_pressed()
        if keys[pg.K_RETURN]:
            gameOverScreen = False

    game.screen.fill((0, 0, 0))
    return

def main():
    game = Game(800, 600, "SanMartin1")
    mainMenu(game)
    if game.gameRunning:
        reglas(game)
        game.marchaSanLorenzo.play()
        game.script.renderBox(game.screen)
        pg.draw.rect(game.screen, (50, 50, 50), (1, 1, 800, 197))
        pg.display.set_caption("Paso a la Inmortalidad del General José de San Martín")
        while game.gameRunning:
            game.clock.tick(120)
            game.update()
            game.render(int(round(time.time() * 1000)))

    pg.quit()
    return

main()
