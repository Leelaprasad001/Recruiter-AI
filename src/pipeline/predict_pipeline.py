from imports import *

class PreprocessPipeline:
    def __init__(self):
        pass

    def run(self):
        try:
            resume_path = os.path.join("artifacts", "Resume_file.pdf")
            preprocessor = Preprocessing()
            Text = preprocessor.extract_resume_text(resume_path)
            # if(Text==""): print("Why not given")
            Tokens = preprocessor.preprocess_text(Text)
            Model_input = preprocessor.pos_filter(Tokens)
            return Model_input
        except Exception as e:
            raise CustomException(e,sys)

class ModelPipeline:
    def __init__(self):
        pass

    def predictrole(self,Model_input):
        try:
            labels = {6: 'Data Science', 12: 'HR', 0: 'Advocate', 1: 'Arts', 24: 'Web Designing', 16: 'Mechanical Engineer', 22: 'Sales', 14: 'Health and fitness', 5: 'Civil Engineer', 15: 'Java Developer', 4: 'Business Analyst', 21: 'SAP Developer', 2: 'Automation Testing', 11: 'Electrical Engineering', 18: 'Operations Manager', 20: 'Python Developer', 8: 'DevOps Engineer', 17: 'Network Security Engineer', 19: 'PMO', 7: 'Database', 13: 'Hadoop', 10: 'ETL Developer', 9: 'DotNet Developer', 3: 'Blockchain', 23: 'Testing'}
            tokenizer = AutoTokenizer.from_pretrained("./models/")
            model = AutoModelForSequenceClassification.from_pretrained("./models/")
            tokens = tokenizer.encode_plus(Model_input,max_length=512, truncation=True,padding="max_length",return_tensors="pt")
            outputs = model(**tokens)
            predicted_label = outputs.logits.argmax().item()
            output=labels[predicted_label]
            return output
        except Exception as e:
            raise CustomException(e,sys)


class ScorePipeline:
    def __init__(self):
        pass
    
    def scoreprocess(self):
        try:
            resume_path = os.path.join("artifacts", "Resume_file.pdf")
            job_description_path = os.path.join("artifacts", "Job_description_file.pdf")
            preprocessor = Preprocessing()
            Resume_Text = preprocessor.extract_resume_text(resume_path)
            Job_description_Text = preprocessor.extract_resume_text(job_description_path)
            # Resume_Named_Entities = preprocessor.extract_named_entities(Resume_Text)
            # job_description_keywords = preprocessor.extract_keywords(Job_description_Text)
            Score_Model_input=[Resume_Text,Job_description_Text]
            return Score_Model_input
        except Exception as e:
            raise CustomException(e,sys)

    def predictscore(self,Score_Model_input):
        try:
            ob = CountVectorizer()
            matrix = ob.fit_transform(Score_Model_input)
            similarity_matrix =  cosine_similarity(matrix)
            score = similarity_matrix[0][1] * 100
            score = round(score,2)
            return score
        except Exception as e:
            raise CustomException(e,sys)


class Recommend:
    def __init__(self):
        self.Role_recommen_file= pd.read_csv("artifacts/Recom.csv")


    def Get_skills(self,Job_Role):
        category_data = self.Role_recommen_file[self.Role_recommen_file['Category'] == Job_Role]
        skills = eval(category_data['Skills'].iloc[0])[:5]
        return skills

    def Get_jobs(self,Job_Role):
       category_data = self.Role_recommen_file[self.Role_recommen_file['Category'] == Job_Role]
       job_roles = eval(category_data['Job_Roles'].iloc[0])[:5]
       return job_roles

class WebScraping:
    def __init__(self):
        pass

    def internshala(self,job_url):
        try:
            job_url = requests.get(job_url)
            soup = BeautifulSoup(job_url.content, 'html.parser')
            job_cards = soup.find_all('div', class_='individual_internship')
            jobs_list = []
            for card in job_cards:

                job_title_elem = card.find('h3', class_='heading_4_5 profile')
                company_name_elem = card.find('h4', class_='heading_6 company_name')
                location_elem = card.find('a', class_='location_link')
                start_date_elem = card.find('div', id='start-date-first')
                salary = card.find('div', class_='salary')
                experience = card.find('div', class_='desktop-text')
                apply = card.find('a')

                if not all([job_title_elem, company_name_elem, location_elem, start_date_elem, salary, experience]):
                    continue

                job_title = job_title_elem.text.strip()
                company_name = company_name_elem.text.strip()
                location = location_elem.text.strip()
                start_date = start_date_elem.text.replace('Starts\xa0','').strip()
                salary = salary.text.strip()
                experience = experience.text.strip()
                apply = "https://internshala.com" + apply['href']

                job_info = {
                    'Job_Title': job_title,
                    'Company_Name': company_name,
                    'Location': location,
                    'Start_Date': start_date,
                    'Salary': salary,
                    'experience': experience,
                    'apply' : apply
                }
                jobs_list.append(job_info)
            return jobs_list
        except Exception as e:
            raise CustomException(e,sys)
        
    
    def fresherworld(self,job_url,Job_Role):
        try:
            r = requests.get(job_url)
            soup = BeautifulSoup(r.content, 'html.parser')
            job_cards = soup.find_all('div', class_='col-md-12 col-lg-12 col-xs-12 padding-none job-container jobs-on-hover top_space')
            jobs_list = []
            for card in job_cards:
                job_title_elem = card.find('span', class_='wrap-title seo_title')
                company_name_elem = card.find('h3', class_='latest-jobs-title font-16 margin-none inline-block company-name')
                location_elem = card.find('span', class_='job-location display-block modal-open job-details-span')
                start_date_elem = card.find('span', class_='desc')
                apply = card.get('job_display_url')
                experience = card.find('span', class_='experience job-details-span')
                if not all([job_title_elem, company_name_elem, location_elem, start_date_elem, apply, experience]):
                    continue
                # job_title = Job_Role
                # job_title = job_title_elem.text.strip()
                # company_name = "amzur technologies"
                company_name = company_name_elem.text.strip()
                location = location_elem.text.strip()
                start_date = start_date_elem.text.strip()
                experience = experience.text.strip()
                salary="Not Mentioned"
                job_info = {
                    'Job_Title': Job_Role,
                    'Company_Name': company_name,
                    'Location': location,
                    'Start_Date': start_date,
                    'Salary': salary,
                    'experience': experience,
                    'apply': apply
                }
                jobs_list.append(job_info)
            return jobs_list
        except Exception as e:
            raise CustomException(e,sys)
        
    def GetList(self,Job_Role):
        try:
            Job_Role=Job_Role.replace(' ','-').lower()+"-jobs/"
            jobs_list_internshala=[]
            # jobs_list_fresherworld=[]

            job_url_string_internshala='https://internshala.com/jobs/'+Job_Role
            jobs_list_internshala=self.internshala(job_url_string_internshala)
            # job_url_string_fresherworld='https://www.freshersworld.com/jobs/jobsearch/python-developer-jobs-for-be-btech?course=16'
            # job_url_string_fresherworld='https://www.freshersworld.com/jobs/jobsearch/'+Job_Role+'-jobs-for-be-btech?course=16'
            # jobs_list_fresherworld=self.fresherworld(job_url_string_fresherworld,Job_Role)
            # print(len(jobs_list_fresherworld))
            # print(jobs_list_freskoherworld[0])
            return jobs_list_internshala
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(self, Resume_file, Job_description_file):
        self.Resume_file = Resume_file
        self.Job_description_file = Job_description_file

    def Savedata(self):
        self.Resume_file.save(os.path.join("artifacts", "Resume_file.pdf"))
        if self.Job_description_file:
            self.Job_description_file.save(os.path.join("artifacts", "Job_description_file.pdf"))
        else:
            return "Job_description_file is not uploaded ..... !"
        return ""
    
    def Deletefiles(self):
        try:
            if os.path.exists(os.path.join("artifacts", "Resume_file.pdf")):
                os.remove(os.path.join("artifacts", "Resume_file.pdf"))
            if os.path.exists(os.path.join("artifacts", "Job_description_file.pdf")):
                os.remove(os.path.join("artifacts", "Job_description_file.pdf"))    
        except Exception as e:
            raise CustomException(e,sys)


if __name__ == "__main__":
    pass