// spec.js
describe('mali index page', function () {
  browser.ignoreSynchronization = true;
  browser.get('http://192.168.1.208');
  browser.sleep(7000);                           //就因为这一行，导致接下来没有顺利执行！！！
    var a = browser.findElement(By.css("#ui-layer>canvas"));

  it('should have a title', function () {
    expect(browser.getTitle()).toEqual('码力中国-最酷的编程教育游戏');
  });


  it('goes to next page', function () {
    // browser.ignoreSynchronization = true;
    // browser.get('http://192.168.1.208');
    
    browser.actions().mouseMove(a, {
      x: 675,
      y: 100
    }).click().perform();                           //点击活动栏

    var EC = protractor.ExpectedConditions;         //等待到下一页面，然后做出断言~
    browser.wait(EC.urlContains('campaign/dungeon'), 5000).then(function (result) {
      expect(browser.getCurrentUrl()).toEqual('http://192.168.1.208/campaign/dungeon');
    });
  });

  it('goes to game page',function(){//以下一系列点击事件还没有找到方法判断，所以先不做断言，直到最后一个页面变化
    var EC = protractor.ExpectedConditions;         //等待到下一页面，然后做出断言~
    browser.wait(EC.urlContains('campaign/dungeon'), 5000).then(function(){
          browser.sleep(5000);
          return a;
    }).then(function(element){
          browser.actions().mouseMove(a, {x:225,y:500}).click().perform();   //点击第一关
          return a;
    }).then(function(){
          browser.actions().mouseMove(a, {
            x: 750,
            y: 145
          }).click().perform(); //点击第一回合
          // browser.sleep(8000);//暂时没有解决方法，要睡一下。
          return element;
    }).then(function () {
      browser.sleep(8000);//暂时没有解决方法，要睡一下。
        browser.actions().mouseMove(a, {
            x: 500,
            y: 130
        }).click().click().perform(); //双击道具装备
        return element;
    }).then(function () {
        browser.actions().mouseMove(a, {
            x: 600,
            y: 500
        }).click().perform(); //开始
    }).then(function () {
          var EC = protractor.ExpectedConditions;         //等待到下一页面，然后做出断言~
          browser.wait(EC.urlContains('level/dungeon-1-1-1-0101gjmz'), 5000)
          .then(function () {
          expect(browser.getCurrentUrl()).toEqual('http://192.168.1.208/level/dungeon-1-1-1-0101gjmz');
          });      
    });
  });  

    it('inputs correct codes',function(){
            var leveldata = require('./level-data.js');
            expect(leveldata.level2).toBe("self.moveLeft()");

    });

  // it('goes to game page',function(){
    
  // });

});