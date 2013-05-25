import wx
import thread
import time

class TestFrame(wx.Frame):
    def __init__(self):
        self.content=""
        wx.Frame.__init__(self, parent = None, id = -1, title = "Testing", pos=(350, 110), size=(450,600), style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX)
        panel = wx.Panel(self)

        self.StartButton = wx.Button(parent = panel, id = -1, label = "Start", pos = (110, 17), size = (50, 20))
        self.MultiLine = wx.TextCtrl(parent = panel, id = -1, pos = (20, 50), size = (410, 500), style = wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_AUTO_URL)

        self.Bind(wx.EVT_BUTTON, self.OnStart, self.StartButton)

    def OnStart(self, event):
        self.StartButton.Disable()
        thread.start_new_thread(self.LongRunning, ())

    def LongRunning(self):
        Counter = 1
        content=""
        while True:
            
            self.MultiLine.AppendText("Hi," + str(Counter) + "\n")
            #content = content +"Hi"+str(Counter)+"\n"
            #self.MultiLine.ChangeValue(content)
            #self.content =self.content + "Hi "+str(Counter) +"\n"
            self.MultiLine.ScrollLines(1)
            #l_cnt=self.MultiLine.
            #self.MultiLine.ScrollLines(-1)

            #self.MultiLine.Refresh(self.content)
            Counter = Counter + 1
            
            time.sleep(1)


class TestApp(wx.App):
    def OnInit(self):
        self.TestFrame = TestFrame()
        self.TestFrame.Show()
        self.SetTopWindow(self.TestFrame)
        return True

def main():
    App = TestApp(redirect = False)
    App.MainLoop()

if __name__ == "__main__":
    main()