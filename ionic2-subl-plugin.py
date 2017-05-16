import sublime
import sublime_plugin
from subprocess import call


class IonicServeCommand(sublime_plugin.WindowCommand):
	def run(self):
		window = sublime.active_window()
		folders = window.folders()
		print (folders)
		#call(["ionic", "serve"])
