import argparse
from althenaxavier import AlthenaXavierEngine

def main():
    parser = argparse.ArgumentParser(description="AlthenaXavier Data Engine")
    parser.add_argument("file", help="CSV file path")
    parser.add_argument("--op", required=True, help="Operation: sum, mean, min, max, count")
    parser.add_argument("--column", required=True, help="Column name")

    args = parser.parse_args()

    engine = AlthenaXavierEngine()
    result = engine.process(args.file, args.op, args.column)

    print("\nResult:", result)
    print("✓ Operation completed successfully")

if __name__ == "__main__":
    main()
