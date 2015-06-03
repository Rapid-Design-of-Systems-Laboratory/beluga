def fix_carets(expr):
    """Converts carets to exponent"""
    import re as _re
    caret = _re.compile('[\^]')
    return caret.sub('**',expr)
