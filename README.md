# TestOne
SimplePythonHttpBrowse

This is a Simple Example of B/C model using Javascript and Python via Http 
Browser send a message to Server  by Object of XMLHttRequest
Server uses HttpServer and BaseHTTPRequestHandler model Responsing Browser by executing do_POST method
recieving message that comes from browser

// Following are headers that Server Responsing Browser
      self.send_response(200)#如果正确返回200
      self.send_header('Access-Control-Allow-Origin', '*') #实现跨域
      self.end_headers()#结束处理
      
      
