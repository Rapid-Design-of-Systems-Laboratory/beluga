from beluga.ivpsol.timesteppers import Method
import numpy as np

m = Method()

keys = m.data.keys()
number_of_methods = len(keys)
max_key_length = max([len(k) for k in keys])
default_col_width = 8


new_row_str = '-'*max_key_length + '  ' + '-'*default_col_width + '  ' + '-'*default_col_width + '  ' +\
              '-'*2*default_col_width + '  ' + '-'*default_col_width + '\n'
new_table_str = new_row_str.replace('-', '=')

with open('../docs/source/modules/ivpsol/integrationmethods.rst', 'w') as f:
    f.write('IVP Integration Methods\n')
    f.write('=======================\n\n')

    f.write(new_table_str)
    f.write('Key' + ' '*(max_key_length-3) + '  Order' + ' '*(default_col_width - 5) + '  nevals' +
            ' '*(default_col_width-6) + '  Variable Step' + ' '*(2*default_col_width - 13) + '  Type\n')
    f.write(new_table_str)

    key_len = len(keys)
    n = 0
    for k in keys:
        n += 1
        order = str(m.data[k]['order'])
        nevals = str(m.data[k]['n'])
        varstep = str(not sum(np.array(m.data[k]['bhat'], dtype=np.float64)) == 0)
        type_ = str(m.data[k]['type'])
        f.write(k + ' '*(max_key_length-len(k)) + '  ' + order + ' '*(default_col_width - len(order)) + '  ' + nevals +
                ' '*(default_col_width - len(nevals)) + '  ' + varstep + ' '*(2*default_col_width - len(varstep)) +
                '  ' + type_ + '\n')
        if n != key_len:
            f.write(new_row_str)
        else:
            f.write(new_table_str)
