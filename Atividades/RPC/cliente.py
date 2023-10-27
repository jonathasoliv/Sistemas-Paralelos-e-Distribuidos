import xmlrpc.client

s = xmlrpc.client.ServerProxy('https://localhost:9050')


print(s.senhas())