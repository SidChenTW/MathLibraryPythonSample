import ctypes

MathLibrary = ctypes.WinDLL('.\MathLibrary.dll')

MathLibrary.fibonacci_init.argtypes = [ctypes.c_ulonglong, ctypes.c_ulonglong]
MathLibrary.fibonacci_init(1,1)

MathLibrary.fibonacci_index.restype = ctypes.c_uint
MathLibrary.fibonacci_current.restype = ctypes.c_ulonglong
MathLibrary.fibonacci_next.restype = ctypes.c_bool

while True:
    print ("{}:{}".format(MathLibrary.fibonacci_index(), MathLibrary.fibonacci_current()))
    if MathLibrary.fibonacci_next() == False:
        break
print (MathLibrary.fibonacci_index() + 1, 
        " Fibonacci sequence values fit in an ", 
        "unsigned 64-bit integer.", sep="")