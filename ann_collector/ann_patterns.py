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
'signature': {'Title': '', 'TitleId' : ''},
'options': [   
    {'name' : 'main',
     'parts' : [
          {
          'AMTitle' : 'self',
          'uri': 'http://anird.techinvestlab.ru/rdl/id83475f51-fcb0-48cf-ab80-ac726cec2202'
          },
          {
          'AniDBMainTitle' : 'self',
          'uri' : 'http://anird.techinvestlab.ru/rdl/id342b298b-9a78-413c-90c4-61f971d66a08'
          },
          {
          'AniDBID' : 'self',
          'uri' : 'http://anird.techinvestlab.ru/rdl/id3c21a8a9-4ede-47fa-952f-a7784ff4465e'
          },
          {
          'Anime' : 'self',
          'type' : 'http://rds.posccaesar.org/2008/02/OWL/ISO-15926-2_2003#ClassOfInformationObject',
          'Title' : 'label',
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
          'AniDBMainTitle' : 'hasContext'
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
'name': 'AnnPerson',
'signature': {'PersonName': ''
               , 'PersonId': ''
               },
'options': [   
    {'name' : 'main',
     'parts' : [

     	{
          'PersonId' : 'annPersonId',
     	'type' : 'http://example.org/rdl/id93e862e7-45ba-4640-83ff-2ea7e61fddeb',
          'Person': 'self',
          },

          {
          'PersonName' : 'label',
          'Person': 'self',
          },
     ]
	},
]
})




patterns.append({
'name': 'AnnStaffPosition',
'signature': { 'Person' : ''
               , 'PersonId': ''
               , 'TitleId' : ''
               , 'PositionName': ''
               },
'options': [   
    {'name' : 'main',
     'parts' : [
          {
          'Person' : 'self',
          'PersonId' : 'annPersonId',
          },
          {
          'Anime' : 'self',
          'TitleId' : 'annTitleId',
          'type' : 'http://example.org/rdl/id9e498b6d-eb75-4b5b-a494-ea3066533ae5',
          },
          {
          'PositionName' : 'label',
          'Position' : 'self',
          'type' : 'http://example.org/rdl/id7c4e2419-0af9-4297-a571-1a2a03a28152',
          },
          {
          'type': part2.ConnectionOfIndividual,
          'Connection': 'self',
          'Person'    : 'hasSide1',
          'Anime'    : 'hasSide2',
          },
          {
          'type': part2.IndividualUsedInConnection,
          'Connection' : 'hasConnection',
          'Position' : 'hasUsage',
          },
     ]
     },
]
})

patterns.append({
'name': 'AnnPersonPosition',
'signature': { 'Person' : 'has staff'
               , 'Anime' : 'in anime/manga'
               , 'Position': 'has task'
               },
'options': [   
    {'name' : 'main',
     'parts' : [
          {
          'Person' : 'self',
          'type' : 'http://example.org/rdl/id93e862e7-45ba-4640-83ff-2ea7e61fddeb',
          },
          {
          'Anime' : 'self',
          'type' : 'http://example.org/rdl/id9e498b6d-eb75-4b5b-a494-ea3066533ae5',
          },
          {
          'Position' : 'self',
          'type' : 'http://example.org/rdl/id7c4e2419-0af9-4297-a571-1a2a03a28152',
          },
          {
          'type': part2.ConnectionOfIndividual,
          'Connection': 'self',
          'Person'    : 'hasSide1',
          'Anime'    : 'hasSide2',
          },
          {
          'type': part2.IndividualUsedInConnection,
          'Connection' : 'hasConnection',
          'Position' : 'hasUsage',
          },
     ]
     },
]
})


patterns.append({
'name': 'AnnDetails',
'signature': {'PersonId': ''
               , 'TitleId' : ''
               , 'PositionName': ''
               , 'Title' : ''
               , 'PersonName' : ''
               , 'PersonId' : ''
               , 'Year' : ''
               },
'options': [
{'name' : 'main',
'parts' : [
{
     'type' : 'patterns.AnnTitle.details',
     'TitleId' : 'TitleId',
     'Title' : 'Title',
     'Year' : 'Year',
},
{
     'type' : 'patterns.AnnPerson.main',
     'PersonName' : 'PersonName',
     'PersonId' : 'PersonId',
},

{
     'type' : 'patterns.AnnStaffPosition.main',
     'PersonId' : 'PersonId',
     'TitleId' : 'TitleId',
     'PositionName' : 'PositionName',
},

]
}
]
})