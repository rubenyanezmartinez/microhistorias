# MeGusta

from google.appengine.ext import ndb

from model.historia import Historia


class MeGusta (ndb.Model):
    idHistoria = ndb.IntegerProperty(indexed=True, required=True)
    fecha = ndb.DateTimeProperty(auto_now_add=True, required=True)
    nombreUsuario = ndb.StringProperty(required=True)