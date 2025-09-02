PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS videos (
  id TEXT PRIMARY KEY,                -- UUID
  original_name TEXT NOT NULL,
  original_ext TEXT NOT NULL,
  mime_type TEXT,
  size_bytes INTEGER NOT NULL,

  duration_sec REAL,
  fps REAL,
  width INTEGER,
  height INTEGER,

  filter TEXT NOT NULL,
  created_at TEXT NOT NULL DEFAULT (datetime('now','utc')),

  path_original TEXT NOT NULL,
  path_processed TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_videos_created_at ON videos(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_videos_filter ON videos(filter);
