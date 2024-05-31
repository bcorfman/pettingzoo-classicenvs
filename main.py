from pettingzoo.classic import connect_four_v3

from core.traineval import eval_action_mask, get_latest_policy, train_action_mask


def main():
    env_fn = connect_four_v3

    env_kwargs = {}

    # Evaluation/training hyperparameter notes:
    # 10k steps: Winrate:  0.76, loss order of 1e-03
    # 20k steps: Winrate:  0.86, loss order of 1e-04
    # 40k steps: Winrate:  0.86, loss order of 7e-06

    if not get_latest_policy(env_fn):
        # Train a model against itself (takes ~40 seconds on a laptop CPU).
        # Train from scratch only if we can't find latest model on disk.
        # If retraining is desired, delete the model .zip files from
        # the project directory.
        train_action_mask(env_fn, steps=41000, seed=0, **env_kwargs)

    print()
    print("-----------------------------------")
    print("Eval 100 games against random agent")
    print("-----------------------------------")
    # Evaluate 100 games against a random agent (winrate should be ~80%)
    eval_action_mask(env_fn, num_games=100, render_mode=None, **env_kwargs)

    print()
    print("------------------------------------")
    print("Display 2 games against random agent")
    print("------------------------------------")
    # Watch two games vs a random agent
    eval_action_mask(env_fn, num_games=2, render_mode="human", **env_kwargs)


if __name__ == "__main__":
    main()
