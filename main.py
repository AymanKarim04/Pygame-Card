# imports
import pygame.font

# initialize pygame
pygame.init()
pygame.font.init()

# defining constants
WIDTH, HEIGHT = 500, 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (252, 222, 109)
ZAPFINO = pygame.font.SysFont("Zapfino", 15)
LUCIDA_GRANDE = pygame.font.SysFont("Lucida Grande", 15)
BRUSH_SCRIPT_MT = pygame.font.SysFont("Lucida Grande", 15, italic=True)

# create the pygame window and set the caption
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ayman's Card Maker")

# loading all the images
startImage = pygame.image.load("background.png")
icon = pygame.image.load("icon.png")
eidImage = pygame.image.load("eid_photo.png")
familyDayImage = pygame.image.load("family_day_photo.jpg")
lunarNewYearImage = pygame.image.load("lunar_new_year_photo.jpg")

# setting the icon of the pygame
pygame.display.set_icon(icon)

# making all the card images the same size
startImage = pygame.transform.scale(startImage, (WIDTH, HEIGHT))
eidImage = pygame.transform.scale(eidImage, (WIDTH, HEIGHT))
familyDayImage = pygame.transform.scale(familyDayImage, (WIDTH, HEIGHT))
lunarNewYearImage = pygame.transform.scale(lunarNewYearImage, (WIDTH, HEIGHT))

# defining functions
def sender_info():
   sender = input("Who is sending this card? ")
   return sender

def receiver_info():
  receiver = input("Who are you sending this card to? ")
  return receiver

def message():
  message_sent = input("What message would you like to send to the receiver? ")
  return message_sent

def card_writing():
 sender_print = "From: " + sender_info()
 receiver_print = "To: " + receiver_info()
 message_print = message()
 return sender_print, receiver_print, message_print

def eid(sender_print, receiver_print, message_print):
  print("Happy Eid!")

  sender_display = ZAPFINO.render(sender_print, True, WHITE)
  receiver_display = ZAPFINO.render(receiver_print, True, WHITE)
  message_display = ZAPFINO.render(message_print, True, WHITE)

  WINDOW.blit(sender_display, (40, 350))
  WINDOW.blit(receiver_display, (40, 400))
  WINDOW.blit(message_display, (300, 400))

def family_day(sender_print, receiver_print, message_print):
  print("Happy Family Day!")

  sender_display = LUCIDA_GRANDE.render(sender_print, True, BLACK)
  receiver_display = LUCIDA_GRANDE.render(receiver_print, True, BLACK)
  message_display = LUCIDA_GRANDE.render(message_print, True, BLACK)

  WINDOW.blit(sender_display, (250, 200))
  WINDOW.blit(receiver_display, (250, 250))
  WINDOW.blit(message_display, (250, 300))

def lunar_new_year(sender_print, receiver_print, message_print):
  print("Happy Lunar New Year!")

  sender_display = BRUSH_SCRIPT_MT.render(sender_print, True, GOLD)
  receiver_display = BRUSH_SCRIPT_MT.render(receiver_print, True, GOLD)
  message_display = BRUSH_SCRIPT_MT.render(message_print, True, GOLD)

  WINDOW.blit(sender_display, (150, 115))
  WINDOW.blit(receiver_display, (150, 135))
  WINDOW.blit(message_display, (110, 340))

# main
# input/variables
running = True

while running:
  # when run start by displaying the start image
  WINDOW.blit(startImage, (0, 0))

  # update the screen so that the start image appears
  pygame.display.update()

  # get which holiday the user wants to make a card for
  choose_holiday = int(input("Which holiday card do you want? 1 for eid, 2 for Family Day, 3 for Lunar New Year: "))

  # process and output
  # assigning numbers to each holiday and then displaying each holiday card according to user input
  if choose_holiday == 1:
    WINDOW.blit(eidImage, (0, 0))
    a, b, c = card_writing()
    eid(a, b, c)

  elif choose_holiday == 2:
    WINDOW.blit(familyDayImage, (0, 0))
    a, b, c = card_writing()
    family_day(a, b, c)

  elif choose_holiday == 3:
    WINDOW.blit(lunarNewYearImage, (0, 0))
    a, b, c = card_writing()
    lunar_new_year(a, b, c)

  # what happens if the number chosen is not from one of the numbers associated with a holiday
  else:
    print("Please choose one of the options that are listed")
    WINDOW.blit(startImage, (0, 0))

  # what happens in the event that the quit button is pressed
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  pygame.display.update()

  # this input asks if the user wants to continue - if they don't want to then they can exit the program
  user = input("Enter to continue: ")