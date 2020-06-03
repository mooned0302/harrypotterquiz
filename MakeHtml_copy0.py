
html="<!doctype html>"
html+="<html><head>"
html+="<style>"
html+="	li{"
html+="		list-style-type:decimal;"
html+="	}"
html+="	.title{"
html+="		list-style-type:disc;"
html+="	}"
html+="	</style>"
html+="	</head>"

html+="	<body>"



f=open('question.txt','r')

#문제 html 생성부분
html+="<ul>"

i=0

for s in f:
    if i==0:
        html+="<li><p>"
        html+=s
        html+="</p><div>"
    else:
        html+="<input type='radio' name='"+str(i)+"' value='"+str(i)+"'>"
        html+="<label>"
        html+=s
        html+="</label><br>"
    
    i+=1
    
    
html+="</div></li>"

    
    
'''
<ul>
			<li><p>해리가 맥고나걸 교수에게 받은 빗자루는?</p>
			<div>
				<input type="radio" name="1" value="1" >
			  	<label for="male">님부스2000</label><br>
			  	<input type="radio" name="1" value="2">
			  	<label for="female">파이어볼트</label><br>
			  	<input type="radio" name="1" value="3">
			  	<label for="other">클린스윕</label><br>
				<input type="radio" name="1" value="4">
			  	<label for="other">님부스1000</label><br>
				<input type="radio" name="1" value="5">
			  	<label for="other">님부스2001</label><br>
			</div>
			</li>
            '''


html+="	</body></html>"
f.close()

f1=open('newhtml.html','w')
f1.write(html)
f1.close()
