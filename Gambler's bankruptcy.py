# Gambler's bankruptcy.py
# Gambler's Ruin Probability (Mathematical Solution)

import sys

def ruin_probability_math(x, N, p):
    q = 1 - p

    # fair game case (p = q = 0.5)
    if p == 0.5:
        return 1 - (x / N)

    # unfair game
    r = q / p
    return (r**x - r**N) / (1 - r**N)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python \"Gambler's bankruptcy.py\" <initial_money> <goal_money> <p_win>")
        sys.exit(1)

    x = int(sys.argv[1])
    N = int(sys.argv[2])
    p = float(sys.argv[3])

    result = ruin_probability_math(x, N, p)
    print(f"Probability of ruin: {result:.6f}")
