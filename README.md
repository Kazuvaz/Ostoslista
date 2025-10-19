# Ostoslista

## Sovelluksen toiminnot

* Käyttäjä pystyy luomaan käyttäjän ja salasalan
* käyttäjä pystyy luomaan reseptejä (reseptit tässä kontextissa ovat vain tarvittavat ainesosat reseptiin)
* käyttäjä pystyy poistamaan itseluomiaan reseptejä
* käyttäjä pystyy laittamaan reseptejä ostoslistaansa
* käyttäjä pystyy näkemään muiden luomia reseptejä
* resepteissä näkyy kuinka moni käyttää niitä
* käyttäjä pystyy näkemään kaikki tarvittavat ainesosat ostoslistassa oleville resepteille

## Sovelluksen asennus

Asenna `flask`-kirjasto:

```
$ pip install flask
```

Luo tietokannan taulut ja lisää alkutiedot:

```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

Voit käynnistää sovelluksen näin:

```
$ flask run
```
