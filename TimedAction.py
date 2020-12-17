import time
import keyboard
import wx
import wx.adv
from wx import Panel

pressed = False

class MyFrame(wx.Frame):
    def __init__(self):

        self.pressed = False

        super().__init__(parent=None, title='Timed Action')
        panel: Panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)

        self.banner = wx.adv.BannerWindow(panel,dir=wx.TOP)
        self.banner.SetText("Time to deliver:", "(00:00 - 24:59)")
        my_sizer.Add(self.banner, 0, wx.ALL | wx.EXPAND, 5)

        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        self.banner2 = wx.adv.BannerWindow(panel, dir=wx.TOP)
        self.banner2.SetText("What to press:", "(add space in between every letter, and not for enter & such)")
        my_sizer.Add(self.banner2, 0, wx.ALL | wx.EXPAND, 5)

        self.text_ctrl2 = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl2, 0, wx.ALL | wx.EXPAND, 5)



        my_btn = wx.Button(panel, label='Submit')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def on_press(self, event):
        if self.pressed == False:
            self.pressed = True
            value = str(self.text_ctrl.GetValue())
            value2 = str(self.text_ctrl2.GetValue())
            if value:

                t = time.localtime()
                current_time = time.strftime("%H:%M", t)
                while current_time != value:

                    t = time.localtime()
                    current_time = time.strftime("%H:%M", t)
                    time.sleep(30)
                else:
                    for word in value2.split():
                        keyboard.press_and_release(word)

                    self.pressed = False


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()