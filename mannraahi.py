from flask import Flask, render_template, request
import mysql.connector
from datetime import date
mydb=mysql.connector.connect(host="127.0.0.1",user="root",passwd="1111",database="blog")
mycursor=mydb.cursor()

app = Flask(__name__)
  
@app.route('/connections', methods=['POST'])
def connections():
    if request.method=="POST":
        a = request.form['username']
        b = request.form['Follow']
        b=str(b)+","
        l="update users set connections=CONCAT(connections,"+"'"+b+"')"+"where username="+"'"+a+"'"
        mycursor.execute(l)
        mydb.commit()
        lst1=[]
        lst2=[]
        l="select username from users"
        mycursor.execute(l)
        for i in mycursor:
            lst1.append(i[0])
        lst1.remove(a)
        l="select connections from users where username="+"'"+a+"'"
        mycursor.execute(l)
        for i in mycursor:
            cons=i[0]
            lst2=cons.split(sep=",")
        set1 = set(lst1)
        set2 = set(lst2)
        lst=list(set1.symmetric_difference(set2))
        try:
            lst.remove('')
            return render_template('connections.html',username=a,my_array=lst)
        except:
            return render_template('connections.html',username=a,my_array=lst)
        
@app.route('/writeblog', methods=['POST'])
def writeblog():
    if request.method=="POST":
        a = request.form['username']
        title=str(request.form['title'])
        dat=str(date.today())
        blog=str(request.form['content'])
        blogs=title+","+dat+","+blog+":"
        l="update users set blogs=CONCAT(blogs,"+"'"+blogs+"')"+"where username="+"'"+a+"'"
        mycursor.execute(l)
        mydb.commit()
        l="select blogs from users where username ="+"'"+a+"'"+";"
        mycursor.execute(l)
        for i in mycursor:
            c=str(i).split(sep=":")
            try:
                c=(c[-2]).split(sep=",")
            except:
                c=(c[1]).split(sep=",")
    return render_template('dashboard.html',my_array=c,username=a)

@app.route('/selection', methods=['POST'])
def selection():
    if request.method=="POST":
        a = request.form['username']
        b = request.form['navo']
        if b=="wr":
            return render_template('writeblog.html',username=a)
        

@app.route('/blogs', methods=['POST'])
def blogs():
    if request.method=="POST":
        a = request.form['username']
        b = request.form['navo']
        if b=="yb":
            l="select blogs from users where username ="+"'"+a+"'"+";"
            mycursor.execute(l)
            for i in mycursor:
                c=str(i).split(sep=":")
                c=c[1:-1]
                l=len(c)
            return render_template('yourblogs.html',username=a,l=l,detail=c)
        elif b=="fe":
            lst1=[]
            lst2=[]
            l="select connections from users where username="+"'"+a+"'"
            mycursor.execute(l)
            for i in mycursor:
                cons=i[0]
                lst1=cons.split(sep=",")
                try:
                    lst1.remove('')
                except:
                    continue
            for i in lst1:
                l="select blogs from users where username ="+"'"+i+"'"+";"
                mycursor.execute(l)
                for j in mycursor:
                    c=str(j).split(sep=":")
                    c=c[1:-1]
                try:
                    lst2.append(c[-1]+","+i)
                except:
                    c=["No Blog,--------,No Content"]
                    lst2.append(c[0]+","+i)
            l=len(lst2)
            return render_template('feed.html',username=a,l=l,detail=lst2)
        elif b=="co":    
           if request.method=="POST":
                a = request.form['username']
                lst1=[]
                lst2=[]
                l="select username from users"
                mycursor.execute(l)
                for i in mycursor:
                    lst1.append(i[0])
                lst1.remove(a)
                l="select connections from users where username="+"'"+a+"'"
                mycursor.execute(l)
                for i in mycursor:
                    cons=i[0]
                    try:
                        lst2=cons.split(sep=",")
                    except:
                        continue
                set1 = set(lst1)
                set2 = set(lst2)
                lst=list(set1.symmetric_difference(set2))
                try:
                    lst.remove('')
                    return render_template('connections.html',username=a,my_array=lst)
                except:
                    return render_template('connections.html',username=a,my_array=lst)
    return render_template('ExploreLife.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method=="POST":
        a = request.form['username']
        b = request.form['password']
        c = request.form['contact']
        d = request.form['gender']
        e = request.form['birthdate']
        l="insert into users (username ,passwor,contact,sex,DOB,blogs,connections) values ("+ "'"+a+"'"+","+ "'"+b+"'"+","+ "'"+c+"'"+","+ "'"+d+"'"+","+ "'"+e+"'"+","+ "':'"+","+ "''"+ ")"
        mycursor.execute(l)
        mydb.commit()
    return render_template('login.html')

@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    if request.method=="POST":
        a = request.form['username']
        b = request.form['password']    
        l="select passwor from users where username ="+"'"+a+"'"+";"
        mycursor.execute(l)
        for i in mycursor:
            c=(i[0])
            if b==c:
                l="select blogs from users where username ="+"'"+a+"'"+";"
                mycursor.execute(l)
                for i in mycursor:
                    c=str(i).split(sep=":")
                    c.remove("('")
                    try:
                        c=(c[-2]).split(sep=",")
                    except:
                        c=["No Blog By You","--------","No Content"]
                    
                return render_template('dashboard.html',my_array=c,username=a)
            else:
                return render_template('login.html')
    return render_template('ExploreLife.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method=="POST":
        a = request.form['button_clicked']
        if a=="login":
            return render_template('login.html')
        elif a=="signup":
            return render_template('signup.html')
    return render_template('ExploreLife.html')

@app.route('/')
def index():
    return render_template('ExploreLife.html')

if __name__ == '__main__':
    app.run(debug=True)
