-- Portal surveys sample (used by 10_survey.py, 11_survey.py)
-- Inspired by ecology-style survey tables: plot, species, measurements by date.

CREATE TABLE IF NOT EXISTS surveys (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL,
    year INTEGER NOT NULL,
    plot_id INTEGER,
    species_id TEXT,
    sex TEXT,
    hindfoot_length REAL,
    weight REAL
);

INSERT INTO surveys (month, day, year, plot_id, species_id, sex, hindfoot_length, weight) VALUES
(7, 16, 2001, 1, 'NL', 'M', 32.0, NULL),
(7, 16, 2001, 1, 'NL', 'F', 33.0, 87.0),
(7, 16, 2002, 2, 'DM', 'F', 37.0, 52.0),
(7, 16, 2002, 2, 'DM', 'M', 36.0, 48.0),
(9, 20, 2002, 3, 'PE', 'F', 20.0, 8.0),
(9, 20, 2002, 3, 'DM', 'M', 35.0, 50.0),
(4, 10, 2002, 1, 'NL', 'M', 31.5, 90.0),
(6, 5, 2003, 4, 'PP', 'M', 15.0, 6.5),
(6, 5, 2003, 4, 'DM', 'F', 38.0, 55.0),
(12, 1, 2003, 2, 'OT', 'F', 22.0, 25.0);
