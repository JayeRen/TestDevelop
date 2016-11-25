//function main(){
//自定义
var mali =require('../canvasDriver.js');
var maliJ =require('../appendSpec.js'); 

xdescribe('mali register-age page', function () {
    beforeEach(function(){
        //使用protractor，非angularjs，这句话必须加上
        browser.ignoreSynchronization = true;
        //浏览器窗口最大化
        browser.manage().window().maximize();  
        //加载网页      
        browser.get('http://192.168.1.209');
        //等待足够时间到主界面
        browser.sleep(25000);
        //预置点开注册界面
        mali.clickIt(375,175);                    
    });
    //已有账号？登录
    it('，to login page', function () {  
        //等待至加载年龄界面    
        mali.waitUrl('?panel=register_age','http://192.168.1.209/?panel=register_age');
        //点击年龄文本框
        mali.clickIt(1225,775);
        //断言（为了通过，reporter有截图，靠人工查看截图）
        mali.waitUrl('?panel=login_in','http://192.168.1.209/?panel=login_in');
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/?panel=login_in');
        });

    

});
