# https://github.com/pqrs-org/Karabiner-Elements/blob/master/src/apps/MultitouchExtension/src/MultitouchPrivate.h

import ctypes
from corefoundation import CFMutableArrayRef

MultitouchSupport = ctypes.CDLL("/System/Library/PrivateFrameworks/MultitouchSupport.framework/MultitouchSupport")

class mtPoint(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float)
    ]

class mtReadout(ctypes.Structure):
    _fields_ = [
        ("position", mtPoint),
        ("velocity", mtPoint)
    ]

class Finger(ctypes.Structure):
    _fields_ = [
        ("frame", ctypes.c_int),
        ("timestamp", ctypes.c_double),
        ("identifier", ctypes.c_int),
        ("state", ctypes.c_int),
        ("unknown1", ctypes.c_int),
        ("unknown2", ctypes.c_int),
        ("normalized", mtReadout),
        ("size", ctypes.c_float),
        ("unknown3", ctypes.c_int),
        ("angle", ctypes.c_float),
        ("majorAxis", ctypes.c_float),
        ("minorAxis", ctypes.c_float),
        ("unknown4", mtReadout),
        ("unknown5", ctypes.c_int * 2),
        ("unknown6", ctypes.c_float),
    ]

MTDeviceRef = ctypes.c_void_p

MTContactCallbackFunction = ctypes.CFUNCTYPE(
    ctypes.c_int,
    MTDeviceRef,            # device
    ctypes.POINTER(Finger), # data
    ctypes.c_int,           # fingers
    ctypes.c_double,        # timestamp
    ctypes.c_int            # frame
)

MTDeviceCreateList = MultitouchSupport.MTDeviceCreateList
MTDeviceCreateList.restype = CFMutableArrayRef
MTDeviceCreateList.argtypes = []

MTRegisterContactFrameCallback = MultitouchSupport.MTRegisterContactFrameCallback
MTRegisterContactFrameCallback.restype = None
MTRegisterContactFrameCallback.argtypes = [MTDeviceRef, MTContactCallbackFunction]

MTUnregisterContactFrameCallback = MultitouchSupport.MTUnregisterContactFrameCallback
MTUnregisterContactFrameCallback.restype = None
MTUnregisterContactFrameCallback.argtypes = [MTDeviceRef, MTContactCallbackFunction]

MTDeviceStart = MultitouchSupport.MTDeviceStart
MTDeviceStart.restype = None
MTDeviceStart.argtypes = [MTDeviceRef, ctypes.c_int]

MTDeviceStop = MultitouchSupport.MTDeviceStop
MTDeviceStop.restype = None
MTDeviceStop.argtypes = [MTDeviceRef, ctypes.c_int]
