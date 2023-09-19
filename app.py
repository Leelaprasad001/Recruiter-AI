from imports import *

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':

        Job_Role=""
        Score="Needed Job Description"

        data=CustomData(Resume_file=request.files['Resume_file'],Job_description_file=request.files['Job_description_file'])
        Score=data.Savedata()

        preprocess=PreprocessPipeline()
        RoleModel_input=preprocess.run()
        Modelpredict=ModelPipeline()
        Job_Role=Modelpredict.predictrole(RoleModel_input)

        Scorepredict=ScorePipeline()
        ScoreModel_input=Scorepredict.scoreprocess()
        Score=Scorepredict.predictscore(ScoreModel_input)

        Recom=Recommend()
        skills=Recom.Get_skills(Job_Role)
        jobs=Recom.Get_jobs(Job_Role)

        
        Webscrap=WebScraping()
        fetched_data=Webscrap.GetList(Job_Role)

        # data.Deletefiles()

    return render_template("results.html",Job_Role=Job_Role,Score=Score,fetched_data=fetched_data,skills=skills,jobs=jobs)


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
