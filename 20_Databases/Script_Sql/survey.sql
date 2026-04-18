-- =============================================================
--  survey.db  |  Extended & Optimized Schema
--  SQLite 3.x  |  Inspired by Portal Project ecology data
-- =============================================================

PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;

-- -------------------------------------------------------------
-- 1. CATALOG: plots
--    Replaces the bare integer plot_id with full metadata.
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS plots (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    code        TEXT    NOT NULL UNIQUE,    -- e.g. 'P01', 'CTRL-A'
    treatment   TEXT    NOT NULL            -- e.g. 'control', 'exclosure', 'removal'
                CHECK  (treatment IN ('control', 'exclosure', 'removal', 'spectab exclosure')),
    area_ha     REAL,                       -- plot area in hectares
    latitude    REAL,
    longitude   REAL
);

-- -------------------------------------------------------------
-- 2. CATALOG: species
--    Replaces the bare TEXT species_id with taxonomic detail.
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS species (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    code         TEXT    NOT NULL UNIQUE,   -- original 2-char code, e.g. 'NL', 'DM'
    genus        TEXT    NOT NULL,
    species_name TEXT    NOT NULL,          -- specific epithet
    taxa_order   TEXT,                      -- taxonomic order
    family       TEXT,
    common_name  TEXT,
    UNIQUE (genus, species_name)
);

-- -------------------------------------------------------------
-- 3. MAIN TABLE: surveys  (normalized + optimized)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS surveys (
    id               INTEGER  PRIMARY KEY AUTOINCREMENT,

    -- DATE: single column instead of three separate integers
    survey_date      DATE     NOT NULL,

    -- FOREIGN KEYS (with integrity enforced)
    plot_id          INTEGER  REFERENCES plots(id)   ON UPDATE CASCADE ON DELETE SET NULL,
    species_id       INTEGER  REFERENCES species(id) ON UPDATE CASCADE ON DELETE SET NULL,

    -- VALIDATED categorical field
    sex              TEXT     CHECK (sex IN ('M', 'F', 'U')),  -- U = unknown

    -- MEASUREMENTS with range guards
    hindfoot_length  REAL     CHECK (hindfoot_length > 0 AND hindfoot_length < 100),
    weight           REAL     CHECK (weight > 0 AND weight < 2000),

    -- AUDIT
    notes            TEXT,
    created_at       DATETIME NOT NULL DEFAULT (datetime('now'))
);

-- -------------------------------------------------------------
-- 4. INDEXES for common query patterns
-- -------------------------------------------------------------
CREATE INDEX IF NOT EXISTS idx_surveys_date        ON surveys(survey_date);
CREATE INDEX IF NOT EXISTS idx_surveys_plot        ON surveys(plot_id);
CREATE INDEX IF NOT EXISTS idx_surveys_species     ON surveys(species_id);
CREATE INDEX IF NOT EXISTS idx_surveys_plot_date   ON surveys(plot_id, survey_date);
CREATE INDEX IF NOT EXISTS idx_surveys_species_sex ON surveys(species_id, sex);

-- -------------------------------------------------------------
-- 5. VIEW: enriched_surveys
--    Joins everything for easy consumption without repeating JOINs.
-- -------------------------------------------------------------
CREATE VIEW IF NOT EXISTS enriched_surveys AS
SELECT
    s.id,
    s.survey_date,
    -- formatted date parts for backwards-compat or reporting
    CAST(strftime('%Y', s.survey_date) AS INTEGER) AS year,
    CAST(strftime('%m', s.survey_date) AS INTEGER) AS month,
    CAST(strftime('%d', s.survey_date) AS INTEGER) AS day,
    -- plot info
    p.id           AS plot_id,
    p.code         AS plot_code,
    p.treatment    AS plot_treatment,
    -- species info
    sp.id          AS species_id,
    sp.code        AS species_code,
    sp.genus,
    sp.species_name,
    sp.common_name,
    -- observation
    s.sex,
    s.hindfoot_length,
    s.weight,
    s.notes,
    s.created_at
FROM surveys s
LEFT JOIN plots   p  ON p.id  = s.plot_id
LEFT JOIN species sp ON sp.id = s.species_id;

-- =============================================================
--  SEED DATA
-- =============================================================

INSERT OR IGNORE INTO plots (code, treatment) VALUES
('P01', 'control'),
('P02', 'exclosure'),
('P03', 'removal'),
('P04', 'spectab exclosure');

INSERT OR IGNORE INTO species (code, genus, species_name, taxa_order, family, common_name) VALUES
('NL', 'Neotoma',    'albigula',    'Rodentia', 'Cricetidae',  'White-throated woodrat'),
('DM', 'Dipodomys',  'merriami',    'Rodentia', 'Heteromyidae','Merriam kangaroo rat'),
('PE', 'Peromyscus', 'eremicus',    'Rodentia', 'Cricetidae',  'Cactus mouse'),
('PP', 'Chaetodipus','penicillatus','Rodentia', 'Heteromyidae','Desert pocket mouse'),
('OT', 'Onychomys',  'torridus',    'Rodentia', 'Cricetidae',  'Southern grasshopper mouse');

INSERT INTO surveys (survey_date, plot_id, species_id, sex, hindfoot_length, weight) VALUES
('2001-07-16', 1, 'NL', 'M', 32.0, NULL),
('2001-07-16', 1, 'NL', 'F', 33.0, 87.0),
('2002-07-16', 2, 'DM', 'F', 37.0, 52.0),
('2002-07-16', 2, 'DM', 'M', 36.0, 48.0),
('2002-09-20', 3, 'PE', 'F', 20.0,  8.0),
('2002-09-20', 3, 'DM', 'M', 35.0, 50.0),
('2002-04-10', 1, 'NL', 'M', 31.5, 90.0),
('2003-06-05', 4, 'PP', 'M', 15.0,  6.5),
('2003-06-05', 4, 'DM', 'F', 38.0, 55.0),
('2003-12-01', 2, 'OT', 'F', 22.0, 25.0);

-- =============================================================
--  SAMPLE QUERIES
-- =============================================================

-- Promedio de peso por especie y sexo
-- SELECT genus, common_name, sex,
--        ROUND(AVG(weight), 2)          AS avg_weight_g,
--        ROUND(AVG(hindfoot_length), 2) AS avg_hindfoot_mm,
--        COUNT(*)                       AS n
-- FROM enriched_surveys
-- WHERE weight IS NOT NULL
-- GROUP BY species_id, sex
-- ORDER BY genus, sex;

-- Riqueza de especies por plot y año
-- SELECT plot_code, year,
--        COUNT(DISTINCT species_id) AS species_richness,
--        COUNT(*)                   AS total_records
-- FROM enriched_surveys
-- GROUP BY plot_id, year
-- ORDER BY year, plot_code;

-- Registros sin peso (NULL weight) por especie
-- SELECT species_id, common_name, COUNT(*) AS missing_weight
-- FROM enriched_surveys
-- WHERE weight IS NULL
-- GROUP BY species_id;