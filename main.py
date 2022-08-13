'''Simulation game'''
import random

class GamePlayer:
    '''Simulate a real player.'''

    def __init__(self,name,character_data):
        '''Initialize attributes to describe a player.'''
        self.name = name
        self.character_data = character_data

    def talk(self):
        '''Give players some help.'''
        character_information = random.choice(self.character_data[-1])
        print(f'Hi,{self.name}.{character_information}')

    def show_properties(self):
        '''Show game character properties.'''
        print('-' * 15)
        for properties,value in self.character_data.items():
            if properties == 'crit_rate':
                percentage = str(int(value* 100)) + '%'
                print(f'{properties}:{percentage}')
            elif properties == 'more_information':
                continue
            else:
                print(f'{properties}:{value}')

        print('-' * 15)
        print(f"{self.name}.This is your properties panel.")

class AlPlayer:
    '''Simulate a Al player.'''

    def __init__(self,name,character_data):
        '''Initialize attributes to describe a Al player.'''
        self.name = name
        self.character_data = character_data

    def talk(self):
        '''Give players some help.'''
        character_information = random.choice(self.character_data[-1])
        print(f'About {self.name}.{character_information}')

    def show_properties(self):
        '''Show game character properties.'''
        print('-' * 15)
        for properties,value in self.character_data.items():
            if properties == 'crit_rate':
                percentage = str(int(value* 100)) + '%'
                print(f'{properties}:{percentage}')
            elif properties == 'more_information':
                continue
            else:
                print(f'{properties}:{value}')

        print('-' * 15)
        print("This is Al's properties panel.")

def get_player_name():
    '''Ask the player to get their game name.'''
    print("Hello, what's your name, please?")
    player_name = input()
    print(f"{player_name},What a resounding name!")
    return player_name

def get_character_information(player_type):
    '''Get game character information from the dictionary'''
    character_list = {'warrior':{'health':30,
                                'attack':3,
                                'crit_rate':0.2,
                                'crit_damage':4,
                                'defense':2,
                                'strength_value':5,
                                'more_information':['I am warrior!']},
                      'caster':{'health':20,
                                'attack':4,
                                'crit_rate':0.25,
                                'crit_damage':5,
                                'defense':1,
                                'strength_value':4,
                                'more_information':['I am caster!']}}

    if player_type == 'player':
        print("Next, select a game character")
        while True:
            player_character = input()
            character_data = ''
            if player_character in character_list:
                character_data =  character_list[player_character]
            else:
                print('The game character name you entered does not exist. Please re-enter it.')
            if character_data:
                break
    elif player_type == 'Al':
        character_data = character_list[random.randint(1,2)]

    return character_data

def blank_line(num):
    '''Enter number wrap.'''
    while num != 0:
        print("")
        num -= 1

def generate_pseudonym():
    '''Generate funny names by randomly combining names from 2 separate lists.'''
    first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
             "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
             'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
             'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread',
             'Crab Meat', 'Crapps', 'Dark Skies', 'Dennis Clawhammer',
             'Dicman', 'Elphonso', 'Fancypants', 'Figgs', 'Foncy', 'Gootsy',
             'Greasy Jim', 'Huckleberry', 'Huggy', 'Ignatious', 'Jimbo',
             "Joe 'Pottin Soil'", 'Johnny', 'Lemongrass', 'Lil Debil',
             'Longbranch', '"Lunch Money"', 'Mergatroid', '"Mr Peabody"',
             'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine', 'Pennywhistle',
             'Pitchfork Ben', 'Potato Bug', 'Pushmeet', 'Rock Candy',
             'Schlomo', 'Scratchensniff', 'Scut', "Sid 'The Squirts'",
             'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki', 'Soupcan Sam',
             'Spitzitout', 'Squids', 'Stinky', 'Storyboard', 'Sweet Tea',
             'TeeTee', 'Wheezy Joe', "Winston 'Jazz Hands'", 'Worms')

    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
            'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
            'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple',
            'Goodensmith', 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag',
            'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins',
            'Jingley-Schmidt', 'Johnson', 'Kingfish', 'Listenbee', "M'Bembo",
            'McFadden', 'Moonshine', 'Nettles', 'Noseworthy', 'Olivetti',
            'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler', 'Pealike',
            'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton', 'Porkins',
            'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal', 'Rubbins',
            'Sackrider', 'Snuggleshine', 'Splern', 'Stevens', 'Stroganoff',
            'Sugar-Gold', 'Swackhamer', 'Tippins', 'Turnipseed', 'Vinaigrette',
            'Walkingstick', 'Wallbanger', 'Weewax', 'Weiners', 'Whipkey',
            'Wigglesworth', 'Wimplesnatch', 'Winterkorn', 'Woolysocks')

    first_name = random.choice(first)
    last_name = random.choice(last)
    pseudonym = f"{first_name} {last_name}"
    return pseudonym

def main():
    '''Main things to do.'''
    al_player = AlPlayer(generate_pseudonym(),get_character_information('Al'))
    player_name = get_player_name()
    character_data = get_character_information('player')
    player = GamePlayer(player_name,character_data)
    blank_line(1)
    player.show_properties()
    blank_line(1)
    al_player.show_properties()
    input( "Are you ready?")

if __name__ == "__main__":
    main()
