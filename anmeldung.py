import os
import time
global _AbsoluteZeitIn_

_Rechnername_ = os.uname()[1]
_Benutzername_ = os.getlogin()
_Loginzeit_ = time.ctime()
_AbsoluteZeitIn_ = str(time.time())
print(_AbsoluteZeitIn_)
_Tabs_ = "\t\t"

_Protokoll_linie_ = ( _Rechnername_ + _Tabs_ + _Benutzername_ + _Tabs_ + " In : " + _Loginzeit_ + _Tabs_ +_AbsoluteZeitIn_ + " --> ")

with open('protokoll_loginout.dat','a') as _Protokoll_:
    _Protokoll_.write(_Protokoll_linie_)
_Protokoll_.closed