mongoimport --db Geo --collection Airports --file  C:\Mongo\Mongo_import\convertcsv.geojson --jsonArray

mongo Geo --eval "db.Airports.ensureIndex({'geometry' : '2dsphere'})"

mongoexport -d Geo -c Airports -q "{ geometry: {$near: {$geometry: {type: 'Point', coordinates: [-89.23450472,31.95376472]}, $minDistance: 1000000}}}" -o C:\Mongo\Mongo_export\wynik1.geojson --jsonArray --pretty

mongoexport -d Geo -c Airports -q "{ geometry: {$near: {$geometry: {type: 'Point', coordinates: [-102.7129869,40.10415306]}, $minDistance: 400000, $maxDistance: 1000000 }}}" -o C:\Mongo\Mongo_export\wynik2.geojson --jsonArray --pretty

mongoexport -d Geo -c Airports -q "{ geometry: {$geoWithin: {$geometry: {type : 'Polygon', coordinates: [[[ -102.077029, 41.052873 ], [ -95.236718, 37.044054 ], [ -99.447158, 32.029309 ], [ -104.222035, 32.065320], [-109.057755, 37.023279], [ -102.077029, 41.052873 ]]]}}} }" -o C:\Mongo\Mongo_export\wynik3.geojson --jsonArray --pretty

python C:\Mongo\Python_scripts\processing_script_export.py C:\Mongo\Mongo_export\wynik1.geojson

python C:\Mongo\Python_scripts\processing_script_export.py C:\Mongo\Mongo_export\wynik2.geojson

python C:\Mongo\Python_scripts\processing_script_export_polygon.py C:\Mongo\Mongo_export\wynik3.geojson