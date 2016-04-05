import os
import PYDBuilder
from distutils.extension import Extension

class PYCPPCompiler:

	def __init__(self, includes, p3dVersion, pyxPath, pyxName, outDir):
		self.includes = includes
		self.p3dVersion = p3dVersion
		self.pyxPath = pyxPath
		self.pyxName = pyxName
		self.outDir = outDir
		self.ext_modules = []

	def add_module(self, moduleName):
		self.ext_modules.append(moduleName)

	def remove_module(self, moduleName):
		self.ext_modules.remove(moduleName)

	def setup(self):
		if not self.includes:
			raise Exception("Please provide included files to compile!")

		print ('Compiler: Checking for build directory...')

		if not os.path.isdir(self.outDir):
			os.makedirs(self.outDir)

			print ('Compiler: Created %s directory.' % (self.outDir))

		print ('Compiler: Adding Panda3d required extension modules...')

		self.add_module('C:/Panda3d-%s/bin/libguide40.dll' % self.p3dVersion)
		self.add_module('C:/Panda3d-%s/bin/libp3direct.dll' % self.p3dVersion)
		self.add_module('C:/Panda3d-%s/bin/libp3dtool.dll' % self.p3dVersion)
		self.add_module('C:/Panda3d-%s/bin/libp3dtoolconfig.dll' % self.p3dVersion)
		self.add_module('C:/Panda3d-%s/bin/libp3fmod_audio.dll' % self.p3dVersion)
		self.add_module('C:/Panda3d-%s/bin/libp3framework.dll' % self.p3dVersion)
		self.add_module('C:/Panda3d-%s/bin/libp3glstuff.dll' % self.p3dVersion)
		self.add_module('C:/Panda3d-%s/bin/libp3openal_audio.dll' % self.p3dVersion)
		self.add_module('C:/Panda3d-%s/bin/libp3ptloader.dll' % self.p3dVersion)
		self.add_module('C:/Panda3d-%s/bin/libp3pystub.dll' % self.p3dVersion)
		self.add_module('C:/Panda3d-%s/bin/libp3rocket.dll' % self.p3dVersion)
		self.add_module('C:/Panda3d-%s/bin/libp3tinydisplay.dll' % self.p3dVersion)
		self.add_module('C:/Panda3d-%s/bin/libp3vision.dll' % self.p3dVersion)
		self.add_module('C:/Panda3d-%s/bin/libp3windisplay.dll' % self.p3dVersion)
		self.add_module('C:/Panda3d-%s/bin/libpanda.dll' % self.p3dVersion)
		self.add_module('C:/Panda3d-%s/bin/libp3ptloader.dll' % self.p3dVersion)
		self.add_module('C:/Panda3d-%s/bin/libpandabullet.dll' % self.p3dVersion)
		self.add_module('C:/Panda3d-%s/bin/libpandaegg.dll' % self.p3dVersion)
		self.add_module('C:/Panda3d-%s/bin/libpandaexpress.dll' % self.p3dVersion)
		self.add_module('C:/Panda3d-%s/bin/libpandafx.dll' % self.p3dVersion)
		self.add_module('C:/Panda3d-%s/bin/libpandagl.dll' % self.p3dVersion)
		self.add_module('C:/Panda3d-%s/bin/libpandaode.dll' % self.p3dVersion)
		self.add_module('C:/Panda3d-%s/bin/libpandaphysics.dll' % self.p3dVersion)
		self.add_module('C:/Panda3d-%s/bin/libpandaskel.dll' % self.p3dVersion)
		self.add_module('C:/Panda3d-%s/bin/libpandatiff.dll' % self.p3dVersion)

		for module in self.ext_modules:
			print ('Compiler: Added extension module, %s' % str(module))


		print ('Compiler: Done adding Panda3d required extension modules.')

		# Now write the src file.
		self.make_pyd()

	def make_pyd(self):
		print ('Compiler: Compiling python src to %s.pyd...' % (self.pyxName.strip('.pyx')))

		extensions = [
			Extension (
        		"%s/%s" % (self.outDir, self.pyxName),
        		["modules/%s.pyx" % (self.pyxName)], 
				language='c++',
				include_dirs=self.includes
			)
		]

		self.builder = PYDBuilder.PYDBuilder(extensions)
		self.builder.setBuildDir(self.outDir)
		self.builder.build()

		print ('Compiler: Finished building %s.pyd' % (self.pyxName.strip('.pyx')))
		self.move_ext_modules()

	def move_ext_modules(self):
		pass # TODO!