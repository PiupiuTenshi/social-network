#!/bin/sh
set -eu

provision_database() {
  database_name="$1"
  role_name="$2"
  role_password="$3"

  psql --username "$POSTGRES_USER" --dbname postgres --set ON_ERROR_STOP=1 \
    --set database_name="$database_name" \
    --set role_name="$role_name" \
    --set role_password="$role_password" <<'SQL'
SELECT format('CREATE ROLE %I LOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT PASSWORD %L', :'role_name', :'role_password')
WHERE NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = :'role_name') \gexec
SELECT format('CREATE DATABASE %I OWNER %I', :'database_name', :'role_name')
WHERE NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = :'database_name') \gexec
SELECT format('REVOKE CONNECT ON DATABASE %I FROM PUBLIC', :'database_name') \gexec
SELECT format('GRANT CONNECT ON DATABASE %I TO %I', :'database_name', :'role_name') \gexec
SQL
}

provision_database account_db account_app "$ACCOUNT_DB_PASSWORD"
provision_database social_db social_app "$SOCIAL_DB_PASSWORD"
provision_database chat_db chat_app "$CHAT_DB_PASSWORD"
provision_database feed_db feed_app "$FEED_DB_PASSWORD"
