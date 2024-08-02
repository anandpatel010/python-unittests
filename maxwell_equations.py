class MaxwellEquations:
    def gauss_law_electric(self, divergence_E: float, charge_density: float) -> bool:
        # Gauss's law: ∇·E = ρ
        # For simplicity, assume ε_0 = 1 in the vacuum.
        return divergence_E == charge_density

    def gauss_law_magnetic(self, divergence_B: float) -> bool:
        # Gauss's law for magnetism: ∇·B = 0
        return divergence_B == 0

    def faradays_law(self, curl_E: float, negative_partial_B_partial_t: float) -> bool:
        # Faraday's law: ∇×E = -∂B/∂t
        return curl_E == negative_partial_B_partial_t

    def ampere_maxwell_law(self, curl_B: float, mu_0_J_plus_mu_0_epsilon_0_partial_E_partial_t: float) -> bool:
        # Ampère's law (with Maxwell's correction): ∇×B = μ₀(J + ε₀ ∂E/∂t)
        return curl_B == mu_0_J_plus_mu_0_epsilon_0_partial_E_partial_t
