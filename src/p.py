import wx
import subprocess

ip = "sina.com"
proc = subprocess.Popen("ping %s" % ip, shell=True,
                        stdout=subprocess.PIPE)
print
while True:
    line = proc.stdout.readline()
    wx.Yield()
    if line.strip() == "":
        pass
    else:
        print line.strip()
    if not line: break
proc.wait()