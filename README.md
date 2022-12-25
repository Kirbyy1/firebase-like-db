# RealtimeDatabase
A Python class that simulates a real-time database and saves the data in a JSON file.

# Features
* Real-time event notifications: The on_change method allows you to register a callback function that will be invoked whenever the data at a specific path changes.
* Query data using the child method: The child method allows you to access and modify specific child nodes within the database, similar to how the child method works in Firebase Realtime Database. If the path argument is not provided, a random key will be generated.
* Set, get, and delete data: The set, get, and delete methods allow you to set, retrieve, and delete data from the database, respectively.

# Example
```py
db = RealtimeDatabase('database.json')

# Set data
db.child('users').child('alice').set({'name': 'Alice', 'age': 25})

# Get data
print(db.child('users').child('alice').get())  # {'name': 'Alice', 'age': 25}

# Delete data
db.child('users').child('alice').delete()

# Register a change listener
def on_change(data):
    print(f'Data at path "users/alice" has changed: {data}')

db.child('users').child('alice').on_change(on_change)

# Set data, which will trigger the change listener
db.child('users').child('alice').set({'name': 'Alice', 'age': 25})  # Prints "Data at path "users/alice" has changed: {'name': 'Alice', 'age': 25}"
```

# Requirements
* Python 3.5 or higher
