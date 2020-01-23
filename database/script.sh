#!/bin/sh
export PGPASSWORD='123'
pg_dump -h localhost -U test jenkins > /var/log/nodes-usage/dump_$(date +"%Y-%m-%d_%H:%M:%S").sql