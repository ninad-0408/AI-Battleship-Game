# Battleship Game

### Index
1. [Abstract](#Abstract)
2. [Introduction](#Introduction)
3. [Literature Survey](#Literature%20Survey)
4. [Objective](#Objective)
5. [Methodology](#Methodology)
6. [Working](#Working)
7. [Used Python Libraries](#Used%20Python%20Libraries)
8. [Results and Discussion](#Results%20and%20Discussion)
9. [Conclusion](#Conclusion)

## Abstract
> In this project, a battleship game is played between agent and humans. This is a software mode of the Battleship game. This will be useful for people who live alone or who cannot afford to buy hardware games. This agent is based on a heuristic search algorithm. 


<!-- ## Keywords
+ AI Game playing
+ Heuristic search
+ Numpy
+ Colorama
+ Battleship game
+ Probability and statistics -->

## Introduction

+ ### Game Rules
    + The game is played between two players. 
Each player will have its own ocean area and 5 different kind of ships of different kind:
        + Carrier
        + Battleship
        + Cruiser
        + Submarine
        + Destroyer
    + The ocean is divided into different cells which can be located by row and column pattern.
    + The rows are denoted as A-J and columns are denoted as 0-9 (according to size).
Width of each ship is 1 unit and length of ships are denoted in table below:

        | No. | Class of Ship | Size |
        --- | --- | --- |
        1 | Carrier | 5 |
        2 | Battleship | 4 |
        3 | Cruiser | 3 |
        4 | Submarine | 3 |
        5 | Destroyer | 2 |



    + Each player will place the ships in its ocean either horizontally or vertically. It cannot be placed diagonally and 1 cell cannot be occupied by two ships. Ships should be placed only in allotted regions of the ocean. Ships once placed are not allowed to move during game.
    + After the arrangement the player will target the chosen coordinates of another player’s ocean. If it hits the ship the opponent will mark it as hit and tell which type of ship is hit else will tell as miss and now it's his turn to target.
    + The ship will sink when all cells are hit by an opponent. The first player to sink all opponent ships is the winner.

+ ### How to Play?

    + First you will be promoted to set up your base in the ocean. You will be shown an area of ocean in which you can place your ships as described above. You must input a valid orientation and starting location of ships.
    + After setting up the base your game will be started. You will be shown your base and opponent’s base with hidden ships. You can guess cell position by row and column index values.
    + If you hit an opponent's ship it will print ‘hit’ and name of ship you hit.
    + Then agent will play its move.

## Literature Survey

+ There are many approaches for this project like heuristic search, by using probability and statistics, by using learning agent, etc.
+ Other approaches are:
    + Q-learning best action
    + Agent training using linear model
    + Q-learning using open AI and neural network


## Objective

+ The objective of project is to learn the use of AI in real life scenario.
+ This project will help others to spend their time.
+ This project help to enrich my programming skills and I learnt more about python and its libraries.

## Methodology

+ ### Performance Measure
    + #### Success: 
        > It is defined as how many times the agent wins against the human in a particular set of games.
    + #### Efficiency: 
        > It is defined as the number of moves required by an agent to win a particular game. For this model it is around 60% of total possible moves.
+ ### Environment
    + #### Non-Deterministic: 
    > Agent is not able to tell that the chosen cell has a ship or not before attacking it.
    + #### Static:
    > As we cannot change the position of ships once they are placed.
    + #### Discrete:
    > Agent cannot attack already attacked cells and cells outside the environment.
    + #### Accessible:
    > As an agent can attack any cell in the environment so the environment is fully accessible to agent.
    + #### Partially observable:
    > Agent can explore the attacked cells but cannot know about unattacked cells.
+ ### Actuators
    + When the agent decides the attacking cell actuator will mark it as attacked.
    + Actuators help in setting up ships in base when the cell and orientation of the ship is decided by the agent.
+ ### Sensors
    + Sensors will help agent to get      information about the environment.
    + Sensors can determine the empty region in base while setting up base.
    + It will help to judge whether the attacked cell is empty or which ship is hit at that cell.
    + It will also give information about already attacked cells which cannot be attacked again.

## Working

+ ### Setting up the base
    + For setting all ships into base agent will randomly select the orientation of ship and location in the ocean and search side wise using depth first search.
    + In searching if it encounters a ship or an end it will terminate the search and will guess another cell location and the process continues until the ship is placed in its place.
    + This process is done for all 5 ships.

+ ### Attacking a cell

    + The agent will randomly guess a cell which is not already attacked and mark it as an attacked thought actuator.
    + Sensors will tell that the attacked cell is occupied by which ship and its ship size which can be derived from its name. If it is not attacked it will start guessing another cell.
    + If sensors detect that the cell is occupied by ship it will give the size of ship.
    + The searching in this environment is done by help of sensors and actuators. For accessing a cell actuator will attack it first and the sensor will tell if it has a ship or not. Search will be stopped if it doesn’t encounter a ship.
    + After a sensor encounters a ship agent will start searching around that cell in all directions. Agent will repeatedly perform the Depth first search to find the orientation of the ship. The it will hit all ship cells until ship sinks.
    + Agent will determine whether to search in all directions or in a single direction according to ship size and orientation.
    + Meanwhile if it encounters another ship it recursively performs above operations.


## Used Python Libraries

> + Numpy
> + Random
> + Colorama
> + OS

## Results and Discussion

+ This project is based on blind search algorithms.
+ It will give humans a good opponent to play with.
+ The game will be interesting if player will play optimally and using techniques.

## Conclusion
+ The project is successfully implemented and + can work on python3 compiler.
+ I learned various python libraries and their implementation in making this project.
+ It also enhanced my programming skills in python.
+ I will improve agent performance in this project and introduce learning agent.
