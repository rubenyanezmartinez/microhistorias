# Historia

from google.appengine.ext import ndb

class Historia (ndb.Model):
    id = ndb.IntegerProperty(required=True)
    titulo = ndb.StringProperty(required=True)
    texto = ndb.TextProperty(required=True)
    fecha = ndb.DateTimeProperty(auto_now_add=True, indexed=True, required=True)
    nombreUsuario = ndb.StringProperty(required=True)