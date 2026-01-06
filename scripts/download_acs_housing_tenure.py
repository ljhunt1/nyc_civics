#!/usr/bin/env python3
"""Download ACS housing tenure data for NYC boroughs from the Census API."""

import argparse
import requests
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"

# NYC borough FIPS codes (State 36 = NY)
NYC_COUNTIES = {
    "Bronx": "005",
    "Brooklyn": "047",  # Kings County
    "Manhattan": "061",  # New York County
    "Queens": "081",
    "Staten Island": "085",  # Richmond County
}

# ACS variables for housing tenure (Table B25003)
TENURE_VARS = {
    "B25003_001E": "total_occupied_units",
    "B25003_002E": "owner_occupied",
    "B25003_003E": "renter_occupied",
}


def download_acs_housing_tenure(year: int = 2023):
    """Download ACS 1-year tenure data for NYC boroughs.

    Args:
        year: ACS 1-year estimate year (e.g., 2023)
    """
    DATA_DIR.mkdir(exist_ok=True)

    base_url = f"https://api.census.gov/data/{year}/acs/acs1"
    variables = ",".join(TENURE_VARS.keys())

    # Fetch all NYC counties in one request
    county_fips = ",".join(NYC_COUNTIES.values())
    params = {
        "get": f"NAME,{variables}",
        "for": f"county:{county_fips}",
        "in": "state:36",
    }

    print(f"Fetching ACS {year} 1-year estimates for NYC boroughs...")
    response = requests.get(base_url, params=params)
    response.raise_for_status()

    data = response.json()
    headers = data[0]
    rows = data[1:]

    # Build DataFrame
    df = pd.DataFrame(rows, columns=headers)

    # Add borough names
    fips_to_borough = {v: k for k, v in NYC_COUNTIES.items()}
    df["borough"] = df["county"].map(fips_to_borough)

    # Rename and convert columns
    df = df.rename(columns=TENURE_VARS)
    for col in TENURE_VARS.values():
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Add year column
    df["year"] = year

    # Reorder columns
    df = df[["year", "borough", "NAME", "state", "county"] + list(TENURE_VARS.values())]

    # Save
    output_path = DATA_DIR / f"acs_housing_tenure_{year}.csv"
    df.to_csv(output_path, index=False)

    print(f"Saved to {output_path}")
    print(f"\nACS {year} 1-Year Estimates - Housing Tenure:")
    print(df[["borough"] + list(TENURE_VARS.values())].to_string(index=False))

    return df


def main():
    parser = argparse.ArgumentParser(description="Download ACS housing tenure data for NYC")
    parser.add_argument(
        "--year", "-y",
        type=int,
        default=2023,
        help="ACS 1-year estimate year (default: 2023)"
    )
    args = parser.parse_args()

    download_acs_housing_tenure(year=args.year)


if __name__ == "__main__":
    main()
