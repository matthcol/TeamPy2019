select * from cinema.individu;
select * from cinema.film;

-- Selection (prédicat)
-- qui est l'individu num 2 ?
select * from cinema.individu where num_ind = 2;
-- quels sont les individus prénommés John
select * from cinema.individu where prenom = 'John';
-- les films antérieurs à 1970
select * from cinema.film where annee < 1970;
-- les films des années 60
select * from cinema.film 
where 1960 <= annee and annee < 1970;
select * from cinema.film 
where annee between 1960 and 1969;

-- Projection (colonnes)
-- titres des films
select titre from cinema.film;
-- titre et durée des films
select titre, duree from cinema.film;
-- titre des films des années 60
select titre from cinema.film
where annee between 1960 and 1969;
-- individus avec date de naissance
select * from cinema.individu where date_naissance is not NULL;
-- films pas de 1994 (!= ou  <>)
select * from cinema.film where annee <> 1994;
-- films de 1992 et 1994
select * from cinema.film where annee in (1992,1994);