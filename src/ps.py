import wx
msg='fd'
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
mytest = ErrorFileDlg(redirect=False) 
mytest.MainLoop() 
