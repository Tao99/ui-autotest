# HTest框架

把HTest文件夹复制到本电脑所安装的对应版本的python目录下

cp ./HTest /usr/lib/python3.7/

在被测项目Project下创建相对应的文件目录，参考HTest/content/项目目录.png



>编写yaml测试用例的方法

1,  首先，在HTest中修改setting文件，设置测试项目的绝对路径、url地址和用例

2,  然后，在step目录下新增一个用例步骤，参考HTest/content/step.png

3,  接着，在case目录下新增一个测试用例，参考HTest/content/case.png

4,  最后，在suit目录下新增本次需要测试的用例集，参考HTest/content/suit.png

5,  执行方法: python3 -m HTest login_suit.yml


