from src.PYCPPCompiler import PYCPPCompiler

compiler = PYCPPCompiler (
	includes=['tests/'],
	p3dVersion='1.8.1',
	pyxPath='tests/',
	pyxName='gamedata.pyx',
	outDir='build'
)

compiler.setup()