//function main(){
var mali =require('../canvasDriver.js');
var maliJ =require('../appendSpec.js'); 

xdescribe('mali game page', function () {
   beforeEach(function(){
        //使用protractor，非angularjs，这句话必须加上
        browser.ignoreSynchronization = true;
        //浏览器窗口最大化
        browser.manage().window().maximize();  
        //加载游戏界面      
        browser.get('http://192.168.1.209/level/0102wldsk?campaign=remains&segment=1-1-1');
        //等待足够时间到界面
        browser.sleep(20000); 
        //点击检查focus
        // mali.clickIt(1200,210);
   });
   //观察光标 
    it('check focus index',function(){
        //点击后观察是否有光标
        mali.clickCSS("div.ace_cursor");
        //这个断言是为了截图观察
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/level/0102wldsk?campaign=remains&segment=1-1-1');
    });      
    
    //hint提示
    it('，hint', function () { 
        //点击“提示”
        mali.clickIt(250,1025);
        mali.waitUrl('','http://192.168.1.209/level/0102wldsk?campaign=remains&segment=1-1-1?campaign=remains&segment=1-1-1&panel=story');
        //断言（为了通过，reporter有截图，靠人工查看截图）
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/level/0102wldsk?campaign=remains&segment=1-1-1?campaign=remains&segment=1-1-1&panel=story');
        //点击关闭按钮，断言关闭掉回到游戏界面url
        mali.clickIt(1160,300);
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/level/0102wldsk?campaign=remains&segment=1-1-1?campaign=remains&segment=1-1-1&panel=story');
    });

    //游戏界面的设置
    it('，option', function () {      
        //点击进入设置界面
         mali.clickIt(50,1025);
       ///// // 增加url后再改！！！mali.waitUrl('level_group=1-1','http://192.168.1.209/campaign/remains?level_group=1-1');
        //断言（为了通过，reporter有截图，靠人工查看截图）
         expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/level/0102wldsk?campaign=remains&segment=1-1-1?campaign=remains&segment=1-1-1&panel=level_setting');
         //音效开启
         mali.clickIt(1275,550);   
         expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/level/0102wldsk?campaign=remains&segment=1-1-1?campaign=remains&segment=1-1-1&panel=level_setting');
         //音乐开启
         mali.clickIt(1150,550);   
         expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/level/0102wldsk?campaign=remains&segment=1-1-1?campaign=remains&segment=1-1-1&panel=level_setting');
         //继续游戏
         mali.clickIt(800,550);
         //过后会改   
         expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/level/0102wldsk?campaign=remains&segment=1-1-1?campaign=remains&segment=1-1-1&panel=level_setting');
         //重新进入设置界面(url需要改进)
         mali.clickIt(50,1025);
         expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/level/0102wldsk?campaign=remains&segment=1-1-1?campaign=remains&segment=1-1-1&panel=level_setting?campaign=remains&segment=1-1-1?campaign&segment=1-1-1&undefined=level_setting');
         //退出游戏
         mali.clickIt(650,550); 
         expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/campaign/remains'); 
    });
       
     //技能的显示模式 图标/代码
     it('，to game page', function () {  
        mali.clickIt(1875,1075);
        //断言（为了通过，reporter有截图，靠人工查看截图）
        mali.waitUrl('http://192.168.1.209/level/0102wldsk?campaign=remains&segment=1-1-1');
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/level/0102wldsk?campaign=remains&segment=1-1-1');
        });
    

});
