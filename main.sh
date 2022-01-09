#!/bin/bash
#set -e
#
#psql -v <<-EOSQL
#    CREATE DATABASE bills;
#EOSQL

python /backend/plataforma/manage.py migrate
python /backend/plataforma/manage.py runserver
