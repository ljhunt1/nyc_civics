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
    - "Eviction rate" is calculated as (# executed evictions / # total residential units). So, for example one might say "the bronx has 1 eviction per 79 units".
