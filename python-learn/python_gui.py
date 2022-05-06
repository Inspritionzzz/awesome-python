import wx

def call_func(event):
    # print("click")
    v = txt.GetValue()
    # txt.SetValue("默认值")
    print(v)

def open_dir(event):
    print("todo open_dir()")
    dialog = wx.DirDialog(None, "选择文件夹")
    if dialog.ShowModal()==wx.ID_OK:
        # print("OK")
        txt2.SetValue(dialog.GetPath())
    dialog.Destroy()

def bat_run(event):
    pass

app = wx.App()
frame = wx.Frame(None, title="first gui", size=(500, 300))

txt = wx.TextCtrl(frame, pos=(10, 10), size=(250, 25))  # 获取文本输入
btn1 = wx.Button(frame, label="打开源文件夹", pos=(270, 10), size=(100, 25))
btn1.Bind(wx.EVT_BUTTON, call_func)

txt2 = wx.TextCtrl(frame, pos=(10, 40), size=(250, 25))
btn2 = wx.Button(frame, label="打开目标文件夹", pos=(270, 50), size=(100, 25))
btn2.Bind(wx.EVT_BUTTON, open_dir)

btn3 = wx.Button(frame, label="开始处理", pos=(150, 90), size=(100, 25))
btn3.Bind(wx.EVT_BUTTON, bat_run)

frame.Show()
app.MainLoop()


