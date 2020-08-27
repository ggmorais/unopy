import json

from flask import Flask, jsonify

from deck import deck


app = Flask('game')


class Card:
    def __init__(self,
                color='',
                number=0,
                role='default'):
        self.color = color
        self.number = number
        self.role = role
        self.is_on_trash = False
        
    def __str__(self):
        return json.dumps({
            'color': self.color,
            'number': self.number,
            'role': self.role
        })


class State:
    players = []
    stack = []

    def __str__(self):
        return json.dumps({
            'players': self.players,
            'stack': self.stack
        })

    def create_stack(self):
        for card in deck:
            for i in range(card['count']):
                for times in range(card['times']):
                    c = dict(
                        color=card['color'],
                        number=i if card['role'] == 'default' else None,
                        role=card['role'],
                        is_on_trash=False
                    )
                    self.stack.append(c)


@app.route('/join')
def hello_world():
    if not State.players:
        pass

@app.route('/state')
def state():
    s = State()

    if not s.stack:
        s.create_stack()

    return str(s)
