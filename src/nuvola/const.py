#! /usr/bin/python


class const(object):
    class ConstError(TypeError):
        pass  # base exception class

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't change const.%s" % name)
        if not name.isupper():
            raise self.ConstCaseError('const name %r is not all uppercase' % name)
        self.__dict__[name] = value


class DeviceType(const):
    MOBILE = 1  #
    ANDROID_PHONE = 2
    IOS_PHONE = 3
    WINDOWPHONE = 4
    ANDROID_TABLET = 5
    IOS_TABLET = 6
    MOBILE_WEB = 7
    DESKTOP_WEB = 8
