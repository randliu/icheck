#!/usr/bin/env python
#coding=utf-8


# command:指定事件处理函数
import sys
import os
import wx 

basic_info={}
msg=u"请指定一个.apk文件"
import thread
import time

class RedirectText(object):
    def __init__(self,aWxTextCtrl):
        self.out=aWxTextCtrl
 
    def write(self,string):
        self.out.WriteText(string)
        
class LogFrame(wx.Frame):
 
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "wxPython Redirect Tutorial")
 
        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        log = wx.TextCtrl(panel, wx.ID_ANY, size=(300,100),
                          style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
        btn = wx.Button(panel, wx.ID_ANY, 'Push me!')
        self.Bind(wx.EVT_BUTTON, self.onButton, btn)
 
        # Add widgets to a sizer        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(log, 1, wx.ALL|wx.EXPAND, 5)
        sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizer(sizer)
 
        # redirect text here
        redir=RedirectText(log)
        sys.stdout=redir
 
    def onButton(self, event):        
        print "You pressed the button!"


class ErrorFileDlg(wx.App): 
    def OnInit(self): 
        global msg
        myResult = 0 
        myMessageBox = "" 

        myMessageBox = wx.MessageDialog(None, 
                                         msg, 
                                         "iCheck", 
                                          wx.OK | wx.ICON_QUESTION)
                                         
        myResult = myMessageBox.ShowModal() 
        return True 


base_dir="C:\\test\\"

pkg_type=""
pkg_name=""
full_name=""
file_name=""

def valid_filename():
    global basic_info
    global msg
    if len(sys.argv) !=2:
        return (False,msg)
    global full_name,file_name
    full_name= sys.argv[1]
    file_name = os.path.basename(full_name)
    basic_info['file_name'] = file_name
    basic_info['full_name'] = full_name
    
    ss= file_name.split(".apk")
    if len(ss) !=2 :
        return (False,msg)
    
    global pkg_type,pkg_name
    pkg_name=ss[0]
    pkg_type="apk"
    basic_info['pkg_type'] = pkg_type
    basic_info['pkg_name'] = pkg_name

    return (True,"OK")
"""
for arg in sys.argv:
    print arg
"""    

(result,info) = valid_filename()
if not result:
    mytest = ErrorFileDlg(redirect=False) 
    mytest.MainLoop() 
    os.sys.exit()

else:
    pass

#now to check work space 

print pkg_type
print pkg_name
work_dir="%s\\%s"%(base_dir,pkg_name)
print work_dir

basic_info['work_dir'] = work_dir
file_size=os.path.getsize(full_name)
unit = "K"
file_size = file_size>>10   # as K

if file_size > 1024:
    file_size =file_size >>10
    unit = "M"    
basic_info['file_size'] = "%d%s"%(file_size,unit)

import shutil
print work_dir
if os.path.exists(work_dir):
    #os.rmdir(work_dir)
    shutil.rmtree(work_dir)
#os.mkdir(work_dir)
app = wx.PySimpleApp()
frame = LogFrame().Show()
#app.MainLoop()

apktool_full_path="%s\\apktool.jar"%os.path.dirname(__file__)
#apktool_full_path="%s\\apktool.jar"%os.path.dirname(work_dir)
os.system("java -jar %s d %s"%(apktool_full_path,full_name))
#import zipfile
#unzip the pkg
#z = zipfile.ZipFile(full_name)

#z.extractall(work_dir)

#now to parse xml

print basic_info
