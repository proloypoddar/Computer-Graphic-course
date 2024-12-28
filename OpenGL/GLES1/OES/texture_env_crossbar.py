'''OpenGL extension OES.texture_env_crossbar

This module customises the behaviour of the 
OpenGL.raw.GLES1.OES.texture_env_crossbar to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds the capability to use the texture color from
	other texture units as sources to the COMBINE enviornment
	function. OpenGL ES 1.1 defined texture combine functions which
	could use the color from the current texture unit as a source. 
	This extension adds the ability to use the color from any texture 
	unit as a source.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/texture_env_crossbar.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES1 import _types, _glgets
from OpenGL.raw.GLES1.OES.texture_env_crossbar import *
from OpenGL.raw.GLES1.OES.texture_env_crossbar import _EXTENSION_NAME

def glInitTextureEnvCrossbarOES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION