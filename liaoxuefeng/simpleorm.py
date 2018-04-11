# -*- coding: utf-8 -*-
' Simple ORM using MetaClass '


class Field(object):
    def __init__(self, name, columnType):
        self.name = name
        self.columnType = columnType

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'VARCHAR(100)')


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaClass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()  # 用于存储新建类中的属性
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping %s >> %s' % (k, v))
                mappings[k] = v
        for key in mappings.keys():
            attrs.pop(key)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaClass):

    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        args = []
        fields = []
        params = []
        for k, v in self.__mappings__.items():
            fields.append(k)
            params.append('?')
            args.append(getattr(self, k))
        sql = 'insert into %s (%s) values(%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL %s' % sql)
        print('ARGS %s' % str(args))


# testing code:

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
