from http.server import BaseHTTPRequestHandler, HTTPServer
 
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 def do_GET(self):
 def do_POST(self):
    try:
      length = int(self.headers["Content-Length"])
      request = self.rfile.read(length)
      print (request.decode('utf-8'))
      self.send_response(200)#如果正确返回200
      self.send_header('Access-Control-Allow-Origin', '*') #实现跨域
      self.end_headers()#结束处理
      str="success"
      self.wfile.write(str.encode('utf-8'))      
      print ("success")
     #self.do_GET()
    except:
      pass 
     
def run():
  print('starting server...') 
  # Server settings
  # Choose port 8000, for port 80, which is normally used for a http server, you need root access
  server_address = ('localhost', 8010)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
  
run()









