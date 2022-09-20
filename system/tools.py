import platform # OS check

# OS detection
def OS_check() -> str:
    release = platform.release()
    version = platform.version()
    os_type = platform.system()
    platform = platform.platform()
    print (platform, os_type, version, release)
    return {"platform": platform, "os_type": os_type, "version": version, "release": release}
