// spec.js
describe('mali index page', function () {
  browser.ignoreSynchronization = true;
  browser.get('http://192.168.1.208');

  it('should have a title', function () {
    expect(browser.getTitle()).toEqual('码力中国-最酷的编程教育游戏');
  });


  it('goes to next page', function () {
    // browser.ignoreSynchronization = true;
    // browser.get('http://192.168.1.208');
    browser.sleep(7000);                           //就因为这一行，导致接下来没有顺利执行！！！
    var a = browser.findElement(By.css("#ui-layer>canvas"));
    browser.actions().mouseMove(a, {
      x: 675,
      y: 100
    }).click().perform();                           //点击活动栏

    var EC = protractor.ExpectedConditions;         //等待到下一页面，然后做出断言~
    browser.wait(EC.urlContains('campaign/dungeon'), 150000).then(function (result) {
      expect(browser.getCurrentUrl()).toEqual('http://192.168.1.208/campaign/dungeon');
    });
  });

  it('goes to game page',function(){
    browser.actions().mouseMove(a, {x:225,y:500}).click().perform()   //点击第一关
    .then(function(element){
          driver.actions().mouseMove(element, {
            x: 750,
            y: 145
        }).click().perform(); //点击第一回合
    }).then(function(element){

    });


  });

  it('goes to game page',function(){
    
  });

});