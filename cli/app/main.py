import time
import json

from requests import Session


class Card:
    def __init__(self,
                color='',
                number=0,
                role='default'):
        self.color = color
        self.number = number
        self.role = role
        
    def __str__(self):
        return json.dumps({
            'color': self.color,
            'number': self.number,
            'role': self.role
        })


class State:
    players = []
    stack = []
    trash = []


class Player:
    name = ''
    hand = []

    def __str__(self):
        return json.dumps({
            'name': self.name,
            'hand': self.hand
        })


class Game:
    def __init__(self):
        self.sess = Session()
        self.player = Player()
        self.state = State()

        self.url = 'http://localhost:5001'
        self.conn = True
        self.player.name = input('Name: ')

        self.start()

    def update_state(self):
        try:
            res = self.sess.get(f'{self.url}/state')

            self.conn = True
        except:
            self.conn = False
    
    def update_game(self):
        time.sleep(.5)

        self.update_state()

        if not self.conn:
            print('No connection with the server.')
            return
        
        input('digite algo: ')

    def start(self):
        while True:
            self.update_game()

Game()
