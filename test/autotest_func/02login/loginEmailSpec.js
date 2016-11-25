var mali=require('../canvasDriver.js');

describe('could check right email with fixed psd',function(){
      beforeEach(function(){
            browser.ignoreSynchronization = true;
            browser.manage().window().maximize();        //浏览器窗口最大化
            browser.get('http://192.168.1.209');
            browser.sleep(9000);   
            mali.clickIt(250,175);                        //预置点开登录界面
            browser.sleep(5000);
            mali.clickIt(950,575);
            mali.sendKeys(950,575,"123456");
            browser.sleep(5000);
      });
      it('mail txt is null with psd',function(){
            mali.clickIt(950,750);
            expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/?panel=loginIn');
      });
      it('mail format is wrong with psd',function(){
            mali.clickIt(950,450);
            mali.sendKeys(950,450,"22");
            browser.sleep(5000);
            mali.clickIt(950,750);
            expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/?panel=loginIn');
      });
      it('mail format is right with psd',function(){
            mali.clickIt(950,450);
            mali.sendKeys(950,450,"22@qq.com");
            browser.sleep(5000);
            mali.clickIt(950,750);
            expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/?panel=loginIn');
      });

      });