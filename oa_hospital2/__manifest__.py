# -*- coding: utf-8 -*-
{
    'name': 'Hospital Management ',
    'version': '1.0',
    'category': 'Hospital',
    'author': 'onur',
    'sequence': -110,
    'summary': 'Hospital Management System',
    'description': """ Hospital Management System """,
    'depends': ['mail'],
    'data':[
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
