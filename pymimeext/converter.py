from pymimeext.map import EXTENSION_MIMETYPE

def get_mimetype(extension):
	return EXTENSION_MIMETYPE[extension.replace('.', '').lower()]