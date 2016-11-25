function spec2(){

var mali=require('./appendDriver.js');

describe('mali index page', function () {
        
        browser.ignoreSynchronization = true;
        browser.get('http://192.168.1.208');
        browser.sleep(8000);                           //就因为这一行，导致接下来没有顺利执行！！！
        var a = browser.findElement(By.css("#ui-layer>canvas"));

     it('goes to next page', function () {

        browser.sleep(5000);
        mali.clickIt(a,675,100);//自定义方法
        mali.waitUrl('campaign/dungeon','http://192.168.1.208/campaign/dungeon');
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.208/campaign/dungeon');

})
})

}
module.exports=spec2;