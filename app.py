#  Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser  
# .venv\Scripts\Activate.ps1 
# python -m flask run --host=0.0.0.0 --port=8080

from flask import Flask, redirect, render_template, request, url_for
#from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True
comments = []

import pandas as pd
df = pd.read_csv('/home/im2aaditya/mysite/data.csv')
#print("DataFrame:\n", df )

Prog_list=df.Program.unique()
Inst_list=df.Institute.unique()
Cat_list=df.Category.unique()
Quota_list=df.Quota.unique()
Round_list=df.Round.unique()

Prog='Computer Science and Engineering (Artificial Intelligence & Machine Learning) (Shift I)'
Inst='NOIDA INSTITUTE OF ENGG. & TECHNOLOGY,GAUTAM BUDDH NAGAR'
Cat='OPEN'
Quota='Home State'
Rank=472040
Round='Round 4'

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=comments, proglist=Prog_list, roundlist=Round_list, catlist=Cat_list, quotalist=Quota_list) 

    comments.clear()
    #comments.append(request.form["Prog"])
    Prog=request.form["Prog"]
    Round=request.form["Round"]
    Cat=request.form["Cat"]
    Quota=request.form["Quota"]
    Rank=int(request.form["Rank"])
    
    if (Round == 'Select'):
        rslt_df = df[(df['Program'].str.strip() == Prog) &
              (df['Category'].str.strip() == Cat) & 
              (df['Quota'].str.strip() == Quota) &
              ((df['Closing Rank']) >= Rank)
              ]
    if (Round != 'Select'):
        rslt_df = df[(df['Program'].str.strip() == Prog) &
              (df['Category'].str.strip() == Cat) & 
              (df['Quota'].str.strip() == Quota) &
              ((df['Closing Rank']) >= Rank) &
              ((df['Round']) == Round)
              ]

    comments.append(""+Prog+"    at Rank:"+str(Rank)+"   in - "+Round+"  total:"+str(len(rslt_df))+" ("+Quota+")")
    comments.append("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    sno=0
    for index, row in rslt_df.iterrows():
        sno=sno+1
        comments.append(str(sno)+" "+row['Institute']+" Till Rank: "+str(row['Closing Rank'])+"  In: "+row['Round'] )
    
    return redirect(url_for('index'))

# Program Pridictor -----------------------------

@app.route("/program", methods=["GET", "POST"])
def index1():
    if request.method == "GET":
        return render_template("main_page1.html", comments=comments, instlist=Inst_list, roundlist=Round_list, catlist=Cat_list, quotalist=Quota_list) 

    comments.clear()
    #comments.append(request.form["Prog"])
    Inst=request.form["Inst"]
    Round=request.form["Round"]
    Cat=request.form["Cat"]
    Quota=request.form["Quota"]
    Rank=int(request.form["Rank"])
    
    if (Round == 'Select'):
        rslt_df = df[(df['Institute'].str.strip() == Inst) &
              (df['Category'].str.strip() == Cat) & 
              (df['Quota'].str.strip() == Quota) &
              ((df['Closing Rank']) >= Rank)
              ]
    if (Round != 'Select'):
        rslt_df = df[(df['Institute'].str.strip() == Inst) &
              (df['Category'].str.strip() == Cat) & 
              (df['Quota'].str.strip() == Quota) &
              ((df['Closing Rank']) >= Rank) &
              ((df['Round']) == Round)
              ]

    comments.append(""+Inst+"    at Rank:"+str(Rank)+"   in - "+Round+"  total:"+str(len(rslt_df))+" ("+Quota+")")
    comments.append("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    sno=0
    for index, row in rslt_df.iterrows():
        sno=sno+1
        comments.append(str(sno)+" "+row['Program']+" Till Rank: "+str(row['Closing Rank'])+"  In: "+row['Round'] )
    
    return redirect(url_for('index1'))
