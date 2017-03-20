## Damian Centek

Wybrany zbiór danych: [Transportation - Airlines(2008)](http://stat-computing.org/dataexpo/2009/the-data.html)
 
# [Zadanie GEO](https://dragondc.github.io/NoSQL/)  
     
# Zadanie1  
Zbiór danych - [Aviation](https://archive.org/download/stackexchange/aviation.stackexchange.com.7z)  
        
## Mongo
     
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
     
     
# Liczebność danych  
     
Przykładowe polecenie <code>db.Users.count()</code>  
Badges - 40589  
Comments - 61511  
PostHistory - 89048  
PostLinks - 6285  
Posts - 25695  
Tags - 759  
Users - 14807  
Votes - 225617
     
     
Przykład kodu, który był potrzebny do sparsowania niektórych pól na Inta.  
```
db.Posts.find({Score: {$exists: true}}).forEach(function(obj) {  
	obj.Score = new NumberInt(obj.Score);  
   	db.Posts.save(obj);  
});     
```

# Agregacja 1. Wyświetlenie 10 najbardziej punktowanych postów  
```
db.Posts.aggregate(  
   [  
        { $sort: { Score: -1 } },  
	{ $limit : 10 },  
	{ $project : { _id: 0, Score : 1 , Body : 1  } }   
   ]  
).pretty()  
```     
Ze względu na sporą treść postów zostały one zamienione na Id postu

| Id         | Wynik  |
|------------|--------|
| 2081       | 233    |
| 2078       | 186    |
| 21988      | 142    |
| 16553      | 126    |
| 738        | 122    |
| 22987      | 121    |
| 29809      | 120    |
| 24509      | 115    |     
| 2884       | 113    |
| 26630      | 105    |

# Agregacja 2. Wyświetlenie 10 najczęściej odwiedzanych postów
```
db.Posts.aggregate(  
   [  
	{ $group : {_id: {id: "$Id", wyswietlenia: "$ViewCount"}}},  
        { $sort : { "_id.wyswietlenia": -1 } },  
	{ $limit : 10 },  
	{ $project : { _id: 1} }   
   ]  
).pretty()  
```

| Id      | Wyświetlenia |
|---------|--------------|
| 2078    | 131514    |
| 3300    | 124009    |
| 4966    | 96327    |
| 1418    | 91792    |
| 1807    | 72069    |
| 738     | 69349    |
| 8000    | 67530    |
| 34586   | 63592    |     
| 64      | 60557    |
| 1210    | 59352    |

# Agregacja 3. Policzenie postów które dotyczą air-traffic-control.
```
db.Posts.createIndex(  
   {  
     	Tags: "text"  
   }  
)  

db.Posts.aggregate(  
   [  
     	{ $match: { $text: { $search: "\"air-traffic-control\"" } } },  
     	{ $count: "Air traffic control instances"}  
   ]  
)  
```

Wynik to 461 postów, które dotyczą aircraft-failure.

# Agregacja 4. Wyświetlenie 10 najbardziej aktywnych użytkowników
```
db.Posts.aggregate(  
  [
	{ $lookup : {from:"Users", localField:"OwnerUserId", foreignField: "Id", as:"users_posts"}},  
	{ $group: {  
        	_id: "$users_posts.DisplayName", posts_owned: { $sum: 1 }   
   	}},  
	{ $sort : { posts_owned: -1 } },  
	{ $limit : 10 },  
      	{ $project : { "users_posts.DisplayName" : 1, posts_owned: 1} }  	  
  ]  
).pretty()  
```

| Nick            | Ilość postów |
|-----------------|--------------|
| Peter Kämpf     | 1094   |
| aeroalias       | 817    |
| voretaq7        | 531    |
| fooot           | 525    |
| Dave            | 506    |
| Pondlife        | 491    |
| Lnafziger       | 447    |
| DeltaLima       | 396    |     
| ymb1            | 329    |
| Carlo Felicione | 323    |


# Czas wykonania poszczególnych agregacji


| Agregacja | Czas    |
|-----------|---------|
| 1         | 40ms    |
| 2         | 68ms    |
| 3         | 8ms     |
| 4         | 3,14min |

     
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
