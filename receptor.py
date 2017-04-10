#!/usr/bin/env python
#--encoding: UTF-8--

"""
entra en un loop esperando senales emitidas a:
dbus_interface = ruben.prova
object_path = "/home/ruben/Documents/dbus"
con el nombre de senal: 'estat'
cuando se recibe la senal la mostramos
"""

import gobject, dbus, dbus.mainloop.glib

def mostra(m):
	print m

dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus = dbus.SessionBus()
bus.add_signal_receiver(
				mostra,
				path="/home/ruben/Documents/dbus",				
				dbus_interface="ruben.prova",				
				signal_name = "estat"				
				)

loop = gobject.MainLoop()

loop.run()
