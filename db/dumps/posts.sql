PGDMP                         y           postgres    13.0 (Debian 13.0-1.pgdg100+1)    13.2     ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    13395    postgres    DATABASE     \   CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';
    DROP DATABASE postgres;
                Daft    false            ?           0    0    DATABASE postgres    COMMENT     N   COMMENT ON DATABASE postgres IS 'default administrative connection database';
                   Daft    false    2957            ?            1259    16416    posts    TABLE     ?   CREATE TABLE public.posts (
    idpost integer NOT NULL,
    iduser integer NOT NULL,
    postcontent character varying(160) NOT NULL,
    viewscounter integer DEFAULT 0 NOT NULL
);
    DROP TABLE public.posts;
       public         heap    Daft    false            ?            1259    16414    posts_idpost_seq    SEQUENCE     ?   CREATE SEQUENCE public.posts_idpost_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.posts_idpost_seq;
       public          Daft    false    203            ?           0    0    posts_idpost_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.posts_idpost_seq OWNED BY public.posts.idpost;
          public          Daft    false    202            ?            1259    16387    users    TABLE     ?   CREATE TABLE public.users (
    iduser integer NOT NULL,
    username text NOT NULL,
    hashedpassword text NOT NULL,
    passwordsalt text NOT NULL
);
    DROP TABLE public.users;
       public         heap    Daft    false            ?            1259    16385    users_iduser_seq    SEQUENCE     ?   CREATE SEQUENCE public.users_iduser_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.users_iduser_seq;
       public          Daft    false    201            ?           0    0    users_iduser_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.users_iduser_seq OWNED BY public.users.iduser;
          public          Daft    false    200            ?
           2604    16419    posts idpost    DEFAULT     l   ALTER TABLE ONLY public.posts ALTER COLUMN idpost SET DEFAULT nextval('public.posts_idpost_seq'::regclass);
 ;   ALTER TABLE public.posts ALTER COLUMN idpost DROP DEFAULT;
       public          Daft    false    202    203    203            ?
           2604    16390    users iduser    DEFAULT     l   ALTER TABLE ONLY public.users ALTER COLUMN iduser SET DEFAULT nextval('public.users_iduser_seq'::regclass);
 ;   ALTER TABLE public.users ALTER COLUMN iduser DROP DEFAULT;
       public          Daft    false    200    201    201            ?          0    16416    posts 
   TABLE DATA           J   COPY public.posts (idpost, iduser, postcontent, viewscounter) FROM stdin;
    public          Daft    false    203           ?          0    16387    users 
   TABLE DATA           O   COPY public.users (iduser, username, hashedpassword, passwordsalt) FROM stdin;
    public          Daft    false    201   U       ?           0    0    posts_idpost_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.posts_idpost_seq', 17, true);
          public          Daft    false    202            ?           0    0    users_iduser_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.users_iduser_seq', 34, true);
          public          Daft    false    200                        2606    16422    posts posts_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pkey PRIMARY KEY (idpost);
 :   ALTER TABLE ONLY public.posts DROP CONSTRAINT posts_pkey;
       public            Daft    false    203            ?
           2606    16395    users users_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (iduser);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            Daft    false    201                       2606    16423    posts fkuser    FK CONSTRAINT     n   ALTER TABLE ONLY public.posts
    ADD CONSTRAINT fkuser FOREIGN KEY (iduser) REFERENCES public.users(iduser);
 6   ALTER TABLE ONLY public.posts DROP CONSTRAINT fkuser;
       public          Daft    false    201    203    2814            ?   E   x?3?4?,.)??K?4?2?4????/?LK??4?2C??#s?,@ܔĴ??%?? ?c?0ޒ+F??? =#?      ?   ?  x?5QKo?A<??c??^{??P
?"m??{"I????g??d??G?qZދ?[%V%??-#T?QZ- ???OE????$EijH???p????????????~?镸?>?K??1V???wj?KT???at*??H=F??y??7?+x?Чw????????^B+E??DL
P?#p?Ҥ??W??
%?qH5?.?D?ci?4???x8??p??V????s?%4?AQ??ĩFAz]+?????&9???L2,b??4(??p????????r????p8>??m?`??+??d?@Ľf??????Ō?@???p??????/??v?/???~!?O?O??0???&P?M?ȴ??zK?CfO)g?h#?????'????_tڵ???X??.??,??o*??     