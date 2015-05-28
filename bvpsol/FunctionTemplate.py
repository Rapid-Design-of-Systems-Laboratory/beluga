# TODO: Rename this class ???
import pystache
class FunctionTemplate(object):
    # pystache renderer without HTML escapes
    renderer = pystache.Renderer(escape=lambda u: u)
    @classmethod
    def compile(cls,filename,data,module,verbose=False):
        f = open(filename)
        tmpl = f.read()
        f.close()

        # Render the template using the data 
        code = cls.renderer.render(tmpl,data)
        if verbose:
            print(code)
        exec(code,module.__dict__)