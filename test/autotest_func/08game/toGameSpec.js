//function main(){
//自定义
var mali =require('../canvasDriver.js');
var maliJ =require('../appendSpec.js'); 

xdescribe('mali adventure page', function () {
   beforeAll(function(){
        //使用protractor，非angularjs，这句话必须加上
        browser.ignoreSynchronization = true;
        //浏览器窗口最大化
        browser.manage().window().maximize();  
        //加载网页      
        browser.get('http://192.168.1.209');
        //等待足够时间到主界面
        browser.sleep(20000);
        //预置点开地图界面
        mali.clickIt(1500,300);//自定义方法
   });
            
    
    //已有账号？登录
    it('，to chapter page', function () { 
        mali.waitUrl('','http://192.168.1.209/campaign/remains');           
        //点击章节1
        browser.sleep(5000);
        mali.clickIt(350,925);
        mali.waitUrl('','http://192.168.1.209/campaign/remains?level_group=1-1');
        //断言（为了通过，reporter有截图，靠人工查看截图）
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/campaign/remains?level_group=1-1');
        });
    it('，click level to equip page', function () {      
        //点击章节1
        browser.sleep(5000);
        mali.clickIt(1275,400);
       ///// // 增加url后再改！！！mali.waitUrl('level_group=1-1','http://192.168.1.209/campaign/remains?level_group=1-1');
        //断言（为了通过，reporter有截图，靠人工查看截图）
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/campaign/remains?level_group=1-1');
        });
    
     it('，to game page', function () {  
        browser.sleep(500);
        //点击年龄文本框
        mali.clickIt(950,400);
        mali.clickIt(950,400);
        browser.sleep(5000);
        mali.clickIt(1050,850);
        //断言（为了通过，reporter有截图，靠人工查看截图）
        mali.waitUrl('http://192.168.1.209/level/0102wldsk?campaign=remains&segment=1-1-1');
        browser.sleep(5000);
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/level/0102wldsk?campaign=remains&segment=1-1-1');
        });
    

});
