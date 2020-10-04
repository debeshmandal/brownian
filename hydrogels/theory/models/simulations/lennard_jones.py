from ..integrator import Simulation, Equation
import potentials
import functions

class LennardJones(Simulation):
    def __init__(self, dt, N, **constants):
        super().__init__(
            dt, 
            constants = {
                'sig' : constants['sig'],
                'eps' : constants['eps'],
                'rc' : constants['rc'], 
                'beta' : constants['beta'],
                'c0' : constants['c0'],
                'KV' : constants['KV'],
                'nV' : constants['nV']
            },
            variables = {
                'N' : N,
                'R' : None,
                'V' : None,
                'k' : None
            },
            equations= self.equations
        )

    @property
    def potential(self) -> Equation:
        def func(sig: float = 1., eps: float =1., rc: float = 5.0, R: float = 2.0) -> 'V':
            """ Lennard-Jones 12-6"""
            return potentials.lennard_jones(sig, eps, rc, R)
        return Equation(func, string=func.__doc__)

    @property
    def equations(self) -> list:
        def radius(N: int = 0, nV: float = 1.0) -> 'R':
            """Radius from number of particles and density"""
            return functions.radius_from_number(N, nV)

        def rate(V: float = 0.0, beta: float = 1.0, KV: float = 1.0, c0: float = 1.0) -> 'k':
            """rate from potential, concentratin and rate of encounter"""
            return functions.rate_from_potential_energy(KV, c0, V, beta)

        def number(N: int = 0, k: float = 1.0, dt: float = 1.0) -> 'N':
            """New number from old number and rate"""
            return functions.update_number_from_rate(N, k, dt)

        return [
            Equation(radius, string=radius.__doc__),
            self.potential,
            Equation(rate, string=rate.__doc__),
            Equation(number, string=number.__doc__),
        ]