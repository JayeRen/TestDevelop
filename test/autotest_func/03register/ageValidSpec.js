var mali=require('../canvasDriver.js');
var maliJ =require('../appendSpec.js');

xdescribe('mali register-age page', function () {
    beforeEach(function(){
        browser.ignoreSynchronization = true;
        
        browser.manage().window().maximize();        //浏览器窗口最大化
        browser.get('http://192.168.1.209');
        browser.sleep(25000);
        mali.clickIt(375,175);                    //预置点开登录界面
    });

    //年龄输入空
    it(',age enters null', function () {      
        mali.waitUrl('','http://192.168.1.209/?panel=register_age');
        mali.clickIt(1050,775);
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/?panel=register_age');
    });

    //年龄输入非数字文本
    it(',age enters NaN', function () {      
        mali.waitUrl('','http://192.168.1.209/?panel=register_age');
        mali.clickIt(1000,450);
        mali.sendKeys(1000,450,"haha");
        mali.clickIt(1050,775);
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/?panel=register_age');
    });
    
    //年龄输入数字
    it(',age enters number', function () {
        mali.waitUrl('','http://192.168.1.209/?panel=register_age');
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/?panel=register_age');        
        mali.clickIt(1000,450);
        mali.sendKeys(1000,450,12);
        mali.clickIt(1050,775);//自定义方法
        mali.waitUrl('','http://192.168.1.209/?panel=register&sub_panel=info_alert');//bug修复后要改成注册页
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/?panel=register&sub_panel=info_alert');         
    });

});
//}
//module.exports=spec2;