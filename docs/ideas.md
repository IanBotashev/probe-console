In general, a command terminal game about trying to understand what's going on in space just through a console.  
Control, mine and explore all through the terminal.

## Fog of war
We pre-generate a solar system with around 5-8 celestial objects  
Celestial objects have flags on them indicating what has been revealed  

## Player
The player object is what handles command line inputs  

## Resources
Resources found on celestial objects can be sold  
Sold into dollars, currency allows to build and do actions 
They're mined in "units", whole numbers  
Sell value is for `one unit`  

Maybe a stock market later on  

| Name   | Sell Value ($/unit) |
|--------|---------------------|
| Gold   | 50                  |
| Iron   | 5                   |
| Lead   | 10                  |
| Copper | 10                  |



## Buildings  
things can be built using currency  
on homeworld, can build buildings for upgraded stats  
unlimited slots for objects  

| Name        | Description |
|-------------|-------------|
| None so far |             |


## Probes
Probes are at any time located at a celestial object   
Communicate with them through console, something like:  
`connect probe_1`  
`status`  
gives a status on the probe  
`disconnect`  
Used for tasks outside the homeworld such as, exploration, mining, surveying, increasing range, etc.  
Has a currency for these tasks: energy.  
Essentially a budget for other modules  
Probes can designed, by adding modules to them which can do certain tasks.  

| Module       | Description                                      | Energy Cost | Dollar Cost |
|--------------|--------------------------------------------------|-------------|-------------|
| Solar Panel  | Adds 1 energy to the budget every tick           | 0           | 2           |
| Battery      | Stores 5 energy                                  | 0           | 2           |
| Landing Legs | Allows landing on objects to mine, explore, etc. | 1           | 10          |
| Scanner      | Surveys objects, reveals info on them            | 1           | 5           |
| Drill        | Mines resources                                  | 1           | 10          |


Probes also have a certain amount of fuel, each fuel point allows them to move to another celestial object

## Objects
There's tiers to the objects, each consequent tier has more resources than the last.  
Although, higher tiers have less expensive resources, usually only having lower tiers of resources  
Each tier has a different amount of "resource slots" it can have, each resource slot being the name of a resource, and the amount of units of that resource there.  

| Object Name | Resource Slots |
|-------------|----------------|
| Asteroid    | 1              |
| Moon        | 2              |
| Planet      | 3              |

## General Mechanics
Range: How far we can communicate and see. Defined by the farthest probe  
__str__: used only for pretty printing into the users console.  
__repr__: used for short pretty_printing

## Tick System
1 tick = 1 real life second  
Managed by a thread, that is running a function from the game manager  
Tick length can be adjusted in settings.py under `TICK_SLEEP_TIME`  

## Starting Conditions
Player starts knowing 2 celestial objects  
Initial funds of $100
No probes  