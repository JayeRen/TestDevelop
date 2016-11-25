var mali=require('../canvasDriver.js');

describe('mali login page', function () {
    beforeEach(function(){
        browser.ignoreSynchronization = true;
        
        browser.manage().window().maximize();
        browser.get('http://192.168.1.209');
        browser.sleep(25000);   
        mali.clickIt(250,175); 
    });

      it('goes to register page', function () {
        mali.waitUrl('?panel=loginIn','http://192.168.1.209/?panel=loginIn');
        mali.clickIt(1125,750);
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/?panel=register_age');
      });
      
      it('forgets psd', function () {
        mali.waitUrl('?panel=loginIn','http://192.168.1.209/?panel=loginIn');
        mali.clickIt(775,625);
        mali.waitUrl('?panel=loginIn','http://192.168.1.209/?panel=loginIn');//需修改
        expect(browser.getCurrentUrl()).toEqual('http://192.168.1.209/?panel=loginIn');

      });

});
