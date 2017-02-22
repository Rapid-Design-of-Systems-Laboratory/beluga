def compute_control(_t,_X,_p,_aux):
    [x,y,z,v,psii,gam,lamX,lamY,lamZ,lamV,lamPSII,lamGAM,tf,] = _X[:13]

    # Declare all auxiliary variables
    mu = _aux['const']['mu']
    rho0 = _aux['const']['rho0']
    H = _aux['const']['H']
    re = _aux['const']['re']
    Aref = _aux['const']['Aref']
    bankmax = _aux['const']['bankmax']
    alfamax = _aux['const']['alfamax']
    Tmax = _aux['const']['Tmax']
    Tmin = _aux['const']['Tmin']
    g = _aux['const']['g']
    mass = _aux['const']['mass']
    C1 = _aux['const']['C1']
    C2 = _aux['const']['C2']

    [lagrange_initial_1,lagrange_initial_2,lagrange_initial_3,lagrange_initial_4,lagrange_initial_5,lagrange_initial_6,lagrange_terminal_1,lagrange_terminal_2,lagrange_terminal_3,lagrange_terminal_4,lagrange_terminal_5,lagrange_terminal_6,] = _p

    # Define controls beforehand in case some quantity uses it
    __nancontrols = np.empty(3)
    __nancontrols[:] = np.nan
    [banktrig,alfatrig,Ttrignew,] = __nancontrols

    # Declare all quantities
    bank = bankmax*sin(banktrig)
    alfa = alfamax*sin(alfatrig)
    D = C1*v**2 + C2/v**2
    L = g*mass
    T = 1560*sin(Ttrignew) + 1860
    Ft = -C1*v**2 - C2/v**2 + (1560*sin(Ttrignew) + 1860)*cos(alfamax*sin(alfatrig))
    Fn = g*mass + (1560*sin(Ttrignew) + 1860)*sin(alfamax*sin(alfatrig))

    _saved = np.empty(3)
    _saved[:] = np.nan

    _ham_saved = float('inf')
# Evaluate all control options

    try:
        Ttrignew = -pi/2
        alfatrig = -pi/2
        banktrig = -pi/2
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = asin(0.000215483107529863*(-lamPSII*(z + 50)**2.5/(mass*cos(gam)**2))**0.238095238095238 - 31/26)
        alfatrig = -pi/2
        banktrig = -pi/2
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = pi/2
        alfatrig = -pi/2
        banktrig = -pi/2
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = -pi/2
        alfatrig = -asin(12*atan(lamPSII/(lamV*v*cos(gam)))/pi)
        banktrig = -pi/2
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = asin(0.000215483107529863*(v*(z + 50)**2.5*(-12*lamPSII*atan(lamPSII/(lamV*v*cos(gam)))/(pi*mass*v*cos(gam)) - lamV*sqrt(-144*atan(lamPSII/(lamV*v*cos(gam)))**2/pi**2 + 1)/mass)/cos(gam))**0.238095238095238 - 31/26)
        alfatrig = -asin(12*atan(lamPSII/(lamV*v*cos(gam)))/pi)
        banktrig = -pi/2
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = pi/2
        alfatrig = -asin(12*atan(lamPSII/(lamV*v*cos(gam)))/pi)
        banktrig = -pi/2
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = -pi/2
        alfatrig = asin(12*(-atan(lamPSII/(lamV*v*cos(gam))) + pi)/pi)
        banktrig = -pi/2
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = asin(0.000215483107529863*(v*(z + 50)**2.5*(12*lamPSII*(-atan(lamPSII/(lamV*v*cos(gam))) + pi)/(pi*mass*v*cos(gam)) - lamV*sqrt(-144*(-atan(lamPSII/(lamV*v*cos(gam))) + pi)**2/pi**2 + 1)/mass)/cos(gam))**0.238095238095238 - 31/26)
        alfatrig = asin(12*(-atan(lamPSII/(lamV*v*cos(gam))) + pi)/pi)
        banktrig = -pi/2
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = pi/2
        alfatrig = asin(12*(-atan(lamPSII/(lamV*v*cos(gam))) + pi)/pi)
        banktrig = -pi/2
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = -pi/2
        alfatrig = pi/2
        banktrig = -pi/2
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = asin(0.000215483107529863*(lamPSII*(z + 50)**2.5/(mass*cos(gam)**2))**0.238095238095238 - 31/26)
        alfatrig = pi/2
        banktrig = -pi/2
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = pi/2
        alfatrig = pi/2
        banktrig = -pi/2
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = -pi/2
        alfatrig = -pi/2
        banktrig = asin(3*atan(lamPSII/(lamGAM*cos(gam)))/pi)
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = asin(0.000215483107529863*(v*(z + 50)**2.5*(lamGAM*sqrt(-9*atan(lamPSII/(lamGAM*cos(gam)))**2/pi**2 + 1)/(mass*v) + 3*lamPSII*atan(lamPSII/(lamGAM*cos(gam)))/(pi*mass*v*cos(gam)))/cos(gam))**0.238095238095238 - 31/26)
        alfatrig = -pi/2
        banktrig = asin(3*atan(lamPSII/(lamGAM*cos(gam)))/pi)
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = pi/2
        alfatrig = -pi/2
        banktrig = asin(3*atan(lamPSII/(lamGAM*cos(gam)))/pi)
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = -pi/2
        alfatrig = asin(12*atan(lamGAM*sqrt(-9*atan(lamPSII/(lamGAM*cos(gam)))**2/pi**2 + 1)/(lamV*v) + 3*lamPSII*atan(lamPSII/(lamGAM*cos(gam)))/(pi*lamV*v*cos(gam)))/pi)
        banktrig = asin(3*atan(lamPSII/(lamGAM*cos(gam)))/pi)
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = asin(0.000215483107529863*(v*(z + 50)**2.5*(-12*lamGAM*sqrt(-9*atan(lamPSII/(lamGAM*cos(gam)))**2/pi**2 + 1)*atan(lamGAM*sqrt(-9*atan(lamPSII/(lamGAM*cos(gam)))**2/pi**2 + 1)/(lamV*v) + 3*lamPSII*atan(lamPSII/(lamGAM*cos(gam)))/(pi*lamV*v*cos(gam)))/(pi*mass*v) - 36*lamPSII*atan(lamPSII/(lamGAM*cos(gam)))*atan(lamGAM*sqrt(-9*atan(lamPSII/(lamGAM*cos(gam)))**2/pi**2 + 1)/(lamV*v) + 3*lamPSII*atan(lamPSII/(lamGAM*cos(gam)))/(pi*lamV*v*cos(gam)))/(pi**2*mass*v*cos(gam)) - lamV*sqrt(-144*atan(lamGAM*sqrt(-9*atan(lamPSII/(lamGAM*cos(gam)))**2/pi**2 + 1)/(lamV*v) + 3*lamPSII*atan(lamPSII/(lamGAM*cos(gam)))/(pi*lamV*v*cos(gam)))**2/pi**2 + 1)/mass)/cos(gam))**0.238095238095238 - 31/26)
        alfatrig = asin(12*atan(lamGAM*sqrt(-9*atan(lamPSII/(lamGAM*cos(gam)))**2/pi**2 + 1)/(lamV*v) + 3*lamPSII*atan(lamPSII/(lamGAM*cos(gam)))/(pi*lamV*v*cos(gam)))/pi)
        banktrig = asin(3*atan(lamPSII/(lamGAM*cos(gam)))/pi)
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = pi/2
        alfatrig = asin(12*atan(lamGAM*sqrt(-9*atan(lamPSII/(lamGAM*cos(gam)))**2/pi**2 + 1)/(lamV*v) + 3*lamPSII*atan(lamPSII/(lamGAM*cos(gam)))/(pi*lamV*v*cos(gam)))/pi)
        banktrig = asin(3*atan(lamPSII/(lamGAM*cos(gam)))/pi)
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = -pi/2
        alfatrig = asin(12*(atan(lamGAM*sqrt(-9*atan(lamPSII/(lamGAM*cos(gam)))**2/pi**2 + 1)/(lamV*v) + 3*lamPSII*atan(lamPSII/(lamGAM*cos(gam)))/(pi*lamV*v*cos(gam))) + pi)/pi)
        banktrig = asin(3*atan(lamPSII/(lamGAM*cos(gam)))/pi)
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = asin(0.000215483107529863*(v*(z + 50)**2.5*(-12*lamGAM*sqrt(-9*atan(lamPSII/(lamGAM*cos(gam)))**2/pi**2 + 1)*(atan(lamGAM*sqrt(-9*atan(lamPSII/(lamGAM*cos(gam)))**2/pi**2 + 1)/(lamV*v) + 3*lamPSII*atan(lamPSII/(lamGAM*cos(gam)))/(pi*lamV*v*cos(gam))) + pi)/(pi*mass*v) - 36*lamPSII*(atan(lamGAM*sqrt(-9*atan(lamPSII/(lamGAM*cos(gam)))**2/pi**2 + 1)/(lamV*v) + 3*lamPSII*atan(lamPSII/(lamGAM*cos(gam)))/(pi*lamV*v*cos(gam))) + pi)*atan(lamPSII/(lamGAM*cos(gam)))/(pi**2*mass*v*cos(gam)) - lamV*sqrt(-144*(atan(lamGAM*sqrt(-9*atan(lamPSII/(lamGAM*cos(gam)))**2/pi**2 + 1)/(lamV*v) + 3*lamPSII*atan(lamPSII/(lamGAM*cos(gam)))/(pi*lamV*v*cos(gam))) + pi)**2/pi**2 + 1)/mass)/cos(gam))**0.238095238095238 - 31/26)
        alfatrig = asin(12*(atan(lamGAM*sqrt(-9*atan(lamPSII/(lamGAM*cos(gam)))**2/pi**2 + 1)/(lamV*v) + 3*lamPSII*atan(lamPSII/(lamGAM*cos(gam)))/(pi*lamV*v*cos(gam))) + pi)/pi)
        banktrig = asin(3*atan(lamPSII/(lamGAM*cos(gam)))/pi)
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = pi/2
        alfatrig = asin(12*(atan(lamGAM*sqrt(-9*atan(lamPSII/(lamGAM*cos(gam)))**2/pi**2 + 1)/(lamV*v) + 3*lamPSII*atan(lamPSII/(lamGAM*cos(gam)))/(pi*lamV*v*cos(gam))) + pi)/pi)
        banktrig = asin(3*atan(lamPSII/(lamGAM*cos(gam)))/pi)
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = -pi/2
        alfatrig = pi/2
        banktrig = asin(3*atan(lamPSII/(lamGAM*cos(gam)))/pi)
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = asin(0.000215483107529863*(v*(z + 50)**2.5*(-lamGAM*sqrt(-9*atan(lamPSII/(lamGAM*cos(gam)))**2/pi**2 + 1)/(mass*v) - 3*lamPSII*atan(lamPSII/(lamGAM*cos(gam)))/(pi*mass*v*cos(gam)))/cos(gam))**0.238095238095238 - 31/26)
        alfatrig = pi/2
        banktrig = asin(3*atan(lamPSII/(lamGAM*cos(gam)))/pi)
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = pi/2
        alfatrig = pi/2
        banktrig = asin(3*atan(lamPSII/(lamGAM*cos(gam)))/pi)
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = -pi/2
        alfatrig = -pi/2
        banktrig = asin(3*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/pi)
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = asin(0.000215483107529863*(v*(z + 50)**2.5*(lamGAM*sqrt(-9*(atan(lamPSII/(lamGAM*cos(gam))) + pi)**2/pi**2 + 1)/(mass*v) + 3*lamPSII*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/(pi*mass*v*cos(gam)))/cos(gam))**0.238095238095238 - 31/26)
        alfatrig = -pi/2
        banktrig = asin(3*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/pi)
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = pi/2
        alfatrig = -pi/2
        banktrig = asin(3*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/pi)
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = -pi/2
        alfatrig = asin(12*atan(lamGAM*sqrt(-9*(atan(lamPSII/(lamGAM*cos(gam))) + pi)**2/pi**2 + 1)/(lamV*v) + 3*lamPSII*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/(pi*lamV*v*cos(gam)))/pi)
        banktrig = asin(3*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/pi)
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = asin(0.000215483107529863*(v*(z + 50)**2.5*(-12*lamGAM*sqrt(-9*(atan(lamPSII/(lamGAM*cos(gam))) + pi)**2/pi**2 + 1)*atan(lamGAM*sqrt(-9*(atan(lamPSII/(lamGAM*cos(gam))) + pi)**2/pi**2 + 1)/(lamV*v) + 3*lamPSII*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/(pi*lamV*v*cos(gam)))/(pi*mass*v) - 36*lamPSII*(atan(lamPSII/(lamGAM*cos(gam))) + pi)*atan(lamGAM*sqrt(-9*(atan(lamPSII/(lamGAM*cos(gam))) + pi)**2/pi**2 + 1)/(lamV*v) + 3*lamPSII*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/(pi*lamV*v*cos(gam)))/(pi**2*mass*v*cos(gam)) - lamV*sqrt(-144*atan(lamGAM*sqrt(-9*(atan(lamPSII/(lamGAM*cos(gam))) + pi)**2/pi**2 + 1)/(lamV*v) + 3*lamPSII*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/(pi*lamV*v*cos(gam)))**2/pi**2 + 1)/mass)/cos(gam))**0.238095238095238 - 31/26)
        alfatrig = asin(12*atan(lamGAM*sqrt(-9*(atan(lamPSII/(lamGAM*cos(gam))) + pi)**2/pi**2 + 1)/(lamV*v) + 3*lamPSII*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/(pi*lamV*v*cos(gam)))/pi)
        banktrig = asin(3*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/pi)
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = pi/2
        alfatrig = asin(12*atan(lamGAM*sqrt(-9*(atan(lamPSII/(lamGAM*cos(gam))) + pi)**2/pi**2 + 1)/(lamV*v) + 3*lamPSII*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/(pi*lamV*v*cos(gam)))/pi)
        banktrig = asin(3*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/pi)
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = -pi/2
        alfatrig = asin(12*(atan(lamGAM*sqrt(-9*(atan(lamPSII/(lamGAM*cos(gam))) + pi)**2/pi**2 + 1)/(lamV*v) + 3*lamPSII*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/(pi*lamV*v*cos(gam))) + pi)/pi)
        banktrig = asin(3*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/pi)
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = asin(0.000215483107529863*(v*(z + 50)**2.5*(-12*lamGAM*sqrt(-9*(atan(lamPSII/(lamGAM*cos(gam))) + pi)**2/pi**2 + 1)*(atan(lamGAM*sqrt(-9*(atan(lamPSII/(lamGAM*cos(gam))) + pi)**2/pi**2 + 1)/(lamV*v) + 3*lamPSII*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/(pi*lamV*v*cos(gam))) + pi)/(pi*mass*v) - 36*lamPSII*(atan(lamPSII/(lamGAM*cos(gam))) + pi)*(atan(lamGAM*sqrt(-9*(atan(lamPSII/(lamGAM*cos(gam))) + pi)**2/pi**2 + 1)/(lamV*v) + 3*lamPSII*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/(pi*lamV*v*cos(gam))) + pi)/(pi**2*mass*v*cos(gam)) - lamV*sqrt(-144*(atan(lamGAM*sqrt(-9*(atan(lamPSII/(lamGAM*cos(gam))) + pi)**2/pi**2 + 1)/(lamV*v) + 3*lamPSII*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/(pi*lamV*v*cos(gam))) + pi)**2/pi**2 + 1)/mass)/cos(gam))**0.238095238095238 - 31/26)
        alfatrig = asin(12*(atan(lamGAM*sqrt(-9*(atan(lamPSII/(lamGAM*cos(gam))) + pi)**2/pi**2 + 1)/(lamV*v) + 3*lamPSII*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/(pi*lamV*v*cos(gam))) + pi)/pi)
        banktrig = asin(3*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/pi)
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = pi/2
        alfatrig = asin(12*(atan(lamGAM*sqrt(-9*(atan(lamPSII/(lamGAM*cos(gam))) + pi)**2/pi**2 + 1)/(lamV*v) + 3*lamPSII*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/(pi*lamV*v*cos(gam))) + pi)/pi)
        banktrig = asin(3*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/pi)
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = -pi/2
        alfatrig = pi/2
        banktrig = asin(3*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/pi)
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = asin(0.000215483107529863*(v*(z + 50)**2.5*(-lamGAM*sqrt(-9*(atan(lamPSII/(lamGAM*cos(gam))) + pi)**2/pi**2 + 1)/(mass*v) - 3*lamPSII*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/(pi*mass*v*cos(gam)))/cos(gam))**0.238095238095238 - 31/26)
        alfatrig = pi/2
        banktrig = asin(3*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/pi)
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = pi/2
        alfatrig = pi/2
        banktrig = asin(3*(atan(lamPSII/(lamGAM*cos(gam))) + pi)/pi)
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = -pi/2
        alfatrig = -pi/2
        banktrig = pi/2
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = asin(0.000215483107529863*(lamPSII*(z + 50)**2.5/(mass*cos(gam)**2))**0.238095238095238 - 31/26)
        alfatrig = -pi/2
        banktrig = pi/2
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = pi/2
        alfatrig = -pi/2
        banktrig = pi/2
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = -pi/2
        alfatrig = asin(12*atan(lamPSII/(lamV*v*cos(gam)))/pi)
        banktrig = pi/2
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = asin(0.000215483107529863*(v*(z + 50)**2.5*(-12*lamPSII*atan(lamPSII/(lamV*v*cos(gam)))/(pi*mass*v*cos(gam)) - lamV*sqrt(-144*atan(lamPSII/(lamV*v*cos(gam)))**2/pi**2 + 1)/mass)/cos(gam))**0.238095238095238 - 31/26)
        alfatrig = asin(12*atan(lamPSII/(lamV*v*cos(gam)))/pi)
        banktrig = pi/2
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = pi/2
        alfatrig = asin(12*atan(lamPSII/(lamV*v*cos(gam)))/pi)
        banktrig = pi/2
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = -pi/2
        alfatrig = asin(12*(atan(lamPSII/(lamV*v*cos(gam))) + pi)/pi)
        banktrig = pi/2
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = asin(0.000215483107529863*(v*(z + 50)**2.5*(-12*lamPSII*(atan(lamPSII/(lamV*v*cos(gam))) + pi)/(pi*mass*v*cos(gam)) - lamV*sqrt(-144*(atan(lamPSII/(lamV*v*cos(gam))) + pi)**2/pi**2 + 1)/mass)/cos(gam))**0.238095238095238 - 31/26)
        alfatrig = asin(12*(atan(lamPSII/(lamV*v*cos(gam))) + pi)/pi)
        banktrig = pi/2
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = pi/2
        alfatrig = asin(12*(atan(lamPSII/(lamV*v*cos(gam))) + pi)/pi)
        banktrig = pi/2
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = -pi/2
        alfatrig = pi/2
        banktrig = pi/2
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = asin(0.000215483107529863*(-lamPSII*(z + 50)**2.5/(mass*cos(gam)**2))**0.238095238095238 - 31/26)
        alfatrig = pi/2
        banktrig = pi/2
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    try:
        Ttrignew = pi/2
        alfatrig = pi/2
        banktrig = pi/2
    except Exception as e:
        Ttrignew = 0
        alfatrig = 0
        banktrig = 0
        logging.error('Error : '+str(e))
        raise
    _ham = compute_hamiltonian(_t,_X,_p,_aux,[banktrig,alfatrig,Ttrignew,])
    if _ham < _ham_saved:
        _ham_saved = _ham
        _saved = [banktrig,alfatrig,Ttrignew,]

################################################################
    compute_control.guess_u = _saved
    return _saved
