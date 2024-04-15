class AuthRouter:
    route_app_label = {'auth','contenttypes','admin'}


    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "north_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "north_db"
        return None
    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "north_db"
        return None
    

class South:
    route_app_label = {'south'}


    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "south_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "south_db"
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "south_db"
        return None

class West:
    route_app_label = {'west'}


    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "west_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "west_db"
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "west_db"
        return None