# coding: utf-8

import webapp2
import time

from model.megusta import MeGusta


class EliminarMeGustaHandler(webapp2.RequestHandler):
    def get(self):
        idHistoria = int(self.request.GET["idHistoria"])
        nickName = self.request.GET["usr"]
        redirigir = self.request.GET["paginaRedirigir"]

        meGustas = MeGusta.query()

        for meGusta in meGustas:
            if meGusta.idHistoria == idHistoria and meGusta.nombreUsuario == nickName:
                meGusta.key.delete()
                break


        time.sleep(1)

        redirigir = "/" + redirigir

        return self.redirect(redirigir)


app = webapp2.WSGIApplication([
    ('/meGustas/eliminar', EliminarMeGustaHandler)
], debug=True)
