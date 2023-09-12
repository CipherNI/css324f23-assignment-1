def initial_state():
    return (8, 0, 0)

def is_goal(s):
    a, b, c = s
    return a == 4 and b == 4

def successors(s):
    a, b, c = s
    # List to store successor states and step costs
    successors = []

    # Pour from a to b
    pour = min(a, 5 - b)
    if pour > 0:
        successors.append(((a - pour, b + pour, c), pour))

    # Pour from a to c
    pour = min(a, 3 - c)
    if pour > 0:
        successors.append(((a - pour, b, c + pour), pour))

    # Pour from b to a
    pour = min(b, 8 - a)
    if pour > 0:
        successors.append(((a + pour, b - pour, c), pour))

    # Pour from b to c
    pour = min(b, 3 - c)
    if pour > 0:
        successors.append(((a, b - pour, c + pour), pour))

    # Pour from c to a
    pour = min(c, 8 - a)
    if pour > 0:
        successors.append(((a + pour, b, c - pour), pour))

    # Pour from c to b
    pour = min(c, 5 - b)
    if pour > 0:
        successors.append(((a, b + pour, c - pour), pour))

    return successors
