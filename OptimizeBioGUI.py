import sys
# from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
# 	QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout,QRadioButton,QComboBox,QFont)
# from PyQt5.QtCore import (QFile,QTextStream)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from sequence_operations import *
import re
import webbrowser
import datetime
from dnachisel import *
import collections
from Bio.Align.Applications import MuscleCommandline as MCL

## Retrieved stylesheet from https://github.com/ColinDuquesnoy/QDarkStyleSheet/blob/master/qdarkstyle/style.qss

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Optimize.Bio")
		self.setMinimumSize(1200, 600)

		self.label1 = QLabel("Sequence type")
		self.label1.setFont(QFont("Helvetica",13))
		self.dropdown1 = QComboBox()
		self.dropdown1.addItem("--------")
		self.dropdown1.addItem("Protein Sequence")
		# self.dropdown1.addItem("DNA Sequence")
		self.dropdown1.setFont(QFont("Helvetica"))

		self.label2 = QLabel("Desired Species")
		self.label2.setFont(QFont("Helvetica",13))
		self.dropdown2 = QComboBox()
		self.dropdown2.addItem("--------")
		self.dropdown2.addItem("E. coli")
		self.dropdown2.addItem("B. subtilis")
		self.dropdown2.addItem("C. elegans")
		self.dropdown2.addItem("D. melanogaster")
		self.dropdown2.addItem("G. gallus")
		self.dropdown2.addItem("H. sapiens")
		self.dropdown2.addItem("M. musculus")
		self.dropdown2.addItem("S. cerevisiae")
		self.dropdown2.setFont(QFont("Helvetica"))

		self.label3 = QLabel("Input Method")
		self.label3.setFont(QFont("Helvetica",13))
		self.dropdown3 = QComboBox()
		self.dropdown3.addItem("--------")
		self.dropdown3.addItem("File upload")
		self.dropdown3.addItem("Manual")
		self.dropdown3.setFont(QFont("Helvetica"))

		self.dropdown3.currentIndexChanged.connect(self.enable_text_widgets)

		# self.label8 = QLabel("Upload File Here")
		# self.label8.setFont(QFont("Helvetica",13))
		self.button2 = QPushButton("Select File")
		self.label9 = QLabel("Uploaded File Location")
		self.label9.setFont(QFont("Helvetica",13))
		self.label9.setHidden(True)
		# self.label8.setHidden(True)
		self.button2.setHidden(True)
		self.button2.clicked.connect(self.openFileNameDialog)
		
		self.seq1_text = QLineEdit("Sequence 1 Label")
		self.seq1_sequence = QTextEdit("Sequence 1")
		self.seq2_text = QLineEdit("Sequence 2 Label")
		self.seq2_sequence =QTextEdit("Sequence 2")
		self.seq3_text = QLineEdit("Sequence 3 Label")
		self.seq3_sequence = QTextEdit("Sequence 3")
		self.seq4_text = QLineEdit("Sequence 4 Label")
		self.seq4_sequence = QTextEdit("Sequence 4")
		self.seq5_text = QLineEdit("Sequence 5 Label")
		self.seq5_sequence = QTextEdit("Sequence 5")
		self.seq6_text = QLineEdit("Sequence 6 Label")
		self.seq6_sequence = QTextEdit("Sequence 6")
		self.seq7_text = QLineEdit("Sequence 7 Label")
		self.seq7_sequence = QTextEdit("Sequence 7")
		self.seq8_text = QLineEdit("Sequence 8 Label")
		self.seq8_sequence = QTextEdit("Sequence 8")
		self.seq9_text = QLineEdit("Sequence 9 Label")
		self.seq9_sequence = QTextEdit("Sequence 9")
		self.seq10_text = QLineEdit("Sequence 10 Label")
		self.seq10_sequence = QTextEdit("Sequence 10")

		self.label4 = QLabel("Optimize.Bio")
		self.label4.setFont(QFont("Helvetica",18))
		self.label4.setAlignment(Qt.AlignCenter)
		self.label5 = QLabel("A sequence alignment and codon optimization tool")
		self.label5.setFont(QFont("Helvetica",15))
		self.label5.setAlignment(Qt.AlignCenter)

		self.label6 = QLabel("Sequence Count")
		self.label6.setFont(QFont("Helvetica",13))
		self.dropdown4 = QComboBox()
		self.dropdown4.addItem("--------")
		self.dropdown4.addItem("3")
		self.dropdown4.addItem("4")
		self.dropdown4.addItem("5")
		self.dropdown4.addItem("6")
		self.dropdown4.addItem("7")
		self.dropdown4.addItem("8")
		self.dropdown4.addItem("9")
		self.dropdown4.addItem("10")
		self.dropdown4.setFont(QFont("Helvetica"))

		self.button1 = QPushButton("Generate Sequence")
		self.button1.setEnabled(False)
		self.button1.clicked.connect(self.generate_sequence)

		self.dropdown4.currentIndexChanged.connect(self.select_sequence_cells)

		self.seqlist = [self.seq1_text,self.seq1_sequence,self.seq2_text,self.seq2_sequence,self.seq3_text,self.seq3_sequence,self.seq4_text,self.seq4_sequence,
		self.seq5_text,self.seq5_sequence,self.seq6_text,self.seq6_sequence,self.seq7_text,self.seq7_sequence,self.seq8_text,self.seq8_sequence,
		self.seq9_text,self.seq9_sequence,self.seq10_text,self.seq10_sequence]

		[item.setEnabled(False) for item in self.seqlist]
		[item.setHidden(True) for item in self.seqlist]


		self.label7 = QTextEdit("Final Output")
		self.label7.isReadOnly()
		self.label7.setFont(QFont("Helvetica",13))
		self.label7.setAlignment(Qt.AlignCenter)
		self.label7.setTextInteractionFlags(Qt.TextSelectableByMouse)
		self.label7.setHidden(True)

		### Create the File Dropdown Main Menu

		# self.mainMenu = QMenuBar()
		# fileMenu = self.mainMenu.addMenu('File')
		# editMenu = self.mainMenu.addMenu('Edit')
		# viewMenu = self.mainMenu.addMenu('View')
		# searchMenu = self.mainMenu.addMenu('Search')
		# toolsMenu = self.mainMenu.addMenu('Tools')
		# helpMenu = self.mainMenu.addMenu('Help')
		# self.mainMenu.setGeometry(30,30,1200,1200)
		
		# exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
		# exitButton.setShortcut('Ctrl+Q')
		# exitButton.setStatusTip('Exit application')
		# exitButton.triggered.connect(self.close)
		# fileMenu.addAction(exitButton)
		self.mainMenu = self.CreateMenu()
		self.mainMenu.setFixedHeight(30)
		hbox3 = QHBoxLayout()
		hbox3.addWidget(self.mainMenu)
		hbox3.setContentsMargins(0,0,0,0)
		# self.seq1_text.setEnabled(False)
		# self.seq1_sequence.setEnabled(False)
		# self.seq2_text.setEnabled(False)
		# self.seq2_sequence.setEnabled(False)
		# self.seq3_text.setEnabled(False)
		# self.seq3_sequence.setEnabled(False)
		# self.seq4_text.setEnabled(False)
		# self.seq4_sequence.setEnabled(False)
		# self.seq5_text.setEnabled(False)
		# self.seq5_sequence.setEnabled(False)
		# self.seq6_text.setEnabled(False)
		# self.seq6_sequence.setEnabled(False)
		# self.seq7_text.setEnabled(False)
		# self.seq7_sequence.setEnabled(False)
		# self.seq8_text.setEnabled(False)
		# self.seq8_sequence.setEnabled(False)
		# self.seq9_text.setEnabled(False)
		# self.seq9_sequence.setEnabled(False)
		# self.seq10_text.setEnabled(False)
		# self.seq10_sequence.setEnabled(False)

		# self.seq1_text.setHidden(True)
		# self.seq1_sequence.setHidden(True)
		# self.seq2_text.setHidden(True)
		# self.seq2_sequence.setHidden(True)
		# self.seq3_text.setHidden(True)
		# self.seq3_sequence.setHidden(True)
		# self.seq4_text.setHidden(True)
		# self.seq4_sequence.setHidden(True)
		# self.seq5_text.setHidden(True)
		# self.seq5_sequence.setHidden(True)
		# self.seq6_text.setHidden(True)
		# self.seq6_sequence.setHidden(True)
		# self.seq7_text.setHidden(True)
		# self.seq7_sequence.setHidden(True)
		# self.seq8_text.setHidden(True)
		# self.seq8_sequence.setHidden(True)
		# self.seq9_text.setHidden(True)
		# self.seq9_sequence.setHidden(True)
		# self.seq10_text.setHidden(True)
		# self.seq10_sequence.setHidden(True)


		hbox1 = QHBoxLayout()

		vbox1 = QVBoxLayout()
		vbox1.addWidget(self.label6)
		vbox1.addWidget(self.dropdown4)
		vbox1.addWidget(self.label3)
		vbox1.addWidget(self.dropdown3)

		# vbox1.addWidget(self.label8)
		hbox2 = QHBoxLayout()
		hbox2.addWidget(self.button2)
		hbox2.addWidget(self.label9)
		vbox1.addLayout(hbox2)

		vbox1.addWidget(self.label1)
		vbox1.addWidget(self.dropdown1)
		vbox1.addWidget(self.label2)
		vbox1.addWidget(self.dropdown2)
		vbox1.addWidget(self.button1)
		vbox1.setContentsMargins(10,10,10,10)

		vbox2 = QVBoxLayout()
		vbox2.addWidget(self.seq1_text)
		vbox2.addWidget(self.seq1_sequence)
		vbox2.addWidget(self.seq2_text)
		vbox2.addWidget(self.seq2_sequence)
		vbox2.addWidget(self.seq3_text)
		vbox2.addWidget(self.seq3_sequence)
		vbox2.addWidget(self.seq4_text)
		vbox2.addWidget(self.seq4_sequence)
		[vbox2.addWidget(item) for item in self.seqlist[8:]]
		vbox2.addWidget(self.label7)
		vbox2.setContentsMargins(10,10,10,10)

		hbox1.addLayout(vbox1)
		hbox1.addLayout(vbox2)

		vbox3 = QVBoxLayout()
		vbox3.addLayout(hbox3)
		vbox3.addWidget(self.label4)
		vbox3.addWidget(self.label5)
		vbox3.addLayout(hbox1)
		vbox3.setContentsMargins(0,0,0,5)

		self.setLayout(vbox3)

		### Check to see if conditions are met to enable button
		self.dropdown1.currentIndexChanged.connect(self.enable_button)
		self.dropdown2.currentIndexChanged.connect(self.enable_button)
		self.dropdown3.currentIndexChanged.connect(self.enable_button)
		self.dropdown4.currentIndexChanged.connect(self.enable_button)

		### A variable to store the location of a file that is uploaded
		self.input_file_name = ""



	def enable_text_widgets(self):
		if self.dropdown3.currentText() == "File upload":
			[item.setEnabled(False) for item in self.seqlist]
			self.label9.setHidden(False)
			# self.label8.setHidden(False)
			self.button2.setHidden(False)
		elif self.dropdown3.currentText() == "Manual":
			[item.setEnabled(True) for item in self.seqlist]
			self.label9.setHidden(True)
			# self.label8.setHidden(True)
			self.button2.setHidden(True)
		else:
			[item.setEnabled(False) for item in self.seqlist]
			self.label9.setHidden(True)
			# self.label8.setHidden(True)
			self.button2.setHidden(True)

	def select_sequence_cells(self):
		if self.dropdown4.currentText() != "--------":
			[item.setHidden(True) for item in self.seqlist]
			[item.setHidden(False) for item in self.seqlist[:int(self.dropdown4.currentText())*2]]
			self.label7.setHidden(False)
		if self.dropdown4.currentText() == "--------":
			[item.setHidden(True) for item in self.seqlist]
			self.label7.setHidden(True)

	def enable_button(self):
		if self.dropdown1.currentText() != "--------" and self.dropdown2.currentText() != "--------" and self.dropdown3.currentText() != "--------" and self.dropdown4.currentText() != "--------":
			self.button1.setEnabled(True)
		else:
			self.button1.setEnabled(False)

	def generate_sequence(self):
		try:
			if self.dropdown3.currentText() == "Manual" and self.dropdown1.currentText() == "Protein Sequence":
				number_of_seqs = int(self.dropdown4.currentText())
				for i in range(0,number_of_seqs*2):
					if i%2 == 1:
						if not bool(re.match("^[GALMFWKQESPVICYHRNDT]+$",self.seqlist[i].toPlainText())):
							self.label7.setFont(QFont("Helvetica",10))
							self.label7.setText(f"Your sequence(s) do not have the correct format.")
							return
				sublist = self.seqlist[:number_of_seqs*2]
				write_input_to_file(sublist)
				muscle_exe = "D:/Downloads/muscle3.8.31_i86win32.exe"
				seqdict = generate_sequence_alignment("input.fasta",muscle_exe)
				final_seq = generate_consensus_sequence(seqdict)
				if type(final_seq) == list:
					newseq = final_seq[0]
				else:
					newseq =final_seq
				codon_optimized_seq = codon_optimize_protein(newseq,self.dropdown2.currentText())
				self.label7.setFont(QFont("Helvetica",10))
				self.label7.setText(codon_optimized_seq)
				self.label7.setAlignment(Qt.AlignLeft)
				return
			elif self.dropdown3.currentText() == "File upload":
				if not self.input_file_name:
					raise ValueError("Error in uploaded file location")
				if ".fasta" not in self.input_file_name:
					raise ValueError("File must be in FASTA format.")
				muscle_exe = "D:/Downloads/muscle3.8.31_i86win32.exe"
				seqdict = generate_sequence_alignment(self.input_file_name,muscle_exe)
				final_seq = generate_consensus_sequence(seqdict)
				if type(final_seq) == list:
					newseq = final_seq[0]
				else:
					newseq =final_seq
				codon_optimized_seq = codon_optimize_protein(newseq,self.dropdown2.currentText())
				self.label7.setFont(QFont("Helvetica",10))
				self.label7.setText(codon_optimized_seq)
				self.label7.setAlignment(Qt.AlignLeft)
				return
		except KeyError as c:
			self.label7.setText("Please make sure your file contains at least 3 sequences of approximately the same length." + "\n" + repr(c))
		except Exception as e:
			self.label7.setText("An error has occurred while processing your input. Please try again." + "\n" + repr(e))
			return

	def openFileNameDialog(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
		if fileName:
			self.label9.setText(fileName)
			self.label9.setFont(QFont("Helvetica",10))
			self.input_file_name = fileName

	# def initUI(self):
	# 	# self.setWindowTitle(self.title)
	# 	# self.setGeometry(self.left, self.top, self.width, self.height)
		
	# 	mainMenu = self.menuBar()
	# 	fileMenu = mainMenu.addMenu('File')
	# 	editMenu = mainMenu.addMenu('Edit')
	# 	viewMenu = mainMenu.addMenu('View')
	# 	searchMenu = mainMenu.addMenu('Search')
	# 	toolsMenu = mainMenu.addMenu('Tools')
	# 	helpMenu = mainMenu.addMenu('Help')
		
	# 	exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
	# 	exitButton.setShortcut('Ctrl+Q')
	# 	exitButton.setStatusTip('Exit application')
	# 	exitButton.triggered.connect(self.close)
	# 	fileMenu.addAction(exitButton)

		# self.show()

	def CreateMenu(self):
		# mainMenu = self.menuBar()
		mainMenu = QMenuBar()
		# self.setMenuBar(mainMenu)
		mainMenu.setNativeMenuBar(False)
		fileMenu = mainMenu.addMenu('File')
		exportCurrentAction = QAction(QIcon(),"Export Current Output",self)
		exportCurrentAction.setShortcut("Ctrl+S")
		exportCurrentAction.triggered.connect(self.exportCurrentOutput)
		fileMenu.addAction(exportCurrentAction)
		# exportAllAction = QAction(QIcon(), "Export History",self)
		# exportAllAction.setShortcut("Ctrl+Shift+S")
		# exportAllAction.triggered.connect(self.exportHistoryToFile)
		# fileMenu.addAction(exportAllAction)
		fileMenu.addSeparator()
		clearAction = QAction(QIcon(), "Clear and Reset",self)
		clearAction.setShortcut("Ctrl+X")
		clearAction.triggered.connect(self.resetApplication)
		fileMenu.addAction(clearAction)
		fileMenu.addSeparator()
		exiteAction = QAction(QIcon("exit.png"), 'Exit', self)
		exiteAction.setShortcut("Ctrl+E")
		exiteAction.triggered.connect(self.exitWindow)
		fileMenu.addAction(exiteAction)

		# editMenu = mainMenu.addMenu('Edit')

		# viewMenu = mainMenu.addMenu('View')

		helpMenu = mainMenu.addMenu('Help')
		aboutThisAction = QAction(QIcon(),"About Optimize.Bio",self)
		aboutThisAction.triggered.connect(self.openSummaryDialog)
		helpMenu.addAction(aboutThisAction)
		openGithubAction = QAction(QIcon(), "Documentation/Support",self)
		openGithubAction.triggered.connect(self.openGithubLink)
		helpMenu.addAction(openGithubAction)

		return mainMenu

	def exportCurrentOutput(self):
		text = self.label7.toPlainText()
		if text == "Final Output":
			return
		species = self.dropdown2.currentText()
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)	
		with open(fileName,"w",encoding="utf8") as f:
			f.write("Date/Time: " + str(datetime.datetime.now()) + "\n")
			f.write("Species for Optimization: " + species + "\n")

			if self.dropdown3.currentText() == "Manual":
				for i,item in enumerate(self.seqlist[:int(self.dropdown4.currentText())]):
					f.write(item + "\n")
			else:
				newfile = open(self.label9.text())
				inputFileText = newfile.read()
				f.write(inputFileText)
				newfile.close()

			f.write("\n" + "Final Output: " + text)

	# def exportHistoryToFile(self):
	# 	print("Attempting to Export History")

	def resetApplication(self):
		self.dropdown1.setCurrentIndex(0)
		self.dropdown2.setCurrentIndex(0)
		self.dropdown3.setCurrentIndex(0)
		self.dropdown4.setCurrentIndex(0)
		counter = 0
		for i,item in enumerate(self.seqlist):
			if i%2 == 1:
				item.setText(f"Sequence {counter}")
			else:
				counter += 1
				item.setText(f"Sequence {counter} Label")

	def openSummaryDialog(self):
		dlg = QDialog(self)
		dlg.setWindowTitle("About Optimize.Bio")
		dlg.resize(260,200)

		newstr1 = """Optimize.Bio is a Python Application to perform sequence alignment and codon optimization on DNA/Amino Acid Sequences.
		This program utilizes DNAChisel for Codon Optimization, MuscleCommandLine and BioPython for Sequence Alignment, and standard File
		I/O for file manipulation."""
		newstr2 = """Applications of this program include DNA vaccine design and reverse translation of proteins for plasmid design. 
		In addition, general molecular cloning workflows can utilize this tool to generate an optimized sequence from NIH/NCBI and 
		clone into expression plasmids. """
		newstr3 = "This application was built using PyQt5, Python, and a range of bioinformatics modules by Gaurav Byagathvalli. Credit for modules goes to respective creators."

		newstr = "\n".join([newstr1,newstr2,newstr3])

		newread = QTextEdit(newstr,dlg)
		newread.setReadOnly(True)
		newread.setFont(QFont("Helvetica",10))
		dlg.exec_()

	def openGithubLink(self):
		webbrowser.open("https://github.com/gaubyaga/Optimize.Bio")

	def exitWindow(self):
		self.close()

if __name__ == "__main__":
	app = QApplication(sys.argv)

	file = QFile("style.qss")
	file.open(QFile.ReadOnly | QFile.Text)
	stream = QTextStream(file)
	app.setStyleSheet(stream.readAll())
	
	main = MainWindow()
	main.show()
	sys.exit(app.exec())
