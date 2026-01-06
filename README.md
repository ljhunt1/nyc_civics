# Messing around with NYC civics OpenData

### Env setup

1. Create a Socrata / Tyler account
2. Make an API key, the make a .env like

```
OPENDATA_API_KEY_ID=...
OPENDATA_API_KEY_SECRET=...
```

### TODO

1. Create an OpenData account, store key locally somewhere safe
2. Create scripts for hitting SODA3 apis

### Notes for myself on the OpenData APIs

- Provided by Socrata (business to gov tech company), which was bought by Tyler technologies (-> Data and Insights division of Tyler)
- SODA3 APIs https://support.socrata.com/hc/en-us/articles/34730618169623-SODA3-API, query with SoQL

### Misc Thoughts

- I actually really like "software engineering" not just "LLM learning"
- It is really nice to do this solo lol

## Notes on data

- Evictions
  - This includes executed evictions only - meaning evictions that were actually carried out by city marshals, not just filings or court cases. According to claude, some eviction cases might: get dismissed; result in settlements; lead to voluntary move-outs before execution; get withdrawn
    - Per https://council.nyc.gov/data/evictions/: "out of the 230,071 eviction petitions filed by building owners at NYC Housing Court in 2017, only 9% or 20,804 evictions were executed by the City marshall".
    - Each eviction pertains to one eviction case, which means one housing unit, not one individual
  - Methods for "eviction rate" follow https://evictionlab.org/methods/#filings-and-rates
    - Filing rate: (# evictions filed / # renter-occupied homes)
    - Eviction rate: (# executed evictions / # renter occupied-homes). So, for example one might say "the bronx has 1 eviction per 79 units".
    - The filing rate also counts all eviction cases filed in an area, including multiple cases filed against the same address in the same year. But an eviction rate only counts a single address who received an eviction judgment.
    - For the denominator of our rate, we used the number of occupied renting households in each area. Used ACS 1-year estimates for boroughs, 5-year estimates for zips (1-year doesn't have that granularity). Eviction lab supplements with ESRI Business Analyst demographic estimates, we don't. 2020 and 2025 are missing, so we use 2019 and 2024 respectively
- Other sources of data vis
  https://evictionlab.org/eviction-tracking/new-york-ny/

- Housing units (by month/quarter/year, by zipcode/borough):

* Possible source: DCP Housing Database? https://data.cityofnewyork.us/Housing-Development/Housing-Database/6umk-irkx/about_data
* Possible source: Pluto? https://data.cityofnewyork.us/City-Government/Primary-Land-Use-Tax-Lot-Output-PLUTO-/64uk-42ks
* Possible source: annual census, NYC Housing and Vacancy Survey? https://www.nyc.gov/assets/hpd/downloads/pdfs/about/2023-nychvs-selected-initial-findings.pdf
