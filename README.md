# 消耗型涂装替换器

**中文** | [English](README_en.md)

## 如何使用？

### 从游戏导出 camouflages.xml

- 下载并安装
  [WOWS Unpack Tool](https://forum.worldofwarships.eu/topic/113847-all-wows-unpack-tool-unpack-game-client-resources/)；
- 打开 WOWS Unpack Tool，点击“Load Content”，展开 res 文件夹，双击 camouflages.xml，点击 Unpack；
- 在 WOWS Unpack Tool 运行文件夹（一般是战舰世界游戏安装文件夹）下，进入 res_unpack 文件夹，若前两步操作无误，应能看到
  camouflages.xml 文件；

### 使用本软件修改 camouflages.xml

- 在本项目的 Release 中下载 [consumable_camouflage_replacer.exe
  ](https://github.com/MikhailTapio/ConsumableCamouflageReplacer/releases/download/1.0.0/consumable_camouflage_replacer.exe)
  ，将该执行文件移动到 res_unpack 文件夹下并运行；
- 按照程序指示操作；
- 若 camouflages.xml 可用且您的操作无误，程序退出后，res_unpack 文件夹中应能看到 camouflages_modified.xml 文件；

### 替换游戏中的 camouflages.xml

- 进入战舰世界游戏安装文件夹下的 bin ，在 bin 文件夹下以数字命名的文件夹中找到数字最大的那一个并进入；
- 进入 res_mods 文件夹（若没有该文件夹则手动创建一个），将刚刚的 camouflages_modified.xml 移动到该文件夹，并改名为
  camouflages.xml；
- 进入游戏，检查涂装替换效果（程序会替换前三个消耗型涂装）。