## Damian Centek

<br />  
<br />  

# Zadanie GEO
   
Zbiór danych - [**_Airports_**](http://stat-computing.org/dataexpo/2009/airports.csv)  
W tym zadaniu wykorzystano zbiór danych zawierający porty lotnicze w USA.
Jest to plik csv zajmujący 239KB zawierający podstawowe informacje o portach lotniczych.    
Został on skonwertowany do formatu json przy użyciu [**_TEJ_**](http://www.convertcsv.com/csv-to-geojson.htm) strony.
Po konwersji plik zajmuje 945KB. Zbiór zawiera 3376 rekordów.  

Przykładowy rekord  
```json
{
    "type": "Feature",
    "geometry": {
       "type": "Point",
       "coordinates":  [ -104.5698933,38.94574889 ]
    },
    "properties": {
    	"iata":"00V",
    	"airport":"Meadow Lake",
    	"city":"Colorado Springs",
    	"state":"CO",
    	"country":"USA"
    }
}
```  

Wyjaśnienie pól 

| Pole        | Znaczenie                                         |
|-------------|---------------------------------------------------|
| iata        | Skrótowy kod międzynarodowego portu lotniczego    |
| airport     | Nazwa portu lotniczego                            |
| city        | Nazwa miasta do którego przynależy dane lotnisko  |
| state       | Stan USA w którym znajduje się dany port          |
| country     | Państwo do którego należy dany port lotniczy      |
| coordinates | Długość i szerokość geograficzna portu lotniczego |

## Mongo

1. Stworzenie nowej bazy Geo
```
use Geo
```

2. Stworzenie kolekcji Airports  
```js
db.createCollection("Airports")
```

3. Import danych do bazy
```
mongoimport --db Geo --collection Airports --file  d:\Damian\NoSQL\Airlines\geo_airports.json --jsonArray
```

### Zapytania  
1. Lotniska oddalone o ponad 1000km od lotniska Thigpen(-89.23450472,31.95376472)
```js
db.Airports.find({ 
	geometry: {
	   $near: {
	      $geometry: {
	         type: 'Point', coordinates: [-89.23450472,31.95376472]
	      }, $minDistance: 1000000
	   }
	}
})
```    


2. Lotniska oddalone od lotniska Yuma Municipal(-102.7129869,40.10415306) w przedziale od 400km do 1000km
```js
db.Airports.find({ 
	geometry: {
	   $near: {
	      $geometry: {
	         type: 'Point', coordinates: [-102.7129869,40.10415306]
	      }, $minDistance: 400000, $maxDistance: 1000000 
	   }
	}
})	
```   


3. Lotniska znajdujące się w obrębie pięciokąta
```js
db.Airports.find({ 
	geometry: {
	   $geoWithin: {
	      $geometry: {
	         type : 'Polygon', coordinates: [[[ -102.077029, 41.052873 ], [ -95.236718, 37.044054 ], 
		 [ -99.447158, 32.029309 ], [ -104.222035, 32.065320], 
		 [-109.057755, 37.023279], [ -102.077029, 41.052873 ]]]
	      }
	   }
	} 
})
```  

### Mapki

Link do mapek znajduje się [**_TUTAJ_**](https://dragondc.github.io/NoSQL/).


### Przykład eksportu wyniku zapytania
```
mongoexport -d Geo -c Airports -q "{ 
	geometry: {$near: {$geometry: {type: 'Point', coordinates: [-89.23450472,31.95376472]}, $minDistance: 1000000}}}" -o
	d:\Damian\NoSQL\Airlines\mongo_export\wynik1.json --jsonArray --pretty
```

## WAŻNE
Instrukcja umożliwiająca odtworzenie powyższych wyników na swoim komputerze znajduje się [**_TUTAJ_**](https://github.com/DragonDC/NoSQL/blob/master/User_manual.txt).
<br />  
<br />  
<br />
<br />  
<br /> 

# Zadanie1  
Zbiór danych - [**_Aviation_**](https://archive.org/download/stackexchange/aviation.stackexchange.com.7z)  
W tym zadaniu wykorzystano zbiór danych o tematyce lotniczej. Spakowane dane zajmują na dysku 31,6MB. Po rozpakowaniu wszystkie dane zajmują 174MB. Na zbiór danych składa się 8 plików w formacie xml (Badges, Comments, PostsHistory, PostLinks, Posts, Tags, Users, Votes). Przy użyciu prostego programu Xml ValidatorBuddy wszystkie pliki zostały skonwertowane najpierw do formatu json a w późniejszym etapie do postaci csv, która była potrzebna przy importowaniu plików do postgresqla. Cały zbiór danych zawiera 464 311 rekordów.

Liczebność danych w poszczególnych plikach  
Badges - 40589  
Comments - 61511  
PostHistory - 89048  
PostLinks - 6285  
Posts - 25695  
Tags - 759  
Users - 14807  
Votes - 225617  

W zadaniu tym wybrano 3 pliki(Posts, Tags, Users), których opis znajduje się poniżej.

Przykładowy rekord w Posts.json
```json
{
	"Id": "710",
	"CreationDate": "2014-01-08T02:25:11.510",
	"Score": "0",
	"Body": "Takeoff is the first phase of flight, when an aircraft lifts off from the runway or other surface",
	"OwnerUserId": "327",
	"LastEditDate": "2014-10-31T19:17:13.550",
	"CommentCount": "0"
}
```  

Wyjaśnienie pól 

| Pole         | Znaczenie                          |
|--------------|------------------------------------|
| CreationDate | Data utworzenia posta              |
| Score        | Ilość punktów otrzymana za posta   |
| Body         | Treść posta                        |
| OwnerUserId  | Id użytkownika który napisał posta |
| LastEditDate | Data ostatniej modyfikacji posta   |
| CommentCount | Ilość komentarzy do danego posta   |
<br />  
<br /> 
<br />  
  
Przykładowy rekord w Tags.json  
```json
{
	"Id": "17",
	"TagName": "flight-training",
	"Count": "209"
}
```

Wyjaśnienie pól 

| Pole    | Znaczenie                           |
|---------|-------------------------------------|
| TagName | Nazwa taga                          |
| Count   | Ilość postów która posiada taki tag |  
<br />  
<br />  
<br />  
    
Przykładowy rekord w Users.json  
```json
{
	"Id": "1961",
	"Reputation": "106319",
	"CreationDate": "2014-04-01T12:08:36.283",
	"DisplayName": "Peter Kämpf",
	"LastAccessDate": "2017-03-13T19:02:50.763",
	"Views": "4046",
	"UpVotes": "3572",
	"DownVotes": "29",
	"ProfileImageUrl": "https://i.stack.imgur.com/wmtsV.jpg",
	"Age": "56"
}
```  

Wyjaśnienie pól 

| Pole            | Znaczenie                 |
|-----------------|---------------------------|
| Reputation      | Punkty reputacji          |
| CreationDate    | Data stworzenia konta     |
| DisplayName     | Nazwa użytkownika         |
| LastAccessDate  | Data ostatniego logowania |
| Views           | Ilość wyświetleń profilu  |
| UpVotes         | Głosy na tak              |
| DownVotes       | Głosy na nie              |
| ProfileImageUrl | Zdjęcie profilowe         |
| Age             | Wiek użytkownika          |
<br />  
<br />    

## Mongo
     
### Import danych do bazy
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
     
### Czas importu dokumentów do bazy  
     
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
     
     
### Liczebność danych  
     
Przykładowe polecenie 
```js
db.Users.count()  
```  
     
     
Przykład kodu, który był potrzebny do sparsowania niektórych pól na Inta.  
```js
db.Posts.find({Score: {$exists: true}}).forEach(function(obj) {  
	obj.Score = new NumberInt(obj.Score);  
   	db.Posts.save(obj);  
});     
```
<br />  
<br />

### Agregacja 1. Wyświetlenie 10 najbardziej punktowanych postów  
```js
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
<br />  
<br /> 

### Agregacja 2. Wyświetlenie 10 najczęściej odwiedzanych postów
```js
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
| 2078    | 131514       |
| 3300    | 124009       |
| 4966    | 96327        |
| 1418    | 91792        |
| 1807    | 72069        |
| 738     | 69349        |
| 8000    | 67530        |
| 34586   | 63592        |     
| 64      | 60557        |
| 1210    | 59352        |
<br />  
<br /> 

### Agregacja 3. Policzenie postów które dotyczą air-traffic-control.
```js
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

Wynik to 461 postów, które dotyczą air-traffic-control.
<br />  
<br /> 

### Agregacja 4. Wyświetlenie 10 najbardziej aktywnych użytkowników
```js
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
<br />  
<br /> 


### Czas wykonania poszczególnych agregacji


| Agregacja | Czas    |
|-----------|---------|
| 1         | 40ms    |
| 2         | 68ms    |
| 3         | 8ms     |
| 4         | 3,14min |
<br />  
<br />  

## PostgreSQL

### Stworzenie tabel 

Tags  
```sql
CREATE TABLE Tags (
	Id BIGINT,
	TagName VARCHAR,
	Count INTEGER,
	ExcerptPostId BIGINT,
	WikiPostId BIGINT
);
```  

Users  
```sql
CREATE TABLE Users (
	Id BIGINT,
	Reputation INTEGER,
	CreationDate DATE,
	DisplayName VARCHAR,
	LastAccessDate DATE,
	WebsiteUrl VARCHAR,
	Location VARCHAR,
	Views INTEGER,
	UpVotes INTEGER,
	DownVotes INTEGER,
	AccountId BIGINT
);		
```  

Posts
```sql
CREATE TABLE Posts (
	Id BIGINT,
	PostTypeId BIGINT,
	AcceptedAnswerId BIGINT,
	CreationDate DATE,
	Score INTEGER,
	ViewCount INTEGER,
	OwnerUserId BIGINT,
	LastEditorUserId BIGINT,
	LastEditDate DATE,
	LastActivityDate DATE,
	Title VARCHAR,
	Tags VARCHAR,
	AnswerCount INTEGER,
	CommentCount INTEGER
);						
```  

### Import danych do bazy
```
\copy Tags FROM 'd:\Damian\NoSQL\Airlines\Zad1\Tags.csv' DELIMITER ';' CSV HEADER
\copy Users FROM 'd:\Damian\NoSQL\Airlines\Zad1\Users.csv' DELIMITER ';' CSV HEADER
\copy Posts FROM 'd:\Damian\NoSQL\Airlines\Zad1\Posts.csv' DELIMITER ';' CSV HEADER
```  

### Czas importu do bazy  

Przykładowe polecenie  
```
\timing \copy Tags FROM 'd:\Damian\NoSQL\Airlines\Zad1\Tags.csv' DELIMITER ';' CSV HEADER
```  

| Plik           | Czas w ms  |
|----------------|------------|
| Tags           | 2,291      |
| Users          | 103,621    |
| Posts          | 226,924    |


### Liczebność danych  
     
Przykładowe polecenie   
```sql
SELECT COUNT(*) FROM Tags;  
```  
<br />  
<br /> 

### Agregacja 1. Wyświetlenie 10 najbardziej punktowanych postów  
```sql
SELECT Id,Score 
FROM Posts 
ORDER BY Score 
DESC LIMIT 10;
```  
<br />  
<br /> 

### Agregacja 2. Wyświetlenie 10 najczęściej odwiedzanych postów
```sql
SELECT Id,ViewCount 
FROM Posts 
WHERE ViewCount > 0
ORDER BY ViewCount 
DESC LIMIT 10; 
```  
<br />  
<br /> 

### Agregacja 3. Policzenie postów które dotyczą air-traffic-control.
```sql
SELECT COUNT(*) FROM Posts 
WHERE Tags Like '%air-traffic-control%'; 
```
<br />  
<br /> 

### Agregacja 4. Wyświetlenie 10 najbardziej aktywnych użytkowników
```sql
SELECT DisplayName, COUNT(*) FROM Posts 
JOIN Users 
ON Users.Id = Posts.OwnerUserId
GROUP BY DisplayName
ORDER BY Count 
DESC LIMIT 10; 
```  
<br />   

Wyniki wszystkich agregacji są takie same jak w przypadku mongo, dlatego pominięto ich wyświetlenie.  
<br />  
<br /> 


### Czas wykonania poszczególnych agregacji

| Agregacja | Czas w ms |
|-----------|-----------|
| 1         | 6,649     |
| 2         | 23,228    |
| 3         | 4,715     |
| 4         | 18,428    |
<br /> 

## Porównanie czasu wykonania agregacji dla PostgreSQL oraz Mongo

| Agregacja | Mongo   | PostgreSQL |
|-----------|---------|------------|
| 1         | 40ms    | 6,649ms    |
| 2         | 68ms    | 23,228ms   | 
| 3         | 8ms     | 4,715ms    |
| 4         | 3,14min | 18,428ms   |

Widać doskonale, że Mongo ma dużo gorsze wyniki od Postgresa. Największą dysproporcję widać przy ostatniej agregacji, którą Mongo liczyło aż **_3,14minuty_**! 
<br />  
<br /> 


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



