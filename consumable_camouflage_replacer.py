import xml.etree.ElementTree as Et

language = 0

tex_keys = ['Hull', 'DeckHouse', 'Gun', 'Director', 'Plane', 'Float', 'Misc', 'Bulge', 'Wire', 'Plane', 'Float']

uv_all = [
    {'DeckHouse': '0.5 0.5', 'Tile': '1 1', 'Gun': '0.5 0.5', 'Director': '0.5 0.5',
     'Plane': '0.5 0.5', 'Float': '0.5 0.5', 'Misc': '0.3 0.3', 'Wire': '0.5 0.5', 'Bulge': '1 1'},
    {'DeckHouse': '1.5 1.5', 'Tile': '3 3', 'Gun': '0.8 0.8', 'Director': '0.5 0.5',
     'Plane': '0.5 0.5', 'Float': '0.5 0.5', 'Misc': '0.3 0.3', 'Wire': '0.5 0.5', 'Bulge': '1 1'},
    {'DeckHouse': '1.5 1.5', 'Tile': '3 3', 'Gun': '0.8 0.8', 'Director': '0.5 0.5',
     'Plane': '0.5 0.5', 'Float': '0.5 0.5', 'Misc': '0.3 0.3', 'Wire': '0.5 0.5', 'Bulge': '1 1'},
    {'DeckHouse': '1.5 1.5', 'Tile': '3 3', 'Gun': '0.8 0.8', 'Director': '0.5 0.5',
     'Plane': '0.5 0.5', 'Float': '0.5 0.5', 'Misc': '0.3 0.3', 'Wire': '0.5 0.5', 'Bulge': '1 1'}
]

tex_all = [
    ['content/gameplay/common/camouflage/textures/mat_Steel_01_a.dds', 'content/gameplay/common/camouflage/textures'
                                                                       '/mat_Steel_01_mgn.dds'],
    ['content/gameplay/common/camouflage/textures/mat_Rank_Bronze_a.dds', 'content/gameplay/common/camouflage'
                                                                          '/textures/mat_Rank_Bronze_mgn.dds'],
    ['content/gameplay/common/camouflage/textures/mat_Rank_Silver_a.dds', 'content/gameplay/common/camouflage'
                                                                          '/textures/mat_Rank_Silver_mgn.dds'],
    ['content/gameplay/common/camouflage/textures/mat_Rank_Gold_a.dds', 'content/gameplay/common/camouflage/textures'
                                                                        '/mat_Rank_Gold_mgn.dds']
]


def get_desc() -> str:
    return '''
消耗型涂装替换器
作者：北斗余晖
声明：
1. 本软件系作者出于兴趣爱好制作——仅供学习交流，不得用于商业用途，请于 24 小时内删除！
2. 本软件仅对特定 XML 文件作修改。
''' if language == 0 else '''
Consumable Camouflage Replacer
Author: PloughRemnant
Disclaimer:
1. The software was created by the author as a hobby - for learning and communication purposes only,
 not for commercial use, please delete within 24 hours!
2. The software only makes changes to specific XML files.
'''


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
0. 不修改
1. 钢铁涂装
2. 排位铜涂装
3. 排位银涂装
4. 排位金涂装
''' if language == 0 else '''
Please enter a number to determine which of the following camouflage
 you would like to change the current camouflage to:
0. Do not change
1. Steel camouflage
2. Bronze camouflage
3. Silver camouflage
4. Golden camouflage
'''


def get_change(c: int) -> str:
    return ('camo_{}_tile 应被更改为：' if language == 0 else 'camo_{}_tile should be changed to: ').format(c)


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
    return "camouflages.xml 分析失败！请检查你的文件……" if language == 0 else "Failed to parse camouflages.xml! Please check your file..."


def init_uv(elem: Et.Element, typ: int):
    for k, v in uv_all[typ].items():
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


def init_textures(elem: Et.Element, typ: int):
    tex = tex_all[typ]
    for k in tex_keys:
        r = Et.Element(k)
        r.text = tex[0]
        elem.append(r)
        mgn = Et.Element(k + '_mgn')
        init_mgn(mgn, tex[1])
        elem.append(mgn)


try:
    language = int(input('''
请选择你的语言(Please select your language):
0. 中文
1. English
'''))
except ValueError:
    language = 0
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

print(get_tex())

for i in range(1, 4):
    se = 0
    try:
        se = int(input(get_change(i)))
    except ValueError:
        se = 0
    if se != 0:
        for camo in root.findall(".//camouflage[name='camo_{}_tile']".format(i)):
            camo.remove(camo.find('useColorScheme'))
            camo.remove(camo.find('colorSchemes'))
            # 更改属性
            camo.remove(camo.find('tiled'))
            camo.remove(camo.find('UV'))
            uv = Et.Element('UV')
            init_uv(uv, se - 1)
            camo.append(uv)
            camo.remove(camo.find('Textures'))
            textures = Et.Element('Textures')
            init_textures(textures, se - 1)
            camo.append(textures)

# 将修改后的XML文件写回磁盘
tree.write(file_or_filename='camouflages_modified.xml')
print(get_completed())
input(get_exit())
