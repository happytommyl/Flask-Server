from models import *
from sqlalchemy import Column, Date, Integer, Numeric, Unicode, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import string
from sqlalchemy.ext.declarative import declarative_base


def search(sheetname, **kwargs):

    sheet = eval(sheetname.capitalize())
    mydb_conn_str = 'mssql+pymssql://admin:admin@192.168.100.10/WXZJ?charset=utf8'
    myengine = create_engine(mydb_conn_str, pool_recycle = 3600, echo = False)
    mydb_session = scoped_session(sessionmaker(bind = myengine))

    objects = mydb_session.query(sheet).filter_by(**kwargs).all()

    return sheet.to_json(objects)


def AddDoctorinfo(**kwargs):
    mydb_conn_str = 'mssql+pymssql://admin:admin@192.168.100.10/WXZJ?charset=utf8'

    myengine = create_engine(mydb_conn_str, pool_recycle=3600, echo=False, encoding='utf8', convert_unicode=True)
    mydb_session = scoped_session(sessionmaker(bind=myengine))

    doctor = Doctorinfo(**kwargs)

    mydb_session.add(doctor)
    mydb_session.commit()


def AddHistoryinfo(**kwargs):
    mydb_conn_str = 'mssql+pymssql://admin:admin@192.168.100.10/WXZJ?charset=utf8'

    myengine = create_engine(mydb_conn_str, pool_recycle=3600, echo=False, encoding='utf8', convert_unicode=True)
    mydb_session = scoped_session(sessionmaker(bind=myengine))

    Hinfo = Hisinfo(**kwargs)

    mydb_session.add(Hinfo)
    mydb_session.commit()


def AddPatinet(**kwargs):
    mydb_conn_str = 'mssql+pymssql://admin:admin@192.168.100.10/WXZJ?charset=utf8'

    myengine = create_engine(mydb_conn_str, pool_recycle=3600, echo=False, encoding='utf8', convert_unicode=True)
    mydb_session = scoped_session(sessionmaker(bind=myengine))

    patinet = Patientinfo(**kwargs)

    mydb_session.add(patinet)
    mydb_session.commit()


def AddReport(**kwargs):
    mydb_conn_str = 'mssql+pymssql://admin:admin@192.168.100.10/WXZJ?charset=utf8'

    myengine = create_engine(mydb_conn_str, pool_recycle=3600, echo=False, encoding='utf8', convert_unicode=True)
    mydb_session = scoped_session(sessionmaker(bind=myengine))

    report = Report(**kwargs)

    mydb_session.add(report)
    mydb_session.commit()


def insert(sheet, **kwargs):
    if sheet == "Doctorinfo":
        AddDoctorinfo(**kwargs)
    elif sheet == "Patientinfo":
        AddPatinet(**kwargs)
    elif sheet == "Report":
        AddReport(**kwargs)
    elif sheet == "Hisinfo":
        AddHistoryinfo(**kwargs)

# sheet = "Patientinfo"
# insertvalue = {'P_sex': '0', 'P_wuxing': '火', 'P_add': '深圳', 'P_tel': '13800138008', 'P_name': '梁明浩', 'P_birthcity': '深圳', 'P_birthday': '2018-02-01'}
#
# insert(sheet, **insertvalue)

# # # a = search("Doctorinfo")
# print(a)
# doctor = Doctorinfo(D_name=Dname, D_sex=Dsex, D_birthday=Dbirthday, D_city=Dcity, D_tel=Dtel, D_wuxing=Dwuxing,
#                     D_professional=Dprofessional, D_right=Dright, D_remark=Dremark)
# a = search ("", "patientinfo", P_name="Patient1")
# print(a)