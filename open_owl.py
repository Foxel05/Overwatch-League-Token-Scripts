from OwlSettings import settings as owl_settings;

import webbrowser
import time
import runpy
import pyautogui

url = 'https://www.youtube.com/channel/UCiAInBL9kUzz1XRxk66v-gw/live';

settings = owl_settings.Settings();

if not settings.should_skip_google():
  runpy.run_path(path_name=settings.home_dir() + '/.owl/login_google.py');

settings.log("Opening Owl.");
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(settings.firefox_location()))
webbrowser.get('firefox').open_new(url)
time.sleep(15);
pyautogui.press('space');
