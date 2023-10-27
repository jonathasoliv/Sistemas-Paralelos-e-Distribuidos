from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

server = SimpleXMLRPCServer(("localhost", 9050))

def senhas():
	with open("senhas.txt", "rb") as handle:
		return xmlrpc.client.Binary(handle.read())

server.register_function(senhas, "senhas")

server.register_introspection_functions()
server.serve_forever()