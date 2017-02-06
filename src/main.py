# because the warnings says so…
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk as gtk
from gi.repository import GObject as glib
from gi.repository import AppIndicator3 as appindicator

import signal
import os

class XautolockApplet:

    APPINDICATOR_ID = 'xautolock-toggle'

    ON_LABEL = 'Disable'
    OFF_LABEL = 'Enable'

    def __init__(self):
        self.is_xautolock_enabled = True
        self.enable_xautolock() # ensure xautolock is enabled so the applet state is synch'ed with xautolock

        self.indicator = appindicator.Indicator.new(XautolockApplet.APPINDICATOR_ID, 'xautolock_toggle', appindicator.IndicatorCategory.SYSTEM_SERVICES)
        self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        self.render_menu()
        glib.timeout_add(100, self.render_menu) # refresh the menu every 100ms, let's assume the user won't click on state change then applet icon in less than 100ms

    def enable_xautolock(self):
        os.system('xautolock -enable')

    def disable_xautolock(self):
        os.system('xautolock -disable')

    def render_menu(self):
        menu = self.build_menu()
        menu.show_all()
        self.indicator.set_menu(menu)
        return True # return true to ensure the timeout keep refreshing

    def build_menu(self):
        menu = gtk.Menu()
        menu.append(self.build_toggle_menu_item())
        menu.append(self.build_quit_menu_item())
        return menu

    def build_toggle_menu_item(self):
        menu_item = gtk.MenuItem(self.get_state_label())
        menu_item.connect('activate', lambda _: self.toggle_state()) # use a lambda to explicitely ignore the callback parameter
        return menu_item

    def get_state_label(self):
        return XautolockApplet.ON_LABEL if self.is_xautolock_enabled else XautolockApplet.OFF_LABEL

    def toggle_state(self):
        self.is_xautolock_enabled = not self.is_xautolock_enabled
        self.enable_xautolock() if self.is_xautolock_enabled else self.disable_xautolock()

    def build_quit_menu_item(self):
        menu_item = gtk.MenuItem('Quit')
        menu_item.connect('activate', lambda _: self.quit()) # use a lambda to explicitely ignore the callback parameter
        return menu_item

    def quit(self):
        self.enable_xautolock() # enable xautolock on exit to avoid user forgeting the disabled state
        gtk.main_quit()

    def render(self):
        gtk.main()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL) # be able to quit on Ctrl-C
    xautolock_applet = XautolockApplet()
    xautolock_applet.render()