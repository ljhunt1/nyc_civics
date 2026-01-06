# Messing around with NYC civics OpenData

### Env setup

1. Create a Socrata / Tyler account
2. Make an API key, the make a .env like

```
OPENDATA_API_KEY_ID=...
OPENDATA_API_KEY_SECRET=...
```

## Notes on data

- Evictions
  - This includes executed evictions only - meaning evictions that were actually carried out by city marshals, not just filings or court cases. According to claude, some eviction cases might: get dismissed; result in settlements; lead to voluntary move-outs before execution; get withdrawn
    - Per https://council.nyc.gov/data/evictions/: "out of the 230,071 eviction petitions filed by building owners at NYC Housing Court in 2017, only 9% or 20,804 evictions were executed by the City marshall".
    - Each eviction pertains to one eviction case, which means one housing unit, not one individual
  - Methods for "eviction rate" follow https://evictionlab.org/methods/#filings-and-rates
    - Filing rate: (# evictions filed / # renter-occupied homes)
    - Eviction rate: (# executed evictions / # renter occupied-homes). So, for example one might say "the bronx has 1 eviction per 79 renter-occupied units".
    - For the denominator of our rate, we used the number of occupied renting households in each area. Used ACS 1-year estimates for boroughs, 5-year estimates for zips if used (1-year doesn't have that granularity). Eviction lab supplements with ESRI Business Analyst demographic estimates, we don't. 2020 and 2025 are missing, so we use 2019 and 2024 respectively
    - City council uses a different denominator https://council.nyc.gov/data/evictions/#map-guide https://github.com/NewYorkCityCouncil/PA_evictions - they use PLUTO data which is ALL residential units (renter occupied + owner occupied + vacant). To give a sense, units are roughly 2/3 renter occupied, 1/3 owner occupied, 1-2% vacant, so our numbers are 60% higher
    - Here are some other places which visualize eviction data in superior ways
      https://evictionlab.org/eviction-tracking/new-york-ny/
      https://comptroller.nyc.gov/reports/audit-report-on-the-new-york-city-housing-authoritys-eviction-processes/
      https://evictionlab.org/map
      https://evictionlab.org/in-the-most-expensive-city-in-the-country-evictions-remain-lower-than-before-covid-19/
