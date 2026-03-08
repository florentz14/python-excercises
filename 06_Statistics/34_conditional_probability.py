# -------------------------------------------------
# File Name: 34_conditional_probability.py
# Description: Applies conditional-probability formula P(A|B)=P(A∩B)/P(B) in a simple example.
# -------------------------------------------------

# P(A|B) = P(A and B) / P(B)
# Example: P(rain | clouds)
p_clouds = 0.4 # probability of clouds
p_rain_and_clouds = 0.2 # probability of rain and clouds
p_rain_given_clouds = p_rain_and_clouds / p_clouds # probability of rain given clouds

print("=== CONDITIONAL PROBABILITY ===") # Conditional probability
print("P(A|B) = P(A ∩ B) / P(B)") # P(A|B) = P(A ∩ B) / P(B)
print()
print("Example: P(rain | clouds)") # Example: P(rain | clouds)
print(f"  P(clouds) = {p_clouds}") # print the probability of clouds
print(f"  P(rain ∩ clouds) = {p_rain_and_clouds}") # print the probability of rain and clouds
print(f"  P(rain | clouds) = P(rain ∩ clouds) / P(clouds) = {p_rain_given_clouds}") # print the probability of rain given clouds
