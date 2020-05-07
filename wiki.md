#### 目录介绍
- 1.签名简单说明
- 2.实现多渠道打包的原理
- 3.美团多渠道打包



### 1.签名简单说明
- v1签名是对jar进行签名，V2签名是对整个apk签名
- 官方介绍就是：v2签名是在整个APK文件的二进制内容上计算和验证的，v1是在归档文件中解压缩文件内容。
- 二者签名所产生的结果： 
	- v1：在v1中只对未压缩的文件内容进行了验证，所以在APK签名之后可以进行很多修改——文件可以移动，甚至可以重新压缩。即可以对签名后的文件在进行处理 
	- v2：v2签名验证了归档中的所有字节，而不是单独的ZIP条目，如果您在构建过程中有任何定制任务，包括篡改或处理APK文件，请确保禁用它们，否则您可能会使v2签名失效，从而使您的APKs与Android 7.0和以上版本不兼容。


### 2.实现多渠道打包的原理
- 核心原理就是通过脚本修改androidManifest.xml中的mate-date内容，执行N次打包签名操作实现多渠道打包的需求。 
	- 一般来讲，这个渠道的标识会放在AndroidManifest.xml的Application的一个Metadata中。然后就可以在java中通过API获取对应的数据了。
- 原理：清单文件添加渠道标签读取对应值。打包后修改渠道值的两种方法
	- 第一种方法：通过ApkTool进行解包，然后修改AndroidManifest中修改渠道标示，最后再通过ApkTool进行打包、签名。
	- 第二种方法：使用AXML解析器axmleditor.jar，拥有很弱的编辑功能，工程中用来编辑二进制格式的 AndroidManifest.xml 文件.


### 3.美团多渠道打包
- 基于v2
	- Walle（瓦力）：Android Signature V2 Scheme签名下的新一代渠道包打包神器
- 整个APK（ZIP文件格式）会被分为以下四个区块：
	- Contents of ZIP entries（from offset 0 until the start of APK Signing Block）
	- APK Signing Block
	- ZIP Central Directory
	- ZIP End of Central Directory
- 原理：
	- 原理很简单，就是将渠道信息存放在APK文件的注释字段中。美团的打包方式非常快速，打渠道包几乎就只是进行一次copy apk文件。
 	- 瓦力通过在Apk中的APK Signature Block区块添加自定义的渠道信息来生成渠道包，从而提高了渠道包生成效率





