# Application Architecture
## Basic Structure
This is the main structure of the application:

<p align="center"><img src="https://github.com/ismomehdi/ot-harjoitustyo/blob/main/images/Untitled%20Diagram.drawio.png"></p>

## Setting up the World
Here's a simplified visualization of how the World class uses level maps to set the x & y coordinates of the sprites:

```mermaid

sequenceDiagram
  participant Level
  participant Main
  participant World
  participant GroundTile
  Level-->>Main: level_map
  Main->>World: World(level_map)
  
  alt level_map column == 'X'
    GroundTile->>World: GroundTile(column_index, row_index)
  else level_map column == 'x'
    SkyTile->>World: Skytile(column_index, row_index)
  else level_map column == 'P'
    Player->>World: Player(column_index, row_index)
  else level_map column == 'o'
    Coin->>World: Coin(column_index, row_index)
  end
  
```
