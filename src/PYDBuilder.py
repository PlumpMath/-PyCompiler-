from Cython.Build import cythonize
from distutils.core import setup

class PYDBuilder:

	def __init__(self, extensions):
		self.extensions = extensions

	def setBuildDir(self, buildDir):
		self.buildDir = buildDir

	def build(self):
		for module in self.extensions:
			print ('Builder: Cythonizing modules...')

			try:
				setup (
    				ext_modules=cythonize(self.extensions)
				)
			finally:
				print ('Builder: Built modules, all done!')