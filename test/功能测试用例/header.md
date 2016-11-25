<table  align="left">
    <thead>
        <tr><th>编号</th><th colspan="4">{{page.id}}</th></tr>
        <tr><th>名称</th><th colspan="4">{{page.name}}</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>版本</td><td>作者</td><td>日期</td><td>优先级</td><td>执行次序</td>
        </tr>
        <tr>
            <td>{{page.version}}</td><td>{{config.author}}</td><td>{{file.mtime|timeFormat('YYYY-MM-DD')}}</td><td>{{page.priority}}</td><td></td>
        </tr>
        <tr>
            <td>执行模式</td><td>执行者</td>
        </tr>
        <tr>
            <td>{{page.executing-mode}}</td><td>{{page.executer}}</td>
        </tr>
    </tbody>
</table>