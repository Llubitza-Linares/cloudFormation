import boto3
dynamodb = boto3.resource('dynamodb')
classes_table = dynamodb.Table('movie-theater')
classes_data = [
{
"pk": "store_01",
"sk": "Paul",
"package": "package_01"
},{
"pk": "store_01",
"sk": "Andre",
"package": "package_02"
},{
"pk": "store_01",
"sk": "Juan",
"package": "package_03"
},{
"pk": "store_01",
"sk": "Michael",
"package": "package_04"
},{
"pk": "package_01",
"sk": "delivery_01",
"user": "Adam"
},{
"pk": "package_01",
"sk": "delivery_01",
"user": "Juan"
},{
"pk": "store_01",
"sk": "package_01",
"delivery-guy": "delivery_01"
},{
"pk": "store_01",
"sk": "package_02",
"delivery-guy": "delivery_02"
},{
"pk": "store_01",
"sk": "package_03",
"delivery-guy": "delivery_03"
},{
"pk": "store_01",
"sk": "package_04",
"delivery-guy": "delivery_04"
},{
"pk": "user_01",
"sk": "delivery_01",
"store": "store_01"
},{
"pk": "user_01",
"sk": "delivery_02",
"store": "store_02"
},{
"pk": "user_01",
"sk": "delivery_03",
"store": "store_03"
},{
"pk": "user_01",
"sk": "delivery_04",
"store": "store_04"
},
]
with classes_table.batch_writer() as batch:
        for class_item in classes_data:
                batch.put_item(
                Item=class_item
)
print("All good")