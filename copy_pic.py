import shutil
import os

"""
封装功能模块API：拷贝图片数据到指定路径的文件夹下
author:GriffinChou
date:2021.01.06
"""
def copy_pics():
    file_path = "E:/test_pic/"    #指定要复制的文件路径
    dst_path = 'E:/test/test_copy'+'/'    #指定存放路径
    file_list = [file for file in os.listdir(file_path)]    #第一，获取要拷贝的文件列表
    for i in range(len(os.listdir(file_path))):         #获取目录长度并获取图片
        new_file = file_path +file_list[i]          #拼接成新文件
        shutil.copy(new_file,dst_path)        # 第二，将名称为new_file的文件复制到名为dst_path的文件夹中

copy_pics()