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
    'sets +b  $nick *!*@*'
    '*facepalm*'
    '*facepalm*`s due to  $nick '
    'casts 'Hemorrhoids' on  $nick '
    'kicks  $nick  in the left shin'
    'pants  $nick '
    'pelts a manual at  $nick '
    'pushes  $nick  into a pit of snakes'
    'puts gum in  $nick 's hair'
    'puts on a white glove and slaps  $nick '
    'rocks  $nick 's boat'
    'slaps  $nick  with a 4r7a8i9n11b6o13w trout'
    'slaps  $nick  with a brick'
    'slaps  $nick  with a broken c64 manual '
    'slaps  $nick  with a crowbar'
    'slaps  $nick  with a large }{FISH}'
    'slaps  $nick  with a triangle from the 5'th dimension'
    'slaps  $nick  with a trout'
    'slaps  $nick  with a 1990's TV antenna'
    'stabs  $nick  in the Medulla Oblongata'
    'stabs  $nick  in the Pancreas'
    'throws a Horny Lizard at  $nick '
    'throws a Horny Toad at  $nick '
    'throws a black 2x2 lego under  $nick 's foot'
    'throws a blue 2x2 lego under  $nick 's foot'
    'throws a white 4x1 lego under  $nick 's foot'
    'throws a yellow 4x1 lego under  $nick 's foot'
    'ties  $nick 's shoe to the desk while not looking'
    'zaps  $nick  with a green laser beam'
    'zaps  $nick  with a purple laser beam'
    'zaps  $nick  with a red laser beam'
    'zaps  $nick  with a yellow laser beam'
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
