from Bite import Bite
import random
import gymnasium as gym
import rlcard
from rlcard.agents import RandomAgent

b = Bite()
# class BiteEnv(rlcard.envs.Env):

for player in b.players:
    print("Player Options: ")
    player.cycle_hand(b.draw())
    for card in player.hand:
        print(card)
        b.processFactory(player, random.choice(b.players), card)

for player in b.players:
    print(player, end="\n\n")
