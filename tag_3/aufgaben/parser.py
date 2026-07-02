import json
from pathlib import Path


def csv_to_json(csv_file: Path, json_file: Path) -> None:
    volcanos: list[dict[str, str]] = []

    with open(csv_file, encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines[1:]:
        line = line.strip()

        if not line:
            continue

        data = line.split(",")

        volcano = {
            "name": data[1],
            "country": data[2],
            "region": data[3],
            "lat": data[5],
            "long": data[6],
            "risk": data[12],
        }

        volcanos.append(volcano)

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(volcanos, f, indent=4)
