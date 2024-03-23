import webview
import os
from time import sleep

import win10toast
 
toaster = win10toast.ToastNotifier()
toaster.show_toast("Alacrium", "UI Loaded.", icon_path=None, threaded=True)

def resize(window):
    window.resize(650, 420)

class Api:
  def inject(self):
    sleep(1)
    toaster = win10toast.ToastNotifier()
    toaster.show_toast("Alacrium", "Injected.")

  def execute(self):
    toaster = win10toast.ToastNotifier()
    toaster.show_toast("Alacrium", "Executed.")

if __name__ == '__main__':
    api = Api()
    window = webview.create_window(
        'Resize window example', 'assets/index.html', frameless=True, easy_drag=True, js_api=api, background_color='#333333'
    )
    webview.start(resize,window)