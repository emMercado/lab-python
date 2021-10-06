from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
from PyQt5 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("dobleView.ui", self)

        self.btnAgregar.clicked.connect(self.on_agregar)
        self.btnEditar.clicked.connect(self.on_editar)
        self.btnEliminar.clicked.connect(self.on_eliminar)
        self.btnDerecha.clicked.connect(self.on_derecha)
        self.btnIzquierda.clicked.connect(self.on_izquierda)
        #self.btnEliminarTodos.clicked.connect(self.print_click)
    
    def on_derecha(self):
        text_pass = self.list1.currentItem().text()
        self.list2.addItem(text_pass)
        self.list1.takeItem(self.list1.currentRow())
    
    def on_izquierda(self):
        text_pass2 = self.list2.currentItem().text()
        self.list1.addItem(text_pass2)
        self.list2.takeItem(self.list2.currentRow())

    def on_agregar(self):
        self.list1.addItem(self.inputNombre.text())
        self.inputNombre.setText("")
    
    def on_editar(self):
        texto_item = self.list1.currentItem().text()
        nuevo_texto, ok = QInputDialog.getText(self, 'Editar', 'Ingrese nuevo nombre', text=texto_item)
        if ok:
            self.list1.currentItem().setText(nuevo_texto)
    
    def on_eliminar(self):
        self.list1.takeItem(self.list1.currentRow())
    
    def on_eliminar_todos(self):
        self.list1.clear()


app = QApplication([])
win = MiVentana()
win.show()
app.exec_()
