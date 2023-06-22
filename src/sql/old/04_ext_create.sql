-- public.ext definition

-- Drop table

-- DROP TABLE public.ext;

CREATE TABLE gdx2.ext (
	ext bpchar(10) NULL,
	category bpchar(255) NULL,
	description text NULL,
	product bpchar(255) NULL,
	is_project bpchar(255) NULL
);