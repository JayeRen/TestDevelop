//自定义封装一些在canvas使用的driver

//根据坐标点点击
var clickIt=function(x,y){
    var canvas = browser.findElement(By.css("#ui-layer>canvas"));//每次点击前寻找canvas元素
    browser.actions().mouseMove(canvas, {
    x: x,//通过chrome检查元素肉眼获取，希望以后有更灵活的找法
    y: y //通过chrome检查元素肉眼获取，希望以后有更灵活的找法
    }).click().perform();  
}

//根据css element点击
var clickCSS= function(cssElement){
    var canvas = browser.findElement(By.css("#ui-layer>canvas"));
    browser.actions().mouseMove(browser.findElement(By.css(cssElement))).click().perform();
}
//等待新url加载
var waitUrl=function(suburl,url){
    //等待到下一页面，然后做出断言~
    var EC = protractor.ExpectedConditions;         
    browser.wait(EC.urlContains(suburl), 8000);
}

//清除缓存（未成功）
var moveCookies=function(){
    //第一种通过cookie的name
    browser.manage().deleteCookieNamed("CookieName");
    //第二种通过Cookie对象
    browser.manage().deleteCookie(cookie);
    //第三种全部删除
    browser.manage().deleteAllCookies();
}

//screenshot（暂时不可用）
var screenShot=function(name){
    browser.sleep(5000);
    //每次点击前寻找canvas元素
    var canvas = browser.findElement(By.css("#ui-layer>canvas"));
    browser.takeScreenshot().then((png)=>{
        writeScreenShot(png, name+'.png');   //旧版driver和chromedriver还不支持
    })
}

//sendKeys：根据坐标focus，然后传文本
var sendKeysXY=function(x,y,txt){
    var canvas = browser.findElement(By.css("#ui-layer>canvas"));
    browser.actions().mouseMove(canvas, {
    x: x,//通过chrome检查元素肉眼获取，希望以后有更灵活的找法
    y: y //通过chrome检查元素肉眼获取，希望以后有更灵活的找法
    }).sendKeys(txt).perform();
}
//sendKeys：根据css元素focus，然后传文本
var sendKeysCSS=function(cssElement,txt){
    var canvas = browser.findElement(By.css("#ui-layer>canvas"));
    browser.actions().mouseMove(browser.findElement(By.css(cssElement))).click()
                .sendKeys(txt)
                .perform();
}
exports.clickIt=clickIt;
exports.clickCSS=clickCSS;
exports.waitUrl=waitUrl;
exports.screenShot=screenShot;
exports.sendKeysXY=sendKeysXY;
exports.sendKeysCSS=sendKeysCSS;

