#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import time
import os
import sys
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from sys import path as sysPath
from os import path as osPath
filepath = osPath.dirname(osPath.realpath(__file__))



def graphic(variableGrafica, dataArray, initTime, interval):
	
		#generate timeArray 
		timeArray = []
		for i in range(len(dataArray)):
			timeArray.append(initTime + interval*i)
		#print timeArray

		#plot
   		plt.xlabel('time')
		plt.ylabel(variableGrafica + ' samples')
		plt.title(variableGrafica)
		plt.grid(True)
		plt.plot(timeArray, dataArray, 'ro', timeArray, dataArray, 'g')
		plt.savefig('/var/tmp/'+variableGrafica+'.png')

		#plt.show()

		
		

		

def createPDF(user, machine, id, ip):


		#generate a PDF
		aux = canvas.Canvas(filepath + "/pdf/LAG.pdf")
		aux.drawImage(filepath + "/logo.png",400, 750, 200,100)
		aux.drawString(50,800,'****REPORT FILE****')
		aux.drawString(50,750,'Date: '+ time.strftime("%d/%m/%y"))
		aux.drawString(50,730,'Report time: ' +time.strftime("%H:%M:%S"))
		aux.drawString(50,710,'Worker: ' +user)
		aux.drawString(50,690,'Machine: ' +machine + '      ID: ' +id+'      IP: ' +ip)
	
		#aux.drawString(150,20,"Posicion (X,Y) = (150,20)")


		aux.drawString(50,50,"RT4ALL logger")
		#include graphics

		aux.drawImage("/var/tmp/Temperature.png",100 , 350, 400,250)
		aux.drawImage("/var/tmp/Humidity.png",100, 80,400,250)
		

		aux.showPage()
		aux.save()

	


if __name__ == "__main__":

	#read temperature robot file as string, convert to float and graphic
	file = open(filepath+"/robotTemperature_0.0.txt", 'r')
	dataArrayTemp= file.read()
	arrayStringTemp = dataArrayTemp.split(",")
	print(arrayStringTemp)
	#delete last positicion which is empty
	arrayStringTemp.pop()
	
	tempFloat = np.array(arrayStringTemp, dtype=float)

	#do the same humidity
	file2 = open(filepath+"/robotHumidity_0.0.txt", 'r')
	dataArrayHum= file2.read()
	arrayStringHum = dataArrayHum.split(",")
	print(arrayStringHum)
	arrayStringHum.pop()
	
	tempHum = np.array(arrayStringHum, dtype=float)
	

	#file = open("../../_interfaz/report/robotHumidity_0.0.txt", 'r')
	#dataArrayHum = file.read()
	graphic('Temperature',tempFloat, 1, 2)
	graphic('Humidity',tempHum, 1, 2)

	#input arg to generate pdf report
	userName= sys.argv[1]
	robotName= sys.argv[2] 
	robotID= sys.argv[3]
	IP= sys.argv[4]
	#print(userName +" " + robotName + " "+ robotID +" "+ IP)

	createPDF(userName, robotName, robotID, IP);


