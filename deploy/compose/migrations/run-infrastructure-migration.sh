#!/bin/sh
set -eu

case "${TARGET_DATABASE:?TARGET_DATABASE is required}" in
  account_db) lock_key=410001 ;;
  social_db) lock_key=410002 ;;
  chat_db) lock_key=410003 ;;
  feed_db) lock_key=410004 ;;
  *) echo "TARGET_DATABASE must be one of account_db, social_db, chat_db, feed_db" >&2; exit 64 ;;
esac

case "$TARGET_DATABASE" in
  account_db) migration_user=account_app; migration_password="$ACCOUNT_DB_PASSWORD" ;;
  social_db) migration_user=social_app; migration_password="$SOCIAL_DB_PASSWORD" ;;
  chat_db) migration_user=chat_app; migration_password="$CHAT_DB_PASSWORD" ;;
  feed_db) migration_user=feed_app; migration_password="$FEED_DB_PASSWORD" ;;
esac

export PGPASSWORD="$migration_password"
psql --host postgres --username "$migration_user" --dbname "$TARGET_DATABASE" --set ON_ERROR_STOP=1 \
  --set lock_key="$lock_key" \
  --set migration_id="${MIGRATION_ID:-infra-bootstrap-v1}" \
  --set hold_seconds="${MIGRATION_LOCK_HOLD_SECONDS:-0}" <<'SQL'
BEGIN;
SELECT pg_try_advisory_xact_lock(CAST(:'lock_key' AS bigint)) AS lock_acquired \gset
\if :lock_acquired
  CREATE TABLE IF NOT EXISTS infrastructure_migration_ledger (
    migration_id text PRIMARY KEY,
    applied_at timestamptz NOT NULL DEFAULT now()
  );
  INSERT INTO infrastructure_migration_ledger (migration_id)
  VALUES (:'migration_id')
  ON CONFLICT (migration_id) DO NOTHING;
  SELECT pg_sleep(CAST(:'hold_seconds' AS integer));
  COMMIT;
\else
  ROLLBACK;
  SELECT 1 / 0;
\endif
SQL
