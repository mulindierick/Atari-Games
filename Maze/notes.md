<!-- energy -->
give player initial energy
player looses energy as they move from one scene to another
energy spent is different for each scene
if player users all his energy, game is over

<!-- scene cost -->
--give each scene a cost

<!-- treausres -->
add [certain number] of different kinds of treasures to some of the scenes
player should try to pick 1 treausre from each type while in the scene

<!-- inside scene -->
 --add btn to view map
 --probe DFS(can be used only one BUT player may find same in collected teasures)
** search [desired object] -> what object is this ?
** return path if object is found | null if not

 --probe BFS(can be used only one BUT player may find same in collected teasures) - 
** search [desired object] -> what object is this ?
** return path if object is found | null if not

 --robot
** takes in a path from DFS or BFS
** returns object
** dies if path is too long

 --Dijkstra’s algorithm.
** takes in a map
** returns the cheapest path to exit

<!-- start screen -->
-- explains game controls, devices and treasure

<!-- end game -->
--if user enters exit square - get last scene, if user in last scene, end game
--if user users all their energy

<!-- score -->
--value of all treasures picked along the way
--keep scores of each player in a file

<!-- search scores -->
--build binary search tree of scores ordered by name
<!-- background image -->
