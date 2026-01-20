P_spam = 0.20          
P_free_given_spam = 0.60  
P_free = 0.30          
P_spam_given_free = (P_free_given_spam * P_spam) / P_free
print("Bayes' Theorem: Spam Email Detection\n")
print("P(Spam) =", P_spam)
print("P(Free | Spam) =", P_free_given_spam)
print("P(Free) =", P_free)
print("\nProbability that an email is spam given it contains 'free':")
print("P(Spam | Free) =", round(P_spam_given_free, 2))
print("\nInterpretation:")
print(f"If an email contains the word 'free', there is a {P_spam_given_free*100:.0f}% chance it is spam.")
