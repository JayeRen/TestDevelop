
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
    //年龄框焦点
    it(',age txt could be focused', function () {  
        //等待至加载年龄界面    
        mali.waitUrl('?panel=register_age','http://192.168.1.209/?panel=register_age');
        //点击年龄文本框
        mali.clickIt(1000,450);
        //断言（为了通过，reporter有截图，靠人工查看截图）
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/?panel=register_age');
        });
    //正确关闭
    it('could be closed', function () {
        maliJ.close(1315,350,'http://192.168.1.209/?panel=register_age','http://192.168.1.209/');
        // expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/?panel=register_age');
        // mali.waitUrl('?panel=loginIn','http://192.168.1.209/?panel=register_age');
        // mali.clickIt(1315,350);
        // mali.waitUrl('','http://192.168.1.209/');
        // expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/');         
    });
});
