# 导入sciter支持,必须安装pysciter
import sciter
import ctypes
import json

# 设置dpi, 防止程序在高分屏下发虚
ctypes.windll.user32.SetProcessDPIAware(2)

class Frame(sciter.Window):
    def __init__(self):
        '''
            ismain=False, ispopup=False, ischild=False, resizeable=True,
            parent=None, uni_theme=False, debug=True,
            pos=None,  pos=(x, y)
            size=None
        '''
        super().__init__(ismain=True, debug=True)
        self.set_dispatch_options(enable=True, require_attribute=False)

    def clickMe(self):
        self.call_function('clickCallBack','你已经点到我了!')

if __name__ == '__main__':
    frame = Frame()
    frame.load_file("Gui/main.html")
    frame.run_app()
