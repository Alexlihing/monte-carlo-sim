import numpy as np

def monte_carlo_option_price(S0, K, T, r, sigma, n_sim, option_type="call"):
    np.random.seed(42)  # For reproducibility
    Z = np.random.standard_normal(n_sim)
    ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

    if option_type == "call":
        payoffs = np.maximum(ST - K, 0)
    elif option_type == "put":
        payoffs = np.maximum(K - ST, 0)
    else:
        raise ValueError("Option type must be 'call' or 'put'.")

    discounted_payoff = np.exp(-r * T) * np.mean(payoffs)
    return discounted_payoff
