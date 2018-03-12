import operations
#
# insertvalue = {'P_sex': '0', 'P_wuxing': '土', 'P_add': '深圳', 'P_tel': '13800138008', 'P_name': '梁明浩', 'P_birthcity': '深圳', 'P_birthday': '2018-02-01'}
# sheet = "Patientinfo"
# operations.insert(sheet, **insertvalue)
operations.search("Patientinfo", P_name = "")