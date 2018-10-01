from AppKit import NSWorkspace
from Quartz import (
        CGWindowListCopyWindowInfo,
        kCGWindowListOptionOnScreenOnly,
        kCGNullWindowID
    )


def getInfo() -> tuple:
    # curr_app = NSWorkspace.sharedWorkspace().frontmostApplication() # returns always python
    window_title = app_name = 'Unknown'

    curr_pid = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationProcessIdentifier']

    options = kCGWindowListOptionOnScreenOnly
    window_list = CGWindowListCopyWindowInfo(options, kCGNullWindowID)

    try:
        window = [w for w in window_list if curr_pid == w['kCGWindowOwnerPID']][0]
    except IndexError:
        pass
    else:
        window_title = window.get('kCGWindowName', window_title)
        app_name = window.get('kCGWindowOwnerName', app_name)

    return (app_name, window_title)


def getApp(info) -> str:
    return info[0]


def getTitle(info) -> str:
    return info[1]