import numpy as np
import gymnasium as gym
from gymnasium import spaces

class BiteEnv(gym.Env):
     # metadata
    def __init__(self,render_mode=None):

        # 'other_player_info': gym.spaces.Tuple([
        #                 gym.spaces.MultiDiscrete([5, 2, 2, 2, 4, 4]),
        #                 # num_damage_points, is_bitten, is_cursed, role_revealed, num_suspicion, face_down_cards
        #                 gym.spaces.Discrete(3)  # role
        #             ]).flatten(outermost=True).shape(len(player_list))
        players = 4
        action_space = set()
        set_of_3 = [(card, player) for card in range(28) for player in range(players)]
        for action in set_of_3:
            action_space.add(action)

        # Possible actions for the set of 2 cards
        set_of_2 = [(card, player) for card in range(28) for player in range(players)]
        for action in set_of_2:
            action_space.add(action)

        # Create a gym action space
        n_actions = len(action_space)
        self.action_space = spaces.Discrete(n_actions)

        self.observation_space = gym.spaces.Dict({
            'num_damage_points': gym.spaces.Discrete(5),  # 0-4 damage points
            'is_bitten': gym.spaces.Discrete(2),  # 0 or 1 for isBitten
            'is_cursed': gym.spaces.Discrete(2),  # 0 or 1 for isCursed
            'role_revealed': gym.spaces.Discrete(2),  # 0 or 1 for roleRevealed
            'num_suspicion': gym.spaces.Discrete(4),  # 0-3 suspicion points
            # 'first_card_id': gym.spaces.Discrete(29),  # 0-28 card id for first card
            # 'second_card_id': gym.spaces.Discrete(29),  # 0-28 card id for second card
            'face_down_cards': gym.spaces.Discrete(4),  # 0-3 face down cards (optional)
            'face_up_cards': gym.spaces.Discrete(3)
        })

    # def reset(self, seed=None, options=None):
    #  # We need the following line to seed self.np_random
    #  super().reset(seed=seed)

     # Choose the agent's location uniformly at random


     # # We will sample the target's location randomly until it does not coincide with the agent's location
     # self._target_location = self._agent_location
     # while np.array_equal(self._target_location, self._agent_location):
     #     self._target_location = self.np_random.integers(
     #         0, self.size, size=2, dtype=int
     #     )
     #
     # observation = self._get_obs()
     # info = self._get_info()
     #
     # if self.render_mode == "human":
     #     self._render_frame()
     #
     # return observation, info
