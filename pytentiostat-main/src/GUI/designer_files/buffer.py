## CA
from Adv_params_GUI import Ui_Adv_Params
from Load_config_GUI import Ui_Load


class Ui_CA(object):

    def load_folder_name(self):
        """Initializes the 'Load config file' window.

        Returns
        ------
        string : the loaded filename
        """
        self.window = QtWidgets.QWidget()
        self.Load = Ui_Load()
        return self.Load.setupUi_save(self.window)

    def AP_window(self):
        """Initializes the 'Advanced parameters' window.

        Returns
        ------
        AP : the Ui_Adv_Params object
        window : QtWidgets.QMainWindow object
        """
        self.window = QtWidgets.QMainWindow()
        self.AP = Ui_Adv_Params()
        self.AP.setupUi(self.window)
        self.window.show()
        return self.AP, self.window


from Adv_params_GUI import Ui_Adv_Params

## CV
from Load_config_GUI import Ui_Load  # more


class Ui_CV(object):
    """Initializes the 'Load config file' window.

    Returns
    ------
    string : the loaded filename
    """

    def load_folder_name(self):
        self.window = QtWidgets.QWidget()
        self.Load = Ui_Load()
        return self.Load.setupUi_save(self.window)

    def AP_window(self):
        """Initializes the 'Advanced parameters' window.

        Returns
        ------
        AP : the Ui_Adv_Params object
        window : QtWidgets.QMainWindow object
        """
        self.window = QtWidgets.QMainWindow()
        self.AP = Ui_Adv_Params()
        self.AP.setupUi(self.window)
        self.window.show()
        return self.AP, self.window


## LSV
class Ui_LSV(object):

    def load_folder_name(self):
        """Initializes the 'Load config file' window.

        Returns
        ------
        string : the loaded filename
        """
        self.window = QtWidgets.QWidget()
        self.Load = Ui_Load()
        return self.Load.setupUi_save(self.window)

    def AP_window(self):
        """Initializes the 'Advanced parameters' window.

        Returns
        ------
        AP : the Ui_Adv_Params object
        window : QtWidgets.QMainWindow object
        """
        self.window = QtWidgets.QMainWindow()
        self.AP = Ui_Adv_Params()
        self.AP.setupUi(self.window)
        self.window.show()
        return self.AP, self.window


from CA_GUI import Ui_CA
from CV_GUI import Ui_CV
from Exp_type_GUI import Ui_Experiment
from Load_config_GUI import Ui_Load

## main
## main
from LSV_GUI import Ui_LSV


class Ui_MainWindow(object):
    def show_exp(self):
        """Initializes the 'Experiment Type' window.

        Returns
        ------
        exp: the Ui_Experiment object
        """
        self.window = QtWidgets.QDialog()
        self.exp = Ui_Experiment()
        self.exp.setupUi(self.window)
        self.window.show()
        return self.exp

    def show_LSVwindow(self):
        """Initializes the 'LSV' window.

        Returns
        ------
        LSV: the Ui_LSV object
        window : the LSV QMainWindow object
        """
        self.window = QtWidgets.QMainWindow()
        self.LSV = Ui_LSV()
        self.LSV.setupUi(self.window)
        self.window.show()
        return self.LSV, self.window

    def show_CVwindow(self):
        """Initializes the 'CV' window.

        Returns
        ------
        CV: the Ui_CV object
        window : the CV QMainWindow object
        """
        self.window = QtWidgets.QMainWindow()
        self.CV = Ui_CV()
        self.CV.setupUi(self.window)
        self.window.show()
        return self.CV, self.window

    def show_CAwindow(self):
        """Initializes the 'CA' window.

        Returns
        ------
        CA: the Ui_CA object
        window : the CA QMainWindow object
        """
        self.window = QtWidgets.QMainWindow()
        self.CA = Ui_CA()
        self.CA.setupUi(self.window)
        self.window.show()
        return self.CA, self.window

    def load_config(self):
        """Initializes the 'Load config file' window.

        Returns
        ------
        string: the loaded filename
        """
        self.window = QtWidgets.QWidget()
        self.Load = Ui_Load()
        return self.Load.setupUi(self.window)
