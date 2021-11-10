# HTest框架

把HTest文件夹复制到本电脑所安装的对应版本的python目录下

在被测项目下创建相对应的文件目录，参考setting.py或者content/项目目录.png



>编写yaml测试用例的方法

1,  首先，在HTest中修改setting文件，设置测试项目的绝对路径、url地址和被测用例的步骤和数据地址

2,  然后，在step目录下新增一个测试用例的步骤，参考content/step.png

3,  接着，在case目录下新增一个测试用例，参考content/case.png

4,  最后，在suit目录下新增本次需要测试的用例集，参考content/suit.png

5,  执行方法: python3 -m HTest login_suit.yml


