import sys, os
sys.path.append(os.getcwd()+'/../')

tmpl = """
# TODO: Preprocess, postprocess hooks?
def deriv_func(_t,_X,_p,_aux):
    [{{state_names}}] = _X[:{{num_states}}]
    [{{#state_list}}{{.}},{{/state_list}}] = _X[:{{num_states}}]
    # Constants and constraints
    # constant_name = constant_value 
    # etc.
    # aux_list: { type: const, vars: [a,b,c,d]}
    #
    
{{#aux_list}}
{{#vars}}
    {{.}} = _aux['{{type}}']['{{.}}']
{{/vars}}
{{/aux_list}}
    
    return {{deriv_expr}}
"""

tmpl2 = """
# Evaluate all control options

{{#control_options}}
    try:
        {{#.}}
        {{name}} = {{expr}}
        {{/.}}
    except:
        pass
    _ham = compute_hamiltonian(t,X,p,aux,[{{#control_list}}{{.}},{{/control_list}}])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [{{#control_list}}{{.}},{{/control_list}}]
        
################################################################

{{/control_options}}
"""
import pystache
ctrl = {'control_options':[
    [{'name':'theta','expr':'atan(y/x)'},{'name':'sigma','expr':'acos(a/b)'}],
    [{'name':'theta','expr':'-atan(y/x)'},{'name':'sigma','expr':'-acos(a/b)'}],
    ],
    'control_list':['theta','sigma']
}
print pystache.render(tmpl2,ctrl)
#
# stuff = {'aux_list': [
#             {
#             'type' : 'const',
#             'vars': ['g','foo']
#             },
#             {
#             'type' : 'constraint',
#             'vars': ['qdot']
#             }
#          ],
#          'state_list': [
#              'a','b','c','d'
#          ],
#          'num_states': 4,
#          'state_names': 'a,b,c,d'
#         }
# print pystache.render(tmpl,stuff)