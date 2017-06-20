from twisted.application.service import Application, Service
from twisted.application.internet import TCPServer
from twisted.web import server, static, resource 

application = Application("my-server")
root_resource = resource.Resource()
data_resource = static.Data(
   "<html><body><em>Hello, world!</em></body></html>",
   "text/html")
root_resource.putChild("", data_resource)
site = server.Site(root_resource)
web_service = TCPServer(8080, site)
web_service.setServiceParent(application)
