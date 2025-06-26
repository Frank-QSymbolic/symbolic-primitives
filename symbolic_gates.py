# Symbolic values are strings or structured tokens
# e.g., '0', '1', '∆', or {'type': 'θ', 'angle': 'π/2'}

def pauli_x(state):
    if state == '0':
        return '1'
    if state == '1':
        return '0'
    return state  # ∆ or θ pass through unchanged

def pauli_z(state):
    if state == '0':
        return '0'
    if state == '1':
        return '1'
    if isinstance(state, dict) and state['type'] == 'θ':
        # Z gate flips phase
        return {'type': 'θ', 'angle': f"-{state['angle']}"}
    return state

def hadamard(state):
    if state in ('0', '1'):
        return '∆'  # classical → ambiguous
    return state  # ∆ and θ remain as-is

def phase_s(state):
    if isinstance(state, dict) and state['type'] == 'θ':
        return {'type': 'θ', 'angle': state['angle'] + ' + π/2'}
    if state == '1':
        return {'type': 'θ', 'angle': 'π/2'}
    return state

def phase_t(state):
    if isinstance(state, dict) and state['type'] == 'θ':
        return {'type': 'θ', 'angle': state['angle'] + ' + π/4'}
    if state == '1':
        return {'type': 'θ', 'angle': 'π/4'}
    return state

# Rotation gates: return θ-states
def rx(state, angle='π/4'):
    return {'type': 'θ', 'angle': angle}

def ry(state, angle='π/3'):
    return {'type': 'θ', 'angle': angle}

def rz(state, angle='π/2'):
    return {'type': 'θ', 'angle': angle}

# CNOT: entangle control and target registers
def cnot(control, target):
    if control == '1':
        return pauli_x(target)
    return target

def cz(control, target):
    if control == '1':
        return pauli_z(target)
    return target

def swap(a, b):
    return b, a

def toffoli(ctrl1, ctrl2, target):
    if ctrl1 == '1' and ctrl2 == '1':
        return pauli_x(target)
    return target

def fredkin(ctrl, a, b):
    if ctrl == '1':
        return b, a
    return a, b

# Controlled rotation
def crx(ctrl, target, angle='π/6'):
    if ctrl == '1':
        return rx(target, angle)
    return target

def cry(ctrl, target, angle='π/8'):
    if ctrl == '1':
        return ry(target, angle)
    return target

def crz(ctrl, target, angle='π/12'):
    if ctrl == '1':
        return rz(target, angle)
    return target
