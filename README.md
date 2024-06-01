# PettingZoo-ConnectFour

[PettingZoo](https://pettingzoo.farama.org/) ConnectFour example configured with [Rye](https://rye.astral.sh/) as dependency manager. Tested with MacOS Sonoma and Ubuntu on WSL2.

<img src="res/c4.png" style="width: 500px">

## Prerequisites
* At a command prompt in the project directory, type `make devinstall` to set up Rye with the appropriate Python version plus the project-level dependencies in development mode, or just `make install` to set up the code as runnable only.

## To run the example
* At a command prompt in the project directory, type `make run`.
* The first time through, the RL model will be trained and then saved to disk. After that, the trained model will be loaded from disk before evaluation.
* If retraining is desired, delete the model .zip files from the project directory.

## Notes for Visual Studio Code users
* I've included some extension recommendations that can make your development easier.
  * [Run On Save](https://marketplace.visualstudio.com/items?itemName=emeraldwalk.RunOnSave)
  * [Make support and task provider](https://marketplace.visualstudio.com/items?itemName=carlos-algms.make-task-provider)
* These recommendations will pop up when opening the project inside VSCode.
* Installing both extensions will
  * Use the code in `settings.json` to run `make format` and `make lint` on each `File:Save`.
  * Display available Make targets within the _Makefile Tasks_ sidebar pane and allow them to be run with a mouse click.
