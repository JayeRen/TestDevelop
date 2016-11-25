var webdriver = require('selenium-webdriver'),
    chrome = require('selenium-webdriver/chrome'),
    By = webdriver.By,
    until = webdriver.until;

var driver = new webdriver.Builder()
.forBrowser('chrome')
.setChromeOptions(/* ... */)
.build();
driver.get('http://192.168.1.208/');


driver.sleep(7000);
var a=driver.findElement(By.css("div#ui-layer>canvas"));//定位canvas

driver.actions().mouseMove(a, {x:675,y:100}).click().perform();//点击活动栏
// driver.manage().timeouts().implicitlyWait(8000);
//  driver.wait(until.urlIs('http://192.168.1.208/campaign/dungeon'),5000).actions().mouseMove(a, {x:225,y:500}).click().perform();;
//脚本：如果当前关卡==1
driver.wait(until.urlContains('campaign/dungeon'),3000)
    .then(function(result){
            console.log(result);
            driver.sleep(3000);
            return a; 
    }).then(function(element){
         console.log('click 1#');
         driver.actions().mouseMove(a, {x:225,y:500}).click().perform();
          console.log('before sleep');
            driver.sleep(3000);
            console.log('after sleep');
            return a;
        //点击第一关
    }).then(function(element){
        console.log('点击开始1-1 145');
        driver.actions().mouseMove(element, {
            x: 750,
            y: 145
        }).click().perform(); //
         console.log('before sleep');
            driver.sleep(3000);
            console.log('after sleep');
            return element;
    }).then(function(element){
        driver.actions().mouseMove(element, {
            x: 500,
            y: 130
        }).click().click().perform(); //双击道具装备
           driver.sleep(3000);
            return element;
    }).then(function(element){
        driver.actions().mouseMove(element, {x: 600, y: 500}).click().perform(); //开始
    }).then(function(element){
        driver.wait(until.elementLocated(By.id("opentips_start_btn"))).click();
        // driver.findElement(By.id("opentips_start_btn")).click();
        console.log("开始游戏"); //开始游戏
    }).then(function(element){
        driver.wait(until.elementLocated(By.css("div.ace_cursor")));
                console.log("输入文本");
                var leveldata = require('./level-data');
                driver.actions().mouseMove(driver.findElement(By.css("div.ace_cursor"))).click()
                .sendKeys(leveldata.level1)
                .perform();
                driver.sleep(3000);
    }).then(function(element){
        driver.actions().mouseMove(a, {x: 745,y: 370}).click().perform();
    });

driver.close();
driver.quit();