-- Table: public.users

-- DROP TABLE IF EXISTS public.users;

CREATE TABLE IF NOT EXISTS public.users
(
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    username character varying(80) COLLATE pg_catalog."default" NOT NULL,
    password character varying(80) COLLATE pg_catalog."default" NOT NULL,
    email character varying(80) COLLATE pg_catalog."default" NOT NULL,
    created_at time with time zone NOT NULL,
    updated_at time with time zone NOT NULL,
    age integer NOT NULL,
    shop_rating integer NOT NULL DEFAULT 50,
    is_farmer integer NOT NULL DEFAULT 0,
    CONSTRAINT client_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users
    OWNER to postgres;

-- Table: public.farmer

-- DROP TABLE IF EXISTS public.farmer;

CREATE TABLE IF NOT EXISTS public.farmer
(
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    created_at character varying(80) COLLATE pg_catalog."default" NOT NULL,
    updated_at character varying(80) COLLATE pg_catalog."default" NOT NULL,
    farmer_rating character varying(80) COLLATE pg_catalog."default" NOT NULL,
    user_id bigint NOT NULL,
    nickname bit varying(80) NOT NULL,
    CONSTRAINT farmer_pkey PRIMARY KEY (id),
    CONSTRAINT user_id_key FOREIGN KEY (user_id)
        REFERENCES public.users (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.farmer
    OWNER to postgres;