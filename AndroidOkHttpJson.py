import sublime
import sublime_plugin
import re


class AndroidOkHttpJsonCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selection = sublime.Region(0, self.view.size())
		selection_text = self.view.substr(selection)
		text = re.sub(r'(\n\s+)(.*.)', r'\2', selection_text, flags=re.MULTILINE)
		text = re.sub(r'(.*.OkHttp:\s)(.*.)(\n{0,1})', r'\2', text, flags=re.MULTILINE)
		self.view.replace(edit, selection, text)
		try:
			self.view.run_command("pretty_json_and_sort")
		except Exception:
			self.show_exception()
