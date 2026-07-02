from pathlib import Path

from parser import csv_to_json


DATA_DIR = Path("data")


def main() -> None:
    csv_to_json(
        DATA_DIR / "volcanos.csv",
        DATA_DIR / "volcanos.json",
    )


if __name__ == "__main__":
    main()
