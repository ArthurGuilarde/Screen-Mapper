# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 09:51:09 2022

@author: arthur.guilarde
"""
import os
import time
import pyautogui as pg
from datetime import timedelta

# =============================================================================
# GLOBAL VARIABLES
# =============================================================================
__FILES_MAP__ = {}
__PATH__ = os.getcwd() + '/images/'


# =============================================================================
# All action functions
# =============================================================================
def click_xy(x, y, button='left', action=1):
    """Click at X, Y value
        x: value in X axis
        y: value in Y axis
        button: left or right mouse button
        action: qtd of clicks
    """
    for a in range(action):
        pg.click(x, y, clicks=1, interval=0.25, button=button)

def click_img(img, button='left', action=1):
    """Find image and click
        img: image path
        button: left or right mouse button
        action: qtd of clicks
    """  
    x = None
    y = None
    counter = 0   
    
    # Find img at screen
    while x == None and y == None:
        try:
            x, y = pg.locateCenterOnScreen(img)
        except Exception:
            if counter < 50:
                print(f'Image - {img} not found. retrying...')
            else:
                raise Exception(f'Image - {img} not found!!!')
        finally:
            counter += 1
    
    click_xy(x, y, button, action)
        
def press_tab(action=1):
    """Key press 'TAB'
        action: qtd of press by key
    """  
    for a in range(action):
         pg.press('tab')

def press_space(action=1):
    """Key press 'SPACE'
        action: qtd of press by key
    """ 
    for a in range(action):
        pg.press('space')
         
def press_arrow_down(action=1):
    """Key press 'DOWN'
        action: qtd of press by key
    """ 
    for a in range(action):
         pg.press('down')

def write(message='foo', interval=0):
    """Write a message
        message: message will be written
    """ 
    pg.write(message, interval)
    
def press_enter(action=1):
    """Key press 'ENTER'
        action: qtd of press by key
    """  
    for a in range(action):
         pg.press('enter')
         
def set_timer(seconds=1):
    """Set timer sleep
        seconds: seconds of sleep
    """  
    time.sleep(seconds)
         

# =============================================================================
# Function to perform into dictinory 
# =============================================================================
"""Exmaple of dictinory

   {0: (click_img, ['teste.png', ], write, ['teste', ])}
   
   key: 0
   functions: click_img and write
   params: ['click_img_param_list.png', ] and  ['write_param_list', ]
   
"""
def dict_map_perform(dict_map):
    for key in dict_map:
        params = None
        function = None
        
        for v in dict_map[key]:
            if type(v) == list:
                params = v
            else:
                function = v
            
            if params != None and function != None:
                function(*params)
                
                params = None
                function = None


# =============================================================================
# Dictinory format build func, params list
# =============================================================================   
__FILES_MAP__ = {
    0: (click_img, [f'{__PATH__}google.png', 'left', 0]),
    1: (
        click_img, [f'{__PATH__}search_bar.png', ],
        write, ['github', ],
        press_enter, [1, ]
        ),
    2: (click_img, [f'{__PATH__}github_url.png', ]),
    3: (
        click_img, [f'{__PATH__}github_search.png', ],
        write, ['Arthur Guilarde', ],
        press_enter, [1, ]
        ),
    4: (click_img, [f'{__PATH__}github_arthur.png', ]),
    
    }



if __name__ == '__main__':
        
    START = time.time()
    
    dict_map_perform(__FILES_MAP__)
      
    END = time.time()
    
    print(str(timedelta(seconds=(END - START))))
