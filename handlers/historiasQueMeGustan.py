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


class HistoriasQueMeGustanHandler(webapp2.RequestHandler):
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
        numHistorias = Historia.query().count()
        historias = Historia.query().order(-Historia.fecha).fetch(limit=numHistoriasMostrar)

        meGustas = {}
        leHaDadoMeGusta = {}

        for historia in historias:
            tempFecha = historia.fecha
            historia.fecha = datetime.datetime(tempFecha.year, tempFecha.month, tempFecha.day, tempFecha.hour,
                                               tempFecha.minute, tempFecha.second)

            meGustas[historia.id] = devolverNumeroDeHistoria(historia.id)
            leHaDadoMeGusta[historia.id] = existeMeGusta(usr.nickname(), historia.id)

        numHistorias = 0
        for mg in leHaDadoMeGusta.items():
            if mg[1] == True:
                numHistorias = numHistorias + 1

        ## PLANTILLA
        valores_plantilla = {
            "numHistorias": numHistorias,
            "paginaRedirigir": "historiasQueMeGustan",
            "leHaDadoMeGusta": leHaDadoMeGusta,
            "numHistoriasMostrar": numHistoriasMostrar + 5,
            "usr": usr,
            "usr_url": usr_url,
            "historias": historias,
            "meGustas": meGustas
        }

        jinja = jinja2.get_jinja2(app=self.app)

        self.response.write(
            jinja.render_template("historiasQueMeGustan.html",
                                  **valores_plantilla))


app = webapp2.WSGIApplication([
    ('/historiasQueMeGustan', HistoriasQueMeGustanHandler)
], debug=True)
