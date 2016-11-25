var webdriver = require('selenium-webdriver'),
    chrome = require('selenium-webdriver/chrome'),
    By = webdriver.By,
    until = webdriver.until;

var driver = new webdriver.Builder()
.forBrowser('chrome')
.setChromeOptions(/* ... */)
.build();

driver.get('http://192.168.1.208/');
driver.sleep(8000);
driver.takeScreenshot().then(function(a){
    // console.log(a);
    a.getScreenshotAs(OutputType.FILE);
});