var mali=require('../canvasDriver.js');

describe('mali login page', function () {
    beforeEach(function(){
        browser.ignoreSynchronization = true;
        //浏览器窗口最大化
        browser.manage().window().maximize();        
        browser.get('http://192.168.1.209');
        browser.sleep(25000);
        //预置点开登录界面
        mali.clickIt(250,175);                    
    });

    //邮件框焦点
    it(',mail txt could be focused', function () {      
      mali.waitUrl('?panel=loginIn','http://192.168.1.209/?panel=loginIn');
      mali.clickIt(1000,450);
      browser.sleep(4000);
      expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/?panel=loginIn');
    });

    //密码框焦点
    it(',psd txt could be focused', function () {      
      mali.waitUrl('?panel=loginIn','http://192.168.1.209/?panel=loginIn');
      mali.clickIt(1000,575);
      browser.sleep(4000);
      expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/?panel=loginIn');
    });

    //正确关闭
    it('could be closed', function () {
      
      expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/?panel=loginIn');
      mali.waitUrl('?panel=loginIn','http://192.168.1.209/?panel=loginIn');
      mali.clickIt(1315,350);//自定义方法
      mali.waitUrl('','http://192.168.1.209/');
      expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/');         
    });

});
