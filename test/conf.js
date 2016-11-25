var Jasmine2HtmlReporter = require('protractor-jasmine2-html-reporter');

var reporter = new Jasmine2HtmlReporter({
  savePath: './autotest_func/reports/',
  screenshotsFolder: 'images',
  filePrefix: 'index',

  dest: './autotest_func/screenshots/',
  filename: 'my-report.html',

  cleanDestination: true,
  showSummary: false,
  showConfiguration: false,
  reportTitle: null,

  consolidate: true,
  consolidateAll: true
});

exports.config = {
  seleniumAddress: 'http://localhost:4444/wd/hub',
  // specs: ['./autotest_func/02login/*.js'],
  //specs: ['./autotest_func/01main/mainSpec.js'],
  // specs: ['./autotest_func/03register/*.js'],
  specs: ['./autotest_func/08game/*.js'],


//  // Setup the report before any tests start
//   beforeLaunch: function() {
//     return new Promise(function(resolve){
//       reporter.beforeLaunch(resolve);
//     });
//   },
  // Assign the test reporter to each running instance
  onPrepare: function() {
      jasmine.getEnv().addReporter(reporter);
   },
   // Close the report after all tests finish
  // afterLaunch: function(exitCode) {
  //   return new Promise(function(resolve){
  //     reporter.afterLaunch(resolve.bind(this, exitCode));
  //   });
  // }
  // ????不会玩 afterLaunch: function(){
  //   // var a = require('./autoexecute.js');
  //   // return new Promise(function(resolve){a.html;});
  //   return browser.get('file:///C:/Users/MALIWANJIA/work/test_protractor/test/reports/index.html');
  // }

};