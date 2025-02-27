{{ config(materialized='table') }}

with base as (
    select
        country_name,                   -- Common name of the country
        official_country_name,                 -- Official name of the country
        capital,                       -- Capital city
        region,                        -- Region of the country
        subregion,                     -- Subregion of the country
        languages,                       --  to handle multiple language
        currency_code,                 -- Currency code
        currency_name,                 -- Currency name
        currency_symbol,               -- Currency symbol
        continents                  -- When the record was last updated
    from countries_data                   -- Refers to your raw country data table
)

select * from base