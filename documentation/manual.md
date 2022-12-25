# Manual

Download the latest release [here](https://github.com/ismomehdi/ot-harjoitustyo/releases/tag/viikko6).

## Installation

Install dependencies using the following command:

```bash
poetry install
```

## Run

Run the application with the command:

```bash
poetry run invoke start
```

The database will be set up automatically the first time.

## Play

- Use arrow keys to navigate in the main menu and return key to choose an option. 
- **Note**: the *Options* window is not created yet and will not react to user input.

![](https://github.com/ismomehdi/ot-harjoitustyo/blob/main/images/menu.png)

- You can move the player using the left and right keys. The player jumps from the up key.
- You get points for collecting coins and destroying enemies. Destroy enemies by jumping on top of them.
- Don't let the enemies hurt you, they can be deadly!
- Press Esc to pause the game.

![](https://github.com/ismomehdi/ot-harjoitustyo/blob/main/images/play.png)

- The game ends when you reach the goal pole.
- Your name is requested for the High Scores table if you make it to the top 10.
- Every game ends with the top 10 High Scores listed.

![](https://github.com/ismomehdi/ot-harjoitustyo/blob/main/images/top10.png)

