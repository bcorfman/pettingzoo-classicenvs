from collections import namedtuple

from pettingzoo.classic import (
    connect_four_v3,
    tictactoe_v3,
)

from core.traineval import eval_action_mask, get_latest_policy, train_action_mask


def main():
    # Evaluation/training hyperparameter notes:
    # ConnectFour 40k steps: Winrate:  0.86, loss order of 7e-06
    # TicTacToe 60k steps: Winrate for P2 (O) when P1 (X) moves first: 0.66, loss order of 6e-06
    Env = namedtuple("Env", ["fn", "num_steps"])
    envs = [
        Env(connect_four_v3, 41000),
        Env(tictactoe_v3, 61000),
    ]
    for env in envs:
        env_kwargs = {}

        if not get_latest_policy(env.fn):
            # Train a model against itself.
            # Train from scratch only if we can't find latest model on disk.
            # If retraining is desired, delete the model .zip files from
            # the project directory.
            train_action_mask(env.fn, steps=env.num_steps, seed=0, **env_kwargs)

        print()
        print("-----------------------------------")
        print("Eval 100 games against random agent")
        print("-----------------------------------")
        # Evaluate 100 games against a random agent (winrate should be ~80%)
        eval_action_mask(env.fn, num_games=100, render_mode=None, **env_kwargs)

        print()
        print("------------------------------------")
        print("Display 2 games against random agent")
        print("------------------------------------")
        # Watch two games vs a random agent
        eval_action_mask(env.fn, num_games=2, render_mode="human", **env_kwargs)


if __name__ == "__main__":
    main()
