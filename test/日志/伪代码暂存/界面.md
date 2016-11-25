--------
id: mali-ft-adventure-001
name: 
priority: 高
sequence: 
version: v1.0
author: 
date: 
--------
### 测试范围
    module 探险模块（ADVENTURE） 关卡界面

### 前置条件
  加载关卡界面
### 输入

### 预期输出

### 测试步骤




### 伪代码

# module 探险模块（ADVENTURE）

## 用例集（describe）： 回合页面（level page game）
* before each加载回合页面
### 用例（it）： 点击重新战斗能进入装备页面（click refight could go to equip page）
1. 如果没有“重新战斗”按钮
* 断言（expect）断言：返回“noRebattle”/返回false.ToBe（false），表示断言过关且重新战斗不存在
2. else 点击重新战斗按钮
* 断言（expect）断言： 跳转到装备界面
### 用例（it）:点击战斗能进入装备页面（ click fight could go to equip page）
1. 点击回合1-1/2/3...的战斗按钮
* 断言（expect）断言： 跳转到装备页面
### 用例（it）: 点击锁定回合，不能产生变化（could not make any change）
* 断言（expect）断言： 有指定元素，能标示为该页面
1. 点击回合1-1/2/3...（锁定回合）
* 断言（expect）断言： 仍是当前url
* 断言（expect）断言： 有指定元素，能标示为该页面