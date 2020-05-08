# coding: utf-8
# Nueva historia

import webapp2
import time

from model.historia import Historia


class NuevaHistoriaHandler(webapp2.RequestHandler):
    def post(self):
        titulo = self.request.get("titulo", "")
        texto = self.request.get("texto", "")
        nombreUsuario = self.request.get("nombreUsuario", "")

        #Comprobar si algún parámetro es incorrecto
        if titulo.__len__() == 0 or texto.__len__() == 0:
            return self.redirect("/")
        else:
            # Obtener historias para obtener el ID
            historias = Historia.query()
            ids = []
            for historia in historias:
                ids.append(historia.id)

            if not ids:
                indice = 0
            else:
                indice = (max(ids) + 1)

            #Crear una nueva historia y guardar
            historia = Historia(id=indice, titulo=titulo, texto=texto, nombreUsuario=nombreUsuario)
            historia.put()
            time.sleep(1)

            return self.redirect("/")





app = webapp2.WSGIApplication([
    ('/historias/nueva', NuevaHistoriaHandler)
], debug=True)
