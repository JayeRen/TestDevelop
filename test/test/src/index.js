// api document
// http://seleniumhq.github.io/selenium/docs/api/javascript/module/selenium-webdriver/
var webdriver = require('selenium-webdriver'),
    By = webdriver.By,
    until = webdriver.until,
    chrome = require('selenium-webdriver/chrome');
    // firefox = require('selenium-webdriver/firefox');

var driver = new webdriver.Builder()
    .forBrowser('chrome')
    .setChromeOptions(/* ... */)
    .build();

driver.get('http://spoonium.com/example.html');
driver.sleep(2000);
driver.findElement(By.id("pic_check")).click();
driver.findElement(By.id("tv_check")).click();

// #answer question #2
driver.sleep(2000);
driver.findElement(By.id("yes_span")).click();

// #answer question #3
pagetitle = driver.title;
driver.findElement(By.linkText("this link")).click();
if (driver.title == pagetitle){
    // #link didn't go anywhere
    driver.findElement(By.id("true_link")).click();
}else{
    // #link left the page - should not get here!
    driver.back();
    driver.findElement(By.id("false_link")).click();
}
driver.sleep(2000);

// #answer question #4
// row1_xpath = '//*[@id=\"magic_square_table\"]/tbody/tr[1]/';
// magic_constant = 0;
// for(var i=0; i< 4;i++){
//     node_path = row1_xpath + "td["+i + "]";
//     node_value = driver.findElement(By.xpath(node_path)).text;
//     magic_constant += node_value;
//     console.log("Found value %s, new magic_constant value = %s", node_value, magic_constant);
// }

// textbox_question4 = driver.findElement(By.id("table_answer_text"));
// textbox_question4.click();
// textbox_question4.clear();
// textbox_question4.sendKeys(magic_constant);

driver.sleep(2000);
// #click submit
driver.findElement(By.css('#submit > input[type="button"]:nth-child(1)')).click();
driver.sleep(2000);

// #verify that we score 100%
score_text = driver.findElement(By.id("score")).text;

// driver.wait(until.titleIs('webdriver -sample'), 5000);
driver.close();
driver.quit();

        