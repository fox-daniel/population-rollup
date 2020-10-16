def int_clean(astring):
    """removes commas and quotes"""
    astring = astring.replace(",", "").replace('"', "")
    return astring


new = int_clean('"1,2345"')
print(new)
