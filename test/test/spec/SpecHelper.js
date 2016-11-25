//例子
beforeEach(function () {
  jasmine.addMatchers({
    
    
    
    toBePlaying: function () {
            return {
                        compare: function (actual, expected) {
                        var player = actual;

                            return {
                                pass: player.currentlyPlayingSong === expected && player.isPlaying
                            };

                        }
            };
    },
//matcher形式写法 
    isClickable: function(url){
    //定位按键，点击，检测是否转换元素   
            return{
                    compare:function(actual,expected){
                    var url= actual;
                    var result={};
                    result.pass= util.equals(url);
                    return result;
                }
           }
     }

  });
});
