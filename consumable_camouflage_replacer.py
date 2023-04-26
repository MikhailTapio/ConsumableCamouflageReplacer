# Consumable Camouflage replacer
# Copyright (C) 2023 MikhailTapio
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program. If not,
# see <https://www.gnu.org/licenses/>.

import xml.etree.ElementTree as Et
from typing import List

version = '1.2.0'

language = 0

tex_keys = ['Hull', 'DeckHouse', 'Gun', 'Director', 'Plane', 'Float', 'Misc', 'Bulge', 'Wire']

tex_locales = [
    ['船体', '甲板室', '火炮', '火控系统', '舰载飞机', '救生船', '杂项', '凸出部分', '金属网'],
    tex_keys
]

uv_all = {'DeckHouse': '1.5 1.5', 'Tile': '3 3', 'Gun': '0.8 0.8', 'Director': '0.5 0.5',
          'Plane': '0.5 0.5', 'Float': '0.5 0.5', 'Misc': '0.3 0.3', 'Wire': '0.5 0.5', 'Bulge': '1 1'}

tex_all = [
    ['content/gameplay/common/camouflage/textures/mat_Steel_01_a.dds', 'content/gameplay/common/camouflage/textures'
                                                                       '/mat_Steel_01_mgn.dds'],
    ['content/gameplay/common/camouflage/textures/mat_Rank_Bronze_a.dds', 'content/gameplay/common/camouflage'
                                                                          '/textures/mat_Rank_Bronze_mgn.dds'],
    ['content/gameplay/common/camouflage/textures/mat_Rank_Silver_a.dds', 'content/gameplay/common/camouflage'
                                                                          '/textures/mat_Rank_Silver_mgn.dds'],
    ['content/gameplay/common/camouflage/textures/mat_Rank_Gold_a.dds', 'content/gameplay/common/camouflage/textures'
                                                                        '/mat_Rank_Gold_mgn.dds'],
    ['content/gameplay/common/camouflage/textures/mat_Rank_Bronze_a.dds', 'content/gameplay/common/camouflage/textures'
                                                                          '/mat_Steel_01_mgn.dds'],
    ['content/gameplay/common/camouflage/textures/mat_Rank_Silver_a.dds', 'content/gameplay/common/camouflage/textures'
                                                                          '/mat_Steel_01_mgn.dds'],
    ['content/gameplay/common/camouflage/textures/mat_Rank_Gold_a.dds', 'content/gameplay/common/camouflage/textures'
                                                                        '/mat_Steel_01_mgn.dds']
]


def get_license() -> str:
    return '''
Consumable Camouflage replacer
Copyright (C) 2023 MikhailTapio
This program comes with ABSOLUTELY NO WARRANTY;
This is free software, and you are welcome to redistribute it
under certain conditions.
'''


def get_desc() -> str:
    return ('''
消耗型涂装替换器
作者：北斗余晖
版本：{}
源代码地址：https://github.com/MikhailTapio/ConsumableCamouflageReplacer
声明：
1. 本软件系作者出于兴趣爱好制作——仅供学习交流，不得用于商业用途，请于 24 小时内删除！
2. 本软件仅对特定 XML 文件作修改。
''' if language == 0 else '''
Consumable Camouflage Replacer
Author: MikhailTapio
Version: {}
Source: https://github.com/MikhailTapio/ConsumableCamouflageReplacer
Disclaimer:
1. The software was created by the author as a hobby - for learning and communication purposes only,
 not for commercial use, please delete within 24 hours!
2. The software only makes changes to specific XML files.
''').format(version)


def get_agree() -> str:
    return '''
如您知悉并同意以上声明，请将 camouflages.xml 放置到运行目录。
按回车键继续。
''' if language == 0 else '''
If you are aware of and agree to the above disclaimer,
 please place camouflages.xml in the run directory.
Press ENTER to go ahead.
'''


def get_tex() -> str:
    return '''
请输入数字以决定当前涂装应被修改为哪种涂装：
0. 不修改（仅在“全部修改模式”下可用）
1. 钢铁涂装
2. 排位铜涂装（原版）
3. 排位银涂装（原版）
4. 排位金涂装（原版）
5. 排位铜涂装（无纹路）
6. 排位银涂装（无纹路）
7. 排位金涂装（无纹路）
''' if language == 0 else '''
Please enter a number to determine which of the following camouflage
 you would like to change the current camouflage to:
0. Do not change (Only available in "ALL Mode")
1. Steel camouflage
2. Bronze camouflage (Normal)
3. Silver camouflage (Normal)
4. Golden camouflage (Normal)
5. Bronze camouflage (No Grain)
6. Silver camouflage (No Grain)
7. Golden camouflage (No Grain)
'''


def get_mode(s: int) -> str:
    return ('''
请选择 camo_{}_tile 的涂装修改模式：
0. 全部修改模式
1. 分部位修改模式
''' if language == 0 else '''
Please select a camouflage modification mode for camo_{}_tile:
0. ALL Mode
1. SUBPART Mode
''').format(s)


def get_change(c: int, part: int) -> str:
    if part == -1:
        return (
            'camo_{}_tile 修改为：' if language == 0 else "camo_{}_tile should be modified to be: ").format(c)
    else:
        return (
            'camo_{}_tile {} 部分修改为：' if language == 0 else "camo_{}_tile\'s {} part should be modified to be") \
            .format(c, tex_locales[language][part])


def get_completed() -> str:
    return "若无意外情况，新的涂装文件已生成为同目录下的 camouflages_modified.xml。" if language == 0 else '''
Barring unforeseen circumstances, the new camouflages file has been generated as
camouflages_modified.xml in the same directory.
    '''


def get_exit() -> str:
    return "按回车键退出……" if language == 0 else "Press ENTER to exit..."


def get_fnf() -> str:
    return "未找到 camouflages.xml 文件……" if language == 0 else "File camouflages.xml not found..."


def get_parse() -> str:
    return "camouflages.xml 分析失败！请检查你的文件……" if language == 0 else '''
Failed to parse camouflages.xml!
Please check your file...
'''


def init_uv(elem: Et.Element):
    for k, v in uv_all.items():
        n = Et.Element(k)
        n.text = v
        elem.append(n)


def init_mgn(elem: Et.Element, text: str):
    elem.text = text
    m = Et.Element('Influence_m')
    m.text = ' 1.0 '
    g = Et.Element('Influence_g')
    g.text = ' 1.0 '
    n = Et.Element('Influence_n')
    n.text = ' 0.0 '
    elem.append(m)
    elem.append(g)
    elem.append(n)


def init_textures(elem: Et.Element, modifications: List[int]):
    for z in range(0, 9):
        k = tex_keys[z]
        tex = tex_all[modifications[z]]
        r = Et.Element(k)
        r.text = tex[0]
        elem.append(r)
        mgn = Et.Element(k + '_mgn')
        init_mgn(mgn, tex[1])
        elem.append(mgn)


print(get_license())
try:
    language = int(input('''
请选择你的语言(Please select your language):
0. 中文
1. English
'''))
    if language != 0:
        language = 1
except ValueError:
    language = 1
print(get_desc())
input(get_agree())

try:
    tree = Et.parse('camouflages.xml')
except FileNotFoundError:
    print(get_fnf())
    input(get_exit())
    exit(0)
except Et.ParseError:
    print(get_parse())
    input(get_exit())
    exit(0)

root = tree.getroot()

for i in range(1, 4):
    modification = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    try:
        mode = int(input(get_mode(i)))
    except ValueError:
        mode = 0
    if mode == 0:
        print(get_tex())
        try:
            se = int(input(get_change(i, -1))) - 1
            modification = [se, se, se, se, se, se, se, se, se]
            if se == -1:
                modification = None
        except ValueError:
            modification = None
    else:
        for x in range(0, 9):
            print(get_tex())
            try:
                sp = int(input(get_change(i, x))) - 1
                if sp == -1:
                    print("分部位修改模式必须修改，默认改为钢铁涂装" if language == 0 else '''
Must change when in SUBPART mode, use Steel camouflage by default''')
                    sp = 0
            except ValueError:
                sp = 0
            modification[x] = sp
    if modification is not None:
        for camo in root.findall(".//camouflage[name='camo_{}_tile']".format(i)):
            camo.remove(camo.find('useColorScheme'))
            camo.remove(camo.find('colorSchemes'))
            camo.remove(camo.find('tiled'))
            camo.remove(camo.find('UV'))
            uv = Et.Element('UV')
            init_uv(uv)
            camo.append(uv)
            camo.remove(camo.find('Textures'))
            textures = Et.Element('Textures')
            init_textures(textures, modification)
            camo.append(textures)

tree.write(file_or_filename='camouflages_modified.xml')
print(get_completed())
input(get_exit())
