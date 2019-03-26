import numpy as np

info = \
{
 'reference': 'Bouwens et al., 2014',
 'data': 'Table 2', 
 'fits': 'Table 4', 
}

redshifts = [4, 5, 6, 7, 8]
wavelength = None
units = {'beta': 1.}


_data = \
{
 4: {'M': np.arange(-21.75, -15.25, 0.5),
     'beta': [-1.54, -1.61, -1.7, -1.8, -1.81, -1.9, -1.97, -1.99, -2.09, 
         -2.09, -2.23, -2.15, -2.15],
     'err': [0.07, 0.04, 0.03, 0.02, 0.03, 0.02, 0.06, 0.06, 0.08, 0.07,
         0.1, 0.12, 0.12],
     'sys': [0.06] * 13,
 },
 5 : {'M': np.array(list(np.arange(-21.75, -16.75, 0.5)) + [-16.5]),
     'beta': [-1.36, -1.62, -1.74, -1.85, -1.82, -2.01, -2.12, -2.16, -2.09, 
         -2.27, -2.16],
     'err': [0.48, 0.11, 0.05, 0.05, 0.04, 0.07, 0.1, 0.09, 0.1, 0.14, 0.17],
     'sys': [0.06] * 11,
 },
 6 : {'M': np.array(list(np.arange(-21.75, -17.25, 0.5)) + [-17.]),
     'beta': [-1.55, -1.58, -1.74, -1.9, -1.9, -2.22, -2.26, -2.19, -2.4, -2.24],
     'err': [0.17, 0.1, 0.1, 0.09, 0.13, 0.18, 0.14, 0.22, 0.3, 0.2],
     'sys': [0.08] * 10,
 },
 7 : {'M': np.array([-21.25, -19.95, -18.65, -17.35]),
     'beta': [-1.75, -1.89, -2.3, -2.42],
     'err': [0.18, 0.13, 0.18, 0.28],
     'sys': [0.13] * 4,
 },
 8 : {'M': np.array([-19.95, -18.65]),
     'beta': [-2.3, -1.41],
     'err': [0.01, 0.6],
     'sys': [0.27, 0.27],
 },   
}


data = {}
data['beta'] = {}
for key in _data:
    data['beta'][key] = {}
    for element in _data[key]:
        data['beta'][key][element] = np.array(_data[key][element])