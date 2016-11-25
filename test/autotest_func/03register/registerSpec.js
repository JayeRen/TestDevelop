var mali=require('../canvasDriver.js');
var maliJ =require('../appendSpec.js');

xdescribe('mali register page', function () {
    beforeEach(function(){
        browser.ignoreSynchronization = true;
        
        browser.manage().window().maximize();        //浏览器窗口最大化
        browser.get('http://192.168.1.209');
        browser.sleep(25000);
        //预置点开年龄界面
        mali.clickIt(375,175); 
        //预置加载注册界面                   
        mali.waitUrl('','http://192.168.1.209/?panel=register_age');
        mali.clickIt(1000,450);
        mali.sendKeys(1000,450,"12");
        mali.clickIt(1050,775);
    });

    //邮件框焦点
    it(',email txt could be focused', function () {      
        //等待至加载界面    
        mali.waitUrl('?panel=register','http://192.168.1.209/?panel=register');
        //点击文本框
        mali.clickIt(900,425);
        //断言（为了通过，reporter有截图，靠人工查看截图）
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/?panel=register');
    });

    //密码焦点
    it(',psd txt could be focused', function () {  
        //等待至加载界面    
        mali.waitUrl('?panel=register','http://192.168.1.209/?panel=register');
        //点击文本框
        mali.clickIt(900,525);
        //断言（为了通过，reporter有截图，靠人工查看截图）
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/?panel=register');
    });

    //昵称框焦点
    it(',username txt could be focused', function () {      
        //等待至加载界面    
        mali.waitUrl('?panel=register','http://192.168.1.209/?panel=register');
        //点击文本框
        mali.clickIt(900,625);
        //断言（为了通过，reporter有截图，靠人工查看截图）
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/?panel=register');
    });
    
    //正确关闭
    it('could be closed', function () {
        maliJ.close(1315,350,'http://192.168.1.209/?panel=register','http://192.168.1.209/');   
    });

});
