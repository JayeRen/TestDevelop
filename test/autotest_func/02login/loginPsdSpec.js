var mali=require('../canvasDriver.js');

describe('could check right psd with fixed email',function(){
      beforeEach(function(){
            browser.ignoreSynchronization = true;
            //浏览器窗口最大化
            browser.manage().window().maximize();        
            browser.get('http://192.168.1.209');
            browser.sleep(9000);
            //预置点开登录界面   
            mali.clickIt(250,175);                        
            browser.sleep(5000);
            //预置输入密码
            mali.clickIt(950,450);
            mali.sendKeys(950,450,"acte@foxmail.com");
            browser.sleep(5000);
      });
      it('psd txt is null with mail',function(){
            mali.clickIt(950,750);
            expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/?panel=loginIn');
      });
      it('psd format is wrong with mail',function(){
            mali.clickIt(950,575);
            mali.sendKeys(950,575,"12321");
            browser.sleep(5000);
            mali.clickIt(950,750);
            expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/?panel=loginIn');
      });
      it('psd format is right with mail',function(){
            mali.clickIt(950,575);
            mali.sendKeys(950,575,'1');
            mali.sendKeys(950,575,'2');
            mali.sendKeys(950,575,'3');
            mali.sendKeys(950,575,'4');
            mali.sendKeys(950,575,'5');
            mali.sendKeys(950,575,'6');
            browser.sleep(5000);
            mali.clickIt(950,750);
            browser.sleep(5000);
            expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/?panel=loginIn');
      });

      });