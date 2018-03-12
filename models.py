# coding: utf-8
from sqlalchemy import Column, Date, Integer, Numeric, Unicode, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import *
import json
import pylimit
from flask import jsonify
import copy
from copy import deepcopy
Base = declarative_base()
metadata = Base.metadata




class Doctorinfo(Base):
    __tablename__ = 'Doctorinfo'

    Doctor_ID = Column(Integer, primary_key=True)
    D_name = Column(Unicode(20), nullable=False)
    D_sex = Column(Integer, nullable=False)
    D_birthday = Column(Date, nullable=False)
    D_city = Column(Unicode(10), nullable=False)
    D_tel = Column(Numeric(14, 0), nullable=False)
    D_wuxing = Column(Unicode(2), nullable=False)
    D_professional = Column(Integer, nullable=False)
    D_right = Column(Integer, nullable=False)
    D_remark = Column(Unicode(50))

    @staticmethod
    def to_json(data):
        return_json = list()
        for i in data:
            var_json = {
                'Doctor_ID': str(i.Doctor_ID),
                'D_name': str(i.D_name),
                'D_sex':str(i.D_sex),
                'D_birthday': str(i.D_birthday),
                'D_city': str(i.D_city),
                'D_wuxing': str(i.D_wuxing),
                'D_tel': str(i.D_tel),
                'D_professional': str(i.D_professional),
                'D_right': str(i.D_right),
                'D_remark': str(i.D_remark)
            }

            return_json.append(var_json)
        return return_json

    def __init__(self,D_name,D_sex,D_birthday,D_city,D_tel,D_wuxing,D_professional,D_right,D_remark):
        self.D_name = D_name
        self.D_sex = D_sex
        self.D_birthday = D_birthday
        self.D_city = D_city
        self.D_tel = D_tel
        self.D_wuxing = D_wuxing
        self.D_professional = D_professional
        self.D_right = D_right
        self.D_remark = D_remark

class Hisinfo(Base):
    __tablename__ = 'Hisinfo'

    Report_ID = Column(Integer, primary_key=True)
    His_eat = Column(Integer, nullable=False)
    His_daBianTian = Column(Integer, nullable=False)
    His_daBianCi = Column(Integer, nullable=False)
    His_daBianType = Column(Integer, nullable=False)
    His_sleep = Column(Integer, nullable=False)
    His_YJzhouqi = Column(Integer, nullable=False)
    His_YJjingqi = Column(Integer, nullable=False)
    His_YJliang = Column(Integer, nullable=False)
    His_YJcolor = Column(Integer, nullable=False)
    His_YJblood = Column(Integer, nullable=False)
    His_BDliang = Column(Integer, nullable=False)
    His_BDwei = Column(Integer, nullable=False)
    His_huaiTai = Column(Integer, nullable=False)
    His_shengChan = Column(Integer, nullable=False)
    His_remark = Column(Unicode(80))

    @staticmethod
    def to_json(data):
        return_json = list()
        for i in data:
            var_json = {
                'Report_ID': str(i.Report_ID),
                'His_eat': str(i.His_eat),
                'His_daBianTian': str(i.His_daBianTian),
                'His_daBianCi': str(i.His_daBianCi),
                'His_daBianType':str(i.His_daBianType),
                'His_sleep': str(i.His_sleep),
                'His_YJzhouqi': str(i.His_YJzhouqi),
                'His_YJjingqi': str(i.His_YJjingqi),
                'His_YJliang': str(i.His_YJliang),
                'His_YJcolor': str(i.His_YJcolor),
                'His_YJblood': str(i.His_YJblood),
                'His_BDliang': str(i.His_BDliang),
                'His_BDwei': str(i.His_BDwei),
                'His_huaiTai': str(i.His_huaiTai),
                'His_shengChan': str(i.His_shengChan),
                'His_remark': str(i.His_remark)
            }

            return_json.append(var_json)
        return return_json




class Operation(Base):
    __tablename__ = 'Operation'

    Opration_ID = Column(Integer, primary_key=True)
    Operation_name = Column(Unicode(20), nullable=False)
    @staticmethod
    def to_json(data):
        return_json = list()
        for i in data:
            var_json = {
                'Report_ID': str(i.Report_ID),
                'Operation_name': str(i.Operation_name)
            }

            return_json.append(var_json)
        return return_json



class Patientinfo(Base):
    __tablename__ = 'Patientinfo'

    Patient_ID = Column(Integer, primary_key=True)
    P_name = Column(Unicode(20), nullable=False)
    P_sex = Column(Integer, nullable=False)
    P_birthday = Column(Date, nullable=False)
    P_wuxing = Column(Unicode(2))
    P_yinYang = Column(Integer, nullable=False)
    P_birthtime = Column(Time, nullable=False)
    P_birthcity = Column(Unicode(10), nullable=False)
    P_tel = Column(Numeric(12, 0), nullable=False)
    P_addcity = Column(Unicode(10), nullable=False)
    P_add = Column(Unicode(40))
    P_remark = Column(Unicode(80))


    @staticmethod
    def to_json(data):
        return_json = list()
        for i in data:
            var_json = {
                'Patient_ID': str(i.Patient_ID),
                'P_name': str(i.P_name),
                'P_sex': str(i.P_sex),
                'P_birthday': str(i.P_birthday),
                'P_yinYang': str(i.P_yinYang),
                'P_wuxing' : str(i.P_wuxing),
                'P_birthtime': str(i.P_birthtime),
                'P_birthcity': str(i.P_birthcity),
                'P_tel': str(i.P_tel),
                'P_addcity': str(i.P_addcity),
                'P_add': str(i.P_add),
                'P_remark': str(i.P_remark)
            }

            return_json.append(var_json)
        return return_json



class Report(Base):
    __tablename__ = 'Report'

    Report_ID = Column(Integer, primary_key=True)
    Doctor_ID = Column(Integer, nullable=False)
    Patient_ID = Column(Integer, nullable=False)
    R_cishu = Column(Integer, nullable=False)
    R_color = Column(Unicode(20))
    R_voice = Column(Unicode(20))
    R_smile = Column(Unicode(20))
    R_mood = Column(Unicode(20))
    R_pressure = Column(Unicode(20))
    R_up = Column(Integer, nullable=False)
    R_mid = Column(Integer, nullable=False)
    R_low = Column(Integer, nullable=False)
    R_wuxing = Column(Integer, nullable=False)
    R_BL_cun = Column(Unicode(20), nullable=False)
    R_BL_guan = Column(Unicode(20), nullable=False)
    R_BL_chi = Column(Unicode(20), nullable=False)
    R_BR_cun = Column(Unicode(20), nullable=False)
    R_BR_guan = Column(Unicode(20), nullable=False)
    R_BR_chi = Column(Unicode(20), nullable=False)
    R_AL_cun = Column(Unicode(20), nullable=False)
    R_AL_guan = Column(Unicode(20), nullable=False)
    R_AL_chi = Column(Unicode(20), nullable=False)
    R_AR_cun = Column(Unicode(20), nullable=False)
    R_AR_guan = Column(Unicode(20), nullable=False)
    R_AR_chi = Column(Unicode(20), nullable=False)
    R_after = Column(Unicode(80), nullable=False)
    R_remark = Column(Unicode(80))

    @staticmethod
    def to_json(data):
        return_json = list()
        for i in data:
            var_json = {
                'Report_ID': str(i.Report_ID),
                'Doctor_ID': str(i.Doctor_ID),
                'Patient_ID': str(i.Patient_ID),
                'R_cishu': str(i.R_cishu),
                'R_color':str(i.R_color),
                'R_voice': str(i.R_voice),
                'R_smile': str(i.R_smile),
                'R_mood': str(i.R_mood),
                'R_pressure': str(i.R_pressure),
                'R_up': str(i.R_up),
                'R_mid': str(i.R_mid),
                'R_low': str(i.R_low),
                'R_wuxing': str(i.R_wuxing),
                'R_BL_cun': str(i.R_BL_cun),
                'R_BL_guan': str(i.R_BL_guan),
                'R_BL_chi': str(i.R_BL_chi),
                'R_BR_cun': str(i.R_BR_cun),
                'R_BR_guan': str(i.R_BR_guan),
                'R_BR_chi': str(i.R_BR_chi),
                'R_AL_cun': str(i.R_AL_cun),
                'R_AL_guan': str(i.R_AL_guan),
                'R_AL_chi': str(i.R_AL_chi),
                'R_AR_cun': str(i.R_AR_cun),
                'R_AR_guan': str(i.R_AR_guan),
                'R_AR_chi': str(i.R_AR_chi),
                'R_after': str(i.R_after),
                'R_remark': str(i.R_remark)
            }

            return_json.append(var_json)
        return return_json


class Wxxwinfo(Base):
    __tablename__ = 'Wxxwinfo'

    wuxing_ID = Column(Integer, primary_key=True)
    wuxing_name = Column(Unicode(2), nullable=False)
    mu1 = Column(Unicode(10), nullable=False)
    mu2 = Column(Unicode(10), nullable=False)
    yuan1 = Column(Unicode(10), nullable=False)
    yuan2 = Column(Unicode(10), nullable=False)
    shiling1 = Column(Unicode(10), nullable=False)
    shiling2 = Column(Unicode(10), nullable=False)
    zi1 = Column(Unicode(10), nullable=False)
    zi2 = Column(Unicode(10), nullable=False)

    @staticmethod
    def to_json(data):
        return_json = list()
        for i in data:
            var_json = {
                'wuxing_ID': str(i.wuxing_ID),
                'wuxing_name': str(i.wuxing_name),
                'mu1': str(i.mu1),
                'mu2': str(i.mu2),
                'yuan1':str(i.yuan1),
                'yuan2': str(i.yuan2),
                'shiling1': str(i.shiling1),
                'shiling2': str(i.shiling2),
                'zi1': str(i.zi1),
                'zi2': str(i.zi2)
            }

            return_json.append(var_json)
        return return_json


class Test(Base):
    __tablename__ = 'test'

    v_id = Column(Integer, primary_key=True)
    hello = Column(Integer)
    world = Column(Integer)
    test = Column(Integer)

    @staticmethod
    def to_json(data):
        return_json = list()
        for i in data:
            var_json = {
                'v_id': str(i.v_id),
                'hello': str(i.hello),
                'world': str(i.world),
                'test': str(i.test)
            }

            return_json.append(var_json)
        return return_json

    def __init__(self, vid, h, w, t):
        self.v_id = vid
        self.hello = h
        self.world = w
        self.test = t


