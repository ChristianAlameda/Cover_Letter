from fpdf import FPDF
from docx2pdf import convert
from docx import Document
import datetime
import time
import os

######################
# Unchanging variables
your_name = 'Christian Alameda'
your_address = '3516 Beachler Drive'
city_state_zip = 'Modesto, California, 95356'
email_address = 'cdalamed@gmail.com'
phone_number = '1-(209)-496-5686'
date = str(datetime.date.today())
#SCHOOLING
degree = 'B.S. in Computer Science'
college = 'CSU Stanislaus'
#FOR COMPANY
recipients_name = 'Whoever May Receive This'
recipients_job_title = 'Reviewer'
#######################

#######################
#CHANGING VARIABLES
company_name = 'Desert Research Institute'
company_address = ''
city_state_zip_1 = ''
#FOR JOB DESCRIPTION

jobs = ['Full-Stack Web Developer', #jobs I'd be fine with
        'Frontend Web Developer', 
        'Backend Web Developer',
        'Software Developer',
        'Data Analyst',
        'Mobile App Developer',
        'Game Developer',
        'DevOps Engineer'
        ]
cs_job_title = 'Full-Stack Web Developer'
company_website = 'Zip Recruiter'
#######################

def make_cover_letter():
    x = f"""
    {your_name}
    {your_address}
    {city_state_zip}
    {email_address}
    {phone_number}
    {date}
    
    {company_name}
    {company_address}
    {city_state_zip_1}

    Dear {recipients_job_title},

    I am writing to express my strong interest in the {cs_job_title} position at {company_name}, as advertised on {company_website}. With a passion for computer science and a proven track record of success in software development, I am confident in my ability to contribute to your team and help drive innovation at {company_name}.

    I recently graduated with a {degree} in Computer Science from {college}. Throughout my academic journey, I have acquired a solid foundation in various programming languages, algorithms, data structures, and software engineering principles. My coursework and projects have equipped me with the technical skills necessary to excel in a CS role. Additionally, I have a strong ability to quickly learn new technologies and adapt to changing environments, which I believe is crucial in the ever-evolving field of computer science.

    During my time at {college}, I actively sought opportunities to apply my knowledge through internships and personal projects. Notably, I completed a summer internship at {company_name}, where I collaborated with a team of developers to design and implement a web application that streamlined the company's internal processes. This experience allowed me to enhance my problem-solving skills, communicate effectively within a team, and deliver high-quality software within tight deadlines.

    In addition to my technical expertise, I possess strong analytical and critical thinking abilities. I can effectively identify and resolve complex issues by employing logical reasoning and utilizing my troubleshooting skills. Furthermore, my attention to detail and commitment to producing clean, efficient code enable me to deliver reliable software solutions.

    Beyond technical skills, I am a dedicated and proactive individual who thrives in a collaborative environment. I have excellent communication skills, which have been honed through team projects and presentations during my academic pursuits. I value teamwork and understand the importance of effective collaboration, as it is essential for delivering successful projects.

    I am particularly drawn to {company_name} because of its reputation for cutting-edge technological advancements and its commitment to innovation. I am eager to contribute to the company's growth by leveraging my technical skills and passion for problem-solving. I believe that my abilities align well with the requirements of the {cs_job_title} position, and I am confident in my potential to make a positive impact on your team.

    Thank you for considering my application. I would welcome the opportunity to further discuss how my skills and experiences align with the goals of {company_name}. I have attached my resume for your review, and I am available at your convenience for an interview. I look forward to the possibility of joining {company_name} and contributing to its ongoing success.

    Sincerely,

    {your_name}
    """
    return x

def make_txt():
    with open('cover_letter.txt', 'w') as f:
        f.write(make_cover_letter())

def make_docx():
    document = Document()
    document.add_paragraph(make_cover_letter())
    file_name = str(company_name)+'.docx'
    document.save(file_name)
    path = "cover_letters"

    if not os.path.exists(path):
        os.makedirs(path)

    
    os.replace(file_name, 'cover_letters/'+file_name)
   
def split_txt():
    #SPLITS TXT DOCUMENT INTO WORDS TO PUT INTO A LIST
    list_of_words = []
    with open("cover_letter.txt") as f:
        for line in f:
            for word in line.split():
                list_of_words.append(word)
    return list_of_words

def make_pdf():
    pass

if __name__ == "__main__":
    make_docx()


