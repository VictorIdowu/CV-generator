from tkinter import *
from tkinter import messagebox
import pyqrcode
from fpdf import FPDF

class PDFCV(FPDF):
  def header(self):
    self.image("mywebsite.png",10,8,33,title="Portfolio Site")
  
  def footer(self):
    pass

  def generate_cv(self, name, email, phone, address, website, skills, education, experience, about):
    self.add_page()
    self.ln(20)

    # Display Name
    self.set_font('helvetica', 'B', 26)
    self.cell(0,10,name,new_x='LMARGIN',new_y="NEXT",align="C")

    # Display contact info 
    self.set_font('helvetica', 'B', 12)
    self.cell(0,10,"Contact Information",new_x='LMARGIN',new_y="NEXT",align="L")
    self.set_font('helvetica', '', 10)
    self.cell(0,5,"Email: {}".format(email),new_x='LMARGIN',new_y="NEXT")
    self.cell(0,5,"Phone: {}".format(phone),new_x='LMARGIN',new_y="NEXT")
    self.cell(0,5,"Address: {}".format(address),new_x='LMARGIN',new_y="NEXT")

    # Display Skills
    self.ln(10)
    self.set_font('helvetica', 'B', 12)
    self.cell(0,10,"Skills",new_x='LMARGIN',new_y="NEXT",align="L")
    self.set_font('helvetica', '', 10)
    for skill in skills:
      self.cell(0,5,"- {}".format(skill),new_x='LMARGIN',new_y="NEXT")

    # Display Experience
    self.ln(10)
    self.set_font('helvetica', 'B', 12)
    self.cell(0,10,"Work Experience",new_x='LMARGIN',new_y="NEXT",align="L")
    self.set_font('helvetica', '', 10)
    for exp in experience:
      self.cell(0,5,"{}: {}".format(exp['title'],exp['description']),new_x='LMARGIN',new_y="NEXT")
    
    # Display Education
    self.ln(10)
    self.set_font('helvetica', 'B', 12)
    self.cell(0,10,"Education",new_x='LMARGIN',new_y="NEXT",align="L")
    self.set_font('helvetica', '', 10)
    for edu in education:
      self.cell(0,5,"{}: {}".format(edu['degree'],edu['university']),new_x='LMARGIN',new_y="NEXT")
    
    # Display About me
    self.ln(10)
    self.set_font('helvetica', 'B', 12)
    self.cell(0,10,"About me",new_x='LMARGIN',new_y="NEXT",align="L")
    self.set_font('helvetica', '', 10)
    self.multi_cell(0,5,about)

    self.output("cv.pdf")

def generate_cv_pdf():
  name = name_entry.get()
  email = email_entry.get()
  phone = phone_entry.get()
  address = address_entry.get()
  website = website_entry.get()
  skills = skills_entry.get("1.0", END).strip().split('\n')
  education = []
  experience = []

  if not name or not email or not phone or not address or not website or not skills or not education_entry.get("1.0", END) or not experience_entry.get("1.0", END) or not about_entry.get("1.0", END):
    messagebox.showerror("Error", "Please fill all the fields")
    return

  education_lines = education_entry.get("1.0", END).strip().split('\n')
  for line in education_lines:
    degree,university = line.split(":")
    education.append({'degree':degree.strip(), 'university':university.strip()})

  experience_lines = experience_entry.get("1.0", END).strip().split('\n')
  for line in experience_lines:
    title,description = line.split(":")
    experience.append({'title':title.strip(), 'description':description.strip()})
  
  about = about_entry.get("1.0", END)

  # Create QRcode
  qrcode = pyqrcode.create(website)
  qrcode.png("mywebsite.png",scale=5)
  
  cv = PDFCV()
  cv.generate_cv(name,email, phone, address, website, skills, education, experience, about) 


root = Tk()
root.title("CV Generator")


# Name Input
name_label = Label(root, text="Name:")
name_label.pack()
name_entry = Entry(root)
name_entry.pack()

# Email Input
email_label = Label(root, text="Email:")
email_label.pack()
email_entry = Entry(root)
email_entry.pack()

# Phone Input
phone_label = Label(root, text="Phone:")
phone_label.pack()
phone_entry = Entry(root)
phone_entry.pack()

# Address Input
address_label = Label(root, text="Address:")
address_label.pack()
address_entry = Entry(root)
address_entry.pack()

# Website Input
website_label = Label(root, text="Website:")
website_label.pack()
website_entry = Entry(root)
website_entry.pack()

# Skills Input
skills_label = Label(root, text="Skills(Enter one skill per line)")
skills_label.pack()
skills_entry = Text(root, height=5)
skills_entry.pack()

# Education Input
education_label = Label(root, text="Education(Enter one skill per line in format 'Degree':'University')")
education_label.pack()
education_entry = Text(root, height=5)
education_entry.pack()

# Experience Input
experience_label = Label(root, text="Experience(Enter one skill per line in format 'Job Title':'Description')")
experience_label.pack()
experience_entry = Text(root, height=5)
experience_entry.pack()

# About Input
about_label = Label(root, text="About me")
about_label.pack()
about_entry = Text(root, height=5)
about_entry.pack()

# Generate Button
genearte_button = Button(root, text="Generate CV", command=generate_cv_pdf)
genearte_button.pack()

root.mainloop()