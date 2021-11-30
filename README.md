# HTest框架


下载安装：pip install HTest

> 使用方法：

（1）查看版本：HTest（htest或者hs）-v

（2）新建项目：hs -s 项目名

（3）帮助：hs -h


> 编写yaml测试用例的方法

1,  在step目录下新增一个测试步骤，参考HTest/content/step.png

2,  在case目录下新增一个测试用例，参考HTest/content/case.png

3,  在suit目录下新增一个测试用例集，参考HTest/content/suit.png


> 测试执行

1,  在HTest中修改setting文件，修改测试项目的绝对路径和用例名

2,  执行方法: python -m HTest login_suit.yml


