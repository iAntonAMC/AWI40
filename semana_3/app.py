import web

urls = ('/(.*)', 'Visitas')
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()


class Visitas:

    def GET(self, name):
        try:
            cookie = web.cookies()
            visitas = "0"
            print(cookie)
            if name:
                web.setcookie("name", name, expires="", domain=None)
            else:
                name = "Anónimo"
                web.setcookie("name", name, expires="", domain=None)

            if cookie.get("visitas"):
                visitas = int(cookie.get("visitas"))
                visitas += 1
                web.setcookie("visitas", str(visitas), expires="", domain=None)
            else:
                web.setcookie("visitas", str(1), expires="", domain=None)
                visitas = "1"

            return "Visitas " + str(visitas) + " Nombre " + name

        except Exception as e:
            return "Error " + str(e.args)
