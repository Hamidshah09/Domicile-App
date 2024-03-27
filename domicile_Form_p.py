from fpdf import FPDF
import os
from PIL import Image, ImageTk


def preview():
    pdf = FPDF()
    pdf.add_page()
    #pdf.add_font('Courier New', '', 'GOTHIC.TTF', uni=True)
    #pdf.add_font('Centory Gothic', 'B', 'GOTHICB.TTF', uni=True)
    pdf.image('PROVISIONAL.png', x=0, y=0, w=200, h=400)
    pdf.set_font('Helvetica', '', size=12)
    pdf.set_fill_color(211, 211, 211)
    pdf.ln(8)
    pdf.set_font('Helvetica', 'BU', size=11)
    pdf.cell(45, 6, txt='No.29046',
             align='C')
    pdf.cell(38, 6, txt='',
             align='C')
    pdf.cell(30, 6, txt='Form P',
             align='C')
    pdf.cell(38, 6, txt='',
             align='C')
    pdf.cell(30, 6, txt='Date:2023-04-12',
             align='C', ln=1)
    # pdf.set_font('Helvetica', '', size=11)
    pdf.ln(8)
    pdf.ln(8)
    pdf.cell(
        0, 6, txt='THE PAKISTAN CITIZEN ACT, 1951 (II OF 1951) AND RULES', ln=1, align='C')
    pdf.cell(
        0, 6, txt='MADE THERE UNDER (VIDE RULES 23)', ln=1, align='C')
    pdf.cell(
        0, 6, txt='PROVISIONAL DOMICILE USED ONLY FOR CITIZENSHIP CASE', ln=1, align='C')
    pdf.ln(8)
    pdf.set_font('Helvetica', '', size=11)
    pdf.multi_cell(0, 6, txt="Whereas Mr/Ms/Mrs SIMAR DEVI (s/d/w)/o MUKHTAR AHMAD has applied for a certificate of Domicile under the Pakistan Citizenship Act 1951 (II of 1951) alleging with respect to himself/herself here is the particulars set on below, and has satisfied the undersigned that the condition laid down in section 17 of the said Act, for the grant of the certificate of domicile are fulfilled in the said SIMAR DEVI case.")
    pdf.ln(8)
    pdf.multi_cell(0, 6, txt='Now, therefore, in pursuance of the powers conferred by the said Act and rules made there under the undersigned hereby grants to the said SIMAR DEVI this certificate of domicile. In witness where of I have to subscribed my name at this day of 2023-04-12')
    pdf.ln(8)
    pdf.cell(
        0, 6, txt='PARTICULARS RELATING TO THE APPLICANT', ln=1, align='C')
    pdf.ln(8)
    pdf.cell(70, 6, txt='Full Name')
    pdf.cell(40, 6, txt='SIMAR DEVI', ln=1)

    pdf.cell(70, 6, txt='Father/Husband Name :')
    pdf.cell(40, 6, txt='MUKHTAR AHMAD', ln=1)

    pdf.cell(70, 6, txt='Place of Domicile')
    pdf.cell(40, 6, txt='Islamabad', ln=1)

    pdf.cell(70, 6, txt='Prov/Admin/West Pakistan :')
    pdf.cell(40, 6, txt='FEDERAL AREA', ln=1)

    pdf.cell(70, 6, txt='Date of arrival in place of Domicile')
    pdf.cell(40, 6, txt='27/01/2022', ln=1)

    pdf.cell(70, 6, txt='Married/Single/Widow/Widower')
    pdf.cell(40, 6, txt='Married', ln=1)

    pdf.cell(70, 6, txt='Spouce Name :')
    pdf.cell(40, 6, txt='MUKHTAR AHMAD', ln=1)

    pdf.cell(70, 6, txt='Address in Islamabad')
    pdf.cell(100, 6, txt='H # 799, ST # 16, SEC. I-8/2, ISLAMABAD', ln=1)
    pdf.cell(130, 6, txt='')
    pdf.cell(25, 6, txt='Date of Birth:')
    pdf.set_font('Helvetica', 'BU', size=11)
    pdf.cell(25, 6, txt='07/12/1976')
    pdf.set_font('Helvetica', '', size=11)

    pdf.image('sign.jpeg', x=140, y=235, w=35, h=30)
    pdf.image('applicant_pic.jpeg', x=140, y=195, w=35, h=45)
    pdf.ln(8)
    pdf.ln(8)
    pdf.cell(50, 6, txt='Name of children and their ages:')
    pdf.ln(8)
    # pdf.cell(70, 6, txt='Name')
    # pdf.cell(40, 6, txt='Date of Birth', ln=1)
    # pdf.cell(70, 6, txt='MAHNOOR FATIMA')
    # pdf.cell(40, 6, txt='21/12/2015', ln=1)
    # pdf.cell(70, 6, txt='MUHAMMAD IBRAHIM')
    # pdf.cell(40, 6, txt='03/03/2020', ln=1)
    pdf.ln(8)
    pdf.ln(8)
    pdf.cell(70, 6, txt='Trade of Occupation :')
    pdf.cell(40, 6, txt='House Wife', ln=1)
    pdf.cell(70, 6, txt='Note: ', ln=1)
    pdf.cell(5, 6, txt='')
    pdf.cell(40, 6, txt='This is Provisional Domicile Certificate only valid for obtaining Citizenship.', ln=1)
    pdf.ln(8)
    pdf.ln(8)
    pdf.set_font('Helvetica', 'B', size=11)
    pdf.cell(125, 6, txt='')
    pdf.cell(70, 6, txt='DISTRICT MAGISTRATE', ln=1)
    pdf.cell(135, 6, txt='')
    pdf.cell(30, 6, txt='ISLAMABAD', ln=1)

    pdf.output('plan.pdf')
    path = 'plan.pdf'
    os.system(path)


preview()

# pdf.cell('row width', 'row height', txt='text', ln=1 (for line break), align='c', (Text Center))
