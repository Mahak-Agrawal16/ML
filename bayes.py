def bayes_theorem(prior, likelihood, evidence):
    """
    Calculate posterior probability using Bayes' Theorem.
    """
    return (likelihood * prior) / evidence
print("Bayes' Theorem Calculator\n")
prior = float(input("Enter Prior Probability P(A): "))
likelihood = float(input("Enter Likelihood P(B|A): "))
false_positive = float(input("Enter False Positive Rate P(B|¬A): "))
no_event = 1 - prior
evidence = (likelihood * prior) + (false_positive * no_event)
posterior = bayes_theorem(prior, likelihood, evidence)
print("\n🔹 Bayes' Theorem Formula")
print("P(A|B) = [ P(B|A) × P(A) ] / P(B)\n")
print("Prior (P(A))        =", prior)
print("Likelihood (P(B|A)) =", likelihood)
print("Evidence (P(B))     =", round(evidence, 4))
print("Posterior (P(A|B))  =", round(posterior, 4))
print("\nInterpretation:")
print(f"After observing the evidence, the updated probability is {posterior:.2%}.")
