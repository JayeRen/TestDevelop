//代码块用例，以后可作为功能块复用，里面包含正确代码，错误代码，过程从游戏界面到点击继续后回到地图。
//function main(){}
//driver结合canvas坐标定位的封装
var mali =require('../canvasDriver.js');
//关闭功能用例的封装
var maliJ =require('../appendSpec.js'); 

describe('mali game page - code module', function () {
   //beforeEach 是在每个用例前重复该步骤，AllEach是在整个describe的开头预置步骤。
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

    //输入正确代码
    it('，types right code', function () { 
        //模拟键入代码文本，div.ace_cursor为光标tag
        mali.sendKeysCSS("div.ace_cursor","self.moveDown()");
        //点击运行
        mali.clickIt(1200,625);
        browser.sleep(5000);
        //点击完成
        mali.clickIt(1750,625);
        browser.sleep(5000);
        //////!!!修改url后修改
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/level/0102wldsk?campaign=remains&segment=1-1-1');
        //点击继续
        mali.clickIt(1000,775);
        browser.sleep(5000);
        //等待回到地图界面
        mali.waitUrl('','http://192.168.1.209/campaign/remains');
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/campaign/remains');
    });

    //输入错误代码
    xit('，types wrong code', function () {      
        //点击章节1
    }); 
    
    //点击代码块输入正确代码
    it('，types right skill code', function () { 
        //模拟键入代码文本，div.ace_cursor为光标tag
        //点击正确代码块
        mali.clickCSS("div.ace_cursor");
        mali.clickIt(1275,775);
        //点击运行
        mali.clickIt(1200,625);
        browser.sleep(5000);
        //点击完成
        mali.clickIt(1750,625);
        browser.sleep(5000);
        //////!!!修改url后修改
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/level/0102wldsk?campaign=remains&segment=1-1-1');
        //点击继续
        mali.clickIt(1000,775);
        browser.sleep(5000);
        //等待回到地图界面
        mali.waitUrl('','http://192.168.1.209/campaign/remains');
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/campaign/remains');
    });

    //点击代码块输入错误代码（使用剩下未使用块）
    it('，types left skill code with twice speed', function () { 
        //模拟键入代码文本，div.ace_cursor为光标tag
        //点击剩下的代码块
        mali.clickCSS("div.ace_cursor");
        mali.clickIt(1375,775);
        mali.clickIt(1500,775);
        mali.clickIt(1625,775);
        mali.clickIt(1750,775);
        //点击加速
        mali.clickIt(1450,625);
        //点击运行
        mali.clickIt(1200,625);
        browser.sleep(5000);
        //点击完成
        mali.clickIt(1750,625);
        browser.sleep(5000);
        //////!!!修改url后修改
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/level/0102wldsk?campaign=remains&segment=1-1-1');
        //点击继续
        mali.clickIt(1000,775);
        browser.sleep(5000);
        //等待回到地图界面
        mali.waitUrl('','http://192.168.1.209/campaign/remains');
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/campaign/remains');
    });

});
