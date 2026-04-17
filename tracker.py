import argparse

def parse_args()-> argparse.Namespace:
    """Parse Command Line Arguments"""
    parser = argparse.ArgumentParser(description = "Expense Tracker")
    return parser.parse_args()

def main() -> None:
    """Entry point for the Application"""
    args = parse_args()
    print(args)

if __name__ == "__main__":
    main()

