# Runchise

# How to Use this project:
1. download this direcotry
2. extract somewhere
3. open command prompt, and go to the extracted folder
4. type in the command prompt
```
python manage.py migrate
```
5. type in the command prompt
```
python manage.py runserver
```

# List of endpoints:
1. create a new restaurant
```
method POST
http://127.0.0.1:8000/restaurant/create
```
note: send the data in the body

2. show detail a restaurant (name, email, phone number, address) by ID
```
method GET
http://127.0.0.1:8000/restaurant/<id>
```

3. update restaurant's information (name, email, phone number, address)
```
method PUT
http://127.0.0.1:8000/restaurant/<id>
```

4. delete a restaurant by ID
```
method DELETE
http://127.0.0.1:8000/restaurant/<id>
```

5. find restaurant(s) by (name, address, email, and phone number can be 1 or more
field)
```
method GET
http://127.0.0.1:8000/restaurant/search
```

# How to run Unit test
1. open the project directory in command prompt
2. type in the command prompt
```
python manage.py test runchise/
```
