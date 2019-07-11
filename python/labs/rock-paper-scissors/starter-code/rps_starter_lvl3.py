#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""While loop Example"""
# index = 0
# while index <= 10:
# print(index)
# index += 1

"""For loop Example"""
# for letter in "hello":
# print(letter.upper())

import random

print("welcome to Rock Paper Scissors :)")
print("You will have a match with the computer")

computerWins = 0
playerWins = 0
tie = 0

def get_player_move():
    """Asks the user to enter a move as 'r', 'p', or 's', and return it"""
    player = raw_input("Which do you choose (type: 'rock', 'paper', or 'scissors'): ").lower
    return player

    # TODO


def get_computer_move():
    """Randomly generates the computer's move and
    returns it in the form of 'r', 'p', or 's'"""
    computerChoice = ["rock", "paper", "scissors"]
    computer = random.choice(computerChoice)
    return computer

    # TODO


def determine_winner(player_move, comp_move):
    """Takes in a player move and computer move each as 'r', 'p', or 's',
    and returns the winner as 'player', 'computer', or 'tie'"""
    if player == computer:
        tie += 1
        return "tie"
    elif player == "rock" and computer == "scissors" or
         player == "paper" and computer == "rock" or
         player == "scissors" and computer == "paper":
         playerWins += 1
         return "player"
     else:
         computerWins += 1
         return "computer"

    # TODO


def print_scoreboard(player_wins, comp_wins, ties):
    """Prints out the scoreboard neatly.  Returns nothing."""
    print("ties: " + str(tie))
    print("player: " + str(playerWins))
    print("computer: " + str(computerWins))

    # TODO


def get_move_name(short_move):
    """Takes in 'r', 'p', or 's', and returns 'Rock', 'Paper, or
    'Scissors' respectively. Use this to neatly print move choices"""

    # TODO


# Write your code below - make RPS happen using the functions above!
determine_winner(get_player_move(), get_computer_move())
