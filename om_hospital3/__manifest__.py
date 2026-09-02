{
    'name':"Hello World",
    'version':"18.0",
    'summary':"a simple hello world module for try",
    'author':"Banastech",
    'category':"Tools",
     "sequence": -100,
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'depends':["base","mail","website"],
   'data': [
            'security/ir.model.access.csv',
            'data/sequence.xml',
            'views/patient.xml',
            'views/appointment.xml',
            'views/menu.xml',
            'views/template.xml',
        ],

 
}