from engine import monte_carlo_option_price
from black_scholes import black_scholes_price

def get_input():
    S0 = float(input("Enter initial stock price (S0): "))
    K = float(input("Enter strike price (K): "))
    T = float(input("Enter time to maturity in years (T): "))
    r = float(input("Enter risk-free rate (r): "))
    sigma = float(input("Enter volatility (σ): "))
    n_sim = int(input("Enter number of simulations: "))
    option_type = input("Option type ('call' or 'put'): ").lower()
    return S0, K, T, r, sigma, n_sim, option_type

def main():
    print("Monte Carlo Option Pricing Engine")
    S0, K, T, r, sigma, n_sim, option_type = get_input()

    mc_price = monte_carlo_option_price(S0, K, T, r, sigma, n_sim, option_type)
    bs_price = black_scholes_price(S0, K, T, r, sigma, option_type)

    print(f"\nMonte Carlo {option_type.capitalize()} Price: {mc_price:.4f}")
    print(f"Black-Scholes {option_type.capitalize()} Price: {bs_price:.4f}")

if __name__ == "__main__":
    main()
