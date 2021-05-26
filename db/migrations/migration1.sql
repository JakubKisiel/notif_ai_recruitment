--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0 (Debian 13.0-1.pgdg100+1)
-- Dumped by pg_dump version 13.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: posts; Type: TABLE; Schema: public; Owner: Daft
--

CREATE TABLE public.posts (
    idpost integer NOT NULL,
    iduser integer NOT NULL,
    postcontent character varying(160) NOT NULL,
    viewscounter integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.posts OWNER TO "Daft";

--
-- Name: posts_idpost_seq; Type: SEQUENCE; Schema: public; Owner: Daft
--

CREATE SEQUENCE public.posts_idpost_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.posts_idpost_seq OWNER TO "Daft";

--
-- Name: posts_idpost_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: Daft
--

ALTER SEQUENCE public.posts_idpost_seq OWNED BY public.posts.idpost;


--
-- Name: users; Type: TABLE; Schema: public; Owner: Daft
--

CREATE TABLE public.users (
    iduser integer NOT NULL,
    username text NOT NULL,
    hashedpassword text NOT NULL,
    passwordsalt text NOT NULL
);


ALTER TABLE public.users OWNER TO "Daft";

--
-- Name: users_iduser_seq; Type: SEQUENCE; Schema: public; Owner: Daft
--

CREATE SEQUENCE public.users_iduser_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_iduser_seq OWNER TO "Daft";

--
-- Name: users_iduser_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: Daft
--

ALTER SEQUENCE public.users_iduser_seq OWNED BY public.users.iduser;


--
-- Name: posts idpost; Type: DEFAULT; Schema: public; Owner: Daft
--

ALTER TABLE ONLY public.posts ALTER COLUMN idpost SET DEFAULT nextval('public.posts_idpost_seq'::regclass);


--
-- Name: users iduser; Type: DEFAULT; Schema: public; Owner: Daft
--

ALTER TABLE ONLY public.users ALTER COLUMN iduser SET DEFAULT nextval('public.users_iduser_seq'::regclass);


--
-- Data for Name: posts; Type: TABLE DATA; Schema: public; Owner: Daft
--

COPY public.posts (idpost, iduser, postcontent, viewscounter) FROM stdin;
3	2	string	13
4	2	string	1
5	29	notifai	0
6	29	notifai	0
7	29	notifai	1
8	29	daft	0
9	29	daft	0
10	29	daft	0
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: Daft
--

COPY public.users (iduser, username, hashedpassword, passwordsalt) FROM stdin;
2	xdd	be966bac3588383f068d710c5726dc9009ce6ba498393a16064816d8a13b7e6e	y1kkN5Ejs5PUCKoF
24	xddd	ef4b6ef3283a08512c13935126be3d9592857faaa4312b39fc5af04e22be7b5f	ZUKR0rI8sDMcqHal
25	raz	d99846699814800cbe105c89d6ea80bc0e9c634872f6ca88e60133f529d9a84e	BonEGqS4sAjfk8ch
29	daft	8186e7454c261360139ab068b5d515a6747d23dd2346fa21cf7969ce46bbfb6b	5O0XmSHc5eq6Ron1
30	notfiai	f500724e106a2dff997b6a97b335ec7a2e9913ddbbed2716693bcd06adaada7c	QAQj1I1lWH5zymKk
31	notfiaidaft	6fa006e76ac310037ed6c66d99189b8bd4ce075b444fb5171af2d2bdcf104e48	yivCu3yjdRyWfAkT
37	DaftAi	960923de95ab9c302a55f6fdb22aecea9fe158abca534fec78297a3d35144b8a	3GF4DjeQ55uPKKmv
38	DaftAii	4b17d34c9ade316ba7629e184d54b0ecbe09640b6dc9d7a7ed8dac2187f33b64	AIOlHLRuYhk5STQz
39	DaftAiii	fb5833bba118142f12dc9114ef6d045453313725c5729b11c0f270a4cf65fe04	Yo3aNKU0Ei8GDA9s
40	DaftAiiii	4371536e31e5ee8b76535699d8d0542d792534b4c5e4dd69b1d09ba11dcf5766	T9Mq4Bn9JVHEHRYq
\.


--
-- Name: posts_idpost_seq; Type: SEQUENCE SET; Schema: public; Owner: Daft
--

SELECT pg_catalog.setval('public.posts_idpost_seq', 21, true);


--
-- Name: users_iduser_seq; Type: SEQUENCE SET; Schema: public; Owner: Daft
--

SELECT pg_catalog.setval('public.users_iduser_seq', 41, true);


--
-- Name: posts posts_pkey; Type: CONSTRAINT; Schema: public; Owner: Daft
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pkey PRIMARY KEY (idpost);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: Daft
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (iduser);


--
-- Name: posts fkuser; Type: FK CONSTRAINT; Schema: public; Owner: Daft
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT fkuser FOREIGN KEY (iduser) REFERENCES public.users(iduser);


--
-- PostgreSQL database dump complete
--

