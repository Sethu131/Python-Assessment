def main():
    qty = None
    cost = None


def fetch_quantity():
    """
    Returns a number, any number
    """
    ...
    return ...


def fetch_cost():
    """
    Returns a number, any number
    """
    ...
    return ...


def compute_cost_per_quantity():
    try:
        qty = fetch_quantity()
        cost = fetch_cost()
        cost_per_quantity = cost / qty
        return cost_per_quantity
    except Exception as e:
        print(e)
        exit()


try:
    cost_per_quantity = compute_cost_per_quantity()
    a = 1 + 2 + cost_per_quantity
    b = 4 + 5
    print(a + b)
except Exception as e:
    print(e)
