# Relativistic Space Invaders

[![Language](https://img.shields.io/badge/language-python-blue.svg?style=flat)](https://www.python.org)
[![Module](https://img.shields.io/badge/module-pygame-brightgreen.svg?style=flat)](http://www.pygame.org/news.html)

## About 

Relativistic Space Invaders uses the classic game Space Invaders to demonstrate the visual effect of special relativity using [jarrydac/gl_relativity](https://github.com/jarrydac/gl_relativity).

The relativistic effects are relative to an observer inside the ship. Enemy bullets are blue-shifted as they fly towards the player, and player bullets are red-shifted as they fly away from the player. Likewise the game objects experience length contraction, time dilation and doppler shift as the player flies back and forth.

This project is forked from [leerob/space-invaders](https://github.com/leerob/space-invaders).

<img src="https://i.imgur.com/HF5Ub8v.png" />

## Space Invaders

Space Invaders is a two-dimensional fixed shooter game in which the player controls a ship with lasers by moving it horizontally across the bottom of the screen and firing at descending aliens. The aim is to defeat five rows of ten aliens that move horizontally back and forth across the screen as they advance towards the bottom of the screen. The player defeats an alien, and earns points, by shooting it with the laser cannon. As more aliens are defeated, the aliens' movement and the game's music both speed up.

The aliens attempt to destroy the ship by firing at it while they approach the bottom of the screen. If they reach the bottom, the alien invasion is successful and the game ends. A special "mystery ship" will occasionally move across the top of the screen and award bonus points if destroyed. The ship is partially protected by several stationary defense bunkers that are gradually destroyed by projectiles from the aliens and player.

## Installation

Install the dependencies listed for [gl_relativity](https://github.com/jarrydac/gl_relativity#building). This project also depends on [Pygame](http://www.pygame.org).

Run the `INSTALL.sh` script, which will download, build and install `gl_relativity`.

## How To Play

- If you have the correct dependencies installed, you can run the program in the command prompt / terminal.

```bash
python ./spaceinvaders.py
```

## Demo

_TODO_

