import boto3
dynamodb = boto3.resource('dynamodb')
classes_table = dynamodb.Table('movie-theater')
classes_data = [
{
"pk": "movie_01",
"sk": "info",
"main_Actor": "Paul Bettany",
"title": "Wimbledon",
"year": 2003
},{
"pk": "movie_01",
"sk": "room_01",
"schedule": "15:00"
},{
"pk": "movie_01",
"sk": "room_06",
"schedule": "18:30"
},{
"pk": "movie_01",
"sk": "room_08",
"schedule": "21:00"
},{
"pk": "movie_01",
"sk": "room_10",
"schedule": "10:30"
},{
"pk": "movie_01#room_08",
"sk": "person_01",
"name": "Ricardo"
},{
"pk": "movie_01#room_08",
"sk": "person_01",
"name": "Alejandra"
},{
"pk": "movie_01#room_08",
"sk": "person_01",
"name": "Fabricio"
},{
"pk": "movie_01#room_08",
"sk": "person_01",
"name": "Naomi"
},{
"pk": "movie_01#room_08",
"sk": "person_01",
"name": "Natalia"
},{
"pk": "person_01",
"sk": "movie_01",
"date": "14/6/21"
},{
"pk": "person_01",
"sk": "movie_02",
"date": "12/6/21"
},{
"pk": "person_01",
"sk": "movie_03",
"date": "08/8/21"
},{
"pk": "room_01",
"sk": "info",
"3D": "true",
"seats": 120
},{
"pk": "room_02",
"sk": "info",
"3D": "true",
"seats": 100
},{
"pk": "room_03",
"sk": "info",
"3D": "false",
"seats": 200
},{
"pk": "room_04",
"sk": "info",
"3D": "false",
"seats": 150
},{
"pk": "room_05",
"sk": "info",
"3D": "true",
"seats": 300
},
]
with classes_table.batch_writer() as batch:
        for class_item in classes_data:
                batch.put_item(
                Item=class_item
)
print("All good")