try:
    import p2
    print("imported p2")
except Exception:
    print("could not import p2")


def print_dependencies():
    print("Importing p2 version:%s" % p2.__version__)
    return True
