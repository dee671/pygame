


print('hello, it is my game')

has_clean_backyard = False
has_gloves = False
eat_diner = False
has_key = False
get_ready_for_bed = False
complete_homework = False

def outside():
    print('you are outside')
    print('it is dark,cold, and the mist makes visibility low ')
    print('at a distance you see a familiar place')
    print('south: Frontyard')
    print('')
    choice = input('?')
    if choice == 'south':
        front_yard()
    else:
        outside()

   
def front_yard():
    global has_key
    print('you are in the frontyard')
    print('you approach what is seem to be a cozy house')
    print('as you proceed, a metal door stops you on your tracks')
    print('what do you do?')
    print('north: Outside')
    print('take_key: take key from back pack')
    print('use_key: Living Room')
    print('')
    choice = input('?')
    if choice == 'take_key':
       print('you have retrieved front door keys')
       has_key = True
    if choice == 'use_key':
       if has_key:
          print('you use keys to unlock door')
          print('you push the door and nothing happens')
          print('you push a second time and you hear a crack')
          print('You push a third time and with all of your might...')
          print('the door finally budges')
          print('as the door opens wide it makes a loud creaking sound')
          print('you yell, "HELLO! anyone home?"')
          living_room()
           
       else:
          front_yard()
    if choice == 'north':
       outside()
    else:
        front_yard()
        print('try as you might, it will not budge')

     

def living_room():
    print('you are in the Living Room')
    print('it is quiet')
    print('west: Dining Room')
    print('east: Kitchen')
    print('south: Stairs')
    print('north: Front Yard')
    print('')

    choice = input('?')
    if choice == 'east':
       kitchen()
    if choice == 'south':
       stairs()
    if choice == 'west':
       dining_room()
    else:
       living_room()
    
def kitchen():
    print('your are in the kitchen')
    print('you see the remnant of cooking')
    print('east: Closet')
    print('south: Backyard')
    print('west: Living Room')
    print('')

    choice = input('?')
    if choice == 'west':
       living_room()
    if choice == 'south':
       back_yard()
    if choice == 'east':
       closet()
    else:
       kitchen()

def closet():
    global has_gloves
    print('you are in a dark closet')
    print('you stuble and find the light switch')
    print('"click......"')
    print('the light flickers and finally turns on')
    print('')
    if not has_gloves:
        print('on the shelves you find some items')
        print('take_gloves: has Gloves')
    
    choice = input('?')
    if choice == 'take_gloves':
      has_gloves = True
      print('you have medium gloves')
      kitchen()

    if choice == 'west':
       kitchen()
    else: 
       closet()


   
   

def back_yard():
    global has_clean_backyard
    print('you are in the Backyard')
    print('you see the trashbin tipped over')
    print('.....it reeks')
    print('north: kitchen')
    print('clean_up: Clean Backyard')
    print('')
    choice = input('?')
    if choice == 'north':
       kitchen()
    if choice == 'clean_up':
      if has_gloves:
        print('you have cleaned up the trash')
        has_clean_backyard = True
        kitchen()
      else:
        print('you need gloves')
        back_yard()
    else: 
       back_yard()

def dining_room():
    global eat_diner
    print('you are in the dinning room')
    print('the table is set')
    print('east: Living Room')
    print('eat: Eat diner')
    print('')
 
    choice = input('?')
    if choice == 'east':
      living_room()
    if choice == 'eat':
       if has_clean_backyard:
          print('you pull up a chair and enjoy a nice meal')
          eat_diner = True
          living_room()
       else:
          print('you need to clean the back yard first')
          dining_room()
    else:
      dining_room()

def stairs():
    print('you are in creeky set of stairs')
    print('west: Living Room')
    print('north: hallway')
    print('')
    choice = input('?')
    if choice == 'north':
       print('you carefully move down the hall')
       hallway()
    if choice == 'west':
       living_room()
    else:
       stairs()


def hallway():
    print('you are in a Hallway between rooms')
    print('it is dim, your parents are saving money')
    print('north: Parents Bed room')
    print('east: My bed room')
    print('west: Bathroom')
    print('south: Staircase')
    print('')
    choice = input('?')
    if choice == 'west':
      bathroom()
    if choice == 'east':
      my_bed_room()
    if choice == 'south':
      stairs()
    if choice == 'north':
      print('the doors are unlocked')
      print('but you do not dare go in')
      hallway()
    

def my_bed_room():
    global complete_homework
    print('you are in your bedroom')
    print('west: Hallway')
    print('do_homework: Complete Homework')
    print('sleep: end the day')
    print('')
    choice = input('?')
    if choice == 'west':
       hallway()
    if choice == 'do_homework':
       if has_clean_backyard and eat_diner:
          print('you struggle for a bit')
          print('but eventually manage to finish')
          complete_homework = True
       else:
          print('you have to clean the back yard and eat diner first')
    if choice == 'sleep':
       if has_clean_backyard and eat_diner and get_ready_for_bed:
          print('you rest for the night')
          end_the_day()
       else:
          print('you must do chores and clean up first')
          my_bed_room()
    else:
       my_bed_room()
       

    
    

def bathroom():
    global get_ready_for_bed
    print('you are in the bathroom')
    print('clean white walls surround you')
    print('east: Hallway')
    print('wash: Get ready for bed')
    print('')
    choice = input('?')
    if choice == 'east':
       hallway()
    if choice == 'wash':
       if has_clean_backyard and eat_diner and complete_homework:
          print('you shower and brush teeth')
          get_ready_for_bed = True
          bedroom()
       else:
          print('you must clean backyard, eat diner, and do homework')
          bathroom()
    else:
       bathroom()

def parents_room():
    print('you are safe with your parents')
    end_the_day()
    
def end_the_day():
    exit()

outside()
