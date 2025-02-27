{{ config(materialized='view') }}
with base as (
    select
        country_name,                
        population,                    
        area                 
    from countries_data
    where population is not null       
)

select * from base