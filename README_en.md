# Consumable Camouflage Replacer

**English** | [中文](README.md)

## How to Use?

### Export the camouflages.xml from the game

- Download & install an Unpack Tool: WOWS WG - [WOWS Unpack Tool](https://forum.worldofwarships.eu/topic/113847-all-wows-unpack-tool-unpack-game-client-resources/); WOWS RU - [MK Unpack Tool](https://gitlab.com/AutoSpy/mkut/raw/main/MKUnpackTool.exe);
- Run the Unpack Tool, click **Load Content**, unfold the **res** directory, double-click the **camouflages.xml**,
  click **Unpack**;
- Under the running directory of the Unpack Tool (Commonly WoWs\'s installation directory), enter the **res_unpack**
  directory; If the first two steps are correct, you should be able to see a **camouflages.xml**;

### Modify the camouflages.xml via the program

- In the project\'s Release, download the [consumable_camouflage_replacer.exe
  ](https://github.com/MikhailTapio/ConsumableCamouflageReplacer/releases/download/1.2.2/ConsumableCamouflageReplacer-1.2.2.exe);
  Move the executable to the **res_unpack** directory and run it;
- Follow the program\'s instructions;
- If the **camouflages.xml** was available and you\'ve done it right, you will be able to see a
  **camouflages_modified.xml** in the **res_unpack** directory after the program exits;

### Replace the game\'s camouflages.xml

- In WoWs\'s installation directory, find a directory named **bin**; In the folders named after a number in the **bin**
  folder, find the one **with the largest number** and open it;
- Go to the **res_mods** folder (or create one manually if you don't have one), move the **camouflages_modified.xml**
  the program just created to that folder, and rename it **camouflages.xml**.
- Run the game and check if the replacement is valid (the program will replace the first three consumable camouflages).
