-- gdx2.file definition

-- Drop table

-- DROP TABLE gdx2.file;

CREATE TABLE gdx2.file (
	id serial4 NOT NULL,
	root_folder text NULL,
	file_path text NULL,
	file_folder text NULL,
	file_name varchar(255) NULL,
	file_ext varchar(11) NULL,
	file_size int8 NULL,
	file_ctime timestamp NULL,
	file_mtime timestamp NULL,
	date_c varchar(11) NULL,
	date_m varchar(11) NULL,
	date_u varchar(11) NULL,
	fpath text NULL,
	fpath_md5 text NULL,
	file_text text NULL,
	field varchar(255) NULL,
	areaoil varchar(255) NULL,
	lu varchar(255) NULL,
	well varchar(255) NULL,
	lat float8 NULL,
	lon float8 NULL,
	report_name text NULL,
	report_text text NULL,
	report_author text NULL,
	report_year int4 NULL,
	report_tgf text NULL,
	is_deleted bool NULL,
	lastupdate timestamp NULL,
	file_path_fts tsvector NULL,
	CONSTRAINT file_pkey PRIMARY KEY (id)
);
CREATE INDEX ix_file_areaoil ON gdx2.file USING btree (areaoil);
CREATE INDEX ix_file_field ON gdx2.file USING btree (field);
CREATE INDEX ix_file_file_ext ON gdx2.file USING btree (file_ext);
CREATE INDEX ix_file_file_folder ON gdx2.file USING btree (file_folder);
CREATE INDEX ix_file_file_name ON gdx2.file USING btree (file_name);
CREATE INDEX ix_file_file_path ON gdx2.file USING btree (file_path);
CREATE INDEX ix_file_lu ON gdx2.file USING btree (lu);
CREATE INDEX ix_file_report_author ON gdx2.file USING btree (report_author);
CREATE INDEX ix_file_report_name ON gdx2.file USING btree (report_name);
CREATE INDEX ix_file_report_year ON gdx2.file USING btree (report_year);
CREATE INDEX ix_file_root_folder ON gdx2.file USING btree (root_folder);
CREATE INDEX ix_file_well ON gdx2.file USING btree (well);