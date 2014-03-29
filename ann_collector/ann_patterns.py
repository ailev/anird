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
'name': 'AnnTitle',
'signature': {'Title': ''
               , 'TitleId' : ''
               , 'Year': ''
               },
'options': [   
    {'name' : 'main',
     'parts' : [
          {
          'Anime' : 'self',
          'TitleId' : 'annTitleId',
          'type' : 'http://example.org/rdl/id9e498b6d-eb75-4b5b-a494-ea3066533ae5',
          'Year' : 'annYear',
          'Title' : 'label',
          },
     ]
     },
    {'name' : 'details',
     'parts' : [
          {
          'Anime' : 'self',
          'TitleId' : 'annTitleId',
          'type' : 'http://example.org/rdl/id9e498b6d-eb75-4b5b-a494-ea3066533ae5',
          },
          {
          'Year' : 'annYear',
          'Title' : 'label',
          'Anime' : 'self',
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