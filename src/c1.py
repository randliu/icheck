import wx 

class test(wx.App): 

    def OnInit(self): 

         myResult = 0 
         myMessageBox = "" 

         myMessageBox = wx.MessageDialog(None, 
                                         "Yes or No.", 
                                         "test", 
                                         wx.YES_NO | wx.ICON_QUESTION) 

         myResult = myMessageBox.ShowModal() 

         return True 

mytest = test(redirect=False) 
mytest.MainLoop() 