//function main(){
var mali=require('../canvasDriver.js');

describe('mali main page', function () {
    beforeEach(function(){
        browser.ignoreSynchronization = true;
        
        browser.manage().window().maximize();
        browser.get('http://192.168.1.209');
        browser.sleep(8000);                           //就因为这一行，导致接下来没有顺利执行！！！
    });
     it('goes to login page', function () {
        mali.clickIt(250,175);//自定义方法
        mali.waitUrl('?panel=loginIn','http://192.168.1.209/?panel=loginIn');
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/?panel=loginIn');

      });
      it('goes to register page', function () {
        mali.clickIt(400,175);
        mali.waitUrl('?panel=register','http://192.168.1.209/?panel=register');
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/?panel=register');
      });
      xit('goes to diamond page', function () {
        browser.sleep(5000);
        mali.clickIt(1050,50);//自定义方法
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/');

      });
      xit('goes to strength page', function () {
        browser.sleep(5000);
        mali.clickIt(1600,50);//自定义方法
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/');         
      });
      //地图界面
      xit('goes to adventure page', function () {

                browser.sleep(5000);
                mali.clickIt(1500,300);//自定义方法
                mali.waitUrl('campaign/dungeon','http://192.168.1.209/campaign/dungeon');
                expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/campaign/dungeon');

      });
      xit('goes to edit page', function () {

        browser.sleep(5000);
        mali.clickIt(1050,1050);//自定义方法
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/');
      });
      xit('goes to hero page', function () {

        browser.sleep(5000);
        mali.clickIt(1250,1050);//自定义方法
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/');
      });
      xit('goes to achievement page', function () {

        browser.sleep(5000);
        mali.clickIt(1450,1050);//自定义方法
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/');
      });
      xit('goes to shop page', function () {

       browser.sleep(5000);
        mali.clickIt(1650,1050);//自定义方法
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/');

      });
});
//}
//module.exports=spec2;