# Auto SSG

**自动私立炽天使学园**(Auto Shiritsu Seraphim Gakuen)是基于python/ADB，面向游戏Heaven burns red（HBR，绯染天空，炽焰天穹）的自动化工具。

基础工具包含调用ADB指令，调用openCV的模式识别功能，以及一些预制脚本（自用的）。同时也支持通过无代码/低代码的方式编写新的执行脚本。还可以通过较为简易的方式为工具添加特性或替换部分功能。

*目前该项目仍在龟速更新中，可能出现任何意想不到的bug，如果使用该项目导致未知且不可回退的后果发生，该项目不负任何责任。*

*目前全部用于模式匹配的图片素材都采集自繁中版本，存在潜在的对其他语言版本不兼容的现象，如需在日文版本或者国服的App上运行，可以自行截图替换素材或尝试降低模式匹配的阈值。*

## 安装

1. 安装python3.9及以上版本，个人推荐使用conda虚拟环境。

~~~shell
conda create -n AutoSSG python=3.9
conda activate AutoSSG
~~~

2. 手动安装依赖。*如果您对python不熟悉或者不在意代码污染您的python环境，您可以跳过这步，程序会自动帮您安装*

~~~shell
pip install yaml
pip install numpy
pip install matplotlib
pip install opencv-python
~~~

## 填写配置

`./assert/config`是默认的存档目录，需要根据自身情况更改/创建配置

```yaml
'name': 配置名称，任意
'adb_path': ADB安装位置，如：'./ADB.exe'（可查询各模拟器的官方说明）
'device_addr': ADB网络ip以及端口，如：'127.0.0.1:16384'（可查询各模拟器的官方说明）
'screen_resolution': 模拟器分辨率，如：[ 1600,900 ]
'app_rotation': 90 屏幕旋转，固定取90（默认横屏）或0（默认竖屏），极不建议随意修改

'resource_dir': './assert/resource'，脚本图像等资源的存放文件夹，不建议修改
'resource_record_size': [ 1600,900 ]，图片资源采集时，模拟器窗口的分辨率，无需要不建议修改
'max_io_buffer': 64，资源IO的缓冲最大容量，不懂可以不改，实际上也基本没加速IO（
```

## 使用脚本

*目前版本本工具没有GUI，长期内也没有实现GUI的打算*

to be updated

## 脚本编写

[脚本编写指南](old_data/framework/doc/script_guider.md)

## 开发者指南

[开发者指南](old_data/framework/doc/devlop_guider.md)

## 更新路线

本项目纯属本科研民工逃避现实+电子ED的产物，更新频率可能会很低

本项目将会以如下线路龟速更新:

1. 可读性更高，更方便的脚本编写 （优先）
2. 完善未实现的脚本处理逻辑（高）
3. CLI编写（中）
4. 更多脚本（随缘）

## 鸣谢
感谢我的导师，多亏导师给了我现在这个课题，不然我也不会想着逃避现实来写这个项目（

## 赞助作者

赞助作者是作者更新的最大动力（吗？），如果您喜欢本项目，您可以选择如下几种赞助方式：

1. 将皮蛋煮熟，晾凉后去壳，切成小块备用。准备葱花，按照个人口味加入适量生抽、盐和香油，搅拌均匀。
2. 灌注Red Crimson喵，灌注Red Crimson谢谢喵
3. 在Nature或Science上发表一篇关于Flat Hand的论文，调研为什么手子哥温暖的大手这么社。
4. 在飞机社的人气投票上为人气角色“沙海中蠢動的歌女”投上真爱票，助力飞机社早日为她献上婚纱换皮。
