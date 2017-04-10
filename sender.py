#!/usr/bin/env python
#--encoding: UTF-8--

"""
Emite una senal a dbus, al bus 'session' al destino:
	dbus_interface = ruben.prova	
	object_path = "/home/ruben/Documents/dbus"
con el nombre de senal: 'estat'
"""

import gobject
import dbus
from dbus.service import signal,Object
import dbus.mainloop.glib

class EmetSenyal(Object):

	def __init__(self, conn, object_path='/'):
		Object.__init__(self, conn, object_path)

		
	@signal('ruben.prova')	
	def estat(self,m):
		global loop
		print("sended signal: %s" % m)
		gobject.timeout_add(2000, loop.quit)


dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
loop = gobject.MainLoop()
bus = dbus.SessionBus()
o = EmetSenyal(bus,object_path='/home/ruben/Documents/dbus')
o.estat('Tux')
loop.run()
