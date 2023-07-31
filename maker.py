from fpdf import FPDF
from docx2pdf import convert
from docx import Document
import docx

import os
import re

#Unchanging variables
your_name = 'Christian Alameda'
your_address = '3516 Beachler Drive'
city_state_zip = 'Modesto, California, 95356'
email_address = 'cdalamed@gmail.com'
phone_number = '1-(209)-496-5686'
date = 'July 17 2023'
#SCHOOLING
degree = 'B.S.'
college = 'CSU Stanislaus'

#Changing variables
#FOR COMPANY
recipients_name = 'Whoever May Receive This'
recipients_job_title = 'Reviewer'
company_name = 'JPMorgan Chase & Co.'
company_address = '2390 El Camino Real, Unit 110'
city_state_zip_1 = 'Palo Alto, California, 94306'
#for job description
cs_job_title = 'Software Engineering Summer Internship'
company_website = 'Handshake'

def make_cover_letter():
    x = f"""
    {your_name}
    {your_address}
    {city_state_zip}
    {email_address}
    {phone_number}
    {date}
    \n
    {recipients_name}
    {recipients_job_title}
    {company_name}
    {company_address}
    {city_state_zip_1}
    \n

    Dear {recipients_name},

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
    with open('cover_letter.docx', 'w') as f:
        f.write(make_cover_letter())

def split_txt():
    #SPLITS TXT DOCUMENT INTO WORDS TO PUT INTO A LIST
    list_of_words = []
    with open("cover_letter.txt") as f:
        for line in f:
            for word in line.split():
                list_of_words.append(word)
    return list_of_words

def make_pdf():
    """x = split_txt()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', size=12)
    for i in x:
        ten_words = ""
        ten_words = ten_words + i
        pdf.cell(txt=ten_words)
    pdf.output("hello_world.pdf")"""
    """doc.save("cover_letter.docx")"""
    doc = Document()
    doc.add_heading('Report',0)
    doc.save('report.docx')
    #convert("cover_letter.docx", "report.pdf")

if __name__ == "__main__":
    make_pdf()