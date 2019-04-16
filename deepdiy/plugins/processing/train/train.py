import sys,os
sys.path.append('../../../')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import DictProperty
from utils.get_parent_path import get_parent_path
from plugins.processing.networks.model_collector import ModelCollector
import webbrowser
from utils.select_path_dialog import select_file,select_folder
from plugins.processing.train.dataset import Dataset
from core.form_parser import FormParser
import json

class Train(BoxLayout):
	"""docstring for Train."""
	data=DictProperty()
	bundle_dir = get_parent_path(3)
	models=ModelCollector().models
	Builder.load_file(bundle_dir +os.sep+'ui'+os.sep+'train.kv')

	def __init__(self):
		super(Train, self).__init__()
		self.ids.config_spinner.bind(text=self.load_config)

	def load_config(self,instance,text):
		path=os.sep.join([get_parent_path(4),'model_zoo',text,'config_form.json'])
		with open(path) as f:
			form_parser=FormParser()
			form_parser.form=json.load(f)
			self.ids.config_panel.add_widget(form_parser)
			form_parser.bind(minimum_height = form_parser.setter('height'))

	def open_via(self):
		webbrowser.open(get_parent_path(4)+os.sep+'via'+os.sep+'via.html')

	def train(self):
		webbrowser.open('https://colab.research.google.com/github/deepdiy/deepdiy/blob/master/mrcnn.ipynb')

	def select_annotation_path(self):
		self.annoation_path=select_file()

	def select_img_dir(self):
		self.img_dir=select_folder()

	def save_zip(self):
		dataset=Dataset()
		dataset.destination_dir=select_folder()
		dataset.annotation_path=self.annoation_path
		dataset.img_dir=self.img_dir
		dataset.run()


class Test(App):
	def __init__(self,**kwargs):
		super(Test, self).__init__(**kwargs)
		self.train=Train()

	def build(self):
		return self.train


if __name__ == '__main__':
	test=Test().run()