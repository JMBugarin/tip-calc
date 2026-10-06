"""Split a restaurant bill with tip: python tip.py 84.50 --tip 20 --people 3"""
import argparse


def split_bill(amount: float, tip_percent: float = 18, people: int = 1) -> dict:
    if amount < 0 or tip_percent < 0 or people < 1:
        raise ValueError("amount and tip must be >= 0, people must be >= 1")
    tip = round(amount * tip_percent / 100, 2)
    total = round(amount + tip, 2)
    return {"tip": tip, "total": total, "per_person": round(total / people, 2)}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("amount", type=float)
    p.add_argument("--tip", type=float, default=18, help="tip percent (default 18)")
    p.add_argument("--people", type=int, default=1)
    a = p.parse_args()
    r = split_bill(a.amount, a.tip, a.people)
    print(f"Tip: ${r['tip']:.2f}  Total: ${r['total']:.2f}  Each: ${r['per_person']:.2f}")


if __name__ == "__main__":
    main()
