patterns.append({ 
'name': 'GoogleExample', 
'signature': {'address': 'has address', 'object': ''}, 
'options': [    
    {'name': 'base', 
     'parts': [ 
          { 
               'object': 'self', 
               'address': 'hasAddress', 
               'type': 'http://rds.posccaesar.org/2008/02/OWL/ISO-15926-2_2003#Thing' 
          }, 
          { 
               'superclass' : 'self', 
               'uri' : part2.Activity.uri, 
          }, 
          { 
               'type' : part2.Specialization, 
               'object' : 'hasSubclass', 
               'superclass' : 'hasSuperclass', 
          }, 
     ] 
     }, 
] 
})



#ISO 15926-4 SPATIAL LOCATION : ClassOfIndividual
#http://posccaesar.org/rdl/RDS436813841
#PASSAGE : ClassOfArrangedIndividual
#http://posccaesar.org/rdl/RDS11589310

patterns.append({
'name': 'GoogleRoute', 
'signature': {'id_route' : 'is in route', 'name_route' :'', 'id_loc1': 'connected to', 'name_loc1': '', 'id_loc2': 'connected to', 'name_loc2': '', 'creation_date' : '',}, 
'options': [    
    {'name': 'base', 
     'parts': [ 
          { 
               'id_route': 'self', 
               'name_route': 'label', 
               'type': 'http://posccaesar.org/rdl/RDS11589310' 
          },
          { 
               'id_loc1': 'self', 
               'name_loc1': 'label', 
               'type': 'http://posccaesar.org/rdl/RDS436813841' 
          }, 
          { 
               'id_loc2': 'self', 
               'name_loc2': 'label', 
               'type': 'http://posccaesar.org/rdl/RDS436813841' 
          },
          { 
               'type' : part2.IndirectConnection, 
               'id_loc1' : 'hasSide1',
               'id_loc2' : 'hasSide2', 
          },   
          { 
               'type' : part2.AssemblyOfIndividual, 
               'id_loc1' : 'hasPart',
               'id_route' : 'hasWhole', 
          },   
          { 
               'type' : part2.AssemblyOfIndividual, 
               'id_loc2' : 'hasPart',
               'id_route' : 'hasWhole', 
          },   
     ] 
     }, 
    {'name': 'metadata', 
     'parts': [ 
          { 
               'id_route': 'self', 
               'name_route': 'label', 
               'type': 'http://posccaesar.org/rdl/RDS11589310',
          },
          { 
               'id_route': 'self', 
               'creation_date' : 'http://posccaesar.org/rdl/hasCreationDate',
          },
          { 
               'id_loc1': 'self', 
               'name_loc1': 'label', 
               'type': 'http://posccaesar.org/rdl/RDS436813841',
          }, 
          { 
               'id_loc1': 'self', 
               'creation_date' : 'http://posccaesar.org/rdl/hasCreationDate',
          },
          { 
               'id_loc2': 'self', 
               'name_loc2': 'label', 
               'type': 'http://posccaesar.org/rdl/RDS436813841',
          },
          { 
               'id_loc2': 'self', 
               'creation_date' : 'http://posccaesar.org/rdl/hasCreationDate',
          },
          { 
               'conn' : 'self',
               'type' : part2.IndirectConnection, 
               'id_loc1' : 'hasSide1',
               'id_loc2' : 'hasSide2', 
          }, 
          { 
               'conn' : 'self',
               'creation_date' : 'http://posccaesar.org/rdl/hasCreationDate',
          },  
          { 
               'ass1' : 'self',
               'type' : part2.AssemblyOfIndividual, 
               'id_loc1' : 'hasPart',
               'id_route' : 'hasWhole', 
          }, 
          { 
               'ass1' : 'self',
               'creation_date' : 'http://posccaesar.org/rdl/hasCreationDate',
          },   
          { 
               'ass2' : 'self',
               'type' : part2.AssemblyOfIndividual, 
               'id_loc2' : 'hasPart',
               'id_route' : 'hasWhole',
          },   
          { 
               'ass2' : 'self',
               'creation_date' : 'http://posccaesar.org/rdl/hasCreationDate', 
          },   
     ] 
     }, 
] 
})