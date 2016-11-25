var webdriver = require('selenium-webdriver'),
    chrome = require('selenium-webdriver/chrome'),
    By = webdriver.By,
    until = webdriver.until;

var driver = new webdriver.Builder()
.forBrowser('chrome')
.setChromeOptions(/* ... */)
.build();
driver.get('http://192.168.1.208/');

var x=675,y=100;

driver.sleep(7000);
var a=driver.findElement(By.css("div#ui-layer>canvas"));//定位canvas

driver.actions().mouseMove(a, {x,y}).click().perform();//点击活动栏
driver.sleep(7000);

driver.quit();