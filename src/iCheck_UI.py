#!/usr/bin/env python
#coding=utf-8
import wx
import os
import sys
import time

class LogFrame(wx.Frame):
    def __init__(self):
        self.content=""
        wx.Frame.__init__(self, parent = None, id = -1, title = "iCheck it!", pos=(350, 110), size=(450,600), style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX)
        panel = wx.Panel(self)

        #self.StartButton = wx.Button(parent = panel, id = -1, label = "Start", pos = (110, 17), size = (50, 20))
        self.MultiLine = wx.TextCtrl(parent = panel, id = -1, pos = (20, 50), size = (410, 500), style = wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_AUTO_URL)

        #self.Bind(wx.EVT_BUTTON, self.OnStart, self.StartButton)
        #self.LongRunning()


    def write_log(self,msg):
        self.MultiLine.AppendText(msg)
        self.ScrollLines(1)
        wx.Yield()
        
    def LongRunning(self,basic_info):
        Counter = 1
        full_name=basic_info['full_name']
        work_dir=basic_info['work_dir']
        
        import subprocess
        print (__file__)
        apktool_full_path="%s\\jar\\apktool.jar"%os.path.dirname(__file__)
        wx.Yield()
        time.sleep(1)
        self.write_log("Target APK:    %s\n"%full_name) 
        time.sleep(0)   
        self.write_log("Now to Decompile %s\n\n"%os.path.basename(full_name))
        cmd="java -jar %s  d -f %s %s\n\n"%(apktool_full_path,full_name,work_dir)
        print cmd
        self.write_log(cmd)
        proc = subprocess.Popen(cmd,shell=True,stderr=subprocess.PIPE)
        while True:
            line = proc.stderr.readline()
            
            if line.strip() == "":
                pass
            else:
                self.write_log(line)
                
            if not line: 
                self.write_log("Done!\n")
                time.sleep(1)
                break
            wx.Yield()
        #wx.App.ExitMainLoop(wx.GetApp())
        html =  "%s\Report\out.html"%os.path.dirname(__file__)
        time.sleep(1)
        #self.Destroy()
        #wx.GetApp().ExitMainLoop()
        #proc.wait()
        #sys.exit()




class ErrorFileDlg(wx.App): 
    def OnInit(self): 
        #global msg
        self.myResult = 0 
        #self.myMessageBox = "" 

        return True 
    def show_msg(self,msg):
        self.myMessageBox = wx.MessageDialog(None, 
                                         msg, 
                                         "iCheck", 
                                          wx.OK | wx.ICON_QUESTION)
                                         
        self.myResult = self.myMessageBox.ShowModal() 
