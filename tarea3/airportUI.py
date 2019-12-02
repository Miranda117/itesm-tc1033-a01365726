# -*- coding: utf-8 -*-
class user_op:
    def dateInfo(self):
        print("ingrese fecha para generar reporte (YYMMDD): ")
        yymmdDate = int(input())
        return yymmdDate

    def timeInfo(self):
        print("Ingrese hora para generar reporte (HHMM): ")
        hhmmTime = int(input())
        return hhmmTime
