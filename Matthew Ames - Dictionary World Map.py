world_map = {
    'HDUM': {
        'NAME': "Home Dumpster.",
        'DESCRIPTION':
            "Every hobo in the Istan Allies owns a dumpster, this one's yours.\n In it is a chest that you really wanna"
            " open. There are allies to the North, South, East and West of you.",
        'PATHS': {
            'NORTH': 'NA',
            'SOUTH': 'DWPC',
            'WEST': 'UGKN',
            'EAST': 'RDUM'
                 }
                 },
    'NA':   {
        'NAME': 'North Alley.',
        'DESCRIPTION': 'You are in the main North alley. To the east of you is the entrance to an abandoned apartment.'
                       'The alley continues North. ',
        'PATHS': {
            'WEST': 'ABAP',
            'NORTH': 'CORNER',
            'SOUTH': 'HDUM'
                 },
            },
    'DWPC': {
            'NAME': 'Door with passcode.',
            'DESCRIPTION': 'This door is locked.If you could open it, it would open to reveal a room to your East.\n'
                           ' There is a lock on the door that requires a passcode to open it.',
            'PATHS': {
                'EAST': 'BACH',
                'NORTH': 'HDUM'
                     },
                 },
    'RDUM': {
            'NAME': ' A Red Dumpster.',
            'DESCRIPTION': ' Inside it is a flashlight. To the North of you is a mysterious\n'
                           'looking figure. The the west of you is your Home Dumpster.',
            'PATHS': {
                'WEST': 'HDUM',
                'NORTH': 'MWK'
                     }

                },
    'UGKN': {
            'NAME': 'Ugandan Knuckles Territory.',
            'DESCRIPTION': 'You come across an odd red creature. It reminds you of something\n from a show you used to'
                           ' watch as a child. Except kind of deformed.',
            'PATHS': {
                'EAST': 'HDUM',
                'SOUTH': 'HIHE'

                     }

                },
    'HIHE': {
        'NAME': 'High Heels.',
        'DESCRIPTION': "You stumble across an empty area with fabulous red high\n heels in the center."
                       "You think you'd look great in them.",
        'PATHS': {
            'NORTH': 'UGKN'
        },
        'ITEMS': {
            'HIGH HEELS': 'You feel fabulous.'
        }
    },
    'ABAP': {
        'NAME': 'Abandoned Apartment.',
        'DESCRIPTION': 'It is too dark to see.',
        'PATHS': {
            'EAST': 'NA'
                 }

            },
    'CORNER': {
        'NAME': 'Corner.',
        'DESCRIPTION': 'You are at a wall. To the West is an alley leading to a dumpster with food in it. '
                       'To the East is an alley with a \n mysterious looking figure staring at you from the end. '
                       'You are feeling hungry.',
        'PATHS': {
            'WEST': 'FDUM',
            'EAST': 'MWK',
            'SOUTH': 'HDUM'
                 }

              },
    'FDUM': {
        'NAME': 'Dumpster with food.',
        'DESCRIPTION': 'This dumpster has a perfectly fine piece of pizza of pizza sitting on top of a stack of garbage'
                       '\nbags. To the North is a ghostly toilet. To the West is an open door to an unknown room.',
        'PATHS': {
            'WEST': 'PERO',
            'EAST': 'CORNER',
            'NORTH': 'GHTO'
                 }

            },
    'PERO': {
        'NAME': 'Penny Room.',
        'DESCRIPTION': "You are in a room full of pennies. Upon further inspection you see that most of the pennies are"
                       "\nfake. If there are real pennies in here, you can't and won't look for them.",
        'PATHS': {
            'EAST': 'FDUM'
                 }
            },
    'GHTO': {
        'NAME': 'Ghostly Toilet.',
        'DESCRIPTION': 'This is an empty room with a randomly placed toilet in the \ncenter and a randomly placed'
                       ' sink to the West of it.',
        'PATHS': {
            'SOUTH': 'FDUM',
            'WEST': 'SINK'
                 }
            },
    'SINK': {
        'NAME': 'The Sink.',
        'DESCRIPTION': "The Sink is very odd, as it doesn't have any nobs to turn the water on. Also, the faucet is"
                       " \nabout 5 inches in diameter for some reason. Maybe there's a way to turn it on.",
        'PATHS': {
            'EAST': 'GHTO'
                 }
            },
    'MWK': {
        'NAME': 'Mysterious man.',
        'DESCRIPTION': "Upon further inspection, the mystery figure is actually a man dressed in a dark trench coat"
                       " \nthat goes down to his ankles, as well as a fedora on top of his head. Around his neck is a"
                       "\nchain with a key on it. It might be what you're looking for. To the North is the entrance "
                       "to an abandoned apartment.",
        'PATHS': {
            'NORTH': 'ABSHE',
            'SOUTH': 'RDUM',
            'WEST': 'CORNER'
                 }
           },
    'ABSHE': {
        'NAME': 'The Abandoned Shop Entrance.',
        'DESCRIPTION': "The shop appears to have been avoided by all life for some time. You don't know why.\n "
                       "To the West of you is a big red button on the wall with a sign above it that says, 'Useless'.",
        'PATHS': {
            'NORTH': 'ABSH',
            'WEST': 'POBU',
            'SOUTH': 'MWK'
                 }
             },
    'ABSH': {
        'NAME': 'The Abandoned Shop.',
        'DESCRIPTION': 'It is too dark to see.',
        'PATHS': {
            'SOUTH': 'ABSHE'
                 }
            },
    'POBU': {
        'NAME': 'The Pointless Button.',
        'DESCRIPTION': "The button is big and red. It's very enticing. You feel a strong urge to push it. Above it is a"
                       " \nsign that says, 'Useless Button'.",
        'PATHS': {
            'EAST': 'ABSHE'
                 }
            }

            }

current_node = world_map['HDUM']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

while True:
    print("You are at", current_node['NAME'], current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            print(name_of_node)
            current_node = world_map[name_of_node]
        except KeyError:
            print("Your leg won't move you in that direction.")
    elif 'TAKE' in command:
        item = command[5:]
        if item in current_node['ITEMS']:
            print(current_node['ITEMS'][item])
            current_node['ITEMS'].pop(item)
        else:
            print("There is nothing there.")
    else:
        print("Welp, I'm feeling a little stupid right now, cause I can't act out my own thoughts.")
