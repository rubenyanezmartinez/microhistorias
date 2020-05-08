# coding: utf-8

import webapp2
import time

from model.historia import Historia


class EliminarHistoriaHandler(webapp2.RequestHandler):
    def get(self):
        idHistoria = int(self.request.GET["idHistoria"])
        redirigir = self.request.GET["paginaRedirigir"]

        historias = Historia.query()

        for historia in historias:
            if historia.id == idHistoria:
                historia.key.delete()
                break


        time.sleep(1)

        redirigir = "/" + redirigir

        return self.redirect(redirigir)


app = webapp2.WSGIApplication([
    ('/historias/eliminar', EliminarHistoriaHandler)
], debug=True)
