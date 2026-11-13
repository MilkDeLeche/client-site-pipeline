-- Capture tables (pipeline live showcase standard). The Worker runs this
-- schema itself before its first insert, because `wrangler deploy` does not
-- apply migrations. Keep every statement idempotent.

CREATE TABLE IF NOT EXISTS subscribers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT NOT NULL UNIQUE,
  first_name TEXT,
  locale TEXT,
  source TEXT,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

-- `fields` holds this client's own form fields as JSON: the request form is
-- designed per client, so its fields are not fixed columns.
CREATE TABLE IF NOT EXISTS inquiries (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created_at TEXT NOT NULL,
  name TEXT NOT NULL,
  email TEXT,
  phone TEXT,
  message TEXT,
  fields TEXT,
  locale TEXT,
  source TEXT,
  delivered_at TEXT
);
