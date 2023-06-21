-- gdx2.mv_all source

CREATE MATERIALIZED VIEW gdx2.mv_all
TABLESPACE pg_default
AS SELECT udata2.compname,
    udata2.ext,
    count(udata2.ext) AS count,
    sum(udata2.size) AS size_sum,
    pg_size_pretty(sum(udata2.size)) AS size_pretty
   FROM udata2
  GROUP BY udata2.compname, udata2.ext
 HAVING (udata2.ext::bpchar IN ( SELECT DISTINCT ext.ext
           FROM ext))
  ORDER BY (sum(udata2.size)) DESC
WITH DATA;

-- gdx2.mv_all_projects source

CREATE MATERIALIZED VIEW gdx2.mv_all_projects
TABLESPACE pg_default
AS SELECT udata2.ext,
    count(udata2.ext) AS count,
    sum(udata2.size) AS size_sum,
    pg_size_pretty(sum(udata2.size)) AS size_pretty
   FROM udata2
  GROUP BY udata2.ext
 HAVING (udata2.ext::bpchar IN ( SELECT ext.ext
           FROM ext
          WHERE ext.is_project IS NOT NULL))
  ORDER BY (sum(udata2.size)) DESC
WITH DATA;


-- gdx2.mv_compname source

CREATE MATERIALIZED VIEW gdx2.mv_compname
TABLESPACE pg_default
AS SELECT udata2.compname,
    sum(udata2.size) AS size_sum,
    pg_size_pretty(sum(udata2.size)) AS size_pretty
   FROM udata2
  GROUP BY udata2.compname
  ORDER BY (sum(udata2.size)) DESC
WITH DATA;


-- gdx2.mv_data_in_profile source

CREATE MATERIALIZED VIEW gdx2.mv_data_in_profile
TABLESPACE pg_default
AS SELECT udata2.compname,
    sum(udata2.size) AS size_sum,
    pg_size_pretty(sum(udata2.size)) AS size_pretty
   FROM udata2
  GROUP BY udata2.compname, udata2.is_profile
 HAVING udata2.is_profile = true
  ORDER BY (sum(udata2.size)) DESC
WITH DATA;

-- gdx2.mv_games source

CREATE MATERIALIZED VIEW gdx2.mv_games
TABLESPACE pg_default
AS SELECT udata2.compname,
    udata2.folder,
    udata2.ext
   FROM udata2
  WHERE (udata2.folder ~~ '%game%'::text OR udata2.folder ~~ '%игры%'::text OR udata2.folder ~~ '%игра%'::text) AND udata2.ext::text ~~ 'exe'::text AND udata2.folder !~~ '%C:\Windows\%'::text
  ORDER BY udata2.compname
WITH DATA;

-- gdx2.mv_geography source

CREATE MATERIALIZED VIEW gdx2.mv_geography
TABLESPACE pg_default
AS SELECT udata2.compname,
    udata2.ext,
    count(udata2.ext) AS count,
    sum(udata2.size) AS size_sum,
    pg_size_pretty(sum(udata2.size)) AS size_pretty
   FROM udata2
  GROUP BY udata2.compname, udata2.ext
 HAVING (udata2.ext::bpchar IN ( SELECT ext.ext
           FROM ext
          WHERE ext.category ~~ 'geog%'::text))
  ORDER BY (sum(udata2.size)) DESC
WITH DATA;

-- gdx2.mv_geology source

CREATE MATERIALIZED VIEW gdx2.mv_geology
TABLESPACE pg_default
AS SELECT udata2.compname,
    udata2.ext,
    count(udata2.ext) AS count,
    sum(udata2.size) AS size_sum,
    pg_size_pretty(sum(udata2.size)) AS size_pretty
   FROM udata2
  GROUP BY udata2.compname, udata2.ext
 HAVING (udata2.ext::bpchar IN ( SELECT ext.ext
           FROM ext
          WHERE ext.category ~~ 'geol%'::text))
  ORDER BY (sum(udata2.size)) DESC
WITH DATA;

-- gdx2.mv_isoline source

CREATE MATERIALIZED VIEW gdx2.mv_isoline
TABLESPACE pg_default
AS SELECT udata2.compname,
    udata2.ext,
    count(udata2.ext) AS count,
    sum(udata2.size) AS summary,
    pg_size_pretty(sum(udata2.size)) AS pg_size_pretty
   FROM udata2
  GROUP BY udata2.compname, udata2.ext
 HAVING (udata2.ext::bpchar IN ( SELECT ext.ext
           FROM ext
          WHERE ext.product ~~ 'Isoline%'::text OR ext.product ~~ 'Izoline%'::text))
  ORDER BY (sum(udata2.size)) DESC
WITH DATA;

-- gdx2.mv_projects source

CREATE MATERIALIZED VIEW gdx2.mv_projects
TABLESPACE pg_default
AS SELECT udata2.compname,
    udata2.ext,
    count(udata2.ext) AS count,
    sum(udata2.size) AS size_sum,
    pg_size_pretty(sum(udata2.size)) AS size_pretty
   FROM udata2
  GROUP BY udata2.compname, udata2.ext
 HAVING (udata2.ext::bpchar IN ( SELECT ext.ext
           FROM ext
          WHERE ext.is_project IS NOT NULL))
  ORDER BY (sum(udata2.size)) DESC
WITH DATA;