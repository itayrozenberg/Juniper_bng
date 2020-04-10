# Juniper_bng
Created op script for showing the pool list on juniers bgp easyer

just install bnp_pools.py to /var/db/scripts/op

then add this config:
set system scripts op file bng_pools.py command pools
set system scripts op file bng_pools.py description "show bng pools"
set system scripts language python

