---
id: mali-ft-adventure-01.01.01.02.10.07
name: 探险之路-遗迹星球-章节1-关卡1-1-1-游戏界面-游戏区-p代码-键盘-错误技能代码
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
   1. 英雄装备鞋子，加载编程界面
   2. 英雄预设为使用Python语言
   3. 清除cookie，使用匿名用户身份游戏
### 输入
   无
### 预期输出
1. 编辑框可以自动提示并补全，编辑框内容：“  self.moveLeft()
                                        self.moveUp()
                                        self.moveXY(x, y)”
2. 英雄在战斗界面按照技能行走，但不能走到终点
3. 观察编辑框，调试指针停留在第二行“self.moveUp()”
4. 编辑栏没有出现“完成”按钮
5. 任务栏下滑，只有“避开火焰陷阱”变为高亮橘色

### 测试步骤

1. 鼠标全选文本框，删除所有内容
2. 依次输入    “ self.ml"+Enter
                self.mu"+Enter
                self.mx”+Enter，观察编辑框
3. 点击“开始运行”，观察
4. 获取“任务栏”截图，观察
5. 观察编辑器界面，观察是否出现“完成”按钮

