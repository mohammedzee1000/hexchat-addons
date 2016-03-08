__module_name__ = "pingall"
__module_version__ = "1.0"
__module_description__ = "Python Module to ping everyone"
 
import hexchat
 
 
#folks = ['ccaf_', 'mzee1000', 'preeti', 'lalatenduM', 'budhram', 'ccaf', 'tuxdna', 'bamacharan', 'adisakala']
#folks = ['ccaf_', 'mzee1000', 'preeti', 'lalatenduM', 'budhram', 'ccaf', 'tuxdna', 'bamacharan', 'pradeepto']
folks = ['ccaf_', 'mzee1000', 'preeti', 'lalatenduM', 'budhram', 'ccaf', 'tuxdna', 'bamacharan', 'adisakala', 'mitesh', 'samuzzel']
 
def broadcast(msg):
    for person in folks:
        hexchat.command("MSG {} {} :)".format(person, msg))
 
 
msg = "Lunch?"
broadcast(msg)
