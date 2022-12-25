# RealtimeDatabase
A Python class that simulates a real-time database and saves the data in a JSON file.

# Features
* Real-time event notifications: The on_change method allows you to register a callback function that will be invoked whenever the data at a specific path changes.
* Query data using the child method: The child method allows you to access and modify specific child nodes within the database, similar to how the child method works in Firebase Realtime Database. If the path argument is not provided, a random key will be generated.
* Set, get, and delete data: The set, get, and delete methods allow you to set, retrieve, and delete data from the database, respectively.
