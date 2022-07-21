# 自动化瓦力多渠道打包python脚本
#### 目录介绍
- 1.本库优势亮点
- 2.使用介绍
- 3.注意要点
- 4.效果展示
- 5.大概步骤
- 6.其他介绍


### 0.首先看看我录制的案例演示
- 如下所示，这段python代码很简单，工具十分强大，一键多渠道打包工具。
    - ![image](https://github.com/yangchong211/YCWalleHelper/blob/master/walle.gif)


### 1.本库优势亮点
- 通过该自动化脚本，只需要run一下或者在命令行运行脚本即可实现美团瓦力多渠道打包，打包速度很快
- 配置信息十分简单，代码中已经注释十分详细。Keystore信息一定要配置，至于渠道apk输出路径，文件配置路径等均有默认路径，不配置也没关系
- 如果输出路径是根目录下的output文件夹，文件不存在则创建，文件存在则先删除之前多渠道打包生成的旧文件【也就是删除output文件夹下所有文件】，然后再重新生成
- 多种分发渠道是在channel这个文件中定义，建议是txt文件格式，你可以根据项目情况修改，十分快捷
- 如果瓦力打包工具更新了，直接替换一下lib中的jar即可。可以在python3.x上跑起来！
- 我也参考了大量的博客，网上博客很多，我始终觉得对于这种实操性很强的案例，还是博客和项目一起学习才效果更好。感谢无数的前辈大神！


### 2.使用介绍
- 第一步：准备基础的文件
    - 准备apk文件
		- 对于未签名：将你未加固的apk文件，keystore，已经需要多渠道配置信息的channel放到指定的"apk"文件夹中
		- 对于已加固：将你加固好的apk文件，已经需要多渠道配置信息的channel放到指定的"apk"文件夹中
    - 初步建议，如果你想自定义存放文件的路径，可以先熟悉一下python的代码再做修改，也没有什么难度
- 第二步：配置Config.py文件中的属性
    - 配置keystore信息，这个地方引用你的keystore信息，对于已经加固的apk可以直接过
    ```
    # keystore信息，这个是针对未加固的，如果已经加固则不需要配置
    # Windows 下路径分割线请注意使用\\转义
    keystorePath = "D:\\GitHub\\YCWalleHelper\\venv\\Include\\apk\\ycPlayer.jks"
    keyAlias = "yc"
    keystorePassword = "19930211"
    keyPassword = "19930211"
    ```
    - 配置其他信息，比如apk的名称，渠道包配置路径，输出路径等等
    ```
    # 加固后的源文件名（未重签名）
    # 必须要配置
    protectedSourceApkName = "app_release.apk"
    
    # 下面这些可以不用配置，代码中会有默认的值
    # 加固后的源文件所在文件夹路径(...path),注意结尾不要带分隔符，默认在此文件夹根目录
    protectedSourceApkDirPath = ""
    # 渠道包输出路径，默认在此文件夹output目录下
    channelsOutputFilePath = ""
    # 渠道名配置文件路径，默认在此文件夹apk目录下
    channelFilePath = ""
    # 额外信息配置文件（绝对路径）
    # 配置信息示例参看，默认是此文件夹apk目录下
    extraChannelFilePath = ""
    
    # Android SDK buidtools path , please use above 25.0+
    # 必须配置，需要用到zipalign
    sdkBuildToolPath = "D:\\Program File\\AndroidSdk\\build-tools\\28.0.3"
    ```
- 第三步：直接运行
    - 第一种方式是通过PyCharm工具运行，这个直接run就可以呢。程序员建议使用这种！
    - 第二种方式是通过命令行运行，就可以实现自动化打包
    ```
	//已经加固：运行这个使用到校验签名，以及瓦力多渠道输出
	python mian.py
	
	//未签名：运行这个使用到命令行签名，校验签名，以及瓦力多渠道输出
        python MainWalle.py
    ```
- 第四步：修改多渠道配置信息
    - 直接找到channel文件，进行修改即可，注意格式！
    ```
    360 #360
    91anzhuo # 91安卓
    anzhuo # 安卓
    baidu # 百度
    wandoujia # 豌豆荚
    xiaoyangdoubi  #小杨逗比
    yingyongbao # 应用宝
    ```


### 3.注意要点
#### 3.1 注意在apk目录中一定要放入channel，keystore，还有加固的apk文件
- channel是指指定多渠道信息
- keystore是指你要签名的apk的钥匙
- apk是指你需要进行多渠道打包的加固文件。注意apk文件名称要和Config配置的apk名称要一致。
![image](https://upload-images.jianshu.io/upload_images/4432347-3a913bde5954e050.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



#### 3.2 配置keystore信息需要注意的问题
- 主要是注意路径是全路径
    ```
    # keystore信息
    # Windows 下路径分割线请注意使用\\转义
    keystorePath = "D:\\GitHub\\YCWalleHelper\\venv\\Include\\apk\\ycPlayer.jks"
    keyAlias = "yc"
    keystorePassword = "19930211"
    keyPassword = "19930211"
    ```

#### 3.3 注意apk下存放的apk文件名称和Config.py中配置的apk名称要相同
- 看下面这个截图
    - ![image](https://upload-images.jianshu.io/upload_images/4432347-4dc2070255be196c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


#### 3.4 关于部分疑问问题
- 关于Config.py中的sdkBuildToolPath，建议和你使用studio的版本保持一致，需要用到zipalign。别忽略这种小的问题！
- 注意如果要配置定义路径等属性，由于编码格式为UTF-8，所以不要带异常字符
- 多渠道打包时，如果要修改多渠道信息，直接修改channel文件，这个channel文件请不要修改成其他的名称！


### 4.效果展示
- 如图所示，建议你亲自尝试一下，特别好玩！
    - ![image](https://upload-images.jianshu.io/upload_images/4432347-24c01dbbf68d1166.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


### 5.大概步骤
- python脚步指令步骤：
	- 5.1 首先获取配置信息，配置信息里主要包括apk加固包，channel渠道文件，keyStroke文件
	- 5.2 获取v2检验签名，美团瓦力walle路径
	- 5.3 检查v2签名是否正确
	- 5.4 利用美团walle写入多渠道，参考美团瓦力命令行文档
- APK的生成步骤：
	- 1、打包资源文件，生成 R.java 文件
	- 2、处理 aidl 文件，生成相应 java 文件
	- 3、编译工程源代码，生成相应 class 文件
	- 4、转换所有 class 文件，生成 classes.dex 文件
	- 5、打包生成 apk
	- 6、对 apk 文件进行签名
	- 7、对签名的 apk 进行 zipalign 对其操作
- 关于命令行参考
	- [APK命令行实现V1、V2签名及验证](https://www.jianshu.com/p/e00f9bb12340)
	- [美团瓦力walle-cli](https://github.com/Meituan-Dianping/walle/blob/master/walle-cli/README.md)
	- [walle-cli](https://github.com/itgowo/walle-cli)
	- [瓦力多渠道打包原理](https://tech.meituan.com/2017/01/13/android-apk-v2-signature-scheme.html)


### 6.其他介绍
#### 关于其他内容介绍
![image](https://upload-images.jianshu.io/upload_images/4432347-7100c8e5a455c3ee.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



#### 其他推荐
- 博客笔记大汇总【15年10月到至今】，包括Java基础及深入知识点，Android技术博客，Python学习笔记等等，还包括平时开发中遇到的bug汇总，当然也在工作之余收集了大量的面试题，长期更新维护并且修正，持续完善……开源的文件是markdown格式的！同时也开源了生活博客，从12年起，积累共计47篇[近20万字]，转载请注明出处，谢谢！
- 链接地址：https://github.com/yangchong211/YCBlogs
- 如果觉得好，可以star一下，谢谢！当然也欢迎提出建议，万事起于忽微，量变引起质变！


#### 参考博客
- https://github.com/Meituan-Dianping/walle
- https://blog.csdn.net/ruancoder/article/details/51893879
- https://www.cnblogs.com/morang/p/python-build-android-apk.html
- https://www.jianshu.com/p/b5b4f7fc5264
- https://www.jianshu.com/p/20a62d1eba3f
- https://github.com/Jay-Goo/ProtectedApkResignerForWalle
- https://blog.csdn.net/u013692888/article/details/77933548
- https://blog.csdn.net/WHB20081815/article/details/89766471



#### 关于LICENSE
```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```



















