---
id: mali-ft-adventure-01.01.01.02.10.09
name: 探险之路-遗迹星球-章节1-关卡1-1-1-游戏界面-游戏区-p代码-键盘-错误顺序-换行-速度
priority: 高
sequence: 
version: v1.0
executing-mode: 人工+自动
executer:  
---

{% include "/header.md" %}

### 测试范围
    探险模块（ADVENTURE） 游戏界面
### 前置条件
   1. 加载编程界面
   2. 英雄预设为使用Python语言
   3. 清除cookie，使用匿名用户身份游戏
### 输入
   self.moveRight()
   self.moveLeft()
### 预期输出
1. enter有效，文本于两行输入
2. 步骤5之后，英雄在战斗界面按照技能行进，但未到达终点
3. 在时间用尽后，英雄停留在最后走到的位置
4. 右侧编辑栏没有出现”完成“按钮
5. 任务栏下滑，避开火焰”陷阱“变为高亮橘色，其他两个任务仍为蓝色，表示未完成
6. 步骤8后，速度图标由蓝色变为黄色高亮色，英雄以之前两倍的速度行进，但未到达终点。

### 测试步骤

1. 全选编辑框内容，删除
2. 鼠标点击编辑框第一行，让光标focus到编辑框首行
3. 输入文本“self.moveRight()"
4. Enter换行，输入文本“self.moveLeft()”
5. 点击“开始运行”
6. 获取“任务栏”截图，观察
7. 观察编辑器界面，观察是否出现“完成”按钮
8. 鼠标放置到“速度”图标，观察2秒，点击
9. 点击“开始运行”
