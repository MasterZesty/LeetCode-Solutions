# Write your MySQL query statement below
select
sample_id,
dna_sequence,
species,
dna_sequence regexp '^ATG' as has_start,
dna_sequence regexp '(TAA|TAG|TGA)$' as has_stop,
dna_sequence regexp 'ATAT+' as has_atat,
dna_sequence regexp 'G{3,}' as has_ggg
from
samples
-- https://regex101.com/

order by sample_id