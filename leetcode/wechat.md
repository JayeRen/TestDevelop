# 测试开发的日子

## 用protractor做一个模拟鼠标的端对端的测试开发
***
### **现在基本上整个流程是搞定了，就来啰嗦一下整体步骤。**
***
* 我现在的任务就是做e2e即端对端的自动化测试，需要模拟鼠标点击，
  所以利用到了之前学习的selenium-webdriver，api还算比较强大。
* jasmine 是一个特别人性化的框架，全是通俗易懂的语言，所以这个框架必须用，
  而且现在我在用它写用例，伪代码。
* 老大当时还预备着要一个报告，jasmine有，karma也有，而且karma还可以自动检测变化，但是karma是主做unit-test的，跟webdriver对接很难过，
  我找到一个集成版本的还是好几年前的，被老大嫌弃了，哼。
* 在我的不懈努力各种挖掘下，当然，少不了npm这个强大的库，终于找到一个为angularjs写的protractor！它集成了jasmine和webdriver，而且还是js的，
  我之前学的也是js，nodejs这些，这样就不用再耗费时间在java逻辑上啦~
* 这个语法搞定之后，也成功让它自动操作我的浏览器啦~然后第二天闲着的时候，就找report怎么写，找着找着，又在git里挖到了一个库，
  protractor-jasmine-reporter，哈哈哈！很棒吧~写的也很好看呢！这样子又省了不少事。
* 未解决：图像识别，截图。截图要用到java，很麻烦，我在js没找到这个接口，还要继续努力，哼。
* 这里还要重点表扬一下nodejs集成的库，npm，真的是功能强大应有尽有，每次需要什么功能的话，在上面一搜，如果有，只要npm install ***就可以了！再方便不过了。
* 还有一个ide，visual studio code，不知道什么时候起它变得这么包容强大，也是各种插件尽情装，我的项目们就是用它写啦~跟git合作起来也很方便，所以自然是它，就是它~
****
1. #git# 在本机为git配置我的用户名和密码 具体方法百度就有
2. #git# 在git上将我的远程密钥设置下来，这样以后clone代码就很方便了
3. #git# 将git上需要的项目文件夹copy下来 命令：git clone "(git上会自动复制你clone需要的地址)"
4. #git# 打开vs code，打开文件夹，选中刚刚clone的文件夹，那么整个文件夹都可以加载啦。
5. #npm# 打开终端，输入命令： npm init，然后一路enter下来，就会生成package.json这个方便我们配置用的文件。
6. #npm# 安装protractor，输入命令： npm install protractor -g(小尾巴可以使这个软件全局安装，这样才可以直接使用protractor **的命令)
7. #npm# 安装测试驱动及服务器：webdriver-manager update
8. 基本安装完毕，下面再打开一个终端，启动服务器： webdriver-manager start
9. 配置一下protractor的conf.js，把要测试的文件名写上。
10. 运行写好的用例：protractor conf.js一整个流程就是这样啦~非常好~哈哈 
11. 下面又新装了一个reporter：npm install protractor-jasmine2-html-reporter --save-dev（小尾巴是局部安装这个程序，并且自动保存在.json中的dev依赖说明里）
12. 同样，在conf.js里配置一下：

`注册reporter(具体传送门:https://www.npmjs.com/package/protractor-jasmine2-html-reporter)：`
```
  var Jasmine2HtmlReporter = require('protractor-jasmine2-html-reporter');

  exports.config = {
   // ...
     onPrepare: function() {
        jasmine.getEnv().addReporter(
        new Jasmine2HtmlReporter({
        savePath: 'target/reports'//保存路径
        screenshotsFolder: 'images'//图片的文件夹名
        })
      );
   }
}
```

13. 这样一整个测试开发流程就写完啦~