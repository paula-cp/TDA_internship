# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '3.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QMessageBox, QDialog
from pyqtgraph import PlotWidget
from pyqtgraph import LegendItem


import pyqtgraph as pg
import pyqtgraph.exporters
import numpy as np
import pandas as pd
import pickle
import joblib

from tmap.tda import mapper, Filter
from tmap.tda.cover import Cover
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from tmap.tda.plot import show, Color,tm_plot,vis_progressX


from matplotlib.figure import Figure # For Matplotlib Figure Object
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D


import sys
# specify the use of PySide
#matplotlib.rcParams['backend.qt5'] = "PyQt"

# import the figure canvas for interfacing with the backend
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg \
                                                                as FigureCanvas

# import 3D plotting
from mpl_toolkits.mplot3d import Axes3D    # @UnusedImport
from matplotlib.figure import Figure


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 789)
        MainWindow.setDocumentMode(False)
        self.data=pd.DataFrame({'A' : []})
        self.targets=pd.DataFrame({'A' : []})
        self.target_names=0
        self.classes=0
        self.lista=[]
        self.graph_dic={}
        self.target_dic={}
        self.name=0
        self.graph=0
        self.dim1=0
        self.dim2=0
        self.component1=0
        self.component2=0
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 60, 551, 641))
        self.graphicsView.setObjectName("graphicsView")
        self.View3d = Mpwidget(parent=self.centralwidget)
        self.View3d.setGeometry(QtCore.QRect(40, 60, 551, 641))
        self.View3d.hide()
        self.overlap = QtWidgets.QSlider(self.centralwidget)
        self.overlap.setGeometry(QtCore.QRect(650, 150, 221, 22))
        self.overlap.setMinimum(1)
        self.overlap.setMaximum(100)
        self.overlap.setOrientation(QtCore.Qt.Horizontal)
        self.overlap.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.overlap.setTickInterval(10)
        self.overlap.setObjectName("overlap")
        self.overlap.valueChanged.connect(self.getValue)
        self.overlap.valueChanged.connect(self.letsdraw)
        self.min_samples = QtWidgets.QSlider(self.centralwidget)
        self.min_samples.setGeometry(QtCore.QRect(650, 290, 221, 22))
        self.min_samples.setMinimum(1)
        self.min_samples.setMaximum(10)
        self.min_samples.setOrientation(QtCore.Qt.Horizontal)
        self.min_samples.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.min_samples.setTickInterval(1)
        self.min_samples.setObjectName("min_samples")
        self.min_samples.valueChanged.connect(self.getValue)
        self.min_samples.valueChanged.connect(self.letsdraw)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(654, 120, 161, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(650, 260, 161, 21))
        self.label_2.setObjectName("label_2")
        self.resolution = QtWidgets.QSlider(self.centralwidget)
        self.resolution.setGeometry(QtCore.QRect(650, 220, 221, 22))
        self.resolution.setMinimum(1)
        self.resolution.setMaximum(100)
        self.resolution.setOrientation(QtCore.Qt.Horizontal)
        self.resolution.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.resolution.setTickInterval(10)
        self.resolution.setObjectName("resolution")
        self.resolution.valueChanged.connect(self.getValue)
        self.resolution.valueChanged.connect(self.letsdraw)
        self.resolution.setEnabled(False)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(654, 190, 161, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(890, 150, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(890, 220, 55, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(890, 290, 55, 16))
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(650, 340, 171, 22))
        self.comboBox.setObjectName("comboBox")
        #listoptions=['out','LV','echo','mitral']#hacerlo mas general
        group=QtGui.QButtonGroup(self.centralwidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 30, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setCheckable(True)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 30, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setCheckable(True)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 30, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setCheckable(True)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 30, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setCheckable(True)
        group.addButton(self.pushButton)
        group.addButton(self.pushButton_2)
        group.addButton(self.pushButton_3)
        group.addButton(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(650, 60, 111, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(650, 660, 131, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        number_group=QtGui.QButtonGroup(self.centralwidget)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(650, 380, 256, 141))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setSelectionMode(2)
        self.radioButton2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton2.setGeometry(QtCore.QRect(770, 60, 131, 41))
        self.radioButton2.setObjectName("radioButton2")
        number_group.addButton(self.radioButton2)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(830, 340, 95, 20))
        self.radioButton.setObjectName("radioButton")
        number_group.addButton(self.radioButton)
        
        self.dim_list=['L1 Centrality','L inf Centrality','Gaussian Density',
                       'PCA', 'T-SNE','MDS','PCoA','UMAP']
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(650, 580, 121, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(self.dim_list)
        self.comboBox_2.hide()
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(780, 580, 121, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItems(self.dim_list)
        self.comboBox_3.hide()
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(650, 540, 221, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.toggled.connect(lambda:self.show_dimensionality())
        number_group.addButton(self.radioButton_2)
        number_group.setExclusive(False)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(650, 610, 71, 31))
        self.label_7.setObjectName("label_7")
        self.label_7.hide()
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(780, 610, 71, 31))
        self.label_8.setObjectName("label_8")
        self.label_8.hide()
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(730, 610, 41, 31))
        self.plainTextEdit.setPlainText("0")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.hide()
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(860, 610, 41, 31))
        self.plainTextEdit_2.setPlainText("0")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_2.hide()
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(840, 650, 61, 31))
        self.pushButton_7.setObjectName("pushButton_8")
        self.pushButton_7.hide()
        self.pushButton_7.clicked.connect(lambda:self.project())
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 975, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen2 = QtWidgets.QAction(MainWindow)
        self.actionOpen2.setObjectName("actionOpen2")
        self.actionRequisites = QtWidgets.QAction(MainWindow)
        self.actionRequisites.setObjectName("actionRequisites")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOpen2)
        self.menuHelp.addAction(self.actionRequisites)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.actionOpen.triggered.connect(self.open_file)
        self.actionOpen2.triggered.connect(self.open_dic)
        self.actionHelp.triggered.connect(self.helpme)
        self.actionRequisites.triggered.connect(self.requisites)
        
        self.pushButton.clicked.connect(lambda:self.where(1))
        self.pushButton_2.clicked.connect(lambda:self.where(2))
        self.pushButton_3.clicked.connect(lambda:self.where(3))
        self.pushButton_4.clicked.connect(lambda:self.where(4))
        self.pushButton_5.clicked.connect(lambda:self.process())
        self.pushButton_6.clicked.connect(lambda:self.save_graph())
        self.radioButton2.clicked.connect(lambda:self.activate())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Overlap"))
        self.label_2.setText(_translate("MainWindow", "min_samples"))
        self.label_3.setText(_translate("MainWindow", "Resolution"))
        self.label_4.setText(_translate("MainWindow", "0.01"))
        self.label_5.setText(_translate("MainWindow", "1"))
        self.label_6.setText(_translate("MainWindow", "1"))
        self.pushButton.setText(_translate("MainWindow", "1x2"))
        self.pushButton_2.setText(_translate("MainWindow", "1x3"))
        self.pushButton_3.setText(_translate("MainWindow", "2x3"))
        self.pushButton_4.setText(_translate("MainWindow", "3D"))
        self.pushButton_5.setText(_translate("MainWindow", "Process data"))
        self.pushButton_6.setText(_translate("MainWindow", "Save current graph"))
        self.radioButton2.setText(_translate("MainWindow", "Edit Resolution"))
        self.radioButton.setText(_translate("MainWindow", "Categorical"))
        self.radioButton_2.setText(_translate("MainWindow", "Apply dimensionality reduction"))
        self.label_7.setText(_translate("MainWindow", "Component"))
        self.label_8.setText(_translate("MainWindow", "Component"))
        self.pushButton_7.setText(_translate("MainWindow", "Apply"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Load new data"))
        self.actionOpen2.setText(_translate("MainWindow","Load already processed data"))
        self.actionRequisites.setText(_translate("MainWindow","Requisites"))
        self.actionHelp.setText(_translate("MainWindow","Help"))

    def activate(self):
        if self.radioButton2.isChecked() == 1:
            self.resolution.setEnabled(True)
        else:
            self.resolution.setEnabled(False)
    
    def getValue(self):
        overlap=self.overlap.value()*0.01
        if self.radioButton2.isChecked() == 1:
            resolution=self.resolution.value()
        else:
            resolution=int(100-overlap*100)
        samples=self.min_samples.value()
        self.label_4.setText(str(overlap))
        self.label_5.setText(str(resolution))
        self.label_6.setText(str(samples))
        
    def letsdraw(self):
        if self.pushButton.isChecked():
            self.where(1)
        elif self.pushButton_2.isChecked():
            self.where(2)
        elif self.pushButton_3.isChecked():
            self.where(3)
        elif self.pushButton_4.isChecked():
            self.where(4)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please choose the dimensions to display the data")
            msg.setWindowTitle(" ")
            msg.exec_()
        
    def where(self,kind):
        if self.data.empty and len(self.graph_dic) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("There is no data uploaded to the program!")
            msg.setWindowTitle("Warning!")
            msg.exec_()
        else:
            if self.graph_dic == {}:
                if kind == 4:
                    self.shownet3d()
                else:
                    self.shownet(kind)
            else:
                if kind == 4:
                    self.showdic3d
                else:
                    self.showdic(kind)
    
    def build_lens(self,dim,component):
        if dim == 0:
            lens=[Filter.L1Centrality()]#l1
        if dim == 1:
            lens=[Filter.LinfCentrality()]#linf
        if dim == 2:
            lens=[Filter.GaussianDensity(components=(2))]#gaussian
        if dim == 3:
            lens=[Filter.PCA(components=[int(component)])]
        if dim == 4:
            lens=[Filter.TSNE(components=[int(component)])]
        if dim == 5:
            lens=[Filter.MDS(components=[int(component)])]
        if dim == 6:
            lens=[Filter.PCOA(components=[int(component)])]
        if dim == 7:
            lens=[Filter.UMAP(components=[int(component)])]
        return(lens)
        
    def showdic(self,kind):
        num_ITEMS=[item.text() for item in self.listWidget.selectedItems()]
        if not num_ITEMS:
            self.shownet
        else:
            overlap=self.overlap.value()*0.01
            if self.radioButton2.isChecked() == 1:
                resolution=self.resolution.value()
            else:
                resolution=int(100-overlap*100)
            samples=self.min_samples.value()
                    
            self.graphicsView.clear()
            
            graph_name=(str(overlap)+'_'+str(resolution)+'_'+str(samples))
            if graph_name in self.graph_dic:
                self.graph=self.graph_dic[graph_name]
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("The desired graph is not available in the uploaded document.\n"\
                            "Please upload the corresponding .csv.")
                msg.setWindowTitle(" ")
                msg.exec_()
                self.shownet(kind)
            
            target=self.comboBox.currentIndex()
            
            if self.radioButton.isChecked() == 1:
                color = Color(target=self.targets.iloc[:,target], dtype="categorical",target_by='sample')
            else:
                color = Color(target=self.targets.iloc[:,target], dtype="numerical",target_by='sample')
            shades=color.get_colors(self.graph.nodes)
            shade=shades[0]
            shades=list(shade.values())
            
            node_positions=self.graph.nodePos
            node_keys = self.graph.nodes
            node_idx = dict(zip(node_keys, range(len(node_keys))))
            
            #vb = self.graphicsView.addViewBox()
            #leg=LegendItem()
            #vb.addItem(legend)
    
            for edge in self.graph.edges:
                if kind == 1:
                    self.graphicsView.plot([node_positions[node_idx[edge[0]], 0], node_positions[node_idx[edge[1]], 0]],
                    [node_positions[node_idx[edge[0]], 1], node_positions[node_idx[edge[1]], 1]],pen=pg.mkPen(shade[node_idx[edge[0]]]),symbol='o',symbolBrush=(shade[node_idx[edge[0]]]))
                elif kind == 2:
                    self.graphicsView.plot([node_positions[node_idx[edge[0]], 0], node_positions[node_idx[edge[1]], 0]],
                    [node_positions[node_idx[edge[0]], 2], node_positions[node_idx[edge[1]], 2]],pen=pg.mkPen(shade[node_idx[edge[0]]]),symbol='o',symbolBrush=(shade[node_idx[edge[0]]]))
                elif kind == 3:
                    self.graphicsView.plot([node_positions[node_idx[edge[0]], 1], node_positions[node_idx[edge[1]], 1]],
                    [node_positions[node_idx[edge[0]], 2], node_positions[node_idx[edge[1]], 2]],pen=pg.mkPen(shade[node_idx[edge[0]]]),symbol='o',symbolBrush=(shade[node_idx[edge[0]]]))
            
    def shownet(self,kind):
        self.graphicsView.show()
        self.View3d.hide()
        if kind == 1:
            data=self.data.iloc[:,[0,1]]
        elif kind == 2:
            data=self.data.iloc[:,[0,2]]
        elif kind == 3:
            data=self.data.iloc[:,[1,2]]
        overlap=self.overlap.value()*0.01
        
        if self.radioButton2.isChecked() == 1:
            resolution=self.resolution.value()
        else:
            resolution=int(100-overlap*100)
        samples=self.min_samples.value()
        
        self.graphicsView.clear()
        
        num_ITEMS=[item.text() for item in self.listWidget.selectedItems()]
        if num_ITEMS==[]:
            pass
        else:
            results = list(map(int, num_ITEMS))
            out=list(self.classes)
            pos=[]
            for kind in range(0,len(results)):
                pos.extend([i for i, e in enumerate(out) if e == results[kind]])
            data = data.loc[pos]
                
        tm = mapper.Mapper(verbose=1)
        
        if self.radioButton_2.isChecked():
            lens1 = self.build_lens(self.dim1, self.component1)
            lens2 = self.build_lens(self.dim2, self.component2)
            projected_X = tm.filter(data, lens=lens1)
            projected_X = tm.filter(projected_X, lens=lens2)
        else:
            projected_X=data
            
        clusterer = DBSCAN(eps=0.5,min_samples=samples)
        cover = Cover(projected_data=MinMaxScaler().fit_transform(projected_X), resolution=resolution, overlap=overlap)
        self.graph = tm.map(data=StandardScaler().fit_transform(data), cover=cover, clusterer=clusterer)
        
        target=self.comboBox.currentIndex()
        
        if self.radioButton.isChecked() == 1:
            color = Color(target=self.targets.iloc[:,target], dtype="categorical",target_by='sample')
        else:
            color = Color(target=self.targets.iloc[:,target], dtype="numerical",target_by='sample')
        shades=color.get_colors(self.graph.nodes)
        shade=shades[0]
        shades=list(shade.values())
        
        node_positions=self.graph.nodePos
        node_keys = self.graph.nodes
        node_idx = dict(zip(node_keys, range(len(node_keys))))
        #vb = self.graphicsView.addViewBox()
        #leg=LegendItem()
        #vb.addItem(legend)

        for edge in self.graph.edges:
            self.graphicsView.plot([node_positions[node_idx[edge[0]], 0], node_positions[node_idx[edge[1]], 0]],
            [node_positions[node_idx[edge[0]], 1], node_positions[node_idx[edge[1]], 1]],pen=pg.mkPen(shade[node_idx[edge[0]]]),symbol='o',symbolBrush=(shade[node_idx[edge[0]]]))
                #leg.addItem(node_positions[node_idx[edge[0]], 0],1)
        #self.graphicsView.plot(node_positions[:,0],node_positions[:,1],pen=None,brush=pg.mkBrush('r'),symbol='o')
            
    
    def showdic3d(self):
        num_ITEMS=[item.text() for item in self.listWidget.selectedItems()]
        if not num_ITEMS:
            self.shownet3d
        else:
            overlap=self.overlap.value()*0.01
            if self.radioButton2.isChecked() == 1:
                resolution=self.resolution.value()
            else:
                resolution=int(100-overlap*100)
            samples=self.min_samples.value()
            
            graph_name=(str(overlap)+'_'+str(resolution)+'_'+str(samples))
            
            if graph_name() in self.graph_dic:
                self.graph=self.graph_dic[graph_name]
            else:
                if self.data.empty:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("The desired graph is not available in the uploaded document.\n"\
                                "Please upload the corresponding .csv.")
                    msg.setWindowTitle(" ")
                    msg.exec_()
                else:
                    self.shownet3d
            
            target=self.comboBox.currentIndex()
            
            if self.radioButton.isChecked() == 1:
                color = Color(target=self.targets.iloc[:,target], dtype="categorical",target_by='sample')
            else:
                color = Color(target=self.targets.iloc[:,target], dtype="numerical",target_by='sample')
            shades=color.get_colors(self.graph.nodes)
            shade=shades[0]
            shades=list(shade.values())
            
            node_positions=self.graph.nodePos
            node_keys = self.graph.nodes
            node_idx = dict(zip(node_keys, range(len(node_keys))))
            #vb = self.graphicsView.addViewBox()
            #leg=LegendItem()
            #vb.addItem(legend)
            self.View3d.drawGraph3d(shade,shades,node_positions,node_idx,self.graph)    
    
    def shownet3d(self):
        #esto no está bien porque haria falta otro entero para la 3a dimension...
        self.graphicsView.hide()
        self.View3d.show()
        self.graphicsView.clear()

        overlap=self.overlap.value()*0.01
        if self.radioButton2.isChecked() == 1:
            resolution=self.resolution.value()
        else:
            resolution=int(100-overlap*100)
        samples=self.min_samples.value()
        
        num_ITEMS=[item.text() for item in self.listWidget.selectedItems()]
        if num_ITEMS==[]:
                data=self.data
        else:
            results = list(map(int, num_ITEMS))
            out=list(self.classes)
            pos=[]
            for kind in range(0,len(results)):
                pos.extend([i for i, e in enumerate(out) if e == results[kind]])
            data = self.data.loc[pos]
                
        tm = mapper.Mapper(verbose=1)
        
        if self.radioButton_2.isChecked():
            lens1 = self.build_lens(self.dim1, self.component1)
            lens2 = self.build_lens(self.dim2, self.component2)
            
            projected_X = tm.filter(data, lens=lens1)
            projected_X = tm.filter(projected_X, lens=lens2)
        else:
            projected_X=data
            
        clusterer = DBSCAN(eps=0.5,min_samples=samples)
        cover = Cover(projected_data=MinMaxScaler().fit_transform(projected_X), resolution=resolution, overlap=overlap)
        self.graph = tm.map(data=StandardScaler().fit_transform(data), cover=cover, clusterer=clusterer)
        
        target=self.comboBox.currentIndex()
        
        if self.radioButton.isChecked() == 1:
            color = Color(target=self.targets.iloc[:,target], dtype="categorical",target_by='sample')
        else:
            color = Color(target=self.targets.iloc[:,target], dtype="numerical",target_by='sample')
        shades=color.get_colors(self.graph.nodes)
        shade=shades[0]
        shades=list(shade.values())
        
        node_positions=self.graph.nodePos
        node_keys = self.graph.nodes
        node_idx = dict(zip(node_keys, range(len(node_keys))))
        #vb = self.graphicsView.addViewBox()
        #leg=LegendItem()
        #vb.addItem(legend)
        self.View3d.drawGraph3d(shade,shades,node_positions,node_idx,self.graph)
        
        
    def helpme(self):
       msg = QMessageBox()
       msg.setIcon(QMessageBox.Question)
       msg.setText("TDA will be performed on the uploaded data, from the menu "\
                   "option File.\n\nThe sliders on the right hand side allow to "\
                   "modify the parameters of the TDA, in order to visualize every possible "\
                   "graph.\n\nThe 'Process data' button allows you to explore the whole TDA "\
                   "landscape, speeding the visualization times up.\nAll these graphs will be"\
                   "stored in a .pkl file, named as the loaded .csv. If you want to study the same"\
                   "file any other time, import the .pkl file to save computational times.\n\n"\
                   "Once the TDA parameters have been set, press the buttons over the visualization"\
                   "panel to plot the TDA graph.\n\n"\
                   "The combo box allows you to color the network with the desired target "\
                   "variable, and the radio button determines whether the variable is categorical "\
                   "or numerical.\n\n"\
                   "In the lower part of the GUI, you can find a button that allows you to "\
                   "save the graph, storing the configuration of the parameters.\n"\
                   "If you want to store a picture of the graph, right click over the visualization "\
                   "panel, and press export.")
       msg.setWindowTitle("Help")
       msg.exec_()
        
    def requisites(self):
       msg = QMessageBox()
       msg.setIcon(QMessageBox.Information)
       msg.setText("The data must be imported from a .csv,"\
                   "with headers naming the target variables.\n"\
                   "The first three rows need to belong to the first 3 dimensions "\
                   "obtained with the desired dimensionality reduction technique.\n\n"\
                   "Regarding the 'Load already processed data' option, it will open"\
                   ".pkl files that will be created after pressing the 'Process data'"\
                   "button in the interface.")
       msg.setWindowTitle("Requisites")
       msg.exec_()

        
    def open_file(self):#falta hacer un no es csv
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Please make sure that the uploaded .csv follows the requisites.")
        msg.setWindowTitle(" ")
        msg.exec_()
        filename=QFileDialog.getOpenFileName()
        path=filename[0]
        try:
            data=pd.read_csv(path)
            path=path.split('/')
            path=path[-1]
            path=path.split('.')
            self.name=path[0]
            
            self.data=data.iloc[:,0:3]
            self.targets=data.iloc[:,3:]
            self.target_names=self.targets.columns.values
            self.comboBox.addItems(self.target_names)
            
            self.classes=self.targets[self.target_names[0]]
            for i in self.classes:
                if i not in self.lista:
                    self.lista.append(i)
                    self.listWidget.addItem(str(i))
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Correctly uploaded data")
            msg.setWindowTitle(" ")
            msg.exec_()
        except UnicodeDecodeError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Make sure that the file is a .csv!")
            msg.setWindowTitle(" ")
            msg.exec_()

        
    def open_dic(self):#falta hacer un no es pkl o algo asi
        filename=QFileDialog.getOpenFileName()
        path=filename[0]
        path=path.split('/')
        path=path[-1]
        path=path.split('.')
        self.name=path[0]
        try:
            with open(self.name + '.pkl', 'rb') as handle:
                super_dic = pickle.load(handle)
            self.graph_dic=super_dic[1]
            self.target_dic=super_dic[2]
            for x in self.graph_dic:
                print(x)             
            self.target_names=list(self.target_dic.keys())
            self.targets=pd.DataFrame.from_dict(self.target_dic)
            self.comboBox.addItems(self.target_names)
            
            self.classes=self.targets[self.target_names[0]]
            for i in self.classes:
                if i not in self.lista:
                    self.lista.append(i)
                    self.listWidget.addItem(str(i))
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Correctly uploaded data")
            msg.setWindowTitle(" ")
            msg.exec_()
        except FileNotFoundError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Make sure that the file is a .pkl!")
            msg.setWindowTitle(" ")
            msg.exec_()
            
    def process(self):
        if self.data.empty and len(self.graph_dic) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("There is no data uploaded to the program!")
            msg.setWindowTitle("Warning!")
            msg.exec_()
            pass
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Data is being processed. This will take a while...")
            msg.setWindowTitle(" ")
            msg.exec_()
            #self.radioButton2.hide()
            #self.progressBar.show()
            vec_overlap=np.arange(0.01,1.00,0.1)
            vec_samples=np.arange(1,5,1)
            
            for overlap in vec_overlap:
                overlap=round(overlap,2)
                resolution=int(100-overlap*100)
                for samples in vec_samples:
                    tm = mapper.Mapper(verbose=1)
                    clusterer = DBSCAN(eps=0.5,min_samples=samples)
                    cover = Cover(projected_data=MinMaxScaler().fit_transform(self.data), resolution=resolution, overlap=overlap)
                    graph = tm.map(data=self.data, cover=cover, clusterer=clusterer)
                    
                    name_graph=(str(overlap)+'_'+str(resolution)+'_'+str(samples))
                    self.graph_dic[name_graph]=graph
        
            for i,name in zip(range(0,len(self.target_names)),self.target_names):
                self.target_dic[name]=self.targets.iloc[:,i]
            super_dic={}
            super_dic[1]=self.graph_dic
            super_dic[2]=self.target_dic
            
            with open('eii' + '.pkl', 'wb') as f:
                pickle.dump(super_dic, f, pickle.HIGHEST_PROTOCOL)
            #self.progressBar.hide()
            #self.radioButton2.show()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("The data has been correctly processed!")
            msg.setWindowTitle(" ")
            msg.exec_()
            #poner un aviso de data processed correctly
            
    def save_graph(self):
        if self.graph == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("There is no graph being displayed!")
            msg.setWindowTitle("Warning!")
            msg.exec_()
        else:
            overlap=self.overlap.value()*0.01
            resolution=self.resolution.value()
            samples=self.min_samples.value()
            
            super_graph={}
            for i,name in zip(range(0,len(self.target_names)),self.target_names):
                self.target_dic[name]=self.targets.iloc[:,i]
            
            super_graph[1]=self.graph
            super_graph[2]=self.target_dic
            
            with open(str(overlap) + '_' + str(resolution) + '_' + str(samples) + '.pkl', 'wb') as f:
                pickle.dump(super_graph, f, pickle.HIGHEST_PROTOCOL)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Correctly stored graph.")
            msg.setWindowTitle(" ")
            msg.exec_()
            
            
    def show_dimensionality(self):
        if self.radioButton_2.isChecked():
            self.comboBox_2.show()
            self.comboBox_3.show()
            self.label_7.show()
            self.label_8.show()
            self.plainTextEdit.show()
            self.plainTextEdit_2.show()
            self.pushButton_7.show()
        else:
            self.comboBox_2.hide()
            self.comboBox_3.hide()
            self.label_7.hide()
            self.label_8.hide()
            self.plainTextEdit.hide()
            self.plainTextEdit_2.hide()
            self.pushButton_7.hide()
    
    def project(self):
        self.dim1=self.comboBox_2.currentIndex()
        self.component1=self.plainTextEdit.toPlainText()
        self.dim2=self.comboBox_3.currentIndex()
        self.component2=self.plainTextEdit_2.toPlainText()
        self.letsdraw()
        
        
        

class Mpwidget(FigureCanvas):
    def __init__(self, parent=None):
        self.fig =plt.figure(figsize=(7,7))
        FigureCanvas.__init__(self, self.fig) # creating FigureCanvas
        self.axes = self.fig.gca(projection='3d') # generates 3D Axes object
        self.setParent(parent)
        
    def drawGraph3d(self, shade,shades,node_positions,node_idx,graph):
        self.axes.clear()
        self.axes = self.fig.gca(projection='3d')
        for edge in graph.edges:
            self.axes.plot([node_positions[node_idx[edge[0]], 0], node_positions[node_idx[edge[1]], 0]],
            [node_positions[node_idx[edge[0]], 1], node_positions[node_idx[edge[1]], 1]],
            [node_positions[node_idx[edge[0]], 2], node_positions[node_idx[edge[1]], 2]],
            c=shade[node_idx[edge[0]]], zorder=1)
        self.axes.scatter(node_positions[:, 0], node_positions[:, 1], node_positions[:, 2],
                              c=shades, zorder=2)
        self.draw()        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

