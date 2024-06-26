def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if hasattr(par, '__doc__') and par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if hasattr(node, '__doc__') and node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))
