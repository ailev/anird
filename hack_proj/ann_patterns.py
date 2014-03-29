patterns.append({
'name': 'ANNTitle',
'signature': {'Title': '', 'TitleId' : '', 'Year': '' },
'options': [   
    {'name' : 'main',
     'parts' : [
          {
          'AMTitle' : 'self',
          'uri': 'http://anird.techinvestlab.ru/rdl/id83475f51-fcb0-48cf-ab80-ac726cec2202'
          },
          {
          'ANNMainTitle' : 'self',
          'uri' : 'http://anird.techinvestlab.ru/rdl/id602498b4-5737-4ee4-876e-5bb3a64471d7'
          },
          {
          'ANNID' : 'self',
          'uri' : 'http://anird.techinvestlab.ru/rdl/idbc8794fd-3091-4ca9-8af4-2ccad34d5a5b'
          },
          {
          'Anime' : 'self',
          'type' : 'http://rds.posccaesar.org/2008/02/OWL/ISO-15926-2_2003#ClassOfInformationObject',
          'Year' : 'annYearAired',
          'Title' : 'label',
          'TitleId' : 'annDataBaseID',
          },
          {
          'type' : p7tpl.Classification,
          'Anime' : 'hasClassified',
          'AMTitle' : 'hasClassifier'
          },
          {
          'type' : p7tpl.ClassifiedIdentification,
          'Anime' : 'hasObject',
          'Title' : 'valIdentifier',
          'ANNMainTitle' : 'hasContext'
          },
          {
          'type' : p7tpl.ClassifiedIdentification,
          'Anime' : 'hasObject',
          'TitleId' : 'valIdentifier',
          'ANNID' : 'hasContext'
          },
     ]
     }
     ]
})

patterns.append({
'name': 'AniDBTitle',
'signature': {'Title': '', 'TitleId' : '', 'TitleTypeName' : '', 'TitleMain' : ''},
'options': [   
    {'name' : 'main',
     'parts' : [
          {
          'AMTitle' : 'self',
          'uri': 'http://anird.techinvestlab.ru/rdl/id83475f51-fcb0-48cf-ab80-ac726cec2202'
          },
          {
          'AniDBTitle' : 'self',
          'uri' : 'http://anird.techinvestlab.ru/rdl/id342b298b-9a78-413c-90c4-61f971d66a08'
          },
          {
          'AniDBID' : 'self',
          'uri' : 'http://anird.techinvestlab.ru/rdl/id3c21a8a9-4ede-47fa-952f-a7784ff4465e'
          },
          {
          'Anime' : 'self',
          'type' : 'http://rds.posccaesar.org/2008/02/OWL/ISO-15926-2_2003#ClassOfInformationObject',
          'TitleMain' : 'label',
          'TitleId' : 'annDataBaseID',
          },
          {
          'TitleType' : 'self',
          'type' : 'http://rds.posccaesar.org/2008/02/OWL/ISO-15926-2_2003#ClassOfClassOfIdentification',
          'TitleTypeName' : 'label'
          },
          {
          'type' : p7tpl.Specialization,
          'TitleType' : 'hasSubclass',
          'AniDBTitle' : 'hasSuperclass'
          },
          {
          'type' : p7tpl.Classification,
          'Anime' : 'hasClassified',
          'AMTitle' : 'hasClassifier'
          },
          {
          'type' : p7tpl.ClassifiedIdentification,
          'Anime' : 'hasObject',
          'Title' : 'valIdentifier',
          'TitleType' : 'hasContext'
          },
          {
          'type' : p7tpl.ClassifiedIdentification,
          'Anime' : 'hasObject',
          'TitleId' : 'valIdentifier',
          'AniDBID' : 'hasContext'
          },
     ]
     }
     ]
})

patterns.append({
'name': 'ANNPerson',
'signature': {'PersonName': '', 'PersonId': ''},
'options': [   
    {'name' : 'main',
     'parts' : [
          {
          'Staff' : 'self',
          'uri': 'http://anird.techinvestlab.ru/rdl/id916121bd-3613-426c-8346-11ccac3698e8'
          },
          {
          'ANNMainName' : 'self',
          'uri' : 'http://anird.techinvestlab.ru/rdl/id71efaa3c-5b02-4a2c-b854-d357cbe5b5bc'
          },
          {
          'ANNID' : 'self',
          'uri' : 'http://anird.techinvestlab.ru/rdl/idbc8794fd-3091-4ca9-8af4-2ccad34d5a5b'
          },
     	{
          'type' : 'http://rds.posccaesar.org/2008/02/OWL/ISO-15926-2_2003#ActualIndividual',
          'Person': 'self',
          'PersonName': 'label',
          'PersonId' : 'annDataBaseID',
          },
          {
          'type' : p7tpl.Classification,
          'Person' : 'hasClassified',
          'Staff' : 'hasClassifier'
          },
          {
          'type' : p7tpl.ClassifiedIdentification,
          'Person' : 'hasObject',
          'PersonName' : 'valIdentifier',
          'ANNMainName' : 'hasContext'
          },
          {
          'type' : p7tpl.ClassifiedIdentification,
          'Person' : 'hasObject',
          'PersonId' : 'valIdentifier',
          'ANNID' : 'hasContext'
          },
          
     ]
	},
]
})

patterns.append({
'name': 'AniDBPerson',
'signature': {'PersonName': '', 'PersonId': ''},
'options': [   
    {'name' : 'main',
     'parts' : [
          {
          'Staff' : 'self',
          'uri': 'http://anird.techinvestlab.ru/rdl/id916121bd-3613-426c-8346-11ccac3698e8'
          },
          {
          'AniDBMainName' : 'self',
          'uri' : 'http://anird.techinvestlab.ru/rdl/id333c9202-2408-4fe9-8612-61ab05c564e9'
          },
          {
          'AniDBID' : 'self',
          'uri' : 'http://anird.techinvestlab.ru/rdl/id3c21a8a9-4ede-47fa-952f-a7784ff4465e'
          },
          {
          'type' : 'http://rds.posccaesar.org/2008/02/OWL/ISO-15926-2_2003#ActualIndividual',
          'Person': 'self',
          'PersonName': 'label',
          'PersonId' : 'annDataBaseID',
          },
          {
          'type' : p7tpl.Classification,
          'Person' : 'hasClassified',
          'Staff' : 'hasClassifier'
          },
          {
          'type' : p7tpl.ClassifiedIdentification,
          'Person' : 'hasObject',
          'PersonName' : 'valIdentifier',
          'AniDBMainName' : 'hasContext'
          },
          {
          'type' : p7tpl.ClassifiedIdentification,
          'Person' : 'hasObject',
          'PersonId' : 'valIdentifier',
          'AniDBID' : 'hasContext'
          },
          
     ]
     },
]
})


patterns.append({
'name': 'ANNStaffPosition',
'signature': {'Person' : 'Creator', 'PersonId': '', 'Position' : 'involved as', 'TitleId' : '', 'PositionName': '', 'Anime': 'involved in'},
'options': [   
    {'name' : 'main',
     'parts' : [
          {
          'ANNActClass' : 'self',
          'uri' : 'http://anird.techinvestlab.ru/rdl/id540f9542-c335-4ef1-97c3-af658501be8a'
          },
          {
          'Person' : 'self',
          'PersonId' : 'annDataBaseID',
          'type': 'http://anird.techinvestlab.ru/rdl/id916121bd-3613-426c-8346-11ccac3698e8'
          },
          {
          'Anime' : 'self',
          'TitleId' : 'annDataBaseID',
          'type': 'http://anird.techinvestlab.ru/rdl/id83475f51-fcb0-48cf-ab80-ac726cec2202'
          },
          {
          'PositionName' : 'label',
          'Position' : 'self',
          'type' : 'http://rds.posccaesar.org/2008/02/OWL/ISO-15926-2_2003#ClassOfActivity',
          },
          {
          'type' : p7tpl.Specialization,
          'Position' : 'hasSubclass',
          'ANNActClass' : 'hasSuperclass'
          },
          {
          'Act' : 'self',
          'type' : 'http://rds.posccaesar.org/2008/02/OWL/ISO-15926-2_2003#Activity'
          },
          {
          'type' : p7tpl.Classification,
          'Act' : 'hasClassified',
          'Position' : 'hasClassifier'
          },
          {
          'type' : p7tpl.InvolvementByReference,
          'Anime' : 'hasInvolved',
          'Act': 'hasInvolver'
          },
          {
          'type' : p7tpl.CompositionOfIndividual,
          'Person' : 'hasPart',
          'Act' : 'hasWhole'
          },
     ]
     },
]
})

patterns.append({
'name': 'AniDBStaffPosition',
'signature': {'Person' : 'Staff', 'PersonId': '', 'Position' : 'Staff positions', 'TitleId' : '', 'PositionName': '', 'Anime': 'involved in'},
'options': [   
    {'name' : 'main',
     'parts' : [
          {
          'AniDBActClass' : 'self',
          'uri' : 'http://anird.techinvestlab.ru/rdl/id50160897-3495-4b3a-8f79-4b73df8a534c'
          },
          {
          'Person' : 'self',
          'PersonId' : 'annDataBaseID',
          'type': 'http://anird.techinvestlab.ru/rdl/id916121bd-3613-426c-8346-11ccac3698e8'
          },
          {
          'Anime' : 'self',
          'TitleId' : 'annDataBaseID',
          'type': 'http://anird.techinvestlab.ru/rdl/id83475f51-fcb0-48cf-ab80-ac726cec2202'
          },
          {
          'PositionName' : 'label',
          'Position' : 'self',
          'type' : 'http://rds.posccaesar.org/2008/02/OWL/ISO-15926-2_2003#ClassOfActivity',
          },
          {
          'type' : p7tpl.Specialization,
          'Position' : 'hasSubclass',
          'AniDBActClass' : 'hasSuperclass'
          },
          {
          'Act' : 'self',
          'type' : 'http://rds.posccaesar.org/2008/02/OWL/ISO-15926-2_2003#Activity'
          },
          {
          'type' : p7tpl.Classification,
          'Act' : 'hasClassified',
          'Position' : 'hasClassifier'
          },
          {
          'type' : p7tpl.InvolvementByReference,
          'Anime' : 'hasInvolved',
          'Act': 'hasInvolver'
          },
          {
          'type' : p7tpl.CompositionOfIndividual,
          'Person' : 'hasPart',
          'Act' : 'hasWhole'
          },
     ]
     },
]
})

patterns.append({
'name': 'ANNTitleDetails',
'signature': {'PersonName' : '', 'PersonId': '', 'TitleId' : '', 'PositionName': ''},
'options': [   
    {'name' : 'main',
     'parts' : [
          {
          'type' : 'patterns.ANNPerson.main',
          'PersonName' : 'PersonName',
          'PersonId' : 'PersonId',
          },
          {
          'type' : 'patterns.ANNStaffPosition.main',
          'PersonId' : 'PersonId',
          'TitleId' : 'TitleId',
          'PositionName' : 'PositionName',
          },
     ]
     },
]
})

patterns.append({
'name': 'AniDBTitleDetails',
'signature': {'PersonName' : '', 'PersonId': '', 'TitleId' : '', 'PositionName': ''},
'options': [   
    {'name' : 'main',
     'parts' : [
          {
          'type' : 'patterns.AniDBPerson.main',
          'PersonName' : 'PersonName',
          'PersonId' : 'PersonId',
          },
          {
          'type' : 'patterns.AniDBStaffPosition.main',
          'PersonId' : 'PersonId',
          'TitleId' : 'TitleId',
          'PositionName' : 'PositionName',
          },
     ]
     },
]
})