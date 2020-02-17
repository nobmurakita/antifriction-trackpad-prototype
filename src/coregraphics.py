import ctypes
from ctypes.util import find_library

CoreGraphics = ctypes.CDLL(find_library('CoreGraphics'))

# https://developer.apple.com/documentation/coregraphics/cgeventtype/kcgeventmousemoved?language=objc
kCGEventMouseMoved = 5

# https://developer.apple.com/documentation/coregraphics/cgeventtaplocation/kcghideventtap?language=objc
kCGHIDEventTap = 0

# https://developer.apple.com/documentation/coregraphics/cgeventref?language=objc
CGEventRef = ctypes.c_void_p

# https://developer.apple.com/documentation/coregraphics/cgeventsourceref?language=objc
CGEventSourceRef = ctypes.c_void_p

# https://developer.apple.com/documentation/coregraphics/cgeventtype?language=objc
CGEventType = ctypes.c_uint32

# https://developer.apple.com/documentation/coregraphics/cgmousebutton?language=objc
CGMouseButton = ctypes.c_uint32

# https://developer.apple.com/documentation/coregraphics/cgeventtaplocation?language=objc
CGEventTapLocation =  ctypes.c_uint32

# https://developer.apple.com/documentation/coregraphics/cgfloat?language=objc
CGFloat = ctypes.c_double

# https://developer.apple.com/documentation/coregraphics/cgpoint?language=objc
class CGPoint(ctypes.Structure):
    _fields_ = [
        ("x", CGFloat),
        ("y", CGFloat)
    ]

# https://developer.apple.com/documentation/coregraphics/cgsize?language=objc
class CGSize(ctypes.Structure):
    _fields_ = [
        ("x", CGFloat),
        ("y", CGFloat)
    ]

# https://developer.apple.com/documentation/coregraphics/1454913-cgeventcreate?language=objc
CGEventCreate = CoreGraphics.CGEventCreate
CGEventCreate.restype = CGEventRef
CGEventCreate.argtypes = [CGEventSourceRef]

# https://developer.apple.com/documentation/coregraphics/1454356-cgeventcreatemouseevent?language=objc
CGEventCreateMouseEvent = CoreGraphics.CGEventCreateMouseEvent
CGEventCreateMouseEvent.restype = CGEventRef
CGEventCreateMouseEvent.argtypes = [CGEventSourceRef, CGEventType, CGPoint, CGMouseButton]

# https://developer.apple.com/documentation/coregraphics/1455788-cgeventgetlocation?language=objc
CGEventGetLocation = CoreGraphics.CGEventGetLocation
CGEventGetLocation.restype = CGPoint
CGEventGetLocation.argtypes = [CGEventRef]

# https://developer.apple.com/documentation/coregraphics/1456527-cgeventpost?language=objc
CGEventPost = CoreGraphics.CGEventPost
CGEventPost.restype = None
CGEventPost.argtypes = [CGEventTapLocation, CGEventRef]
