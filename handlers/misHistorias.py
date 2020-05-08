# coding: utf-8

import webapp2
from google.appengine.ext import ndb
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.historia import Historia
from model.megusta import MeGusta
import datetime


def devolverNumeroDeHistoria(id):
    megustas = MeGusta.query()

    toret = 0
    for meGusta in megustas:
        if meGusta.idHistoria == id:
            toret = toret + 1

    return toret


def existeMeGusta(nombreUsuario, idHistoria):
    megustas = MeGusta.query()

    toret = False

    for meGusta in megustas:
        if meGusta.nombreUsuario == nombreUsuario and meGusta.idHistoria == idHistoria:
            toret = True

    return toret


class MisHistoriasHandler(webapp2.RequestHandler):
    def get(self):

        ## USUARIO
        usr = users.get_current_user()

        if usr:
            usr_url = users.create_logout_url("/")
        else:
            usr_url = users.create_login_url("/")

        ## PAGINACIÓN
        try:
            numHistoriasMostrar = int(self.request.GET["numHistoriasMostrar"])
        except KeyError:
            numHistoriasMostrar = 5

        ## RECUPERAR HISTORIAS
        numHistorias = Historia.query().filter(ndb.StringProperty("nombreUsuario") == usr.nickname()).count()
        historias = Historia.query().filter(ndb.StringProperty("nombreUsuario") == usr.nickname()).order(-Historia.fecha).fetch(limit=numHistoriasMostrar)

        meGustas = {}
        leHaDadoMeGusta = {}

        for historia in historias:
            tempFecha = historia.fecha
            historia.fecha = datetime.datetime(tempFecha.year, tempFecha.month, tempFecha.day, tempFecha.hour,
                                               tempFecha.minute, tempFecha.second)

            meGustas[historia.id] = devolverNumeroDeHistoria(historia.id)
            leHaDadoMeGusta[historia.id] = existeMeGusta(usr.nickname(), historia.id)

        ## PLANTILLA
        valores_plantilla = {
            "numHistorias": numHistorias,
            "paginaRedirigir": "misHistorias",
            "leHaDadoMeGusta": leHaDadoMeGusta,
            "numHistoriasMostrar": numHistoriasMostrar + 5,
            "usr": usr,
            "usr_url": usr_url,
            "historias": historias,
            "meGustas": meGustas
        }

        jinja = jinja2.get_jinja2(app=self.app)

        self.response.write(
            jinja.render_template("misHistorias.html",
                                  **valores_plantilla))


app = webapp2.WSGIApplication([
    ('/misHistorias', MisHistoriasHandler)
], debug=True)
