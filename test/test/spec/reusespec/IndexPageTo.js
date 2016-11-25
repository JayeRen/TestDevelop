var mali=require('../appendDriver.js');

//对首页，有各个图标，点击图标跳转到下一页面的测试可以都用本方法调用
//参数用.json封装即可
function IndexPageTo(x,y,surl,url){

                browser.ignoreSynchronization = true;
                browser.get('http://192.168.1.208');
                browser.sleep(8000);                           //就因为这一行，导致接下来没有顺利执行！！！
                // var a = browser.findElement(By.css("#ui-layer>canvas"));

        it('goes to next page',function(){
                browser.sleep(5000);        
                mali.clickIt(x,y);
                mali.waitUrl(surl,url);
                expect(browser.getCurrentUrl()).toEqual(url);
         })
     
}
module.exports = IndexPageTo;