import os.path
import json


    ###################################################
    #
    # Class user creates structures of the diffrent the diffrent modes of
    # Bradycardia Therapy and there programable parameters.
    # It also writes and reads user's saved values of programble parameters.
    #
    # Atributes:
    #   username: the username of the user
    #    
    ###################################################
class user:
    def __init__(self, username):
        self._username = username
        self._filename = self._username+'.txt'
        self._modes_struct ={ # intializes current values for user of all parameters of all modes
            'VOO': {'Lower Rate Limit':0, 'Upper Rate Limit':0, 'Ventricular Amplitude':0, 'Ventricular Pulse Width':0},
            'AOO': {'Lower Rate Limit':0, 'Upper Rate Limit':0, 'Atrial Amplitude':0, 'Atrial Pulse Width':0}
            }
        self._parameters_struct={ # all posible values for each parameter
            'Lower Rate Limit':['30', '35', '40', '45', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '95', '100', '105', '110', '115', '120', '125', '130', '135', '140', '145', '150', '155', '160', '165', '170', '175'],
            'Upper Rate Limit':['50', '55', '60', '65', '70', '75', '80', '85', '90', '95', '100', '105', '110', '115', '120', '125', '130', '135', '140', '145', '150', '155', '160', '165', '170', '175'],
            'Ventricular Amplitude':['0.5', '0.6', '0.7', '0.8', '0.9', '1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8', '1.9', '2.0', '2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '2.9', '3.0', '3.1', '3.2', '3.5', '4.0', '4.5', '5.0', '5.5', '6.0', '6.5', '7.0'],
            'Ventricular Pulse Width':['0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8', '1.9'],
            'Atrial Amplitude':['0.5', '0.6', '0.7', '0.8', '0.9', '1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8', '1.9', '2.0', '2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '2.9', '3.0', '3.1', '3.2', '3.5', '4.0', '4.5', '5.0', '5.5', '6.0', '6.5', '7.0'],
            'Atrial Pulse Width':['0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8', '1.9'],
            }
        x=self._modes_struct

        # creates a file with the users name and if file already exists,
        # it updates self._modes_struct using that file
        if os.path.isfile(self._filename):
            with open(self._filename, 'r') as file1:
                a = file1.read()
                x = json.loads(a)
        else:
            with open(self._filename, 'w') as file2:
                file2.write(json.dumps(self._modes_struct))
        self._modes_struct = x

    def update(self):
        # updates the file of the user using the dictinary self._modes_struct
        with open(self._filename, 'w') as file2:
                file2.write(json.dumps(self._modes_struct))
        

    def get_allmodes(self):
        # returns all the modes in dictinary self._modes_struct
        modes = []
        for i in self._modes_struct.keys():
            modes.append(i)
        return modes

    def get_allparameters(self, mode):
        # returns all the parameters in dictinary self._modes_struct
        # for a specifide mode
        parameters = []
        for i in self._modes_struct[mode].keys():
            parameters.append(i)
        return parameters

    def get_value(self, mode, parameter):
        # return a value from dictinary self._modes_struct for a
        # specifide mode and parameter
        return self._modes_struct[mode][parameter]

    def set_value(self, mode, parameter, value):
        # changes a value in dictinary self._modes_struct and
        # the user's file for a specifide mod and parameter
        self._modes_struct[mode][parameter] = value
        self.update()

    def get_allvalues(self,parameter):
        # returns all possible values for a specifide parameter
        return self._parameters_struct[parameter]


