# Source Generated with Decompyle++
# File: XCM.pyc (Python 3.6)

import pygame
import random
import copy
import sys
import json
import os
import tkinter as tk
import threading
import time
import math

def 归位(jiantou, yj):
    for l in range(2):
        z = l + 2
        if jiantou[z] > 0:
            jiantou[z] -= yj
        elif jiantou[z] < 0:
            jiantou[z] += yj
        x = jiantou[l] - jiantou[l + 4]
        t = jiantou[z] / yj
        if x < 0 or x < (-jiantou[z] / 2) * t:
            jiantou[z] += yj * 2
        elif x > 0 and x > (jiantou[z] / 2) * t:
            jiantou[z] -= yj * 2
        if jdz(jiantou[l] + jiantou[z] - jiantou[l]) < jdz(jiantou[l] - jiantou[l + 4]):
            jiantou[l] += jiantou[z]
            continue
        jiantou[l] = c(jiantou[l + 4])
    


def 随位置(wz, l):
    if 怪[l]['上一位置'] in wz:
        for lzx in range(len(wz)):
            if wz[lzx] == 怪[l]['上一位置']:
                del wz[lzx]
                break
    return c(wz[随(0, len(wz) - 1)])


def 你的cd(name):
    if name == '熊大':
        cd = 1500
    if name == '毛毛':
        cd = 500
    if name == '萝卜头':
        cd = 1000
    if name == '涂涂':
        cd = 1500
    if name == '蹦蹦':
        cd = 1900
    if name == '吉吉国王':
        cd = 500
    if name == '熊二':
        cd = 1500
    if name == '肥波':
        cd = 800
    jy = 第几夜 - 1
    jian = cd // 10
    return 随(cd - jy * jian, cd - jy * jian)


def 旋转(图片, zuobiao, dushu):
    dushu = -dushu
    center = 图片.get_rect().center
    temp = pygame.transform.rotate(图片, dushu)
    new = temp.get_rect(center, **('center',))
    return [
        temp,
        [
            zuobiao[0] + new[0],
            zuobiao[1] + new[1]]]


def 读取(weizhi):
    cd = open(weizhi, 'r')
    lzx = cd.read()
    cd.close()
    
    try:
        return json.loads(lzx)
    except:
        return ''
        return None



def 保存(weizhi, dongxi):
    
    try:
        cd = open(weizhi, 'w')
        cd.write(json.dumps(dongxi))
        cd.close()
    except:
        pass



def 播BGM(weizhi):
    pygame.mixer.music.load(weizhi)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)


def 加载音(weizhi):
    
    try:
        return pygame.mixer.Sound(weizhi)
    except:
        pass
    



def 变图(lzx, 横, 竖):
    
    try:
        return pygame.transform.scale(lzx, (横, 竖)).convert_alpha()
    except:
        pass
    



def 加载原图(地址):
    
    try:
        return pygame.image.load(地址)
    except:
        pass
    



def 加载图(地址, 横, 竖):
    
    try:
        return pygame.transform.scale(pygame.image.load(地址), (横, 竖)).convert_alpha()
    except:
        pass
    



def 抖(fudu):
    return 随(-fudu, fudu) * bi * 10


def 渐亮():
    global 渐
    if 渐 > 0:
        黑.set_alpha(渐)
        显示(黑, [
            0,
            0])
        渐 -= 10


def 关游戏():
    global 关
    关 = 1
    sys.exit()


def c(cs):
    return copy.deepcopy(cs)


def 随(小, 大):
    return random.randint(小, 大)


def jdz(shu):
    return abs(shu)


def 剪裁显示(图片, 坐标, jc):
    screen.blit(图片, (坐标[0], 坐标[1]), jc)


def 显示(图片, 坐标):
    screen.blit(图片, (坐标[0], 坐标[1]))


def 显小字(zi, zuobiao, se):
    zii = 小font.render(zi, True, se)
    screen.blit(zii, (zuobiao[0], zuobiao[1]))


def 显字(zi, zuobiao, se):
    zii = font.render(zi, True, se)
    screen.blit(zii, (zuobiao[0], zuobiao[1]))


def 走流程():
    渐亮()
    fpss.tick_busy_loop(fps)
    pygame.display.update()


def 播音(name):
    音效[name].play()


def 渐黑():
    global 渐, 渐
    渐 = 0
    while None:
        渐 += 20
        if 渐 >= 250:
            break
        return None


def 麻花():
    for yy in range(10):
        for xx in range(17):
            jianx = 随(0, 总高 - 比)
            jiany = 随(0, 总高 - 比)
            screen.blit(麻花图, (xx * 比, yy * 比), (jianx, jiany, 比, 比))
        
    


def 真麻花():
    for yy in range(10):
        for xx in range(17):
            jianx = 随(0, 总高 - 比)
            jiany = 随(0, 总高 - 比)
            screen.blit(真麻花图, (xx * 比, yy * 比), (jianx, jiany, 比, 比))
        
    


def 数加密(shu):
    return shu ** 2 - 2413


def 数解密(shu):
    return int((shu + 2413) ** 0.5)


def 选项y坐标(l):
    return 总高 // 2 + l * 比

root = tk.Tk()
总宽 = root.winfo_screenwidth()
总高 = root.winfo_screenheight()
root.destroy()
比 = 总高 // 9
监控比 = 比 + 比 // 5
行距 = 比 * 2 // 3
bi = 比 / 810
黑色 = (50, 50, 50)
白色 = (250, 250, 250)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((总宽, 总高), pygame.FULLSCREEN)
版本 = 'v1.3.0'
pygame.display.set_caption('熊出没的五夜后宫' + 版本)
pygame.mixer.set_num_channels(100)
fps = 120
fpss = pygame.time.Clock()

try:
    ziti = 'SimHei'
    font = pygame.font.SysFont(ziti, 行距)
    小font = pygame.font.SysFont(ziti, 行距 // 2)
except:
    ziti = 'SimSun'
    font = pygame.font.SysFont(ziti, 行距)
    小font = pygame.font.SysFont(ziti, 行距 // 2)

监控位置 = [
    [
        '山洞',
        '树洞',
        ''],
    [
        '森林',
        '树洞外',
        ''],
    [
        '',
        '院子',
        '仓库'],
    [
        '厕所',
        '你',
        '卧室']]
音效名 = [
    '切换监控',
    '第六夜电话',
    '第一夜电话',
    '第二夜电话',
    '第三夜电话',
    '第四夜电话',
    '第五夜电话',
    '关门',
    '毁坏',
    '开关监控',
    '锤子',
    '喵',
    '翻动',
    '通关',
    '跳杀',
    '完工',
    '撞门',
    '看见',
    '强光',
    '猴叫',
    '吸引',
    '熊二']
音效 = { }
for l in 音效名:
    音效[l] = 加载音('音效/' + l + '.wav')

背景图名 = [
    '大门：有门',
    '大门：没门',
    '大门',
    '后背']
监控图名 = [
    '树洞',
    '卧室',
    '厕所',
    '院子',
    '树洞外',
    '森林',
    '山洞',
    '仓库']
背景图集 = { }
for l in 背景图名:
    背景图集[l] = 加载图('图片/' + l + '.png', 总宽 + 总宽 // 2, 总高 + 比 * 2)

for l in 监控图名:
    背景图集[l] = 加载图('图片/' + l + '.png', 总宽, 总高 + 比 // 5)

背景图集['纸箱视角'] = 加载图('图片/纸箱视角.png', 总宽, 总高 * 2 + 比 // 5)
背景图集['窗户'] = 加载图('图片/窗户.png', 比 * 6, 比 * 4)
道具 = [
    '监控面板',
    '手电筒',
    '纸箱',
    '香蕉',
    '锤子']
动物 = [
    '熊大',
    '熊二',
    '肥波',
    '吉吉国王',
    '毛毛',
    '发疯吉吉国王',
    '蹦蹦',
    '涂涂',
    '萝卜头']
图集 = { }
for l in 动物:
    图集[l] = 加载图('图片/' + l + '.png', 比 * 10, 比 * 10)

for l in 道具:
    图集[l] = 加载图('图片/' + l + '.png', 比 * 2, 比 * 2)

图集['吸引按键'] = 加载图('图片/吸引按键.png', 比, 比)
图集['选中吸引按键'] = 加载图('图片/选中吸引按键.png', 比, 比)
图集['监控位'] = 加载图('图片/监控位.png', 比, 比)
图集['选中监控位'] = 加载图('图片/选中监控位.png', 比, 比)
真麻花图 = 加载图('图片/麻花.png', 总高, 总高)
麻花图 = 加载图('图片/麻花.png', 总高, 总高)
麻花图.set_alpha(70)
主界面 = 加载图('图片/主界面.png', 总宽, 总高 + 比 // 5)
黑 = 加载图('图片/黑.png', 总宽, 总高)
黑背景 = 加载图('图片/黑.png', 总宽, 总高)
第几夜 = 读取('存档/数据.json')
if 第几夜 == '':
    保存('存档/数据.json', 数加密(1))
    第几夜 = 1
else:
    第几夜 = 数解密(第几夜)
渐 = 250
shijian = 0
while None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            关游戏()
    显字('警告：', [
        总宽 // 2 - 比,
        总高 // 2 - 比 - 比 // 2], 白色)
    显字('患心脏病者请勿游玩', [
        总宽 // 2 - 比 * 3,
        总高 // 2 - 比 // 2], 白色)
    走流程()
    shijian += 1
    if shijian == 300:
        break
    播BGM('音效/主界面.mp3')
    渐黑()
    while None:
        选项 = [
            '开始']
        if 第几夜 > 1:
            选项.append('继续:第' + str(第几夜) + '夜')
        选项.append('离开')
        上一选中 = -1
        关 = 0
        时间 = 0
        呼吸 = [
            0,
            0,
            0,
            0,
            0,
            0]
        while 关 == 0:
            shubiao = pygame.mouse.get_pos()
            选中 = -1
            if shubiao[0] > 比 and shubiao[0] < 比 * 3:
                for l in range(len(选项)):
                    if shubiao[1] > 选项y坐标(l) and shubiao[1] < 选项y坐标(l) + 行距:
                        选中 = l
                        break
            if 上一选中 != 选中:
                上一选中 = 选中
                播音('切换监控')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    关游戏()
                if event.type == pygame.MOUSEBUTTONUP and 选中 != -1:
                    播音('切换监控')
                    if 选项[选中][0] == '继':
                        关 = 3
                if 选项[选中] == '离开':
                    关游戏()
                if 选项[选中] == '开始':
                    关 = 1
                if 选项[选中] == '声明':
                    关 = 2
            时间 += 1
            sj = 时间 % 200
            if sj < 100:
                呼吸[5] = -比 // 10
            else:
                呼吸[5] = 比 // 10
            归位(呼吸, bi / 20)
            显示(主界面, (0, 呼吸[1] - 比 // 10))
            显字('熊出没的', [
                比 + 抖(1),
                比], 白色)
            显字('五夜后宫', [
                比 * 2 + 抖(1),
                比 * 2], 白色)
            显小字(版本, [
                0,
                总高 - 比 // 3], 白色)
            for l in range(len(选项)):
                if 选中 == l:
                    zi = '》'
                else:
                    zi = ''
                zi += 选项[l]
                显字(zi, [
                    比,
                    选项y坐标(l)], 白色)
            
            麻花()
            走流程()
        if 关 == 2:
            渐黑()
            shijian = 0
            while None:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        关游戏()
                麻花()
                显字('作者：一坨馬  一个sans-', [
                    (总宽 // 2 - 比 * 4) + 比 // 2,
                    总高 // 2 - 比], 白色)
                显字('一坨馬B站UID：102361671', [
                    总宽 // 2 - 比 * 4,
                    总高 // 2], 白色)
                显字('一个sans-B站UID：486774442', [
                    总宽 // 2 - 比 * 4,
                    总高 // 2 + 比], 白色)
                走流程()
                shijian += 1
                if shijian == 400:
                    break
                渐黑()
                continue
                if 关 == 1:
                    第几夜 = 1
        pygame.mixer.music.stop()
        while None:
            播音('强光')
            shijian = 0
            while None:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        关游戏()
                显字('12：00 AM', [
                    (总宽 // 2 - 比 * 2) + 比 // 2,
                    总高 // 2 - 比], 白色)
                显字('第' + str(第几夜) + '夜', [
                    总宽 // 2 - 比,
                    总高 // 2], 白色)
                麻花()
                走流程()
                shijian += 1
                if shijian == 150 + 第几夜 * 50:
                    break
                渐黑()
                音效['强光'].stop()
                播BGM('音效/BGM.mp3')
                视角 = '大门'
                监控视角 = '院子'
                有门 = True
                关门 = False
                关窗 = False
                开监控 = False
                关门上限 = 5
                时间 = 0
                挪动 = 0
                怪 = { }
                if 第几夜 > 3:
                    怪['萝卜头'] = { }
                    怪['萝卜头']['位置'] = '森林'
                    怪['萝卜头']['吸引'] = '森林'
            怪['肥波'] = { }
            怪['肥波']['位置'] = '院子'
            怪['熊大'] = { }
            怪['熊大']['位置'] = '树洞'
            怪['熊二'] = { }
            怪['熊二']['位置'] = '树洞'
            if 第几夜 > 1:
                怪['毛毛'] = { }
                怪['毛毛']['位置'] = '山洞'
                怪['毛毛']['香蕉'] = -1
                怪['毛毛']['\xe6\x8a\x96'] = 0
                怪['吉吉国王'] = { }
                怪['吉吉国王']['位置'] = '山洞'
                怪['吉吉国王']['忍'] = 8000
            if 第几夜 > 2:
                怪['涂涂'] = { }
                怪['涂涂']['位置'] = '森林'
            if 第几夜 > 4:
                怪['蹦蹦'] = { }
                怪['蹦蹦']['位置'] = '仓库'
            for l in 怪:
                怪[l]['挪动'] = 随(-总宽 // 3, 总宽 - 总宽 // 4)
                怪[l]['cd'] = 你的cd(l) + 2000
                怪[l]['上一位置'] = c(怪[l]['位置'])
            
            道具 = [
                '监控面板',
                '锤子',
                '纸箱']
            if 第几夜 == 1:
                播音('第一夜电话')
            if 第几夜 == 2:
                播音('第二夜电话')
            if 第几夜 == 3:
                播音('第三夜电话')
            if 第几夜 == 4:
                播音('第四夜电话')
            if 第几夜 == 5:
                播音('第五夜电话')
            if 第几夜 == 6:
                播音('第六夜电话')
            监控过渡 = 0
            开关监控 = [
                30,
                1]
            修门 = -1
            修窗 = -1
            躲纸箱 = [
                0,
                0]
            关 = 0
            呼吸 = [
                0,
                0,
                0,
                0,
                0,
                0]
            锤子抖 = 0
            吸引 = 0
            while 关 == 0:
                shubiao = pygame.mouse.get_pos()
                选中 = -1
                监控选中 = [
                    -1,
                    -1]
                if 开监控:
                    for y in range(len(监控位置)):
                        for x in range(len(监控位置[y])):
                            if 监控位置[y][x] != '' and 监控位置[y][x] != '你' and 监控位置[y][x] != 监控视角:
                                xx = 总宽 - 3 * 监控比
                                yy = 总高 - 4 * 监控比
                                if shubiao[1] >= 监控比 * y + yy + 比 // 4 and shubiao[1] <= 监控比 * y + yy + 比 - 比 // 4 and shubiao[0] >= 监控比 * x + xx and shubiao[0] <= 监控比 * x + xx + 比:
                                    监控选中 = [
                                        y,
                                        x]
                                    break
                            if 第几夜 > 3 and 吸引 == 0 and shubiao[1] > 总高 - 比 and shubiao[0] > 比 // 4 and shubiao[0] < 比 // 4 + 比:
                                监控选中 = [
                                    -2,
                                    -2]
                            elif 躲纸箱[1] == 0 and shubiao[1] > 总高 - 比:
                                for l in range(len(道具)):
                                    if shubiao[0] >= l * 比 * 2 and shubiao[0] <= (l + 1) * 比 * 2:
                                        选中 = l
                                        break
                if shubiao[0] > 总宽 - 比 * 2:
                    挪动 += 比 // 10
                    if 挪动 > 总宽 // 2:
                        挪动 = 总宽 // 2
                if shubiao[0] < 比 * 2:
                    挪动 -= 比 // 10
                    if 挪动 < 0:
                        挪动 = 0
                sb = pygame.mouse.get_pressed()
                if sb[0] and 躲纸箱[1] == 0 and '毛毛' in 怪 and 怪['毛毛']['位置'] == '你' and shubiao[0] + 挪动 > 比 * 4 and shubiao[0] + 挪动 < 比 * 8 and shubiao[1] < 比 * 5 and 怪['毛毛']['香蕉'] < 2000:
                    怪['毛毛']['香蕉'] += 1
                    怪['毛毛']['\xe6\x8a\x96'] = 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        关游戏()
                    if event.type == pygame.MOUSEBUTTONUP or event.button == 3:
                        if 开监控:
                            播音('开关监控')
                            开监控 = False
                            开关监控 = [
                                30,
                                -1]
                        elif 躲纸箱[1] == 1:
                            躲纸箱[1] = 0
                            播音('翻动')
                        else:
                            渐黑()
                            if 视角 == '大门':
                                视角 = '后背'
                            else:
                                视角 = '大门'
                        break
                        continue
                    if 躲纸箱[1] == 1:
                        躲纸箱[1] = 0
                        播音('翻动')
                        continue
                    if 监控选中 != [
                        -1,
                        -1]:
                        播音('切换监控')
                        if 监控选中 == [
                            -2,
                            -2]:
                            播音('吸引')
                            吸引 = 200
                            怪['萝卜头']['吸引'] = 监控视角
                        else:
                            监控视角 = 监控位置[c(监控选中[0])][c(监控选中[1])]
                            监控过渡 = 10
                        continue
                    if 选中 != -1:
                        if 道具[选中] == '监控面板':
                            播音('开关监控')
                            开监控 = True
                            开关监控 = [
                                0,
                                1]
                        if 道具[选中] == '纸箱':
                            播音('翻动')
                            躲纸箱[1] = 1
                        if 道具[选中] == '锤子' and 修门 == -1 and 修窗 == -1:
                            if 视角 == '后背':
                                修窗 = 0
                            else:
                                修门 = 0
                        elif 开监控 and 视角 == '大门' and (shubiao[0] - 总宽 // 2) + 挪动 > 总宽 // 3 and 躲纸箱[1] == 0 and 有门 and 关门上限 > 0 and 修门 == -1:
                            播音('关门')
                            if 关门:
                                关门 = False
                                关门上限 -= 1
                                if 关门上限 == 0:
                                    播音('毁坏')
                                else:
                                    关门 = True
                
                if 开监控 and 开关监控[0] == 30:
                    if 监控过渡 > 0:
                        监控过渡 -= 1
                        真麻花()
                    else:
                        显示(背景图集[监控视角], [
                            0,
                            0])
                        for l in 怪:
                            if (怪[l]['位置'] == 监控视角 or l == '吉吉国王') and 怪[l]['忍'] == 0:
                                显示(图集['发疯吉吉国王'], [
                                    怪[l]['挪动'] + 抖(5),
                                    比 * 2 + 抖(5)])
                            else:
                                lzx = 2
                                if l == '蹦蹦' and l == '肥波' or l == '毛毛':
                                    lzx = 3
                                显示(图集[l], [
                                    怪[l]['挪动'],
                                    比 * lzx])
                            if l == '毛毛' and 怪[l]['香蕉'] == 2000:
                                显示(图集['香蕉'], [
                                    怪[l]['挪动'] + 比 * 6 - 比 // 2,
                                    比 * 4 + 比 // 2])
                        麻花()
                    for y in range(len(监控位置)):
                        for x in range(len(监控位置[y])):
                            if 监控位置[y][x] != '':
                                xx = 总宽 - 3 * 监控比
                                yy = 总高 - 4 * 监控比
                                zi = '监控位'
                                if 监控位置[y][x] == 监控视角:
                                    zi = '选中监控位'
                            if 监控选中 != -1 and 监控选中[0] == y and 监控选中[1] == x:
                                zi = '选中监控位'
                            显示(图集[zi], [
                                监控比 * x + xx,
                                监控比 * y + yy])
                            显小字(监控位置[y][x], [
                                监控比 * x + (3 - len(监控位置[y][x])) * 行距 // 4 + xx,
                                监控比 * y + 比 // 3 + yy], 白色)
                        
                    
                    if 第几夜 > 3:
                        if 吸引 > 0:
                            pass
                        else:
                            zi = '吸引按键'
                            if 监控选中 == [
                                -2,
                                -2]:
                                zi = '选中吸引按键'
                            显示(图集[zi], [
                                比 // 4,
                                总高 - 比])
                    elif 监控过渡 > 0:
                        监控过渡 -= 1
                        真麻花()
                    elif 视角 == '大门':
                        if 有门:
                            tu = '大门：有门'
                            if 关门:
                                tu = '大门：没门'
                            else:
                                tu = '大门：没门'
                        else:
                            tu = 视角
                剪裁显示(背景图集[tu], [
                    0,
                    0], (挪动, 比 - 呼吸[1], 总宽, 总高))
                if 视角 == '大门':
                    if '毛毛' in 怪 and 怪['毛毛']['位置'] == '你':
                        dou = 0
                        if 怪['毛毛']['\xe6\x8a\x96'] > 0:
                            怪['毛毛']['\xe6\x8a\x96'] = 0
                            dou = 5
                        dx = 抖(dou)
                        dy = 抖(dou)
                        显示(图集['毛毛'], [
                            -挪动 + 比 + dx,
                            (-比 * 2 - 比 // 2) + 呼吸[1] + dy])
                        图集['香蕉'].set_alpha(int((怪['毛毛']['香蕉'] / 2000) * 255))
                        显示(图集['香蕉'], [
                            -挪动 + 比 * 6 + 比 // 2 + dx,
                            (-比 // 2 - 比 // 4) + 呼吸[1] + dy])
                    if 怪['熊二']['位置'] == '你':
                        显示(图集['熊二'], [
                            -挪动 + 总宽 - 比 * 3,
                            0 + 呼吸[1]])
                    zm = False
                    if 怪['熊大']['位置'] == '你' or 怪['熊大']['位置'] == '撞门':
                        dou = 0
                        if 怪['熊大']['位置'] == '撞门':
                            zm = True
                            dou = 10
                        显示(图集['熊大'], [
                            (-挪动 + 总宽 - 比 * 3) + 抖(dou),
                            0 + 呼吸[1] + 抖(dou)])
                    if '萝卜头' in 怪 and 怪['萝卜头']['位置'] == '你':
                        显示(图集['萝卜头'], [
                            -挪动 + 总宽 - 比 * 3,
                            比 * 3 + 呼吸[1]])
                    if '吉吉国王' in 怪:
                        if 怪['吉吉国王']['位置'] == '你' or 怪['吉吉国王']['位置'] == '撞门':
                            显示(图集['发疯吉吉国王'], [
                                (-挪动 + 总宽 - 比 * 3) + 抖(5),
                                0 + 呼吸[1] + 抖(5)])
                    if '吉吉国王' in 怪 and 怪['吉吉国王']['位置'] == '撞门' and 怪['吉吉国王']['cd'] > 100:
                        zm = True
                    if 关门:
                        dou = 0
                        if zm:
                            dou = 5
                        剪裁显示(背景图集['大门'], [
                            0,
                            0], (挪动 + 抖(dou), (比 - 呼吸[1]) + 抖(dou), 总宽, 总高))
                    if 修门 != -1:
                        xm = 修门 % 100
                        if xm < 50:
                            a = 0.04
                            dushu = 50 - int(xm * xm * a / 2)
                        else:
                            a = 0.04
                            xm -= 50
                            dushu = int(xm * xm * a / 2)
                        a = 旋转(变图(图集['锤子'], 比 * 4, 比 * 4), [
                            (-挪动 + 总宽 - 比 * 5) + 抖(锤子抖),
                            比 * 2 + 呼吸[1] + 抖(锤子抖)], dushu * 2)
                        显示(a[0], a[1])
                    elif '蹦蹦' in 怪 and 怪['蹦蹦']['位置'] == '你':
                        显示(图集['蹦蹦'], [
                            -挪动 - 比 * 3,
                            比 * 2 + 比 // 2 + 呼吸[1]])
                if '涂涂' in 怪 and 怪['涂涂']['位置'] == '你':
                    显示(图集['涂涂'], [
                        (-挪动 + 总宽 - 比 * 5) + 比 // 3,
                        -比 * 3 + 比 // 2 + 呼吸[1]])
                if 关窗:
                    显示(背景图集['窗户'], [
                        (-挪动 + 总宽 - 比 * 3) + 比 // 3,
                        比 // 3 + 呼吸[1]])
                if 修窗 != -1:
                    xm = 修窗 % 100
                    if xm < 50:
                        a = 0.04
                        dushu = 50 - int(xm * xm * a / 2)
                    else:
                        a = 0.04
                        xm -= 50
                        dushu = int(xm * xm * a / 2)
                    a = 旋转(变图(图集['锤子'], 比 * 4, 比 * 4), [
                        (-挪动 + 总宽 - 比 * 5) + 抖(锤子抖),
                        比 + 呼吸[1] + 抖(锤子抖)], dushu * 2)
                    显示(a[0], a[1])
                if 躲纸箱[1] == 1:
                    躲纸箱[0] += 1
                    if 躲纸箱[0] > 30:
                        躲纸箱[0] = 30
                if 躲纸箱[0] > 0:
                    a = 总高 * 2 * 2 / 900
                    y = a * 躲纸箱[0] * 躲纸箱[0] / 2
                    显示(背景图集['纸箱视角'], [
                        0,
                        int(y) - 总高 * 2])
                if 躲纸箱[1] == 0:
                    躲纸箱[0] -= 1
                    if 躲纸箱[0] < 0:
                        躲纸箱[0] = 0
                    for l in range(len(道具)):
                        y = 0
                        if 选中 == l:
                            y = 比 // 2
                        if (修门 != -1 or 修窗 != -1) and 道具[l] == '锤子':
                            continue
                        显示(图集[道具[l]], [
                            l * 比 * 2,
                            总高 - 比 - y])
                    
                有 = False
                if 开关监控[1] == 1 and 开关监控[0] != 30:
                    开关监控[0] += 1
                    if 开关监控[0] == 30:
                        监控过渡 = 20
                    有 = True
                if 开关监控[1] == -1 and 开关监控[0] != 0:
                    开关监控[0] -= 1
                    有 = True
                if 有:
                    a = 总宽 * 2 / 900
                    jia = a * 开关监控[0] * 开关监控[0] / 2
                    显示(变图(图集['监控面板'], 比 * 2 + jia, 比 * 2 + jia), [
                        -比 // 3,
                        (总高 - 比 * 2 - jia) + jia // 5])
                if 时间 < 5000:
                    zi = '12 AM'
                else:
                    zi = str(时间 // 5000) + ' AM'
                显字(zi, [
                    总宽 - len(zi) * 比 // 3 - 比 // 5,
                    比 // 5], 白色)
                走流程()
                if 修窗 > -1:
                    修窗 += 1
                    if 修窗 % 100 == 0:
                        播音('锤子')
                        锤子抖 = 20
                    if 修窗 == 1000:
                        关窗 = True
                        修窗 = -1
                        播音('完工')
                if 修门 > -1:
                    修门 += 1
                    if 修门 % 100 == 0:
                        播音('锤子')
                        锤子抖 = 20
                    if 修门 == 2000:
                        播音('完工')
                        关门上限 = 5
                        修门 = -1
                if 锤子抖 > 0:
                    锤子抖 -= 1
                时间 += 1
                sj = 时间 % 200
                if sj < 100:
                    呼吸[5] = -比 // 10
                else:
                    呼吸[5] = 比 // 10
                归位(呼吸, bi / 20)
                if 吸引 > 0:
                    吸引 -= 1
                if 时间 == 30000:
                    关 = 2
                    break
                for l in 怪:
                    if l == '毛毛' and 怪[l]['香蕉'] > -1 and 怪[l]['香蕉'] != 2000:
                        continue
                    if l == '吉吉国王' and 怪[l]['忍'] > 0:
                        怪[l]['忍'] -= 1
                        if 怪[l]['忍'] == 0:
                            播音('猴叫')
                        怪[l]['cd'] = 1000
                    if 怪[l]['cd'] < 0:
                        怪[l]['cd'] = 1
                    if 怪[l]['cd'] > 0:
                        怪[l]['cd'] -= 1
                        if (怪[l]['cd'] == 0 or 开监控) and 监控视角 == 怪[l]['位置']:
                            监控过渡 = 10
                    怪[l]['挪动'] = 随(-总宽 // 2, 总宽 - 总宽 // 3)
                    怪[l]['cd'] = 你的cd(l)
                    上一位置 = c(怪[l]['位置'])
                    if l == '熊大':
                        if 怪[l]['位置'] == '树洞':
                            怪[l]['位置'] = '树洞外'
                        elif 怪[l]['位置'] == '树洞外':
                            怪[l]['位置'] = 随位置([
                                '树洞',
                                '森林',
                                '院子'], l)
                        elif 怪[l]['位置'] == '森林':
                            怪[l]['位置'] = '树洞外'
                        elif 怪[l]['位置'] == '院子':
                            怪[l]['位置'] = '你'
                        elif 怪[l]['位置'] == '你':
                            if not 关门:
                                怪[l]['位置'] = '死'
                            else:
                                怪[l]['位置'] = '撞门'
                                怪[l]['cd'] = 200
                                播音('撞门')
                        elif 怪[l]['位置'] == '撞门':
                            关门上限 -= 1
                            if 关门上限 == 0:
                                关门 = False
                                播音('毁坏')
                            if 关门:
                                怪[l]['位置'] = '树洞外'
                            else:
                                怪[l]['位置'] = '你'
                    if l == '萝卜头':
                        if 怪[l]['位置'] == 怪[l]['吸引']:
                            if 怪[l]['位置'] == '院子':
                                怪[l]['位置'] = '你'
                                怪[l]['吸引'] = '你'
                            elif 怪[l]['位置'] == '你' and 怪[l]['位置'] == '厕所' or 怪[l]['位置'] == '卧室':
                                if 关门:
                                    pass
                                else:
                                    怪[l]['位置'] = '死'
                            else:
                                怪[l]['位置'] = '院子'
                                怪[l]['吸引'] = '院子'
                        else:
                            怪[l]['位置'] = c(怪[l]['吸引'])
                    if l == '熊二':
                        if 怪[l]['位置'] == '树洞':
                            怪[l]['位置'] = '树洞外'
                        elif 怪[l]['位置'] == '树洞外':
                            怪[l]['位置'] = 随位置([
                                '树洞',
                                '森林',
                                '院子'], l)
                        elif 怪[l]['位置'] == '森林':
                            怪[l]['位置'] = '树洞外'
                        elif 怪[l]['位置'] == '院子':
                            怪[l]['位置'] = 随位置([
                                '树洞外',
                                '森林',
                                '你',
                                '厕所',
                                '卧室'], l)
                        elif 怪[l]['位置'] == '你':
                            if 关门 or 躲纸箱[1] == 1:
                                怪[l]['位置'] = '院子'
                            else:
                                怪[l]['位置'] = '死'
                        elif 怪[l]['位置'] == '厕所' or 怪[l]['位置'] == '卧室':
                            if 躲纸箱[1] == 0:
                                怪[l]['位置'] = '死'
                            else:
                                播音('熊二')
                                怪[l]['位置'] = '院子'
                    if l == '吉吉国王':
                        if 怪[l]['位置'] == '山洞':
                            怪[l]['位置'] = '森林'
                        elif 怪[l]['位置'] == '森林':
                            怪[l]['位置'] = '院子'
                        elif 怪[l]['位置'] == '院子':
                            怪[l]['位置'] = '你'
                        elif 怪[l]['位置'] == '你':
                            if not 关门:
                                怪[l]['位置'] = '死'
                            else:
                                怪[l]['位置'] = '撞门'
                                怪[l]['cd'] = 300
                                播音('撞门')
                        elif 怪[l]['位置'] == '撞门':
                            关门上限 -= 1
                            if 关门上限 == 0:
                                关门 = False
                                播音('毁坏')
                            怪[l]['位置'] = '你'
                    if l == '毛毛':
                        if 怪[l]['香蕉'] == -1:
                            if 怪[l]['位置'] == '山洞':
                                怪[l]['位置'] = '森林'
                            elif 怪[l]['位置'] == '森林':
                                怪[l]['位置'] = '院子'
                            elif 怪[l]['位置'] == '院子':
                                怪[l]['位置'] = '你'
                                怪[l]['香蕉'] = 0
                            else:
                                怪[l]['cd'] = 200
                                if 怪[l]['位置'] == '你':
                                    怪[l]['位置'] = '院子'
                                elif 怪[l]['位置'] == '院子':
                                    怪[l]['位置'] = '森林'
                                elif 怪[l]['位置'] == '森林':
                                    怪[l]['位置'] = '山洞'
                                    if 怪['吉吉国王']['忍'] > 0:
                                        怪['吉吉国王']['忍'] = 6000
                                        怪[l]['香蕉'] = -1
                    if l == '肥波':
                        if 怪[l]['位置'] == '院子':
                            怪[l]['位置'] = 随位置([
                                '厕所',
                                '卧室',
                                '仓库'], l)
                        elif 怪[l]['位置'] == '厕所':
                            怪[l]['位置'] = 随位置([
                                '卧室',
                                '你'], l)
                            if 怪[l]['位置'] == '你':
                                播音('喵')
                            elif 怪[l]['位置'] == '仓库':
                                怪[l]['位置'] = '院子'
                            elif 怪[l]['位置'] == '卧室':
                                怪[l]['位置'] = 随位置([
                                    '厕所',
                                    '你'], l)
                                if 怪[l]['位置'] == '你':
                                    播音('喵')
                                elif 怪[l]['位置'] == '你':
                                    怪[l]['位置'] = '死'
                                    播音('喵')
                    if l == '涂涂':
                        if 怪[l]['位置'] == '森林':
                            怪[l]['位置'] = 随位置([
                                '树洞外',
                                '院子'], l)
                        elif 怪[l]['位置'] == '树洞外':
                            怪[l]['位置'] = '院子'
                        elif 怪[l]['位置'] == '院子':
                            怪[l]['位置'] = '你'
                        elif 怪[l]['位置'] == '你':
                            if 关窗:
                                关窗 = False
                                播音('毁坏')
                                怪[l]['位置'] = '森林'
                            else:
                                怪[l]['位置'] = '死'
                    if l == '蹦蹦':
                        if 怪[l]['位置'] == '森林':
                            怪[l]['位置'] = 随位置([
                                '树洞外',
                                '院子'], l)
                        elif 怪[l]['位置'] == '树洞外' or 怪[l]['位置'] == '仓库':
                            怪[l]['位置'] = '院子'
                        elif 怪[l]['位置'] == '院子':
                            怪[l]['位置'] = 随位置([
                                '厕所',
                                '卧室',
                                '仓库'], l)
                        elif 怪[l]['位置'] == '厕所' or 怪[l]['位置'] == '卧室':
                            怪[l]['位置'] = '你'
                        elif 怪[l]['位置'] == '你':
                            if 视角 == '大门' or 开监控:
                                播音('翻动')
                                if 开监控 or len(道具) > 1:
                                    del 道具[1]
                                elif len(道具) > 0:
                                    del 道具[0]
                            怪[l]['位置'] = '森林'
                    怪[l]['上一位置'] = c(上一位置)
                    if 怪[l]['位置'] == '死':
                        if l == '肥波':
                            怪[l]['位置'] = '院子'
                            if 关门:
                                播音('关门')
                                if 关门:
                                    关门 = False
                                    关门上限 -= 1
                                    if 关门上限 == 0:
                                        播音('毁坏')
                                    else:
                                        关 = 1
                    if not 开监控:
                        if (怪[l]['位置'] == '你' or 上一位置 == '撞门') and l != '肥波' and l != '蹦蹦':
                            可 = True
                            if l == '毛毛':
                                可 = False
                            elif l == '涂涂' or 视角 == '大门':
                                可 = False
                            elif 视角 != '大门':
                                可 = False
                            elif 上一位置 == '撞门' or 上一位置 == '你':
                                可 = False
                            if 可:
                                播音('看见')
                    if 开监控 and 监控视角 == 怪[l]['位置']:
                        监控过渡 = 10
            if 关 == 1:
                for l in 怪:
                    if 怪[l]['位置'] == '死' and l != '肥波' or l == '吉吉国王':
                        l = '发疯吉吉国王'
                
                播音('跳杀')
                shijian = 0
                while None:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            关游戏()
                    jia = shijian * 总宽 // 70
                    显示(变图(图集[l], jia, jia), [
                        (总宽 // 2 - jia // 2) + 抖(10),
                        -jia + 总高 + 总高 // 2 + 抖(10)])
                    走流程()
                    shijian += 1
                    if shijian == 70:
                        break
                    音效['跳杀'].stop()
                    shijian = 0
                    while None:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                关游戏()
                        shijian += 1
                        走流程()
                        if shijian == 100:
                            break
                        渐黑()
                        播BGM('音效/主界面.mp3')
                        break
                        continue
                        渐黑()
                        pygame.mixer.music.stop()
                        播音('通关')
                        第几夜 += 1
                        保存('存档/数据.json', 数加密(第几夜))
                        shijian = 0
                        while None:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    关游戏()
                            shijian += 1
                            a = 总高 * 2 / 640000
                            sj = shijian
                            if sj > 800:
                                sj = 800
                            jia = a * sj * sj / 2
                            显字('      AM', [
                                (总宽 // 2 - 比 * 2) + 比 // 2,
                                总高 // 2], 白色)
                            显字('5：59', [
                                (总宽 // 2 - 比 * 2) + 比 // 2,
                                总高 // 2 - jia], 白色)
                            显字('6：00', [
                                (总宽 // 2 - 比 * 2) + 比 // 2,
                                总高 + 总高 // 2 - jia], 白色)
                            走流程()
                            if shijian == 1200:
                                break
                    return None
