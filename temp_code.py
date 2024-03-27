def print_extra_line(name, fname):
                # split input in words
                name_lst = name.split()
                fname_lst = fname.split()
                name_line = ''
                name_line_lst = []
                piece_lenth = 0
                # if flag will determine where the last word ended either on if piece_lenth on true or false
                if_flag = 'True'
                for piece in name_lst:
                    piece_lenth = piece_lenth + len(piece)
                    last_line = ''
                    # cheking if combination of words excedded the lenth of cell than it will be added in name_line_list as next member and so on until the full name ended
                    if piece_lenth < 16:
                        # if two word lenth is within cell width limit then combining words
                        name_line = name_line + ' ' + piece
                        last_line = name_line  # trace for last remaining word

                        if_flag = 'True'
                    else:
                        # add to name_line_list
                        name_line_lst.append(name_line)
                        name_line = piece
                        piece_lenth = len(piece)
                        if_flag = 'False'
                # adding last remaining word
                if if_flag == 'False':
                    name_line_lst.append(name_line)
                else:
                    name_line_lst.append(last_line)

                name_line = ''
                fname_line_lst = []
                piece_lenth = 0
                if_flag = 'True'
                for piece in fname_lst:
                    piece_lenth = piece_lenth + len(piece)
                    last_line = ''
                    if piece_lenth < 17:
                        name_line = name_line + ' ' + piece

                        last_line = name_line

                        if_flag = 'True'
                    else:
                        fname_line_lst.append(name_line)
                        name_line = piece
                        piece_lenth = len(piece)
                        if_flag = 'False'

                if if_flag == 'False':
                    fname_line_lst.append(name_line)
                else:
                    fname_line_lst.append(last_line)
                # adding empty members to smaler list in order to make it equal so that it can be
                # loop through one loop
                name_line_lst_lenth = len(name_line_lst)
                fname_line_lst_lenth = len(fname_line_lst)

                if name_line_lst_lenth > fname_line_lst_lenth:
                    # max_rng is the finle loop lenth where all list members will be printed
                    max_rng = name_line_lst_lenth
                    rng = name_line_lst_lenth - fname_line_lst_lenth
                    for lop in range(rng):
                        fname_line_lst.append(' ')
                elif fname_line_lst_lenth > name_line_lst_lenth:
                    max_rng = fname_line_lst_lenth
                    rng = fname_line_lst_lenth - name_line_lst_lenth
                    for lop in range(rng):
                        name_line_lst.append(' ')
                else:

                    max_rng = name_line_lst_lenth
                    pass
                a = 0
                for itm in range(max_rng):

                    if a == 0:
                        pdf.cell(
                            55, 6, txt=name_line_lst[itm].strip(), border='LTR')
                        pdf.cell(
                            60, 6, txt=fname_line_lst[itm].strip(), border='LTR', ln=1)

                    else:
                        pdf.cell(10, 6, txt='')
                        pdf.cell(17, 6, txt='', border='LR')
                        pdf.cell(47, 6, txt='', border='LR')
                        pdf.cell(
                            55, 6, txt=name_line_lst[itm].strip(), border='LR')
                        pdf.cell(
                            60, 6, txt=fname_line_lst[itm].strip(), border='LR', ln=1)
                    a = a + 1
            sno = 0
            if data[0]['Applicant_Name'] is not None:
                for item in data:
                    sno = sno + 1
                    pdf.cell(10, 6, txt='')
                    pdf.cell(17, 6, txt=str(sno), border='LTR', align='C')
                    pdf.cell(47, 6, txt=str(
                        item['CNIC'][:5]+'-'+item['CNIC'][5:12]+'-'+item['CNIC'][12:13]), border='LTR')

                    if len(item['Applicant_Name']) > 18 or len(item['Applicant_FName']) > 18:
                        print_extra_line(item['Applicant_Name'],
                                         item['Applicant_FName'])
                    else:
                        pdf.cell(55, 6, txt=str(
                            item['Applicant_Name']), border='LTR')
                        pdf.cell(60, 6, txt=str(
                            item['Applicant_FName']), border='LTR', ln=1)