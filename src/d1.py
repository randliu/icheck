import wx
import thread
import time

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent = None, id = -1, title = "Testing", pos=(350, 110), size=(490,530), style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX)
        panel = wx.Panel(self)

        self.StartButton = wx.Button(parent = panel, id = -1, label = "Start", pos = (110, 17), size = (50, 20))
        self.MultiLine = wx.TextCtrl(parent = panel, id = -1, pos = (38, 70), size = (410, 90), style = wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_AUTO_URL)

        self.Bind(wx.EVT_BUTTON, self.OnStart, self.StartButton)

    def OnStart(self, event):
        self.StartButton.Disable()
        thread.start_new_thread(self.LongRunning, ())

    def LongRunning(self):
        Counter = 1
        while True:
            self.MultiLine.AppendText("Hi," + str(Counter) + "\n")
            Counter = Counter + 1
            time.sleep(2)


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