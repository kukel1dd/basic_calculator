import pygame
import calculator_app as program
from sys import exit
import buttons
#6.1.2023 LK
calcoperators = None
calc_answer = None
val0 = ''
val1 = ''
error = False

decpoint = False
calc_answer = None


program.Calculator

pygame.init()
clock = pygame.time.Clock()
#Display window
calculator_display = pygame.display.set_mode((500, 600))
calculator_display.fill((128,128,128))
#Application Title
pygame.display.set_caption("Basic Calculator")
#The screen for the calculator
calculator_screen = pygame.Surface((265,120))
screen_outline = pygame.Surface((275,128))
calculator_screen.fill((139,172,15))
#Font for the app
calc_text = ''
# calc_text = ((val0) + (calcoperators) +(val1))
base_font = pygame.font.Font(None, 45)
# calc_font = base_font.render(calc_text, False, 'black')
#The background of the application
calc_background = pygame.image.load('Images/calculator.png')


#load button images
button0_img = pygame.image.load('Images/button0.png').convert_alpha()
button1_img = pygame.image.load('Images/button1.png').convert_alpha()
button2_img = pygame.image.load('Images/button2.png').convert_alpha()
button3_img = pygame.image.load('Images/button3.png').convert_alpha()
button4_img = pygame.image.load('Images/button4.png').convert_alpha()
button5_img = pygame.image.load('Images/button5.png').convert_alpha()
button6_img = pygame.image.load('Images/button6.png').convert_alpha()
button7_img = pygame.image.load('Images/button7.png').convert_alpha()
button8_img = pygame.image.load('Images/button8.png').convert_alpha()
button9_img = pygame.image.load('Images/button9.png').convert_alpha()
buttondec_img = pygame.image.load('Images/buttondec.png').convert_alpha()
buttoneql_img = pygame.image.load('Images/buttoneql.png').convert_alpha()
buttonadd_img = pygame.image.load('Images/buttonadd.png').convert_alpha()
buttonsub_img = pygame.image.load('Images/buttonsub.png').convert_alpha()
buttonmult_img = pygame.image.load('Images/buttonmult.png').convert_alpha()
buttondiv_img = pygame.image.load('Images/buttondiv.png').convert_alpha()
buttonclear_img = pygame.image.load('Images/buttonclear.png').convert_alpha()

#button class
class Button():
    def __init__(self, x, y, image, keypress):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    def draw(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        
        #Check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        calculator_display.blit(self.image, (self.rect.x, self.rect.y))
        
        return action
#creating button instances
button0 = Button(10, 455, button0_img, keypress= pygame.K_0)
button1 = Button(10, 260, button1_img, keypress= pygame.K_1)
button2 = Button(80, 260, button2_img, keypress= pygame.K_2 )
button3 = Button(150, 260, button3_img, keypress= pygame.K_3 )
button4 = Button(10, 325, button4_img, keypress= pygame.K_4 )
button5 = Button(80, 325, button5_img, keypress= pygame.K_5)
button6 = Button(150, 325, button6_img, keypress= pygame.K_6)
button7 = Button(10, 390, button7_img, keypress= pygame.K_7)
button8 = Button(80, 390, button8_img, keypress=  pygame.K_8)
button9 = Button(150, 390, button9_img, keypress= pygame.K_9)
buttondec = Button(80, 455, buttondec_img, keypress= pygame.K_KP_PERIOD)
buttoneql = Button(150, 455, buttoneql_img, keypress= pygame.K_KP_EQUALS)
buttonadd = Button(220, 260, buttonadd_img, keypress= pygame.K_PLUS)
buttonsub = Button(220, 325, buttonsub_img, keypress= pygame.K_KP_MINUS)
buttonmult = Button(220, 390, buttonmult_img, keypress= pygame.K_KP_MULTIPLY)
buttondiv = Button(220, 455, buttondiv_img, keypress= pygame.K_SLASH)
buttonclear = Button(10, 520, buttonclear_img, keypress= pygame.K_c)

#gameloop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            calc_text += event.unicode

    calc_font = base_font.render(calc_text, False, 'black')
    #text_surface = base_font.render(calc_text, 255,)
    calculator_display.blit(calc_background, (0,0))
    calculator_display.blit(screen_outline, (78,65)) #This is just an outline.
    calculator_display.blit(calculator_screen, (82,68))
    calculator_display.blit(calc_font, (85,105))
    

    
   
#Buttons for the numbers
    if button0.draw():
        if  error or len(str(calc_text)) >= 14:
            pass
        else:
            if calcoperators == None:
                if calc_answer == None:
                    val0 += '0'
                    calc_text += '0'
            elif calc_answer:
                if calcoperators == None:
                    pass
                else:
                    val1 += '0'
                calc_text += '0'
                print(f"first number {val0}")
                print(f"second number {val1}")
            else:
                val1 += '0'
                calc_text += '0'
                print(f"first number {val0}")
                print(f"second number {val1}")
    if button1.draw():
        if error or len(str(calc_text)) >= 14:
            pass
        else:
            if calcoperators == None:
                if calc_answer == None:
                    val0 += '1'
                    calc_text += '1'
            elif calc_answer:
                if calcoperators == None:
                    pass
                else:

                    val1 += '1'
                calc_text += '1'
                print(f"first number {val0}")
                print(f"second number {val1}")
            else:
                val1 += '1'
                calc_text += '1'
                print(f"first number {val0}")
                print(f"second number {val1}")
        

    if button2.draw():
        if error or len(str(calc_text)) >= 14:
            pass
        else:
            if calcoperators == None:
                if calc_answer == None:
                    val0 += '2'
                    calc_text += '2'
            elif calc_answer:
                if calcoperators == None:
                    pass
                else:
                    val1 += '2'
                calc_text += '2'
                print(f"first number {val0}")
                print(f"second number {val1}")
            else:
                val1 += '2'
                calc_text += '2'
                print(f"first number {val0}")
                print(f"second number {val1}")
        
    if button3.draw():
        if error or len(str(calc_text)) >= 14:
            pass
        else:
            if calcoperators == None:
                if calc_answer == None:
                    val0 += '3'
                    calc_text += '3'
            elif calc_answer:
                if calcoperators == None:
                    pass
                else:
                    val1 += '3'
                calc_text += '3'
                print(f"first number {val0}")
                print(f"second number {val1}")
            else:
                val1 += '3'
                calc_text += '3'
                print(f"first number {val0}")
                print(f"second number {val1}")
    if button4.draw():
        if error or len(str(calc_text)) >= 14:
            pass
        else:
            if calcoperators == None:
                if calc_answer == None:
                    val0 += '4'
                    calc_text += '4'
            elif calc_answer:
                if calcoperators == None:
                    pass
                else:
                    val1 += '4'
                calc_text += '4'
                print(f"first number {val0}")
                print(f"second number {val1}")
            else:
                val1 += '4'
                calc_text += '4'
                print(f"first number {val0}")
                print(f"second number {val1}")
    if button5.draw():
        if error or len(str(calc_text)) >= 14:
            pass
        else:
            if calcoperators == None:
                if calc_answer == None:
                    val0 += '5'
                    calc_text += '5'
            elif calc_answer:
                if calcoperators == None:
                    pass
                else:
                    val1 += '5'
                calc_text += '5'
                print(f"first number {val0}")
                print(f"second number {val1}")
            else:
                val1 += '5'
                calc_text += '5'
                print(f"first number {val0}")
                print(f"second number {val1}")
    if button6.draw():
        if error or len(str(calc_text)) >= 14:
            pass
        else:
            if calcoperators == None:
                if calc_answer == None:
                    val0 += '6'
                    calc_text += '6'
            elif calc_answer:
                if calcoperators == None:
                    pass
                else:
                    val1 += '6'
                calc_text += '6'
                print(f"first number {val0}")
                print(f"second number {val1}")
            else:
                val1 += '6'
                calc_text += '6'
                print(f"first number {val0}")
                print(f"second number {val1}")
    if button7.draw():
        if error or len(str(calc_text)) >= 14:
            pass
        else:
            if calcoperators == None:
                if calc_answer == None:
                    val0 += '7'
                    calc_text += '7'
            elif calc_answer:
                if calcoperators == None:
                    pass
                else:
                    val1 += '7'
                calc_text += '7'
                print(f"first number {val0}")
                print(f"second number {val1}")
            else:
                val1 += '7'
                calc_text += '7'
                print(f"first number {val0}")
                print(f"second number {val1}")
    if button8.draw():
        if error or len(str(calc_text)) >= 14:
            pass
        else:
            if calcoperators == None:
                if calc_answer == None:
                    val0 += '8'
                    calc_text += '8'
            elif calc_answer:
                if calcoperators == None:
                    pass
                else:
                    val1 += '8'
                calc_text += '8'
                print(f"first number {val0}")
                print(f"second number {val1}")
            else:
                val1 += '8'
                calc_text += '8'
                print(f"first number {val0}")
                print(f"second number {val1}")
    if button9.draw():
        if error or len(str(calc_text)) >= 14:
            pass
        else:
            if calcoperators == None:
                if calc_answer == None:
                    val0 += '9'
                    calc_text += '9'
            elif calc_answer:
                if calcoperators == None:
                    pass
                else:
                    val1 += '9'
                calc_text += '9'
                print(f"first number {val0}")
                print(f"second number {val1}")
            else:
                val1 += '9'
                calc_text += '9'
                print(f"first number {val0}")
                print(f"second number {val1}")

#buttons for the symbols
    if buttondec.draw():
        if error or len(str(calc_text)) >= 14:
            pass
        else:
            decpoint = True
            if calcoperators == None:
                if calc_answer == None:
                    if '.' not in val0:
                        if val0 == '':
                            val0 += '0.'
                            calc_text += '0.'
                        else:
                            val0 +='.'
                            calc_text += '.'
            elif calcoperators:
                if '.' not in val1:
                    val1 += '.'
                    calc_text += '.'

    if buttoneql.draw():
        if val1 == '':
            #if calcoperators:
            pass
        else:
            if calcoperators != None:
                if decpoint == True:
                    val_0_result = float(val0)
                    val_1_result = float(val1)
                else:
                    val_0_result = int(val0)
                    val_1_result = int(val1)
         
            if calcoperators == '+':
                calc_answer = program.Calculator.addition(number0=val_0_result, number1 =val_1_result)
                if len(str(calc_answer))> 14:
                    error = True
                    calc_text = "Error"
                else:
                    val0 = calc_answer
                    val1 = ''  
                    calc_text = str(f"{calc_answer}")
                    calcoperators = None
                
            elif calcoperators == '-':
                calc_answer = program.Calculator.subtraction(number0=val_0_result, number1=val_1_result)
                if len(str(calc_answer))> 14:
                    error = True
                    calc_text = "Error"
                else:
                    val0 = calc_answer
                    val1 = ''
                    calc_text = str(f"{calc_answer}")
                    calcoperators = None
            elif calcoperators == '*':
                calc_answer = program.Calculator.multiplication(number0=val_0_result, number1=val_1_result)
                if len(str(calc_answer))> 14:
                    error = True
                    calc_text = "Error"
                else:
                    val0 = calc_answer
                    val1 = ''
                    calc_text = str(f"{calc_answer}")
                    calcoperators = None
            elif calcoperators == '/':
                calc_answer = program.Calculator.division(number0=val_0_result, number1=val_1_result)
                if val_1_result == 0:
                    val0 = ''
                    val1 = ''
                    calc_text = str("ZeroDivisionError")
                    error = True
                    calcoperators = None
                    calc_answer = None
                elif val_0_result == 0:
                    if (calc_answer).is_integer() == True:
                        
                        calc_answer = int(calc_answer)
                        val0 = calc_answer
                        val1 = ''
                        calc_text = str(calc_answer)
                        calcoperators = None
                    else:
                        val0 = calc_answer
                        val1 = ''
                        calc_text = str(calc_answer)
                        calcoperators = None
                
                elif calc_answer:
                    if (calc_answer).is_integer() == True:
                        
                        calc_answer = int(calc_answer)
                        val0 = calc_answer
                        val1 = ''
                        calc_text = str(calc_answer)
                        calcoperators = None
                    else:
                        val0 = calc_answer
                        val1 = ''
                        calc_text = str(calc_answer)
                        calcoperators = None
                else:
                    pass
                    
            else:
                val0 = ''
                val1 = ''
                calc_text = ''
        # else:
        #     pass
    if buttonclear.draw():
        if error:
            """A Clear all button if conditions are met."""
            val0 = ''
            val1 = ''
            calc_answer = None
            calcoperators = None
            calc_text = ''
            print('Clear All')
            error = False
        elif calc_answer != None and val1 == '':
            if calcoperators == None:
                val0 = ''
                val1 = ''
                calc_answer = None
                calcoperators = None
                calc_text = ''
                print('Clear All')
            else:
                calc_text = calc_text[:-1]
                calcoperators = None
        else:
            """Clears one value at a time"""
            if calcoperators == None:
                val0 = val0[:-1]
                calc_text = calc_text[:-1]
            elif calcoperators:
                if val1 == '':
                    calcoperators = None
                    calc_text = calc_text[:-1]
                else:
                    val1 = val1[:-1]
                    calc_text = calc_text[:-1]
    

#buttons for the operators
    if buttonadd.draw():
        if calc_text == 'ZeroDivisionError' or len(str(calc_text)) >= 14:
            pass
        else:
            calcoperators = "+"
            if calc_answer:
                calc_answer = "+"
                
            if val0 == '':
                val0 = 0
                calc_text += '0'
                calc_text += '+'
                print(calcoperators)

            elif '+' not in calc_text:
                calc_text += "+"
            else:
                pass

    if buttonsub.draw():
        if calc_text == 'ZeroDivisionError' or len(str(calc_text)) >= 14:
            pass
        else:
            val0 = str(val0)
            if val0 == '':
                if '-' in val0:
                    pass
                else:
                    val0 += '-'
                    calc_text +='-'
            elif len(val0) >=1:
                if calcoperators == '-':
                    pass
                else: 
                    calcoperators = '-'
                    calc_text +='-'

    if buttonmult.draw():
        if calc_text == 'ZeroDivisionError' or len(str(calc_text)) >= 14:
            pass
        else:
            calcoperators = "*"
            if val0 == '':
                val0 = 0
            if '*' in calc_text:
                pass
            else:
                calc_text += '*'

    if buttondiv.draw():
        if calc_text == 'ZeroDivisionError' or len(str(calc_text)) >= 14:
            pass
        else:
            calcoperators = "/"
            if val0 == '':
                val0 = 0
            if '/' in calc_text:
                pass
            else:
                calc_text += '/'

    pygame.display.update()
    clock.tick(60)





