<%
dim file,filename
 
file="/tmp/test.html"
filename="test.html"

filename=year(date) & month(date) & day(date) & Hour(time) & minute(time) & second(time) & filename
 
Set objStream = Server.CreateObject("ADODB.Stream")
objStream.Type = 1
objStream.Open
objStream.LoadFromFile file
objStream.SaveToFile 
Server.MapPath(filename),2
objStream.Close
%>
