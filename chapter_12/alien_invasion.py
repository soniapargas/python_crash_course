import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
  """Overall class to manage game assets and behavior. """
  # method = function 
  # except methods belong to classes and get called from class instances
  def __init__(self):
    """Init the game, and create resource"""
    pygame.init()  

    self.settings = Settings()
    self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    self.settings.screen_width = self.screen.get_rect().width
    self.settings.screen_height = self.screen.get_rect().height
    pygame.display.set_caption("Alien Invasion")

    self.ship = Ship(self)

    # Set the background color.
    self.bg_color = (230, 230, 230)

  def run_game(self):
    """Start the main loop for the game."""
    while True:
      self._check_events()
      self.ship.update()
      self._update_screen()
      #  Watch for keyboard and mouse events.
  
  def _check_keydown_events(self, event):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
      self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
      self.ship.moving_left = True
    elif event.key == pygame.K_q:
      sys.exit()
        
  def _check_events(self):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
      # print(event.type)
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        self._check_keydown_events(event)
      elif event.type == pygame.KEYUP:
        self._check_keyup_events(event)

  def _check_keyup_events(self, event):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
      self.ship.moving_right = False
    elif event.key == pygame.K_LEFT:
      self.ship.moving_left = False

  def _update_screen(self):
    """Update images on the screen, and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    self.screen.fill(self.settings.bg_color)
    self.ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

if __name__ == '__main__':
    #  Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

# procedural (todo list)
# step by step
# top of file to bottom the computer runs line by line
# myList = [1,2,3,3]
# for item in myList:
#   print(item)
# functional
# similar to procedural
# you will divide procedures in to blocks of code in functions and then call the functions
# def printList(l = []):
#   for item in l:
#     print(item)

# def printListModified(l = []):
#   for item in l:
#     print(f"here is an item {item}")
# object oriented
# mystr = "slkdjflskdf"
# mystr.title()
# mystr.tolower()
# python string methods
