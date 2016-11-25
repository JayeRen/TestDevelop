var webdriver = require('selenium-webdriver'),
    chrome = require('selenium-webdriver/chrome'),
    By = webdriver.By,
    until = webdriver.until;

var driver = new webdriver.Builder()
    .forBrowser('chrome')
    .setChromeOptions( /* ... */ )
    .build();
driver.get('http://192.168.1.208/');



driver.sleep(4000);

var a = driver.findElement(By.css("div#ui-layer>canvas")); //定位canvas
driver.sleep(2000);

//OK-测试活动模块 
//driver.actions(a).mouseMove({x:300,y:150}).click().perform();
//driver.actions().mouseMove(a, {x:300,y:150}).click().perform();//点击活动栏
//driver.sleep(1000);
//driver.actions().mouseMove(a,{x:475,y:350}).click().perform();//点击弹出的确定键
//driver.sleep(1000);

//OK-成就模块---还有左右翻页
//driver.actions().mouseMove(a, {x:375,y:500}).click().perform();//点击活动栏
//driver.sleep(2000);
//driver.actions().mouseMove(a, {x:460,y:520}).click().perform();//左翻页
//driver.sleep(2000);
//driver.actions().mouseMove(a, {x:575,y:520}).click().perform();//右边翻页
//driver.sleep(2000);
//driver.actions().mouseMove(a,{x:830,y:70}).click().perform();//关闭窗口
//driver.sleep(3000);

//OK-英雄模块
//driver.actions().mouseMove(a, {x:750,y:470}).click().perform();//点击活动栏
//driver.sleep(2000);
//driver.actions().mouseMove(a, {x:725,y:500}).click().perform();//出战
//driver.sleep(2000);
//driver.actions().mouseMove(a, {x:675,y:120}).click().perform();//点击人物
//driver.sleep(2000);
//driver.actions().mouseMove(a,{x:830,y:50}).click().perform();//关闭窗口
//driver.sleep(3000);

//测试设置模块---还有填写昵称，密码，重复输入密码。上传图片。开启音乐选项。退出账号
//driver.actions().mouseMove(a, {x:50,y:350}).click().perform();//点击活动栏
//driver.sleep(1000);
//driver.actions().mouseMove(a,{x:810,y:90}).click().perform();//关闭窗口
//driver.sleep(3000);
//driver.actions().mouseMove(a, {x:50,y:350}).click().perform();//点击活动栏
//driver.sleep(1000);
//driver.actions().mouseMove(a,{x:475,y:470}).click().perform();//保存按钮
//driver.sleep(3000);


//道具模块----还有根据部位看道具，左右翻页，解锁，等级到/未到提示
//driver.actions().mouseMove(a, {x:850,y:300}).click().perform();//点击活动栏
//driver.sleep(2000);
//driver.actions().mouseMove(a,{x:700,y:60}).click().perform();//关闭窗口
//driver.sleep(3000);

//探险模块---选区域等复杂逻辑。
driver.actions().mouseMove(a, {
    x: 675,
    y: 100
}).click().perform(); //点击活动栏
driver.sleep(3000);
//driver.actions().mouseMove(a,{x:1010,y:25}).click().perform();//关闭窗口
//driver.sleep(3000);
//driver.actions().mouseMove(a,{x:1010,y:300}).click().perform();//向右更换地图
//driver.sleep(3000);

driver.actions().mouseMove(a, {
    x: 225,
    y: 500
}).click().perform(); //点击第一关
driver.sleep(3000);

//滚动条----不成功
// driver.actions().mouseMove(a, {x: 800,y: 75}).perform();
// driver.touchActions().scroll({x: 0,y: 200}).perform();
// driver.sleep(5000);

driver.actions().mouseMove(a, {
    x: 750,
    y: 145
}).click().perform(); //点击开始1-1 145
driver.sleep(3000);

// var c = driver.actions().mouseMove(a, {x: 800,y: 275}).click().perform();
// driver.actions().mouseMove(a, {x: 800,y: 275}).dragAndDrop(a,{x: 800,y:75}).perform();//滚动条拖拽滚动，成功
// driver.sleep(5000);
// driver.touchActions().scrollFromElement(a, {x: 0,y: 200}).perform();//滚动条-不成功-因为是touch

// driver.actions().mouseMove(a, {x: 500,y: 125}).doubleClick().perform(); //双击道具装备---不成功
driver.actions().mouseMove(a, {
    x: 500,
    y: 130
}).click().click().perform(); //双击道具装备
driver.sleep(3000);
driver.actions().mouseMove(a, {
    x: 600,
    y: 500
}).click().perform(); //开始
driver.sleep(6000);
driver.findElement(By.id("opentips_start_btn")).click(); //开始游戏
driver.sleep(4000);

//方式一：点击辅助块输入移动文本
// driver.actions().mouseMove(a, {x: 700,y: 145}).click().perform(); //点击打字框
// driver.sleep(3000);
// driver.actions().mouseMove(a, {x: 710,y: 445}).click().perform(); //选择移动块
// driver.sleep(3000);
// driver.actions().mouseMove(a, {x: 900,y: 250}); //选掉提示
// driver.sleep(3000);
var leveldata = require('./level-data');//json
// 方式二：直接输入文本。根据光标标签，找到空行，点击，输入内容-成功~注意，key.XXXX,要加一个key.NULL才有抬起键子过程
// driver.sleep(3000);
// var d = driver.actions().mouseMove(driver.findElement(By.css("div.ace_cursor"))).click().
// sendKeys(leveldata.level1, webdriver.Key.ENTER, webdriver.Key.NULL).perform();
// driver.sleep(3000);

driver.actions().mouseMove(a, {x: 745,y: 370}).click().perform(); //运行----也因为提示框只能在边缘点击，没有标签，需要坐标
driver.sleep(3000);
driver.actions().mouseMove(a, {x: 950,y: 370}).click().perform(); //完成
driver.sleep(3000);
driver.actions().mouseMove(a, {x: 525,y: 460}).click().perform(); //继续
driver.sleep(3000);


driver.close();
driver.quit();