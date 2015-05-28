# TODO: Rename this class ???
import pystache
class FunctionTemplate(object):
    @staticmethod
    def compile(filename,data,module,verbose=False):
        f = open(filename)
        tmpl = f.read()
        f.close()
        
        code = pystache.render(tmpl,data)
        if verbose:
            print(code)
        exec code in module.__dict__