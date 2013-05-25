#!/usr/bin/env python
#coding=utf-8

import sys

import os
app_lib=os.path.dirname(__file__)+"\\..\\lib"
print "app_lib:"+app_lib
sys.path.append(app_lib)
import wx 
from iCheck_UI import *

basic_info={}
msg=u"请指定一个.apk文件"
import codecs

import thread
import time
import thread
import time
import shutil
import wx.html
from jinja2 import Environment
from jinja2.loaders import FileSystemLoader
pkg_info=None



#base_dir="C:\\test\\"
work_dir = "%s\\..\\apk_space"%os.path.dirname(__file__)
print "work_dir:"+work_dir
basic_info['work_dir']=work_dir
pkg_type=""
pkg_name=""
full_name=""
file_name=""



def valid_arg():
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
    basic_info['pkg_name'] = file_name
    basic_info['location'] = full_name
    basic_info['work_dir'] = basic_info['work_dir']+"\\"+pkg_name

    return (True,"OK")

class TestApp(wx.App):
    def OnInit(self):
        self.TestFrame = LogFrame()
        self.TestFrame.Show()
        #self.TestFrame.LongRunning(basic_info['full_name'],basic_info['work_dir'])
        self.TestFrame.LongRunning(basic_info)
        self.SetTopWindow(self.TestFrame)
        time.sleep(3)
        parse_AndroidManifest_xml(pkg_info['path_AndroidManifest_xml'])
        parse_strings_xml(pkg_info['path_string_xml'])
        
        render()
        print pkg_info
        
        import webbrowser 
        html =  "%s\\..\\Report\\out.html"%os.path.dirname(__file__)
        print html
        webbrowser.open(html)
        self.TestFrame.Destroy()
        wx.GetApp().ExitMainLoop()
        return True



def main():
    (result,info) = valid_arg()
    if not result:
        mytest = ErrorFileDlg(redirect=False) 
        #global msg
        mytest.show_msg(info)
        mytest.MainLoop() 
        os.sys.exit()
    global basic_info,pkg_info
    
    print pkg_type
    print pkg_name
    #work_dir="%s\\%s"%(base_dir,pkg_name)
    print work_dir
    basic_info['pkg_name'] = pkg_name
    #basic_info['work_dir'] = work_dir
    file_size=os.path.getsize(full_name)
    unit = "K"
    file_size = file_size>>10   # as K

    if file_size > 1024:
        file_size =file_size >>10
        unit = "M"    
    basic_info['file_size'] = "%d%s"%(file_size,unit)


    
    if os.path.exists(basic_info['work_dir']):
        #os.rmdir(work_dir)
        shutil.rmtree(basic_info['work_dir'])
    
    print basic_info
    path_AndroidManifest_xml = basic_info['work_dir']+"\\"+"AndroidManifest.xml"
    path_string_xml = basic_info['work_dir']+"\\res\\values\\"+"strings.xml"
    
    pkg_info=basic_info.copy()
    pkg_info['path_AndroidManifest_xml'] =path_AndroidManifest_xml
    pkg_info['path_string_xml'] =path_string_xml
    
    
    
    App = TestApp(redirect = False)
    
    App.MainLoop()
    
    

"""
for arg in sys.argv:
    print arg
"""    

from xml.dom import minidom
import string 

class permission:
    def __init__(self,name,protectionLevel):
        self.name=name
        self.protectionLevel=protectionLevel

def parse_AndroidManifest_xml(path_AndroidManifest_xml):
    global pkg_info
    xml = minidom.parse(path_AndroidManifest_xml)
    root = xml.documentElement
    
    pkg_info['package'] = root.getAttribute("package")
    #android:versionName
    pkg_info['versionName']=root.getAttribute("android:versionName")
    pkg_info['versionCode']=root.getAttribute("android:versionCode")
    #print dir(root)    
    #root    :    manifest
    uses_permission = []
    #print root.nodeName
    lev_1 =  root.getElementsByTagName("uses-permission")
    for node in lev_1:
        name= node.getAttribute("android:name")
        uses_permission.append(name)
    pkg_info['lst_uses_permission']=uses_permission
    pkg_info['len_lst_uses_permission']=len(uses_permission)
    #permission
    lst_permission = []
    #print root.nodeName
    lev_1 =  root.getElementsByTagName("permission")
    for node in lev_1:
        
        name= node.getAttribute("android:name")
        protectionLevel = node.getAttribute("android:protectionLevel")
        p=permission(name,protectionLevel)
        lst_permission.append(p)
    pkg_info['lst_permission']=lst_permission
    pkg_info['len_lst_permission']=len(lst_permission)

    node=root.getElementsByTagName("application")

    lst_uses_feature = []
    #print root.nodeName
    lev_1 =  root.getElementsByTagName("uses-feature")
    for node in lev_1:
        name= node.getAttribute("android:name")
        lst_uses_feature.append(name)
    pkg_info['lst_uses_feature']=lst_uses_feature
    pkg_info['len_lst_uses_feature']=len(lst_uses_feature)

    node=root.getElementsByTagName("application")[0]
    debuggable= node.getAttribute("android:debuggable")
    pkg_info['debuggable']=debuggable
    print pkg_info
    return True

import xml.dom


def get_text(node):
    children = node.childNodes
    rc=""
    for child in children:
        if child.nodeType == child.TEXT_NODE:
            rc=rc+ child.data
    return rc

def parse_strings_xml(path_string_xml):
    global pkg_info
    print "string xml:%s"%path_string_xml
    axml = minidom.parse(path_string_xml)
    resources = axml.documentElement
    #print resources.nodeName
    lst_string =  resources.getElementsByTagName("string")
    for node in lst_string:
        print node 
        #print "Element text:%s"% get_text(node)            
        if node.nodeType == xml.dom.Node.ELEMENT_NODE:
            #print 'Element name: %s' % node.nodeName
            for (name, value) in node.attributes.items():
                print '    Attr -- Name: %s  Value: %s' % (name, value)
                #name,value = node.attributes.items()
                #if string.strip(value,' ') == "app_name":
                
                if value == "app_name":
                    pkg_info['app_name']=get_text(node)
                    print "app_name:%s"%pkg_info['app_name']
                    return True
    print pkg_info
    return False




def getTitles(xml):
    """
    Print out all titles found in xml
    """
    doc = minidom.parse(xml)
    node = doc.documentElement
    books = doc.getElementsByTagName("string")
 
    for title in books:
        """
        nodes = title.childNodes
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                print node.data
        """
        print get_text(title)
def render():

    global basic_info
    global pkg_info
    p=basic_info['work_dir']+"\\..\\..\\"+"Report"
    print p
    env = Environment(loader=FileSystemLoader(p))

    tmpl = env.get_template('M.html')
    out=tmpl.render(seq=[3, 2, 4, 5, 3, 2, 0, 2, 1],pkg=pkg_info)
    #f = open(p+"\\"+"out.html","w")
    f=codecs.open(p+"\\"+"out.html", 'wb', 'utf-8')
    f.write(out)
    f.close

#if __name__ == '__main__':
#

main()  
    
    #print "hehe"
    #print work_dir
    
    #basic_info['apk_path']=basic_info['work_dir']


    

