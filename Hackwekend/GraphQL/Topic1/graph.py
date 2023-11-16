from ariadne import gql, QueryType, make_executable_schema
from dotenv import load_dotenv
import os

load_dotenv()

# Function to handling the finding
def find_by_id(list_findings, id):
    if id != "":
        for item in list_findings:
            if item['id'] == int(id):
                return item
    else:
        return list_findings


def find_by_id_and_coordinate(id, coordinates):
    for treasure in list_treasures:
        if treasure['id'] == int(id) and treasure['location']['coordinates'] == coordinates:
            if treasure['id'] == 4:
                temp = {}
                temp = treasure.copy()
                temp['description'] = "Thing is proven you are reach the right place, flag is comming !!!"
                temp['flag'] = os.getenv("FLAG")
                return temp
            else:
                return treasure

# Define type definitions (schema) using SDL
type_defs = gql(
    """
type Place {
  id: Int!
  name: String!
  description: String
  country: String
  coordinates: Coordinates
}

type Coordinates {
  latitude: Float!
  longitude: Float!
}

type Treasure {
  id: Int!
  name: String!
  location: Place
  flag: String
  description: String
}

input CoordinatesInput {
  latitude: Float!
  longitude: Float!
}

type Query {
  getAllPlaces: [Place]
  getPlace(id: ID!): Place
  getTreasure(id: ID!, coordinates: CoordinatesInput!): Treasure
  getAllTreasures: [Treasure]
}
   """
)

list_places = [
    {
        "id": 1,
        "name": "Paris",
        "description": "The city of lights",
        "country": "France",
        "coordinates": {"latitude": 48.86, "longitude": 2.35},
    },
    {
        "id": 2,
        "name": "Rome",
        "description": "The city of pizza",
        "country": "Italy",
        "coordinates": {"latitude": 41.91, "longitude": 12.54},
    },
    {
        "id": 3,
        "name": "London",
        "description": "The city of big buildings",
        "country": "United Kingdom",
        "coordinates": {"latitude": 48.86, "longitude": 2.35},
    },
    {
        "id": 4,
        "name": "Orient - Da Nang",
        "description": "Software Company",
        "country": "Viet Nam",
        "coordinates": {"latitude": 16.04, "longitude": 108.22},
    },
]

list_treasures = [
    {
        "id": 1,
        "name": "Péniche L'Eau Et Les Rêves",
        "description": "Home to Europe's largest science museum, this area rewards daytime and nighttime explorations; there are three concert spaces, plus cinemas and bars, and even open-air cinema in the summer. The surrounding homes are a sharp contrast to the futuristic space",
        "location": find_by_id(list_places, 1),
        "flag": "",
    },
    {
        "id": 2,
        "name": "The Colosseum",
        "description": "A large amphitheater that hosted events like gladiatorial games. Design Pics Inc. The Colosseum, also named the Flavian Amphitheater, is a large amphitheater in Rome. It was built during the reign of the Flavian emperors as a gift to the Roman people",
        "location": find_by_id(list_places, 2),
        "flag": "",
    },
    {
        "id": 3,
        "name": "Big Ben Tower",
        "description": "A tower clock known for its accuracy and for its massive hour bell. Strictly speaking, the name refers only to the bell, which weighs 15.1 tons (13.7 metric tons), but it is commonly associated with the whole clock tower at the northern end of the Houses of Parliament, in the London borough of Westminster",
        "location": find_by_id(list_places, 3),
        "flag": "",
    },
    {
        "id": 4,
        "name": "Orient Treasure",
        "description": "Keep going the treasure is need one more step to exposing",
        "location": find_by_id(list_places, 4),
        "flag": "Opps, Orient treasure is hidden",
    }
]

# Initialize query

query = QueryType()


# Define resolvers
@query.field("getAllPlaces")
def places(*_):
    return find_by_id(list_places, "")


@query.field("getPlace")
def place(*_, id):
    return find_by_id(list_places, id)


@query.field("getAllTreasures")
def treasures(*_):
    return find_by_id(list_treasures, "")

@query.field("getTreasure")
def treasure(*_, id, coordinates):
    return find_by_id_and_coordinate(id, coordinates)


# Create executable schema
schema = make_executable_schema(type_defs, query)
