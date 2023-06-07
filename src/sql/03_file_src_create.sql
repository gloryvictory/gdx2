-- gdx2.file_src definition

-- Drop table

-- DROP TABLE gdx2.file_src;

CREATE TABLE gdx2.file_src (
	id serial4 NOT NULL,
	folder_src text NULL,
	lastupdate timestamp NULL,
	CONSTRAINT file_src_pkey PRIMARY KEY (id)
);
CREATE UNIQUE INDEX ix_file_src_folder_src ON gdx2.file_src USING btree (folder_src);