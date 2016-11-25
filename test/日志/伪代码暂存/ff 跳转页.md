--------
id: mali-ft-register-001
name: 
priority: 高
sequence: 
version: v1.0
author: 
date: 
--------
### 测试范围
    注册模块（REGISTER） 跳转页

### 前置条件
     加载至注册页界面
### 输入

### 预期输出

### 测试步骤




### 伪代码

# module: 注册模块(REGISTER)

## 用例集（describe）: 注册页跳转到（register page goes to page of）
### 用例（it）: （点击注册号后）after click register
1. 输入正确的邮件，密码，昵称
2. 勾选接受协议 
3. 点击注册 
* expect 回到index页面
* expect session的email/昵称跟输入的一样  

### 用例（it）: （点击已有账号后）logIn
1. 点击已有账号
* expect 跳转到登录界面 