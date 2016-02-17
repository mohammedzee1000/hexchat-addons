from __future__ import print_function

from random import choice

import hexchat

__module_name__ = 'Slap'
__module_version__ = '2.0'
__module_description__ = 'Slaps specified users'
__author__ = 'Douglas Brunal (AKA) Frankity'

slaps = [
    'slaps {} around a bit with a large trout',
    'gives {} a clout round the head with a fresh copy of WeeChat',
    'slaps {} with a large smelly trout',
    'breaks out the slapping rod and looks sternly at {}',
    'slaps {}\'s bottom and grins cheekily',
    'slaps {} a few times',
    'slaps {} and starts getting carried away',
    'would slap {}, but is not being violent today',
    'gives {} a hearty slap',
    'finds the closest large object and gives {} a slap with it',
    'likes slapping people and randomly picks {} to slap',
    'dusts off a kitchen towel and slaps it at {}'
    'throws a paticularly large whale at {}'
    'draws {} with ascii art'
    'sets +b  {} *!*@*'
    '*facepalm*'
    '*facepalm*`s due to  {} '
    'casts Hemorrhoids on  {} '
    'kicks  {}  in the left shin'
    'pants  {} '
    'pelts a manual at  {} '
    'pushes  {}  into a pit of snakes'
    'puts gum in  {} s hair'
    'puts on a white glove and slaps  {} '
    'rocks  {} s boat'
    'slaps  {}  with a 4r7a8i9n11b6o13w trout'
    'slaps  {}  with a brick'
    'slaps  {}  with a broken c64 manual '
    'slaps  {}  with a crowbar'
    'slaps  {}  with a large }{FISH}'
    'slaps  {}  with a triangle from the 5th dimension'
    'slaps  {}  with a trout'
    'slaps  {}  with a 1990s TV antenna'
    'stabs  {}  in the Medulla Oblongata'
    'stabs  {}  in the Pancreas'
    'throws a Horny Lizard at  {} '
    'throws a Horny Toad at  {} '
    'throws a black 2x2 lego under  {} s foot'
    'throws a blue 2x2 lego under  {} s foot'
    'throws a white 4x1 lego under  {} s foot'
    'throws a yellow 4x1 lego under  {} s foot'
    'ties  {} s shoe to the desk while not looking'
    'zaps  {}  with a green laser beam'
    'zaps  {}  with a purple laser beam'
    'zaps  {}  with a red laser beam'
    'zaps  {}  with a yellow laser beam'
]


def slap_cb(word, word_eol, userdata):
    if len(word) > 1:
        nick = word[1]
        hexchat.command('me ' + choice(slaps).format(nick))
    else:
        hexchat.command('help slap')
    return hexchat.EAT_ALL


def unload_cb(userdata):
    print(__module_name__, 'version', __module_version__, 'unloaded.')

hexchat.hook_command('slap', slap_cb, help='SLAP <nick>')
hexchat.hook_unload(unload_cb)
print(__module_name__, 'version', __module_version__, 'loaded.')
