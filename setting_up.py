self.Entry_Father_Name.delete(0, 'end')
self.Entry_Father_Name.insert(0, row['First_Name'])

self.Entry_Spouse_Name.delete(0, 'end')
self.Entry_Spouse_Name.insert(0, row['Spouse_Name'])

self.Entry_Contact.delete(0, 'end')
self.Entry_Contact.insert(0, row['Contact'])

self.Entry_Placeofbirth.delete(0, 'end')
self.Entry_Placeofbirth.insert(0, row['Placeofbirth'])

self.Entry_Date_of_Birth.delete(0, 'end')
self.Entry_Date_of_Birth.insert(0, row['Date_of_Birth'])
self.Entry_Arrival_Date.delete(0, 'end')
self.Entry_Arrival_Date.insert(0, row['Arrival_Date'])

# Getting Tehsil and District Lists from db
Tehsil_values = list(self.Tehsil_data_dict.values())
District_values = list(self.District_data_dict.values())
Tehsil_txt = Tehsil_List[Tehsil_values.index(row['Pres_Tehsil'])]
District_txt = District_List[District_values.index(row['Pres_District'])]
self.Entry_Pre_Tehsil.delete(0, 'end')
self.Entry_Pre_Tehsil.insert(0, Tehsil_txt)

self.Entry_Pre_District.delete(0, 'end')
self.Entry_Pre_District.insert(0, District_txt)

self.List_Pres_Province.delete(0, 'end')
self.List_Pres_Province.select_set(Province_Keys.index(row['Pres_Province']))
self.Entry_Present_Address.delete(0, 'end')
self.Entry_Present_Address.insert(0, row['Present_Address'])

Tehsil_txt = Tehsil_List[Tehsil_values.index(row['Perm_Tehsil'])]
District_txt = District_List[District_values.index(row['Perm_District'])]
self.Entry_Prem_Tehsil.delete(0, 'end')
self.Entry_Prem_Tehsil.insert(0, Tehsil_txt)
self.Entry_Prem_District.delete(0, 'end')
self.Entry_Prem_District.insert(0, District_txt)
self.List_Prem_Province.select_set(Province_Keys.index(row['Perm_Province']))


self.Entry_Permenant_Address.delete(0, 'end')
self.Entry_Permenant_Address.insert(0, row['Permenant_Address'])

self.List_Gender.select_set(int(row['Gender'])-1)


self.List_Religion.select_set(int(Religion_list.index(row['Religon']))-1)


self.List_Marital_status.select_set(int(row['Marital_Status'])-1)


self.Qualification.select_set(int(row['Qualification'])-1)

self.List_Occupation.select_set(int(row['Occupation'])-1)


self.List_Process_Type.select_set(Process_List.index(row['Process_Type']))

self.List_Request_Type.select_set(int(row['Request_Type'])-1)


self.List_Application_Type.select_set(int(row['Application_Type'])-1)


self.List_Service_Type.select_set(int(row['Service_Type'])-1)


self.List_Pyament_Type.select_set(int(row['Payment_Type'])-1)


self.List_Approver.select_set(int(Approver_List.index(row['Approver_Desig'])))

# Check Buttons

cnic_front = row['cnic_front']
cnic_back = row['cnic_back']
cnic_guardian = row['cnic_guardian']
form_b = row['form_b']
domicile_of_guardian = row['domicile_of_guardian']
noc_from_concerned_district = row['noc_from_concerned_district']
Residance_Prof = row['Residance_Prof']
utility_bill = row['utility_bill']
educational_certificate = row['educational_certificate']
marriage_registration_certificate = row['marriage_registration_certificate']
affidavit_voterlist = row['affidavit_voterlist']
affidavit_domicile = row['affidavit_domicile']
voter_list = row['voter_list']
domicile_challan = row['domicile_challan']
