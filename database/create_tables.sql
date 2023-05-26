-- Table: public.client

-- DROP TABLE IF EXISTS public.client;

CREATE TABLE IF NOT EXISTS public.client
(
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    username character varying(80) COLLATE pg_catalog."default" NOT NULL,
    password character varying(80) COLLATE pg_catalog."default" NOT NULL,
    email character varying(80) COLLATE pg_catalog."default" NOT NULL,
    created_at time with time zone NOT NULL,
    updated_at time with time zone NOT NULL,
    CONSTRAINT client_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.client
    OWNER to postgres;


-- Table: public.farmer

-- DROP TABLE IF EXISTS public.farmer;

CREATE TABLE IF NOT EXISTS public.farmer
(
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    farmername character varying(80) COLLATE pg_catalog."default" NOT NULL,
    password character varying(80) COLLATE pg_catalog."default" NOT NULL,
    email character varying(80) COLLATE pg_catalog."default" NOT NULL,
    created_at character varying(80) COLLATE pg_catalog."default" NOT NULL,
    updated_at character varying(80) COLLATE pg_catalog."default" NOT NULL,
    farmer_rating character varying(80) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT farmer_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.farmer
    OWNER to postgres;

-- Table: public.role

-- DROP TABLE IF EXISTS public.role;

CREATE TABLE IF NOT EXISTS public.role
(
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    rolename character varying(80) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT role_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.role
    OWNER to postgres;