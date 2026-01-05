#!/usr/bin/env python3
"""Download datasets from NYC OpenData."""

import argparse
import os
import requests
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

DATA_DIR = Path(__file__).parent / "data"
BASE_URL = "https://data.cityofnewyork.us"

# Auth credentials
API_KEY_ID = os.getenv("OPENDATA_API_KEY_ID")
API_KEY_SECRET = os.getenv("OPENDATA_API_KEY_SECRET")

# Known datasets (add more as needed)
DATASETS = {
    "evictions": "6z8x-wfk4",
}


def download_dataset(dataset_id: str, name: str | None = None, format: str = "csv"):
    """Download a dataset from NYC OpenData.

    Args:
        dataset_id: The Socrata dataset ID (e.g., "6z8x-wfk4")
        name: Optional name for the output file (defaults to dataset_id)
        format: "csv" or "json"
    """
    DATA_DIR.mkdir(exist_ok=True)

    if format == "csv":
        url = f"{BASE_URL}/api/views/{dataset_id}/rows.csv?accessType=DOWNLOAD"
    else:
        url = f"{BASE_URL}/resource/{dataset_id}.json?$limit=50000"

    print(f"Downloading {dataset_id} as {format}...")

    response = requests.get(
        url,
        auth=(API_KEY_ID, API_KEY_SECRET) if API_KEY_ID else None,
        stream=True
    )
    response.raise_for_status()

    filename = f"opendata_{name or dataset_id}"
    output_path = DATA_DIR / f"{filename}.{format}"

    with open(output_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    size_mb = output_path.stat().st_size / 1024 / 1024
    print(f"Saved to {output_path} ({size_mb:.2f} MB)")
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Download NYC OpenData datasets")
    parser.add_argument(
        "dataset",
        help="Dataset name (from known list) or Socrata dataset ID"
    )
    parser.add_argument(
        "--format", "-f",
        choices=["csv", "json"],
        default="csv",
        help="Output format (default: csv)"
    )
    parser.add_argument(
        "--name", "-n",
        help="Output filename (without extension, will be prefixed with 'opendata_')"
    )
    args = parser.parse_args()

    # Resolve dataset name to ID if it's a known dataset
    dataset_id = DATASETS.get(args.dataset, args.dataset)
    name = args.name or (args.dataset if args.dataset in DATASETS else None)

    download_dataset(dataset_id, name=name, format=args.format)


if __name__ == "__main__":
    main()
