import json
import uuid


class RealtimeDatabase:
    def __init__(self, filename):
        self.filename = filename
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}

        self._listeners = {}

    def child(self, path):
        parts = path.split('/')
        data = self.data
        for part in parts:
            if part not in data:
                data[part] = {}
            data = data[part]
        return RealtimeDatabaseChild(self, path)

    def set(self, path, value):
        parts = path.split('/')
        data = self.data
        for part in parts[:-1]:
            if part not in data:
                data[part] = {}
            data = data[part]
        data[parts[-1]] = value
        self._save()

    def get(self, path):
        parts = path.split('/')
        data = self.data
        for part in parts:
            if part not in data:
                return None
            data = data[part]
        return data

    def delete(self, path):
        parts = path.split('/')
        data = self.data
        for part in parts[:-1]:
            if part not in data:
                return
            data = data[part]
        del data[parts[-1]]
        self._save()

    def on_change(self, path, callback):
        self._listeners[path] = callback

    def _save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=4, sort_keys=True, separators=(',', ': '))

    def _notify_listeners(self, path):
        for listener_path, callback in self._listeners.items():
            if listener_path == path or listener_path.startswith(f'{path}/'):
                callback(path, self.get(path))


class RealtimeDatabaseChild:
    def __init__(self, db, path=None):
        self.db = db
        self.path = str(uuid.uuid4()) if path is None else path

    def set(self, value):
        self.db.set(self.path, value)

    def get(self):
        return self.db.get(self.path)

    def delete(self):
        self.db.delete(self.path)

    def on_change(self, callback):
        self.db.on_change(self.path, callback)

    def child(self, path=None):
        if path is None:
            return RealtimeDatabaseChild(self.db, f'{self.path}/{str(uuid.uuid4())}')
        else:
            return RealtimeDatabaseChild(self.db, f'{self.path}/{path}')
