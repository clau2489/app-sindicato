from PyQt5 import QtWidgets, QtGui

class ListadoDebitosContextM(QtWidgets.QTableView):

	def __init__(self, parent = None):
		super(ListadoDebitosContextM, self).__init__(parent)
		self.parent = parent

	def contextMenuEvent(self, event):
		self.menu = QtWidgets.QMenu(self)

		eliminarDebito = QtWidgets.QAction('Eliminar', self)
		pagoManualDebito = QtWidgets.QAction('Pago manual', self)

		eliminarDebito.triggered.connect(lambda: self.borrarDebito(event))
		pagoManualDebito.triggered.connect(lambda: self.pagoManual(event))

		self.menu.addAction(eliminarDebito)
		self.menu.addAction(pagoManualDebito)

		# add other required actions
		if self.selectedIndexes():
			self.menu.popup(QtGui.QCursor.pos())

	def borrarDebito(self, event):
		row = self.currentIndex().row()

		idDebitoIndex = self.model().index(row, 0)
		idDebito = self.model().itemData(idDebitoIndex)[0]

		if self.confirmarOperacion():
			self.model().borrarDebito(idDebito)
			self.model().refrescarTabla()

	def pagoManual(self, event):
		row = self.currentIndex().row()

		idDebitoIndex = self.model().index(row, 0)
		idDebito = self.model().itemData(idDebitoIndex)[0]

		debito = {
			'id' : idDebito,
			'estado' : "Cobrado manualmente"
		}

		if self.confirmarOperacion():
			self.model().actualizarDebito(debito)
			self.model().refrescarTabla()

	def confirmarOperacion(self):
		msg = QtWidgets.QMessageBox()

		reply = msg.question(self, "Confirmar operación", "¿Está seguro de realizar esta operación?",
			QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

		msg.show()

		if reply == QtWidgets.QMessageBox.Yes:
			return True
		else:
			return False
