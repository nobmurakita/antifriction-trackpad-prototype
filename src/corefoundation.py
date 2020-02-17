import ctypes
from ctypes.util import find_library

CoreFoundation = ctypes.CDLL(find_library('CoreFoundation'))

# https://developer.apple.com/documentation/corefoundation/cfindex?language=objc
CFIndex = ctypes.c_long

# https://developer.apple.com/documentation/corefoundation/cfarrayref?language=objc
CFArrayRef = ctypes.c_void_p

# https://developer.apple.com/documentation/corefoundation/cfmutablearrayref?language=objc
CFMutableArrayRef = ctypes.c_void_p

# https://developer.apple.com/documentation/corefoundation/cftyperef?language=objc
CFTypeRef = ctypes.c_void_p

# https://developer.apple.com/documentation/corefoundation/1388772-cfarraygetcount?language=objc
CFArrayGetCount = CoreFoundation.CFArrayGetCount
CFArrayGetCount.restype = CFIndex
CFArrayGetCount.argtypes = [CFArrayRef]

# https://developer.apple.com/documentation/corefoundation/1388767-cfarraygetvalueatindex?language=objc
CFArrayGetValueAtIndex = CoreFoundation.CFArrayGetValueAtIndex
CFArrayGetValueAtIndex.restype = ctypes.c_void_p
CFArrayGetValueAtIndex.argtypes = [CFArrayRef, CFIndex]

# https://developer.apple.com/documentation/corefoundation/1521153-cfrelease?language=objc
CFRelease = CoreFoundation.CFRelease
CFRelease.restype = None
CFRelease.argtypes = [CFTypeRef]
