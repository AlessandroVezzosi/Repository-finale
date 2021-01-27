import pygame 
  
pygame.init() 
  

white = (255, 255, 255) 
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0) 
blue = (0, 0, 128) 
  
X = 650
Y = 650
  
display_surface = pygame.display.set_mode((X, Y )) 
  
pygame.display.set_caption('quizzazzo pazzo sgravato assassino') 
  
font = pygame.font.Font('freesansbold.ttf', 55) 
  
text = font.render('Premi il numero pari', True, white, black) 
  
textRect = text.get_rect()  
  
textRect.center = (325, 31) 

font2 = pygame.font.Font('freesansbold.ttf', 55) 
  
text2 = font.render('22', True, white, black) 
  
text2Rect = text.get_rect()  
  
text2Rect.center = (410, 160) 

font3 = pygame.font.Font('freesansbold.ttf', 55) 
  
text3 = font.render('5', True, white, black) 
  
text3Rect = text.get_rect()  
  
text3Rect.center = (750, 160) 

font4 = pygame.font.Font('freesansbold.ttf', 55) 
  
text4 = font.render('19', True, white, black) 
  
text4Rect = text.get_rect()  
  
text4Rect.center = (410, 350) 

font5 = pygame.font.Font('freesansbold.ttf', 55) 
  
text5 = font.render('168,29', True, white, black) 
  
text5Rect = text.get_rect()  
  
text5Rect.center = (370, 550) 

font6 = pygame.font.Font('freesansbold.ttf', 55) 
  
text6 = font.render('99', True, white, black) 
  
text6Rect = text.get_rect()  
  
text6Rect.center = (750, 550) 

font7 = pygame.font.Font('freesansbold.ttf', 55) 
  
text7 = font.render('11', True, white, black) 
  
text7Rect = text.get_rect()  
  
text7Rect.center = (750, 350)

is_running = True

is_running2 = False
  
while is_running: 
  
    display_surface.fill(black) 
  
    display_surface.blit(text, textRect) 
    display_surface.blit(text2, text2Rect)
    display_surface.blit(text3, text3Rect)
    display_surface.blit(text4, text4Rect)
    display_surface.blit(text5, text5Rect)
    display_surface.blit(text6, text6Rect)
    display_surface.blit(text7, text7Rect)
    pygame.draw.line(display_surface, white, (0, 80), (650, 80))
    pygame.draw.line(display_surface, white, (325, 80), (325, 650))
    pygame.draw.line(display_surface, white, (0, 250), (650, 250))
    pygame.draw.line(display_surface, white, (0, 450), (650, 450))

    for event in pygame.event.get():
  
        if event.type == pygame.QUIT : 
  
            
            pygame.quit() 
  
             
            quit() 

        if event.type == pygame.MOUSEBUTTONDOWN:
            if  font2 and text2Rect.collidepoint(pygame.mouse.get_pos()):

                font = pygame.font.Font('freesansbold.ttf', 55) 
  
                text = font.render('corretto', True, white, green) 
  
                textRect = text.get_rect()  
  
                textRect.center = (325, 31)
           
                display_surface.blit(text, textRect)

                is_running = False

                is_running2 = True

            
            elif font3 or text3Rect or font4 or text4Rect or font6 or text6Rect or font7 or text7Rect or font5 or text5Rect.collidepoint(pygame.mouse.get_pos()):
                font = pygame.font.Font('freesansbold.ttf', 55) 
  
                text = font.render('errato', True, white, red) 
  
                textRect = text.get_rect()  
  
                textRect.center = (325, 31)
           
                display_surface.blit(text, textRect)

                is_running = False

                is_running2 = True

                

                


font8 = pygame.font.Font('freesansbold.ttf', 55) 
  
text8 = font.render('Premi il valore più basso', True, white, black) 
  
text8Rect = text.get_rect()  
  
text8Rect.center = (325, 31) 

font9 = pygame.font.Font('freesansbold.ttf', 55) 
  
text9 = font.render('6/6', True, white, black) 
  
text9Rect = text.get_rect()  
  
text9Rect.center = (410, 160) 

font10 = pygame.font.Font('freesansbold.ttf', 55) 
  
text10 = font.render('25%', True, white, black) 
  
text10Rect = text.get_rect()  
  
text10Rect.center = (750, 160) 

font11 = pygame.font.Font('freesansbold.ttf', 55) 
  
text11 = font.render('8/3', True, white, black) 
  
text11Rect = text.get_rect()  
  
text11Rect.center = (410, 350) 

font12 = pygame.font.Font('freesansbold.ttf', 55) 
  
text12 = font.render('0,012/100', True, white, black) 
  
text12Rect = text.get_rect()  
  
text12Rect.center = (370, 550) 

font13 = pygame.font.Font('freesansbold.ttf', 55) 
  
text13 = font.render('8/9', True, white, black) 
  
text13Rect = text.get_rect()  
  
text13Rect.center = (750, 550) 

font14 = pygame.font.Font('freesansbold.ttf', 55) 
  
text14 = font.render('56%', True, white, black) 
  
text14Rect = text.get_rect()  
  
text14Rect.center = (750, 350)

while is_running2:
    

    display_surface.fill(black) 
  
    display_surface.blit(text8, text8Rect) 
    display_surface.blit(text9, text9Rect)
    display_surface.blit(text10, text10Rect)
    display_surface.blit(text11, text11Rect)
    display_surface.blit(text12, text12Rect)
    display_surface.blit(text13, text13Rect)
    display_surface.blit(text14, text14Rect)
    pygame.draw.line(display_surface, white, (0, 80), (650, 80))
    pygame.draw.line(display_surface, white, (325, 80), (325, 650))
    pygame.draw.line(display_surface, white, (0, 250), (650, 250))
    pygame.draw.line(display_surface, white, (0, 450), (650, 450))

    for event in pygame.event.get():
  
        if event.type == pygame.QUIT : 
  
            
            pygame.quit() 
  
             
            quit() 

        if event.type == pygame.MOUSEBUTTONDOWN:
            if  font12 and text12Rect.collidepoint(pygame.mouse.get_pos()):
                font = pygame.font.Font('freesansbold.ttf', 55) 
  
                text = font.render('corretto', True, white, green) 
  
                textRect = text.get_rect()  
  
                textRect.center = (325, 31)
           
                display_surface.blit(text, textRect)
        

            elif font14 or text14Rect or font9 or text9Rect or font10 or text10Rect or font11 or text11Rect or font13 or text13Rect.collidepoint(pygame.mouse.get_pos()):
                font = pygame.font.Font('freesansbold.ttf', 55) 
  
                text = font.render('errato', True, white, red) 
  
                textRect = text.get_rect()  
  
                textRect.center = (325, 31)
           
                display_surface.blit(text, textRect)




pygame.display.update()