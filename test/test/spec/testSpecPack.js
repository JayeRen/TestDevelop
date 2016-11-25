//本页可以用于跳转各个页面，参数用json包装。


var IndexPageTo=require('./reuse/IndexPageTo.js');

describe('CampaignOfIndex',function(){
    IndexPageTo(675,100,'campaign/dungeon','http://192.168.1.208/campaign/dungeon');
});
