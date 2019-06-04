#!/bin/bash

if [ ! -d rems ]
then
    git clone https://github.com/cscfi/rems
fi
cd rems
git checkout dff865e

# wait until postgres is up and running
while ! psql -h 0.0.0.0 -U postgres -c 'select 1;' 2>/dev/null
do
    echo "Postgres not up yet..."
    sleep 5
done

# create tables
psql -h 0.0.0.0 -U postgres < resources/sql/init.sql

# create schema
lein run migrate

# populate database w/ test data
lein run test-data

cd ..
mkdir -p rems_test_data
pg_dumpall -U postgres -h 0.0.0.0 \
    | egrep -v '^(CREATE|DROP) ROLE postgres;' \
    > postgres_test_data/001_restore.sql
