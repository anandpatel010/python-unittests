class PotentialEnergyCalculator:
    def gravitational_potential_energy(self, mass: float, gravity: float, height: float) -> float:
        return mass * gravity * height

    def elastic_potential_energy(self, spring_constant: float, displacement: float) -> float:
        return 0.5 * spring_constant * displacement**2
