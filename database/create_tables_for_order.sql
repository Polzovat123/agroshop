-- Table: public.product_tag

-- DROP TABLE IF EXISTS public.product_tag;

CREATE TABLE IF NOT EXISTS public.product_tag
(
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    nametag character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT product_tag_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.product_tag
    OWNER to postgres;


-- Table: public.product_tag

-- DROP TABLE IF EXISTS public.product_tag;

CREATE TABLE IF NOT EXISTS public.product_type
(
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    product_type character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT product_type_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.product_type
    OWNER to postgres;


-- Table: public.shopping_cart

-- DROP TABLE IF EXISTS public.shopping_cart;

CREATE TABLE IF NOT EXISTS public.shopping_cart
(
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    user_id character varying(80) COLLATE pg_catalog."default" NOT NULL,
    product_id bigint NOT NULL,
    order_date time with time zone NOT NULL,
    CONSTRAINT shopping_cart_pkey PRIMARY KEY (id),
    CONSTRAINT product_id FOREIGN KEY (product_id)
        REFERENCES public.product (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.shopping_cart
    OWNER to postgres;

-- Table: public.product

-- DROP TABLE IF EXISTS public.product;

CREATE TABLE IF NOT EXISTS public.product
(
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    product_name character varying COLLATE pg_catalog."default" NOT NULL,
    description character varying COLLATE pg_catalog."default" NOT NULL,
    type_id bigint NOT NULL,
    tags_id bigint NOT NULL,
    date_of_publication time with time zone NOT NULL,
    price bigint NOT NULL,
    old_price bigint NOT NULL,
    date_update time with time zone NOT NULL,
    image character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT product_pkey PRIMARY KEY (id),
    CONSTRAINT tags_id_key FOREIGN KEY (tags_id)
        REFERENCES public.product_tag_relationship (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT type_id_key FOREIGN KEY (type_id)
        REFERENCES public.product_type (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.product
    OWNER to postgres;

-- Table: public.product_tag_relationship

-- DROP TABLE IF EXISTS public.product_tag_relationship;

CREATE TABLE IF NOT EXISTS public.product_tag_relationship
(
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    product_id bigint NOT NULL,
    tag_id bigint NOT NULL,
    CONSTRAINT product_id_key FOREIGN KEY (product_id)
        REFERENCES public.product (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT tag_id_key FOREIGN KEY (tag_id)
        REFERENCES public.product_tag (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.product_tag_relationship
    OWNER to postgres;


-- Table: public.shopping_cart_product_relationship

-- DROP TABLE IF EXISTS public.shopping_cart_product_relationship;

CREATE TABLE IF NOT EXISTS public.shopping_cart_product_relationship
(
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    shopping_cart_id bigint NOT NULL,
    product_id bigint NOT NULL,
    CONSTRAINT shopping_cart_product_relationship_pkey PRIMARY KEY (id),
    CONSTRAINT product_id FOREIGN KEY (product_id)
        REFERENCES public.product (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT shopping_cart_id_key FOREIGN KEY (shopping_cart_id)
        REFERENCES public.shopping_cart (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.shopping_cart_product_relationship
    OWNER to postgres;
