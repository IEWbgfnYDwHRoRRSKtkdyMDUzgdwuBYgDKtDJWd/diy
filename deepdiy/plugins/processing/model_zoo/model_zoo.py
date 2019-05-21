import os,rootpath
rootpath.append(pattern='plugins')
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty,DictProperty
from kivy.uix.boxlayout import BoxLayout
from plugins.processing.model_zoo.online_models import OnlineModels

class ModelZoo(BoxLayout):
	"""docstring for ModelZoo."""

	data=ObjectProperty()
	bundle_dir = rootpath.detect(pattern='plugins')
	Builder.load_file(bundle_dir +os.sep+'ui'+os.sep+'model_zoo.kv')

	def __init__(self):
		super(ModelZoo, self).__init__()

	def load_online_models(self,*args):
		print('hi')
		self.online_models=OnlineModels()
		self.online_models.open()


class Test(App):
	"""docstring for Test."""

	data=ObjectProperty()
	plugins=DictProperty()

	def __init__(self):
		super(Test, self).__init__()

	def build(self):
		demo=ModelZoo()
		return demo


if __name__ == '__main__':
	Test().run()
