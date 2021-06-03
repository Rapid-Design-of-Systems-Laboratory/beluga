from .pre_process import ensure_sympified, apply_quantities
from .independent import momentum_shift, normalize_independent
from .constraints import regularize_control_constraint, regularize_control_constraints, \
    apply_penatly_method_initial, apply_penatly_method_path, apply_penatly_method_terminal, apply_penatly_method_all
from .switching import regularize_switch, regularize_switches
from .dualize import dualize_traditional, dualize_diffyg, dualize
from .controls import algebraic_control_law, differential_control_law_traditional, differential_control_law_diffy_g,\
    differential_control_law
from .reduction import mf_com, mf_all
from .post_process import squash_to_bvp
from .analysis import hamiltonian_sensitivity_handler
