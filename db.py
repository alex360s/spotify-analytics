import sqlite3
connect = sqlite3.connect('spotik.db')
cur = connect.cursor()
cur.executescript(
"""
CREATE TABLE IF NOT EXISTS artist_stats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    artist_id TEXT NOT NULL,
    name TEXT NOT NULL,
    followers INTEGER NOT NULL,
    popularity INTEGER NOT NULL,
    genres TEXT,
    image_url TEXT,
    spotify_url TEXT,
    raw_json TEXT NOT NULL,
    collected_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_artist_id
    ON artist_stats (artist_id);

CREATE INDEX IF NOT EXISTS idx_artist_time
    ON artist_stats (artist_id, collected_at);
""")
connect.commit()
connect.close()