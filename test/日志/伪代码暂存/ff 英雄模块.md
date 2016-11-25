--------
id: mali-ft-hero-001
name: 
priority: 高
sequence: 
version: v1.0
author: 
date: 
--------
### 测试范围
    module 英雄模块（HERO）加载英雄界面

### 前置条件
  加载英雄界面
### 输入

### 预期输出

### 测试步骤




### 伪代码
# module 英雄模块（HERO）

```
### (可集成)
## 用例集（describe）: 首页英雄图标（hero of index page）
### 用例（it）: 点击后可以进入（could be clicked）
1. 点击英雄按钮
* 断言（expect） 跳出hero界面
```
***
```
### (可集成)
## 用例集（describe）: 英雄界面（hero page）
### 用例（it）: 可用箭头翻看英雄（could use arrow）
1. 获取当前英雄头像区域图像
2. 点击右箭头
3. 获取当前英雄头像区域图像
* 断言（expect） 英雄头像区域图像变化
4. 点击左箭头
5. 获取当前英雄头像区域图像
* 断言（expect） 图像跟1.图像相同
```

### 用例（it）: 可选不同角色（could choose dif roles）
1. 点击英雄头像
* 断言（expect） 出现不同人物

***
## 用例集（describe）: 选择英雄后（after choose hero）
before each：加载英雄界面
### 用例（it）: 英雄可用（，hero could be used）
1. 点击出战
* 断言（expect） 回到index页面

```
### (可集成)
### 用例（it）: 页面可被关闭（page could be closed）
1. 点击关闭按钮
* 断言（expect） 回到index页面 