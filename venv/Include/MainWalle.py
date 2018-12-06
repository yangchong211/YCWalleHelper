# -*-coding:utf-8-*-
import os
import sys
import Config
import platform
import shutil

# /**
#  * <pre>
#  *     @author yangchong
#  *     blog  : https://github.com/yangchong211
#  *     time  : 2017/8/9
#  *     desc  : 自动化python脚本多渠道加固打包工具
#  *     revise: 最新代码更新于2018年10月30日
#  * </pre>
#  */


# 这里是获取encoding，一般是utf-8
if sys.stdout.encoding != 'UTF-8':
    print('sys.stdout.encoding != UTF-8')
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
if sys.stderr.encoding != 'UTF-8':
    print('sys.stderr.encoding != UTF-8')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
print('yc---sys.stdout.encoding-----' + sys.stdout.encoding)
print('yc---sys.stdout.encoding-----' + sys.stderr.encoding)

# 这里是调用Config配置里面的信息，包括keystore路径，密码等信息
keystorePath = Config.keystorePath
keyAlias = Config.keyAlias
keystorePassword = Config.keystorePassword
keyPassword = Config.keyPassword
if os.access(keystorePath, os.F_OK):
    print('yc---keystorePath---文件已经存在--' + keystorePath)
else:
    print('yc---keystorePath---文件已经不存在--请确认是否有keystore')
    exit(0)
print('yc---keystorePath-----' + keystorePath)
print('yc---keyAlias-----' + keyAlias)
print('yc---keystorePassword-----' + keystorePassword)
print('yc---keyPassword-----' + keyPassword)
if len(keystorePath) <= 0:
    print("keystorePath地址不能为空")
    exit(0)
if len(keyAlias) <= 0:
    print("keyAlias不能为空")
    exit(0)
if len(keystorePassword) <= 0:
    print("keystorePassword不能为空")
    exit(0)
if len(keyPassword) <= 0:
    print("keyPassword不能为空")
    exit(0)


# 获取脚本文件的当前路径
def curFileDir():
    # 获取脚本路径
    path = sys.path[0]
    # 判断为脚本文件还是py2exe编译后的文件，
    # 如果是脚本文件，则返回的是脚本的目录，
    # 如果是编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)


# 兼容不同系统的路径分隔符
def getBackslash():
    # 判断当前系统
    if 'windows' in platform.system().lower():
        return "\\"
    else:
        return "/"


# 当前脚本文件所在目录
parentPath = curFileDir() + getBackslash()
print('yc---parentPath当前脚本文件所在目录-----' + parentPath)

# 这里是获取lib的路径，主要是获取lib目录下的文件路径，包含签名和瓦力路径
libPath = parentPath + "lib" + getBackslash()
print('yc---libPath-----' + libPath)
buildToolsPath = Config.sdkBuildToolPath + getBackslash()
print('yc---buildToolsPath-----' + buildToolsPath)
# 获取lib下签名jar的路径
checkAndroidV2SignaturePath = libPath + "CheckAndroidV2Signature.jar"
print('yc---获取lib下签名jar的路径-----' + checkAndroidV2SignaturePath)
# 获取lib下瓦力打包jar的路径
walleChannelPath = libPath + "walle-cli-all.jar"
print('yc---获取lib下瓦力打包jar的路径-----' + walleChannelPath)

# 这里是自定义输入路径

channelsOutputFilePath = parentPath + "output"
print('yc---channelsOutputFilePath-----' + channelsOutputFilePath)
# 这里是获取多渠道打包配置信息
channelFilePath = parentPath + "apk" + getBackslash() + "channel"
print('yc---channelFilePath-----' + channelFilePath)
# 这里是获取加固后源文件的路径
protectedSourceApkPath = parentPath + "apk" + getBackslash() + Config.protectedSourceApkName
print('yc---protectedSourceApkPath-----' + protectedSourceApkPath)
if os.access(protectedSourceApkPath, os.F_OK):
    print('yc---protectedSourceApkPath---apk已经存在--' + protectedSourceApkPath)
else:
    print('yc---protectedSourceApkPath---apk已经不存在--请确认根目录下的apk文件夹中是否有apk')
    exit(0)

# 检查自定义路径，并作替换
if len(Config.protectedSourceApkDirPath) > 0:
    protectedSourceApkPath = Config.protectedSourceApkDirPath + getBackslash() + Config.protectedSourceApkName
    print('yc---protectedSourceApkPath-----' + protectedSourceApkPath)
if len(Config.channelsOutputFilePath) > 0:
    channelsOutputFilePath = Config.channelsOutputFilePath
    print('yc---channelsOutputFilePath-----' + channelsOutputFilePath)
if len(Config.channelFilePath) > 0:
    channelFilePath = Config.channelFilePath
    print('yc---channelFilePath-----' + channelFilePath)


def copyFile(srcFile, dstFile):
    shutil.copyfile(srcFile, dstFile)  # 复制文件


# 定义签名apk路径，如果文件不是_aligned.apk后缀名
if protectedSourceApkPath.find("_aligned.apk"):
    print('yc---protectedSourceApkPath-----' + protectedSourceApkPath)
    zipalignedApkPath = protectedSourceApkPath
    signedApkPath = zipalignedApkPath[0: -4] + "_signed.apk"
    copyFile(zipalignedApkPath, signedApkPath)
else:
    zipalignedApkPath = protectedSourceApkPath[0: -4] + "_aligned.apk"
    print('yc---zipalignedApkPath-----' + zipalignedApkPath)
    copyFile(protectedSourceApkPath, zipalignedApkPath)
    signedApkPath = zipalignedApkPath[0: -4] + "_signed.apk"
    print('yc---signedApkPath-----' + signedApkPath)
    copyFile(zipalignedApkPath, signedApkPath)


# 清空临时资源
def cleanTempResource():
    try:
        # os.remove(zipalignedApkPath)
        os.remove(signedApkPath)
        pass
    except Exception as e:
        # 如果异常则打印日志
        print(e)
        pass


# 清空渠道信息
def cleanChannelsFiles():
    try:
        os.makedirs(channelsOutputFilePath)
        pass
    except Exception as e:
        # 如果异常则打印日志
        print(e)
        pass


# 创建Channels输出文件夹
def createChannelsDir():
    try:
        os.makedirs(channelsOutputFilePath)
        pass
    except Exception as e:
        print(e)
        pass


# 清除所有output文件夹下的文件
def delFile(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)


# 先清除之前output文件夹中所有的文件
if len(Config.channelsOutputFilePath) > 0:
    delFile(channelsOutputFilePath)
# 创建Channels输出文件夹
createChannelsDir()
# 清空Channels输出文件夹
cleanChannelsFiles()

# 对齐
zipalignShell = buildToolsPath + "zipalign -v 4 " + protectedSourceApkPath + " " + zipalignedApkPath
print('yc---zipalignShell-----' + zipalignShell)
os.system(zipalignShell)

# 签名
signShell = buildToolsPath + "apksigner sign --ks " + keystorePath + " --ks-key-alias " \
            + keyAlias + " --ks-pass pass:" + keystorePassword + " --key-pass pass:" \
            + keyPassword + " --out " + signedApkPath + " " + zipalignedApkPath
print('yc---signShell-----' + signShell)
os.system(signShell)

# 检查V2签名是否正确
checkV2Shell = "java -jar " + checkAndroidV2SignaturePath + " " + signedApkPath
print('yc---checkV2Shell-----' + signShell)
os.system(checkV2Shell)

# 写入渠道
if len(Config.extraChannelFilePath) > 0:
    writeChannelShell = "java -jar " + walleChannelPath + " batch2 -f " \
                        + Config.extraChannelFilePath + " " + signedApkPath + " " + channelsOutputFilePath
else:
    writeChannelShell = "java -jar " + walleChannelPath + " batch -f " + channelFilePath + " " \
                        + signedApkPath + " " + channelsOutputFilePath
print('yc---writeChannelShell-----' + writeChannelShell)
os.system(writeChannelShell)

# 清空临时资源
cleanTempResource()

print("\n**** =============================执行完成=================================== ****\n")
print("\n↓↓↓↓↓↓↓↓  Please check output in the path   ↓↓↓↓↓↓↓↓\n")
print("\n" + channelsOutputFilePath + "\n")
print("\n↓↓↓↓↓↓↓↓  哥们，使用方便的话转发起来吧！杨充就此谢过！ ↓↓↓↓↓↓↓↓\n")
print("\n**** =============================执行完成=================================== ****\n")
