---
id: mali-ft-hero-06
name: 英雄-选择python语言出战-已登录用户
priority: 高
sequence: 
version: v1.0
executing-mode: 人工
executer: 
---

{% include "/header.md" %}

### 测试范围
  英雄模块（HERO）英雄界面语言选择

### 前置条件
1. 用户已登录
2. 加载英雄界面

### 输入
1. Python

### 预期输出
1. 战斗场景编辑框内代码为Python代码 （如查找获得的代码区文本中是否有“self”字样）
2. 战斗场景编辑框右上角显示为Python

### 测试步骤
  1. 打开浏览器
  2. 导航到英雄界面，登录
  3. 选择Python语言，点击出战
  4. 进入游戏战斗关卡1-1-1界面，检查战斗场景，是否和预期一致
  5. 记录当前关卡，退出登录，关闭浏览器
  6. 打开浏览器，登录，导航到步骤4的关卡
  7. 检查战斗场景，是否和预期一致

### 伪代码
# module 英雄模块（HERO）

***

### 用例（it）: 可选不同角色（could choose dif roles）
1. 点击英雄头像
* 断言（expect） 出现不同人物

