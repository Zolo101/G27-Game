# Five Nights At Founders
F.K.A
## Base 27

## Building locally

Requirements
- SimpleGUICS2Pygame
- noise

```shell
pip install SimpleGUICS2Pygame noise
```

## What each file does
- **assets**: Contains every asset used in the game
- **src/classes**: Contains utility classes that are used throughout the games code
  - Clock.py - Frame counter, used for animation frames
  - Color.py - Allows for easy color manipulation, used extensively in the terrain
  - ControlManager.py - Provides an easy interface for handling user input
  - Interaction.py - Handles collision detection between objects
  - Music.py - Runs the background music
  - SceneManager.py - Manages the scenes in the game, for example switching between scenes
  - Sprite.py - Base class for all sprites in the game
  - Spritesheet.py - Spritesheet texture manipulator for animated sprites, such as the zombie and player
  - Vector.py - 2D Vectors, used mainly in sprite movement and velocity
- **src/game**: Contains classes that are used to create the game such as sprites
  - Builder.py - Draws the build helper square, so you know where your building
  - Bullet.py - Draws the bullet shot by Shoot.py
  - Cloud.py - Draws the clouds in the background
  - Game.py - Main game loop where all constants and global variables reside
  - Perks.py - Draws the perks that fall from the sky
  - Pew.py - Draws the flamethrower the player yields
  - Player.py - Draws the sprite that the user controls
  - Shoot.py - Handles the bullets collision after shot by the player
  - Sky.py - Draws the background, sun and moon
  - Terrain.py - Draws the terrain blocks that the player can build and destroy on
  - UI.py - Draws the UI elements such as the health bar, score and night counter
  - WaveManager.py - Manages the difficulties of each zombie wave
  - Zombie.py - Draws the zombies that drop down and attack the player at night
- **src/scenes**: Contains every scene in the game, used by SceneManager
  - backstory.py - A (secret!) backstory scene
  - controls.py - Controls scene for the game
  - game_over.py - Game over scene for when you die
  - main.py - This is the main game scene
  - welcome.py - First scene of the game, gives a backstory
  - win.py - Win scene for when you survive all five nights!
- **index.py** - Where you run the game. Do `python index.py`
