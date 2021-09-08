#!/usr/bin/evn python
# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='pytest_log_plugin',
    url='https://github.com/xxx/pytest-log',
    version='1.0',
    author="zhihuan",
    author_email='xxx@qq.com',
    description='set your encoding and logger',
    long_description='Show Chinese for your mark.parametrize(). Define logger variable for getting your log',
    classifiers=[  # 分类索引 ，pip 对所属包的分类
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.8',
    ],
    license='proprietary',
    packages=find_packages(),
    keywords=[
        'pytest', 'py.test', 'pytest_log',
    ],
    # 需要安装的依赖
    install_requires=[
        'pytest'
    ],

    # 加载这个包下的ini文件，如果不是写着ini文件中，需要定义入口函数(pytest_log_plugin = pytest_log_plugin.main)
    entry_points={
        'pytest11': [
            'pytest_log_plugin = pytest_log_plugin',
        ]
    },
    zip_safe=False
)