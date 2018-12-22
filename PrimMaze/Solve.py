# -*- coding: utf-8 -*-
import random
import numpy
import random
import os
import time
import PrimMaze

rows_num = PrimMaze.rows_num#获取行数
cols_num = PrimMaze.cols_num#获取列数
end_point = [PrimMaze.ReturnMap()[1], PrimMaze.ReturnMap()[2]]#获取终点坐标
if_show = input('是否绘制寻路过程？(无法计时)(y/n)')#从输入决定是否展示寻路过程
if if_show == 'y':#如果要绘制寻路过程
	sleep_time = 1.01 - float(input('请设置寻路速度(0.1 - 1)'))#设置寻路速度
run_time_start = time.process_time()#开始运行计时
time_start = time.time()#开始计时
position = [1,0]#将坐标设置在起点
map = PrimMaze.ReturnMap()[0]#获取地图
way = []#未探索的路 -- 0
explored = []#已探索的路 -- 2
for x in range(rows_num + 1):#遍历每一列
    for y in range(cols_num + 1):#遍历每一行
        if map[x][y] == 0:#如果此点为路
            way.append([x,y])#将其置入未探索的路列表
while len(way) != 0:#当还有未探索的路时
	map[position[0]][position[1]] = 2#将当前坐标设为已探索
	explored.append([position[0],position[1]])#置入已探索的路列表
	if position == end_point:#如果当前坐标在终点
		PrimMaze.Draw()#绘制
		print('已完成寻路')#完成
		run_time_end = time.process_time()#运行计时结束
		time_end = time.time()#计时结束
		if if_show != 'y':
			print('寻路共用时', time_end - time_start, 's，其中CPU运行时间', run_time_end - run_time_start, 's')#输出程序运行时间和CPU运行时间
		break#跳出循环
	if map[position[0] + 1][position[1]] == 0:#如果当前坐标下方是路
		position[0] += 1#向下移动
	elif map[position[0] - 1][position[1]] == 0:#如果当前坐标上方是路
		position[0] -= 1#向上移动
	elif map[position[0]][position[1] + 1] == 0:#如果当前坐标右边是路
		position[1] += 1#向右移动
	elif map[position[0]][position[1] - 1] == 0:#如果当前坐标左边是路
		position[1] -= 1#向左移动
	else:#如果都不是，即四边都探索过
		map[position[0]][position[1]] = 3#将此点设为死路
		del explored[-1]#从已探索列表中移除
		position = explored.pop()#回溯一格并从已探索列表中移除
	if if_show == 'y':#如果要绘制
		PrimMaze.Draw()#绘制
		time.sleep(sleep_time)#休眠
input('按任意键退出…')

