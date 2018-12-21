# -*- coding: utf-8 -*-
import random
import numpy
import random
import os
import time

def Draw():#绘制#绘制函数
	os.system('cls')#清屏
	for a in range(rows_num + 1):#纵坐标
		for b in range(cols_num + 1):#横坐标
			if map[a][b] == 0:#若此点为路
				print('  ', end = '')#绘制俩空格
			elif map[a][b] == 1:#若此点为墙
				print('█', end = '')#绘制墙
		print()#换行
	return#返回
cols_num = int(input('列数：'))#从输入获得列数
rows_num = int(input('行数：'))#从输入获得行数
if_draw = input('是否展示绘制过程？这可能会花费大量时间(y/n)')#从输入决定是否展示绘制过程
run_time_start = time.process_time()#开始运行计时
time_start = time.time()#开始计时
map = numpy.ones((rows_num + 1, cols_num + 1), int)#用于存储地图的二维数组map#[行][列]
wall = []#用于存储待处理的墙的数组wall
queue = []#wall[index]四周的方块列表
#0 - - 路
#1 - - 墙
map[1][0] = 0#入口
wall.append([1, 1])#手动设置入口四周的方块
wall.append([2, 0])#手动设置入口四周的方块
wall.append([0, 0])#手动设置入口四周的方块
while len(wall) != 0:#当待处理的墙数目不为0时
	index = random.randint(0, int(len(wall)) - 1)#从wall数组中随机选择一块wall[index]
	if map[wall[index][0] - 1][wall[index][1]] == 0:#当wall[index]上面的方块为路时
	  queue.append([wall[index][0] - 1, wall[index][1], 'up'])#置于queue中
	if map[wall[index][0] + 1][wall[index][1]] == 0:#当wall[index]下面的方块为路时
		queue.append([wall[index][0] + 1, wall[index][1], 'down'])#置于queue中
	if map[wall[index][0]][wall[index][1] + 1] == 0:#当wall[index]右面的方块为路时
		queue.append([wall[index][0], wall[index][1] + 1, 'right'])#置于queue中
	if map[wall[index][0]][wall[index][1] - 1] == 0:#当wall[index]左面的方块为路时
		queue.append([wall[index][0], wall[index][1] - 1, 'left'])#置于queue中
	example = random.choice(queue)#在wall[index]的四面中随机选择一块example
	if example[2] == 'left':#若example在wall[index]左侧
		if map[wall[index][0]][wall[index][1] + 1] == 1:#判断相对于wall[index]，在example的对侧，也就是在wall[index]的右侧的方块C是否为墙
			map[wall[index][0]][wall[index][1]] = 0#将wall[index]置为路
			map[wall[index][0]][wall[index][1] + 1] = 0#将C置为路
			y_C = wall[index][0]#记录C的纵坐标
			x_C = wall[index][1] + 1#记录C的横坐标
			if if_draw == 'y':#若用户需要展示绘制过程
				Draw()#绘制
	elif example[2] == 'right':#若example在wall[index]右侧
		if map[wall[index][0]][wall[index][1] - 1] == 1:#判断相对于wall[index]，在example的对侧，也就是在wall[index]的左侧的方块C是否为墙
			map[wall[index][0]][wall[index][1]] = 0#将wall[index]置为路
			map[wall[index][0]][wall[index][1] - 1] = 0#将C置为路
			y_C = wall[index][0]#记录C的纵坐标
			x_C = wall[index][1] - 1#记录C的横坐标
			if if_draw == 'y':#若用户需要展示绘制过程
				Draw()#绘制
	elif example[2] == 'down':#若example在wall[index]下方
		if map[wall[index][0] - 1][wall[index][1]] == 1:#判断相对于wall[index]，在example的对侧，也就是在wall[index]的上侧的方块C是否为墙
			map[wall[index][0]][wall[index][1]] = 0#将wall[index]置为路
			map[wall[index][0] - 1][wall[index][1]] = 0#将C置为路
			y_C = wall[index][0] - 1#记录C的纵坐标
			x_C = wall[index][1]#记录C的横坐标
			if if_draw == 'y':#若用户需要展示绘制过程
				Draw()#绘制
	elif example[2] == 'up':#若example在wall[index]上方
		if map[wall[index][0] + 1][wall[index][1]] == 1:#判断相对于wall[index]，在example的对侧，也就是在wall[index]的下侧的方块C是否为墙
			map[wall[index][0]][wall[index][1]] = 0#将wall[index]置为路
			map[wall[index][0] + 1][wall[index][1]] = 0#将C置为路
			y_C = wall[index][0] + 1#记录C的纵坐标
			x_C = wall[index][1]#记录C的横坐标
			if if_draw == 'y':#若用户需要展示绘制过程
				Draw()#绘制
	if  x_C > 0 and x_C + 1 < cols_num and y_C > 0 and y_C + 1 < rows_num:#筛掉越界的坐标
		if map[y_C - 1][x_C] == 1:#当C上面的方块为墙时
			wall.append([y_C - 1, x_C])#置于wall中
		if map[y_C + 1][x_C] == 1:#当C下面的方块为墙时
			wall.append([y_C + 1, x_C])#置于wall中
		if map[y_C][x_C - 1] == 1:#当C左面的方块为墙时
			wall.append([y_C, x_C - 1])#置于wall中
		if map[y_C][x_C + 1] == 1:#当C右面的方块为墙时
			wall.append([y_C, x_C + 1])#置于wall中
	temp_index = wall[index]#记录要删除的坐标
	wall = list(set(tuple(x) for x in wall))#去重
	#直接使用set的话，报错unhashable type: ‘list’
	#由于list的子元素也都是list，在内存中存储的是首元素地址，是可变的元素，无法直接使用set
	#先将内部元素转化为tuple，然后再使用set，tuple是不可变对象
	try:#在删除不存在的坐标是不报错
		wall.remove(temp_index)#将wall[index]从wall中删除
	except :#错误解决方案
	    pass#直接跳过
	queue = []#重置wall[index]四周的方块列表
end_point = []#可行的终点列表
for x in range(rows_num + 1):#遍历每一列
    for y in range(cols_num + 1):#遍历每一行
        if y == cols_num - 1 and map[x][y - 1] == 0 and map[x][y] == 0:#取一个在最后一列且它和它左边的方块都为路的坐标
            end_point.append([x, y + 1])#将他列入可行的终点列表中
        if x == 0 or x == rows_num or y == 0 or y == cols_num:#如果此坐标为边界
            map[x][y] = 1#置为墙
map[random.choice(end_point)[0]][random.choice(end_point)[1]] = 0#从可行的终点列表中随机选一个坐标置为终点
map[1][0] = 0#把起点置为路
create_time_end = time.process_time()
Draw()#绘制
run_time_end = time.process_time()#运行计时结束
time_end = time.time()#计时结束
if if_draw == 'y':#若展示绘制过程
    print('生成并绘制', cols_num, '*', rows_num, '的迷宫共用时', time_end - time_start, 's，其中CPU运行时间', run_time_end - run_time_start, 's')#输出程序运行时间和CPU运行时间
else:#若不展示绘制过程
	print('生成并绘制', cols_num, '*', rows_num, '的迷宫共用时', time_end - time_start, 's，其中其中生成时间', create_time_end - run_time_start, 's', 'CPU运行时间', run_time_end - run_time_start, 's')#输出程序运行时间和CPU运行时间
print('绘制程序运行完毕 正在退出…')#地图绘制部分全部完成
if_solve = input('是否运行寻路程序？(y/n)')#从输入确认是否解决此迷宫
if if_solve == 'n':#如果需要
    os._exit()#运行寻路程序
def ReturnMap():#返回map
	return map#不知道为啥import不能引用到map，所以写一个方法返回过去
