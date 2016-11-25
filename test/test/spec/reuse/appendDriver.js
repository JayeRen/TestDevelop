//将一些driver自定义封装
var  clickIt=function(x,y){
    var a = browser.findElement(By.css("#ui-layer>canvas"));//每次点击前寻找canvas元素
    browser.actions().mouseMove(a, {
    x: x,//675,
    y: y//100
    }).click().perform();  
}


var waitUrl=function(suburl,url){
    var EC = protractor.ExpectedConditions;         //等待到下一页面，然后做出断言~
    browser.wait(EC.urlContains(suburl), 5000);
}

exports.clickIt=clickIt;
exports.waitUrl=waitUrl;