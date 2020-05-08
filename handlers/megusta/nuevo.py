# coding: utf-8

import webapp2
import time

from model.megusta import MeGusta


class NuevoMeGustaHandler(webapp2.RequestHandler):
    def get(self):
        idHistoria = int(self.request.GET["idHistoria"])
        nickName = self.request.GET["usr"]
        redirigir = self.request.GET["paginaRedirigir"]

        meGusta = MeGusta(idHistoria=idHistoria, nombreUsuario=nickName)
        meGusta.put()
        time.sleep(1)

        redirigir = "/" + redirigir

        return self.redirect(redirigir)


app = webapp2.WSGIApplication([
    ('/meGustas/nuevo', NuevoMeGustaHandler)
], debug=True)
