#!/usr/bin/python
# -*- coding: utf-8 -*-

#Banner for Image Editor


import random

header1='''
    _                              _ _
   | |                            / (_)   |  o                
   | | _  _  _    __,   __,  _    \__   __|    _|_  __   ,_   
 _ |/ / |/ |/ |  /  |  /  | |/    /    /  |  |  |  /  \_/  |  
 \_/\/  |  |  |_/\_/|_/\_/|/|__/  \___/\_/|_/|_/|_/\__/    |_/
                         /|                                   
                         \|                                   
'''

header2='''
    ____                              ______    ___ __            
   /  _/___ ___  ____ _____ ____     / ____/___/ (_) /_____  _____
   / // __ `__ \/ __ `/ __ `/ _ \   / __/ / __  / / __/ __ \/ ___/
 _/ // / / / / / /_/ / /_/ /  __/  / /___/ /_/ / / /_/ /_/ / /    
/___/_/ /_/ /_/\__,_/\__, /\___/  /_____/\__,_/_/\__/\____/_/     
                   /____/                                        
'''
header3='''
o-O-o                        o--o    o    o          
  |                          |       | o  |          
  |   o-O-o  oo o--o o-o     O-o   o-O   -o- o-o o-o 
  |   | | | | | |  | |-'     |    |  | |  |  | | |   
o-O-o o o o o-o-o--O o-o     o--o  o-o |  o  o-o o   
                   |                                 
                o--o                                 
'''
header4='''

888                              8888    8 w  w              
 8  8d8b.d8b. .d88 .d88 .d88b    8www .d88 w w8ww .d8b. 8d8b 
 8  8P Y8P Y8 8  8 8  8 8.dP'    8    8  8 8  8   8' .8 8P   
888 8   8   8 `Y88 `Y88 `Y88P    8888 `Y88 8  Y8P `Y8P' 8    
                   wwdP                                      
'''
header5='''
 ___                      _                  
  |  ._ _   _.  _   _    |_  _| o _|_  _  ._ 
 _|_ | | | (_| (_| (/_   |_ (_| |  |_ (_) |  
                _|                           
'''

header6='''
 _                                     ___        _     _                
(_)                                   (  _`\     ( ) _ ( )_              
| |  ___ ___     _ _    __     __     | (_(_)   _| |(_)| ,_)   _    _ __ 
| |/' _ ` _ `\ /'_` ) /'_ `\ /'__`\   |  _)_  /'_` || || |   /'_`\ ( '__)
| || ( ) ( ) |( (_| |( (_) |(  ___/   | (_( )( (_| || || |_ ( (_) )| |   
(_)(_) (_) (_)`\__,_)`\__  |`\____)   (____/'`\__,_)(_)`\__)`\___/'(_)   
                     ( )_) |                                             
                      \___/'                                             
'''


def header():
	header = [header1,header2,header3,header4,header5,header6]
	return random.choice(header)
	#return header7

   
