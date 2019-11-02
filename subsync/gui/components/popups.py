import wx


class PopupInfoButton(wx.BitmapButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Bind(wx.EVT_BUTTON, self.onClick)
        self.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_TIP, wx.ART_BUTTON))
        self.message = None

    def onClick(self, event):
        if self.message:
            parent = self.GetParent()
            caption = self.GetLabel() or _('Info')
            with wx.MessageDialog(parent, self.message, caption) as dlg:
                dlg.ShowModal()
