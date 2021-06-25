from .. import bfobject as Object


class Stream:
  def __init__(self,client=None,server=None):
    self.server = server
    self.client = client
  
  
  def create(self,streamid,source,destination,command,startdata,responsecommand):
     self.streamid = streamid
     self.source = source
     self.destination = destination
     self.command = command
     self.startdata = startdata
     self.responsecommand = responsecommand


  
  def format(self):
    response = {
                "streamid" : self.streamid,
                "source" : self.source,
                "destination" : self.destination,
                "command" : self.command,
                "data" : self.startdata,
                "responsecommand" : self.responsecommand
                }
    return response
  def format_for_streams(self):
    response = {
                "streamid" : self.streamid,
                "source" : self.source,
                "destination" : self.destination,
                "command" : self.command,
                "responsecommand" : self.responsecommand
                }
    return response
    
  def push(self,data):
    obj = Object.Object()
    packet = {"stream" : self.format_for_streams() , "data" : data} 
    obj.create(self.destination,"ceo","response","stream", packet)
    self.client.send(obj.format())



