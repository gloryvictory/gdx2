-- gdx2.v_all_projects source

CREATE OR REPLACE VIEW gdx2.v_all_projects
AS SELECT ext.description,
    mv_all_projects.ext,
    mv_all_projects.count,
    mv_all_projects.size_sum,
    mv_all_projects.size_pretty
   FROM mv_all_projects,
    ext
  WHERE mv_all_projects.ext::bpchar = ext.ext;


-- gdx2.v_compname source

CREATE OR REPLACE VIEW gdx2.v_compname
AS SELECT mv_compname.compname,
    mv_compname.size_sum,
    mv_compname.size_pretty
   FROM mv_compname;

-- gdx2.v_data_in_profile source

CREATE OR REPLACE VIEW gdx2.v_data_in_profile
AS SELECT mv_data_in_profile.compname,
    mv_data_in_profile.size_sum,
    mv_data_in_profile.size_pretty
   FROM mv_data_in_profile;

-- gdx2.v_games source

CREATE OR REPLACE VIEW gdx2.v_games
AS SELECT mv_games.compname,
    mv_games.folder,
    mv_games.ext
   FROM mv_games;


-- gdx2.v_geography source

CREATE OR REPLACE VIEW gdx2.v_geography
AS SELECT mv_geography.compname,
    mv_geography.ext,
    mv_geography.count,
    mv_geography.size_sum,
    mv_geography.size_pretty
   FROM mv_geography;

-- gdx2.v_geology source

CREATE OR REPLACE VIEW gdx2.v_geology
AS SELECT mv_geology.compname,
    mv_geology.ext,
    mv_geology.count,
    mv_geology.size_sum,
    mv_geology.size_pretty
   FROM mv_geology;