class DistrictRouter(object):
    """
    Routes reads/writes for the District model to the `districts` DB
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'districts':
            return 'districts'
        return None

    def db_for_write(self, model, **hints):
        return self.db_for_read(model, **hints)

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_syncdb(self, db, model):
        if db == 'districts':
            return model._meta.app_label == 'districts'
        elif model._meta.app_label == 'districts':
            return False
        return None