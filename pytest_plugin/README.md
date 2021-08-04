作业要求
编写一个插件
1.创建一个日志的实例，定义好日志的格式，将日志保存到项目目录下的logs/ 目录下
2.改写编码格式，支持中文
3.打包

打包步骤
需要的两个工具:
pip install setuptools
pip install wheel

打包命令：对包含setup.py目录打包，setup.py可以理解为打包配置文件
python setup.py sdist bdist_wheel

发布需要工具：
python3 -m pip install --upgrade twine

发布到pypi,需要注册账号
python3 -m twine upload --repository testpypi dist/*