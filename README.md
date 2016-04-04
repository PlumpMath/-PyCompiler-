# PyCompiler++ Also Known As PYC++
 PyCompiler++ is a python compiler build to compile Panda3D games, and to prevent source code dumps, and code injection.

# Requirements:
* Cython
* CX_Freeze
* Panda3d

# How it works:
* PYC++ Converts the set modules into c++, then it compiles the modules into a .pyd file. Then PYC++ compiles a __main__ also specified, into an exe which decrypts the .pyd and runs the game.
* Please Note: The compiler is in heavy development, don't expect perfect results!

# Contributors:
* SkippsDev

# Want to Contribute:
* Don't just commit your code, talk to the development team and ensure your changes are complete.