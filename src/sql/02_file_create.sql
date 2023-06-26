-- gdx2.file definition

-- Drop table

-- DROP TABLE gdx2.file;

CREATE TABLE gdx2.file (
	id serial4 NOT NULL,
	f_root text NULL,
	f_path text NULL,
	f_folder text NULL,
	f_name varchar(255) NULL,
	f_ext varchar(255) NULL,
	f_size int8 NULL,
	f_ctime timestamp NULL,
	f_mtime timestamp NULL,
	f_atime timestamp NULL,
	f_path_md5 text NULL,
	f_text text NULL,
	ngp varchar(255) NULL,
	ngo varchar(255) NULL,
	ngr varchar(255) NULL,
	field varchar(255) NULL,
	areaoil varchar(255) NULL,
	lu varchar(255) NULL,
	lu_num varchar(255) NULL,
	well varchar(255) NULL,
	lat float8 NULL,
	lon float8 NULL,
	report_id int4 NULL,
	report_name text NULL,
	report_text text NULL,
	report_author text NULL,
	report_year int4 NULL,
	report_tgf text NULL,
	dog_zakaz text NULL,
	dog_name text NULL,
	dog_num text NULL,
	dog_date timestamp NULL,
	dog_isp text NULL,
	dog_rep text NULL,
	dog_prikaz text NULL,
	is_deleted bool NULL,
	lastupdate timestamp NULL,
	file_path_fts tsvector NULL,
	CONSTRAINT file_pkey PRIMARY KEY (id)
);
CREATE INDEX ix_file_areaoil ON gdx2.file USING btree (areaoil);
CREATE INDEX ix_file_dog_date ON gdx2.file USING btree (dog_date);
CREATE INDEX ix_file_dog_isp ON gdx2.file USING btree (dog_isp);
CREATE INDEX ix_file_dog_name ON gdx2.file USING btree (dog_name);
CREATE INDEX ix_file_dog_num ON gdx2.file USING btree (dog_num);
CREATE INDEX ix_file_dog_prikaz ON gdx2.file USING btree (dog_prikaz);
CREATE INDEX ix_file_dog_rep ON gdx2.file USING btree (dog_rep);
CREATE INDEX ix_file_dog_zakaz ON gdx2.file USING btree (dog_zakaz);
CREATE INDEX ix_file_f_ext ON gdx2.file USING btree (f_ext);
CREATE INDEX ix_file_f_folder ON gdx2.file USING btree (f_folder);
CREATE INDEX ix_file_f_name ON gdx2.file USING btree (f_name);
CREATE INDEX ix_file_f_path ON gdx2.file USING btree (f_path);
CREATE INDEX ix_file_f_path_md5 ON gdx2.file USING btree (f_path_md5);
CREATE INDEX ix_file_f_root ON gdx2.file USING btree (f_root);
CREATE INDEX ix_file_field ON gdx2.file USING btree (field);
CREATE INDEX ix_file_lu ON gdx2.file USING btree (lu);
CREATE INDEX ix_file_lu_num ON gdx2.file USING btree (lu_num);
CREATE INDEX ix_file_ngo ON gdx2.file USING btree (ngo);
CREATE INDEX ix_file_ngp ON gdx2.file USING btree (ngp);
CREATE INDEX ix_file_ngr ON gdx2.file USING btree (ngr);
CREATE INDEX ix_file_report_author ON gdx2.file USING btree (report_author);
CREATE INDEX ix_file_report_id ON gdx2.file USING btree (report_id);
CREATE INDEX ix_file_report_name ON gdx2.file USING btree (report_name);
CREATE INDEX ix_file_report_year ON gdx2.file USING btree (report_year);
CREATE INDEX ix_file_well ON gdx2.file USING btree (well);