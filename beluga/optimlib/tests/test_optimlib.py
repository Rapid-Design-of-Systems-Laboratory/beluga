# from beluga.problem2 import *
#
# def test_problem():
#     p = Problem('test_problem')
#
#     assert p.name == 'test_problem'
#
#     p.add_dynamic_element('x','v*cos(theta)','s',element_kind='states',
#                                 element_props=['name','eom','unit'])
#     assert p._systems['default'] == {'states':
#                             [{'name':'x', 'eom':'v*cos(theta)','unit':'s'}]}
#
#
#     assert p.state.keywords == {'element_kind':'states', 'element_props':['name', 'eom', 'unit']}
#     assert p.control.keywords == {'element_kind':'controls', 'element_props':['name','unit']}
#     assert p.constant.keywords == {'element_kind':'constants', 'element_props':['name','value','unit']}
#     assert p.quantity.keywords == {'element_kind':'quantities', 'element_props':['name','value']}
#
#     p.add_property('path','v^2','m^2/s^2',property_name='cost', arg_list=['type','expr','unit'])
#     assert p._properties == {'cost': {'type':'path', 'expr':'v^2', 'unit':'m^2/s^2'}}
#
#     assert p.independent.keywords == {'property_name': 'independent', 'arg_list': ['name', 'unit']}
