//可复用用例
var mali=require('./canvasDriver.js');
//关闭页面
function close(x,y,before,after){ 
        //断言关闭前界面url：before
        mali.waitUrl('',before);      
        expect(browser.getCurrentUrl()).toEqual(before);
        //点击关闭按钮
        mali.clickIt(1315,350);
        //断言关闭后界面url：after
        mali.waitUrl('',after);
        expect(browser.getCurrentUrl()).toEqual(after);         
}
exports.close=close;