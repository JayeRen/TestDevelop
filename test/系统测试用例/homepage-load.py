#! /usr/bin/env python   
# -*- coding: utf-8 -*-
# PTS Script record tool v0.2.6.4
# PTS脚本SDK：框架API、常用HTTP请求/响应处理API
from util import PTS
from HTTPClient import NVPair
from HTTPClient import Cookie
from HTTPClient import HTTPRequest
from HTTPClient import CookieModule
# 脚本初始化段，可以设置压测引擎的常用HTTP属性
#PTS.HttpUtilities.setKeepAlive(False)
#PTS.HttpUtilities.setUrlEncoding('GBK')
#PTS.HttpUtilities.setFollowRedirects(False)
#PTS.HttpUtilities.setUseCookieModule(False)
PTS.HttpUtilities.setUseContentEncoding(True)
PTS.HttpUtilities.setUseTransferEncoding(True)

## 如想通过ECS内网IP进行压测，必须在下方“innerIp”备注行中输入ECS内网IP，如有多个请以英文逗号分隔，例如：127.0.0.1,127.0.0.2
# innerIp:

## 脚本执行单元类，每个VU/压测线程会创建一个TestRunner实例对象
class TestRunner:
    game_host_url = 'http://10.45.136.127/'
    # TestRunner对象的初始化方法，每个线程在创建TestRunner后执行一次该方法
    def __init__(self):
        self.threadContext = PTS.Context.getThreadContext()
        self.init_cookies = CookieModule.listAllCookies(self.threadContext)
    # 主体压测方法，每个线程在测试生命周期内会循环调用该方法
    def __call__(self):
        PTS.Data.delayReports = 1
        for c in self.init_cookies:
            CookieModule.addCookie(c, self.threadContext)
        statusCode = self.action1()
        PTS.Framework.setExtraData(statusCode)        
        statusCode = self.action2()
        PTS.Framework.setExtraData(statusCode)                
        PTS.Data.report()
        PTS.Data.delayReports = 0
    # TestRunner销毁方法，每个线程循环执行完成后执行一次该方法
    def __del__(self):
        for c in self.init_cookies:
            CookieModule.addCookie(c, self.threadContext)
    # 定义请求函数

    ## action1
    def action1(self):
        statusCode = [0L, 0L, 0L, 0L]        

        headers = [ NVPair('Accept', '*/*'), NVPair('Upgrade-Insecure-Requests', '1'), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url, None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)


        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/bluebird/js/browser/bluebird.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/jquery/dist/jquery.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/lodash/dist/lodash.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/underscore.string/dist/underscore.string.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/backbone/backbone-min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/tv4/tv4.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/backbone_mediator/dist/backbone-mediator.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/fileinput.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/mali-core/dist/mali-core.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/mali-model/dist/mali-model.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/marked/lib/marked.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'scripts/vendor/preloadjs-NEXT.combined.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'scripts/vendor/soundjs-NEXT.combined.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'scripts/vendor/easeljs-NEXT.combined.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'scripts/vendor/tweenjs-NEXT.combined.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'scripts/vendor/movieclip-NEXT.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'scripts/vendor/SpriteContainer.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'scripts/vendor/SpriteStage.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/i18next/i18next.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/aether/build/aether.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'scripts/vendor/coffeescript.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/mali-lib/dist/mali-lib.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/keymaster/keymaster.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/pingpp-pc.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/Subscripe.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/showdown.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/markparse.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'scripts/lib/ace/ace.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/zatanna/build/zatanna.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/LocalMogo.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/modules/egret/egret.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/modules/egret/egret.web.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/modules/eui/eui.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/modules/res/res.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/modules/game/game.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/modules/game/game.web.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/modules/tween/tween.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'main.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/battle/battle_assets/error_down.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/gameBg.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Upgrade-Insecure-Requests', '1'), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url, None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/bluebird/js/browser/bluebird.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/jquery/dist/jquery.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/lodash/dist/lodash.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/underscore.string/dist/underscore.string.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/backbone/backbone-min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/tv4/tv4.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/backbone_mediator/dist/backbone-mediator.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/fileinput.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/mali-core/dist/mali-core.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/mali-model/dist/mali-model.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/marked/lib/marked.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'scripts/vendor/preloadjs-NEXT.combined.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'scripts/vendor/soundjs-NEXT.combined.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'scripts/vendor/easeljs-NEXT.combined.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'scripts/vendor/tweenjs-NEXT.combined.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'scripts/vendor/movieclip-NEXT.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'scripts/vendor/SpriteContainer.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'scripts/vendor/SpriteStage.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/i18next/i18next.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/aether/build/aether.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'scripts/vendor/coffeescript.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/mali-lib/dist/mali-lib.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/keymaster/keymaster.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/pingpp-pc.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/Subscripe.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/showdown.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/markparse.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'scripts/lib/ace/ace.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/zatanna/build/zatanna.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/LocalMogo.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/modules/egret/egret.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/modules/egret/egret.web.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/modules/eui/eui.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/modules/res/res.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/modules/game/game.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/modules/game/game.web.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'libs/modules/tween/tween.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'main.min.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/battle/battle_assets/error_down.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/gameBg.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/battle/battle_assets/error.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/battle/battle_assets/Tips.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/battle/battle_assets/journal.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'bower_components/mali-lib/dist/mali-lib.js', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/default.res.json', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/loading/bar.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/loading/barBg.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/loading/loadingBg.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/loading/FX.json', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/loading/FX.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/loading/miniLoadingBg.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/loading/miniLoadingBar.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/loading/smallLoadingBg.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/loading/smallLoading.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/loading/smallLoading.json', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/loading/bar1Bg.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/loading/loading1Bg.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/default.thm.json', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/common/common.json', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/common/common.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Accept-Encoding', 'identity;q=1, *;q=0'), NVPair('Range', 'bytes=0-'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/sounds/bgm000.mp3', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Accept-Encoding', 'identity;q=1, *;q=0'), NVPair('Range', 'bytes=0-'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/sounds/start.mp3', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/world/worldMap.json', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/world/worldMap.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/explore/tollgateBtn.json', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/explore/tollgateBtn.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        ## statusCode[0]代表http code < 300 个数,    statusCode[1] 代表 300<=http code<400 个数
        # statusCode[2]代表400<=http code<500个数，  statusCode[3] 代表 http code >=500个数
        # 如果http code 300 到 400 之间是正常的
        # 那么判断事务失败，请将statusCode[1:3] 改为   statusCode[2:3] 即可
        if(sum(statusCode[1:3]) > 20):
            PTS.Data.forCurrentTest.success = False
            PTS.Logger.error(u'事务请求中http 返回状态大于300，请检查请求是否正确!')

        return statusCode


    ## action2
    def action2(self):
        statusCode = [0L, 0L, 0L, 0L]    

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/battle/star_anim/star_3.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/battle/star_anim/star_1.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/battle/star_anim/star_2.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/battle/star_anim/star_1.json', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/battle/star_anim/star_2.json', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/battle/star_anim/star_3.json', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/battle/star_anim/fullstar_effect/fullstar_effect.json', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/tpls/SpellPaletteEntryPopover.tpl', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/tpls/SimplePaletteTip.tpl', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/tpls/OpentipsTemplate.tpl', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/role/icon_head_1.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/role/icon_head_2.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/battle/battle.json', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/equipment/equipment.json', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/battle/battle.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/equipment/equipment.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/battle/battle_assets/fullHover_C.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/equipment/highLight.json', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/equipment/highLight.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/battle/star_anim/fullstar_effect/fullstar_effect.json', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/battle/star_anim/fullstar_effect/fullstar_effect.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/common/common_assets/btncommon4_disabled.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/common/common_assets/btncommon_AlreadyReceive_up-.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/common/common_assets/btncommon_Battle_down.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/common/common_assets/btncommon_Battle_over.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/common/common_assets/btncommon_Battle_up.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/common/common_assets/btncommon_NotReached.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/common/common_assets/btncommon_Receive_down.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/common/common_assets/btncommon_Receive_over.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/common/common_assets/btncommon_Receive_up.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/common/common_assets/btncommon_Restart_down.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/common/common_assets/btncommon_Restart_over.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/common/common_assets/btncommon_Restart_up.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/main_tool_btns/btn_frame_highlight.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/main_tool_btns/achievement_image_over.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/main_tool_btns/achievement_image_up.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/main_tool_btns/mall_image_over.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/main_tool_btns/mall_image_up.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/main_tool_btns/setting_image_over.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/main_tool_btns/setting_image_up.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/main_tool_btns/warrior_image_over.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/main_tool_btns/warrior_image_up.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene.json', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/common_utils/common_utils.json', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/common_utils/common_utils.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/diamond_icon.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/header_line.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/main_scene_bg.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/return_normal.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/return_selected.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/util_frame_big.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/vigor_icon.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/gamefeature_btn/campaign_word_normal_1.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/gamefeature_btn/campaign_word_normal_2.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/gamefeature_btn/campaign_word_normal_3.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/gamefeature_btn/campaign_word_normal_4.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/gamefeature_btn/campaign_word_normal_5.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/gamefeature_btn/campaign_word_selected_1.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/gamefeature_btn/campaign_word_selected_2.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/gamefeature_btn/campaign_word_selected_3.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/gamefeature_btn/campaign_word_selected_4.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/gamefeature_btn/campaign_word_selected_5.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/gamefeature_btn/gamefeature_disabled.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/gamefeature_btn/gamefeature_display_normal_1.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/gamefeature_btn/gamefeature_display_normal_2.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/gamefeature_btn/gamefeature_display_normal_3.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/gamefeature_btn/gamefeature_display_selected_1.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/gamefeature_btn/gamefeature_display_selected_2.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/gamefeature_btn/gamefeature_display_selected_3.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/gamefeature_btn/gamefeature_frame_normal.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/gamefeature_btn/gamefeature_frame_normal_gray.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/gamefeature_btn/gamefeature_frame_selected.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/gamefeature_btn/gamefeature_header_normal.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/gamefeature_btn/gamefeature_header_selected.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/battle_scene/battle_scene.json', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/battle_scene/battle_scene_assets/method_default.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/buybtn_selected.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/main_scene/main_scene_assets/buybtn_normal.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/game/battle_scene/battle_scene.png', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('X-Requested-With', 'XMLHttpRequest'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'auth/whoami?_=1478496434409', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)

        headers = [ NVPair('Accept', '*/*'), NVPair('X-Requested-With', 'XMLHttpRequest'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Encoding', 'gzip, deflate, sdch'), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'db/campaign?project=name%2CfullName%2Cdescription%2Cslug%2Ci18n%2Clevels&_=1478496434410', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)


        headers = [ NVPair('Accept', '*/*'), NVPair('Accept-Encoding', 'identity;q=1, *;q=0'), NVPair('Range', 'bytes=6604461-'), NVPair('Referer', TestRunner.game_host_url), NVPair('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'), NVPair('User-Agent', 'PTS-HTTP-CLIENT'), ]
        result = HTTPRequest().GET(TestRunner.game_host_url + 'resource/sounds/bgm000.mp3', None, headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)


        ## statusCode[0]代表http code < 300 个数,    statusCode[1] 代表 300<=http code<400 个数
        # statusCode[2]代表400<=http code<500个数，  statusCode[3] 代表 http code >=500个数
        # 如果http code 300 到 400 之间是正常的
        # 那么判断事务失败，请将statusCode[1:3] 改为   statusCode[2:3] 即可
        if(sum(statusCode[2:3]) > 20):
            PTS.Data.forCurrentTest.success = False
            PTS.Logger.error(u'事务请求中http 返回状态大于300，请检查请求是否正确!')

        return statusCode

# 编织压测事务
PTS.Framework.instrumentMethod(u'action1', 'action1', TestRunner)
PTS.Framework.instrumentMethod(u'action2', 'action2', TestRunner)