# Basic Python Django Backend Project in Docker

It is a basic python django backend project running in a docker container in order to add and update items to the app and JSON Web Tokens (JWT) were used for authentication.

## Build Up Docker Container

To make the project work; build and up docker container:
```
$ docker-compose up -d --build
$ docker-compose exec web python manage.py migrate --noinput
```

Use POSTMAN to test it out at http://localhost:1333/

## Docker Compose

The project includes following containers:

  - Web   : #django application container
  - db    : #database (postgresql) container
  - nginx : #to reach all containers over nginx when a request sent
 
Also the project contain gunicorn

## Django Applications 

The project named addrop includes following three app:

  - myauth    : Authentication app (Register, JWT Login, Logout)
  - items     : add and update items app
  - itemlist  : Listing Items App

## REST api requests and response:

  - ## MYAUTH APP
### REGISTER View:
#### POST - /api/register
#### Request Object : 
```
{
    "name":"test",
    "email" : "test1@t.com",
    "password":"aaa"
}
```
#### Response Object : 
```
{
    "id": 1,
    "name": "test",
    "email": "test1@t.com"
}
```
myauth_user table in the database looks like:

![myauth_user table](https://user-images.githubusercontent.com/48828422/149243820-586631c1-e2c8-4ef8-a7bd-9f94e48058e4.PNG)

Test it with same email : 
#### Request Object : 
```
{
    "name":"test",
    "email" : "test1@t.com",
    "password":"aaa"
}
```
#### Response Object : 
```
{
    "email": [
        "user with this email already exists."
    ]
}
```
### LOGIN View:
#### POST - /api/login
#### Request Object:
```
{
    "email" : "test1@t.com",
    "password":"aaa"
}
```
#### Response:
```
{
    "jwt": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjQyMDExNzkyLCJpYXQiOjE2NDIwMDgxOTJ9.Or3pcqRakw353r3NS8sWo_Ua3a6BNWmeMHSwt9HYEFE"
}
```
Try wrong password:
#### Request Object:
```
{
    "email" : "test1@t.com",
    "password":"bbb"
}
```
#### Response:
```
{
    "detail": "Incorrect password"
}
```
Try wrong email:
#### Request Object:
```
{
    "email" : "test5@t.com",
    "password":"ddd"
}
```
#### Response:
```
{
    "detail": "User not found"
}
```

### USER View:
#### - GET - /api/user
#### Response:
```
{
    "id": 1,
    "name": "test",
    "email": "test1@t.com"
}
```

After logout:
#### Response:
```
{
    "detail": "Unauthenticated"
}
```

### LOGOUT View:
#### -POST- /api/logout
#### Response: 
```
{
    "message": "success"
}
```

  - ## ITEMS APP
### ADD ITEM View:
#### - POST - /items/add
#### Request Object:
```
{
    "name": "testitem",
    "category_id": 1,
    "stock": "400",
    "barcode_num": "67858",
    "seller": "company_1"
}
```
#### Response:
```
{
    "id": 1,
    "name": "testitem",
    "category_id": 1,
    "stock": 400,
    "barcode_num": 67858,
    "seller": "company_1"
}
```

Try add an item with an exist barcode number :
#### Request Object:
```
{
    "name": "mobilexyz",
    "category_id": 1,
    "stock": "600",
    "barcode_num": "67858",
    "seller": "company_2"
}
```
#### Response:
```
{
    "barcode_num": [
        "item with this barcode num already exists."
    ]
}
```

### UPDATE ITEM View:
#### - POST - /items/update
#### Request Object:
```
{
    "id":1,
    "name": "testitem",
    "category_id": 1,
    "stock": "1000",
    "barcode_num": "67858",
    "seller": "company_1"
}
```
#### Response: 
```
{
    "id": 1,
    "name": "testitem",
    "category_id": 1,
    "stock": 400,
    "barcode_num": 101010,
    "seller": "company_1"
}
```
items_item table in database looks like:

![items_item](https://user-images.githubusercontent.com/48828422/149245502-90a76313-1031-4e81-b96f-0aaab9a4ae0a.PNG)

  - ## ITEMLIST APP
### LIST ALL ITEMS View:
#### - GET - /itemlist/all
#### Response:
```
[
    {
        "id": 2,
        "name": "mobilexyz",
        "category_id": 1,
        "stock": 600,
        "barcode_num": 6111222,
        "seller": "company_2"
    },
    {
        "id": 3,
        "name": "vision5",
        "category_id": 1,
        "stock": 700,
        "barcode_num": 118819,
        "seller": "company_2"
    },
    {
        "id": 4,
        "name": "receiver_x",
        "category_id": 2,
        "stock": 35,
        "barcode_num": 7777999,
        "seller": "company_x"
    },
    {
        "id": 5,
        "name": "transmitter",
        "category_id": 2,
        "stock": 3,
        "barcode_num": 454545,
        "seller": "company_x"
    },
    {
        "id": 6,
        "name": "car_x",
        "category_id": 3,
        "stock": 5,
        "barcode_num": 3232,
        "seller": "company_y"
    },
    {
        "id": 1,
        "name": "testitem",
        "category_id": 1,
        "stock": 400,
        "barcode_num": 101010,
        "seller": "company_1"
    }
]
```

### LIST ITEMS FILTERED by CATEGORY ID View:
#### - GET - /category/1
#### Response:
```
[
    {
        "id": 2,
        "name": "mobilexyz",
        "category_id": 1,
        "stock": 600,
        "barcode_num": 6111222,
        "seller": "company_2"
    },
    {
        "id": 3,
        "name": "vision5",
        "category_id": 1,
        "stock": 700,
        "barcode_num": 118819,
        "seller": "company_2"
    },
    {
        "id": 1,
        "name": "testitem",
        "category_id": 1,
        "stock": 400,
        "barcode_num": 101010,
        "seller": "company_1"
    }
]
```
#### - GET - /category/3
#### Response:
```
[
    {
        "id": 6,
        "name": "car_x",
        "category_id": 3,
        "stock": 5,
        "barcode_num": 3232,
        "seller": "company_y"
    }
]
```
Try not existing category id:
#### - GET -  /category/5
#### Response:
```
{
    "detail": "category not found"
}
```

### LIST ITEMS FILTERED by SELLER NAME View:
#### - GET - /seller/company_x
#### Response:
```
[
    {
        "id": 4,
        "name": "receiver_x",
        "category_id": 2,
        "stock": 35,
        "barcode_num": 7777999,
        "seller": "company_x"
    },
    {
        "id": 5,
        "name": "transmitter",
        "category_id": 2,
        "stock": 3,
        "barcode_num": 454545,
        "seller": "company_x"
    }
]
```
Try not existing seller name:
#### - GET - /seller/xyz
#### Response:
```
{
    "detail": "seller not found"
}
```

### LIST ITEM FILTERED by NAME View:
#### - GET - /name/vision5
#### Response:
```
{
    "id": 3,
    "name": "vision5",
    "category_id": 1,
    "stock": 700,
    "barcode_num": 118819,
    "seller": "company_2"
}
```
Try not existing item name
#### - GET - /name/xyz
#### Response:
```
{
    "detail": "name not found"
}
```

