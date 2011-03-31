class DistrictRouter(object):
    """
    Routes reads/writes for the District model to the `districts` DB.
    """
    def db_for_read(self, model, **hints):
        from districts.models import District
        if model == District:
            return 'districts'
        return None

    def db_for_write(self, model, **hints):
        return self.db_for_read(model, **hints)

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_syncdb(self, db, model):
        from districts.models import District
        if db == 'districts':
            return model == District
        elif model == District:
            return False
        return None
