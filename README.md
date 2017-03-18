## Damian Centek

Wybrany zbiór danych: [Transportation - Airlines(2008)](http://stat-computing.org/dataexpo/2009/the-data.html)

(zaliczenie)

- [ ] EDA  
     [Zadanie GEO](https://dragondc.github.io/NoSQL/)  
     
     Zadanie1  
     Zbiór danych - [Aviation](https://archive.org/download/stackexchange/aviation.stackexchange.com.7z)  
     
     
     #### Mongo
     
     # Import danych do bazy
     ```
     mongoimport --db zadanie1 --collection Badges --file  d:\Damian\NoSQL\Airlines\Zad1\Badges.json --jsonArray  
     mongoimport --db zadanie1 --collection Comments --file  d:\Damian\NoSQL\Airlines\Zad1\Comments.json --jsonArray    
     mongoimport --db zadanie1 --collection PostHistory --file  d:\Damian\NoSQL\Airlines\Zad1\PostHistory.json --jsonArray   
     mongoimport --db zadanie1 --collection PostLinks --file  d:\Damian\NoSQL\Airlines\Zad1\PostLinks.json --jsonArray  
     mongoimport --db zadanie1 --collection Posts --file  d:\Damian\NoSQL\Airlines\Zad1\Posts.json --jsonArray    
     mongoimport --db zadanie1 --collection Tags --file  d:\Damian\NoSQL\Airlines\Zad1\Tags.json --jsonArray   
     mongoimport --db zadanie1 --collection Users --file  d:\Damian\NoSQL\Airlines\Zad1\Users.json --jsonArray  
     mongoimport --db zadanie1 --collection Votes --file  d:\Damian\NoSQL\Airlines\Zad1\Votes.json --jsonArray  
     ```  
     
     # Czas importu dokumentów do bazy  
     
     Przykładowe polecenie  
     ```
     powershell "Measure-Command{.\mongoimport --db zadanie1 --collection Badges --file  D:\Damian\NoSQL\Airlines\Zad1\Badges.json --jsonArray}"
     ```  
     
     | Plik           | Czas w ms  |
     |----------------|------------|
     | Badges         | 787,6587   |
     | Comments       | 2136,7319  |
     | PostHistory    | 4720,1151  |
     | PostLinks      | 311,8956   |
     | Posts          | 2911,4128  |
     | Tags           | 158,9691   |
     | Users          | 707,6484   |
     | Votes          | 3304,2604  |
     
     
     # Liczność danych  
     
     Przykładowe polecenie <code>db.Users.count()</code>  
     Badges - 40589  
     Comments - 61511  
     PostHistory - 89048  
     PostLinks - 6285  
     Posts - 25695  
     Tags - 759  
     Users - 14807  
     
     
     Przykład kodu, który był potrzebny do sparsowania niektórych pól na Inta.  
     ```
     db.Posts.find({Score: {$exists: true}}).forEach(function(obj) {  
          obj.Score = new NumberInt(obj.Score);  
          db.Posts.save(obj);  
     });     
     ```
     
     
     
     
- [ ] Aggregation Pipeline

(egzamin)

- [ ] MapReduce

Informacje o komputerze na którym były wykonywane obliczenia:

| Nazwa                 | Wartosć    |
|-----------------------|------------|
| System operacyjny     | Win 10 Pro x64 |
| Procesor              | Intel Core i7 4750HQ |
| Pamięć                | 8GB |
| Dysk                  | Hitachi Travelstar 7K1000 1TB |
| Baza danych           | TODO |
