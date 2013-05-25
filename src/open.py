#coding=utf-8

'''
Created on 2013-5-18

@author: 8000
'''
work_path="c:\\i_tmp"
import win32ui

dlg = win32ui.CreateFileDialog(1) # 1表示打开文件对话框
dlg.SetOFNInitialDir('E:/Python') # 设置打开文件对话框中的初始显示目录
dlg.DoModal()
 
fullname = dlg.GetPathName() # 获取选择的文件名称
print fullname





import os, zipfile

basename = os.path.basename(fullname)
print basename
import string
apk_name = string.split(basename,'.apk')[0]
print apk_name

apk_space="%s\\%s"%(work_path,apk_name)
try:
    os.unlink(apk_space)
except:
    pass
os.mkdir(apk_space)
z = zipfile.ZipFile(fullname)
z.extractall(apk_space)

print "end"
os.sys.exit()
