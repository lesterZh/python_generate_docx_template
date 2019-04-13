import wx


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(200, 300))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        p = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        l1 = wx.StaticText(p, label="Enter a number", style=wx.ALIGN_CENTRE)
        vbox.Add(l1, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 20)
        b1 = wx.Button(p, label="Btn1")
        vbox.Add(b1, 0, wx.EXPAND)

        b2 = wx.Button(p, label="Btn2")
        vbox.Add(b2, 0, wx.ALIGN_CENTER_HORIZONTAL)
        t = wx.TextCtrl(p)
        vbox.Add(t, 1, wx.EXPAND, 10)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        l2 = wx.StaticText(p, label="Label2", style=wx.ALIGN_CENTRE)

        hbox.Add(l2, 0, wx.EXPAND)
        b3 = wx.Button(p, label="Btn3")
        hbox.AddStretchSpacer(1)
        hbox.Add(b3, 0, wx.ALIGN_LEFT, 20)
        vbox.Add(hbox, 1, wx.ALL | wx.EXPAND)
        p.SetSizer(vbox)


app = wx.App()
Example(None, title='BoxSizer Demo - www.yiibai.com')
app.MainLoop()
