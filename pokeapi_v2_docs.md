# PokéAPI v2 Documentation

Documentation scraped from: https://pokeapi.co/docs/v2
Generated on: 2025-05-28 00:48:30

---

If you were using v1 of this API, please switch to v2 (this page). [Read more…](/docs/v1)

**Quick tip:** Use your browser's "find on page" feature to search for specific resource types (`Ctrl+F` or `Cmd+F`).

## Information

This is a **consumption-only** API — only the HTTP GET method is available on resources.

No authentication is required to access this API, and all resources are fully open and available. Since the move to static hosting in November 2018, rate limiting has been removed entirely, but we still encourage you to limit the frequency of requests to limit our hosting costs.

## Fair Use Policy

PokéAPI is free and open to use. It is also very popular. Because of this, we ask every developer to abide by our fair use policy. People not complying with the fair use policy will have their IP address permanently banned.

PokéAPI is primarily an educational tool, and we will not tolerate denial of service attacks preventing people from learning.

Rules:

  * Locally cache resources whenever you request them.
  * Be nice and friendly to your fellow PokéAPI developers.
  * If you spot security vulnerabilities act and [report them](https://github.com/PokeAPI/pokeapi/blob/master/SECURITY.md#reporting-a-vulnerability) responsibly.

## Slack and community

Currently no maintainer has enough free time to support the community on Slack. Our Slack is in an unmaintained status. You can still sign up right [here](https://join.slack.com/t/pokeapi/shared_invite/zt-2ampo6her-_tHSI3uOS65WzGypt7Y96w) then visit our [Slack](https://pokeapi.slack.com) page.

## Wrapper Libraries

  * **Node Server-side with auto caching** : [Pokedex Promise v2](https://github.com/PokeAPI/pokedex-promise-v2) by Thomas Asadurian and Alessandro Pezzé
  * **Browser-side with auto caching** : [pokeapi-js-wrapper](https://github.com/PokeAPI/pokeapi-js-wrapper) by Alessandro Pezzé
  * **Python 3 with auto caching** : [PokeBase](https://github.com/GregHilmes/pokebase) by Greg Hilmes
  * **Python 2/3 with auto caching** : [Pokepy](https://github.com/PokeAPI/pokepy) by Paul Hallett
  * **Kotlin (and Java)** : [PokeKotlin](https://github.com/PokeAPI/pokekotlin) by sargunster
  * **Java (Spring Boot) with auto caching** : [pokeapi-reactor](https://github.com/SirSkaro/pokeapi-reactor) by Benjamin Churchill
  * **.NET (C#, VB, etc)** : [PokeApi.NET](https://gitlab.com/PoroCYon/PokeApi.NET) by PoroCYon
  * **.NET Standard** : [PokeApiNet](https://github.com/mtrdp642/PokeApiNet) by mtrdp642
  * **Swift** : [PokemonAPI](https://github.com/kinkofer/PokemonAPI) by kinkofer
  * **PHP** : [PokePHP](https://github.com/danrovito/pokephp) by Dan Rovito
  * **PHP** : [PHPokéAPI](https://github.com/lmerotta/phpokeapi) by lmerotta
  * **Ruby** : [Poke-Api-V2](https://github.com/rdavid1099/poke-api-v2) by rdavid1099
  * **Go** : [pokeapi-go](https://github.com/mtslzr/pokeapi-go) by mtslzr
  * **Go** : [PokeGo](https://github.com/JoshGuarino/PokeGo) by Josh Guarino
  * **Crystal** : [pokeapi](https://github.com/henrikac/pokeapi) by henrikac
  * **Typescript with auto caching** : [Pokenode-ts](https://github.com/Gabb-c/pokenode-ts) by Gabb-c
  * **Rust with auto caching** : [Rustemon](https://crates.io/crates/rustemon) by mlemesle
  * **Asynchronous Python wrapper with auto caching** : [aiopokeapi](https://github.com/beastmatser/aiopokeapi) by beastmatser
  * **Scala 3 with auto caching** : [pokeapi-scala](https://github.com/juliano/pokeapi-scala) by Juliano Alves
  * **Elixir wrapper with auto caching** : [Max-Elixir-PokeAPI](https://github.com/HenriqueArtur/Max-Elixir-PokeAPI) by Henrique Artur

## Resource Lists/Pagination (group)

Calling any API endpoint without a resource ID or name will return a paginated list of available resources for that API. By default, a list "page" will contain up to 20 resources. If you would like to change this just add a 'limit' query parameter to the GET request, e.g. `?limit=60`. You can use 'offset' to move to the next page, e.g. `?limit=60&offset=60`. `characteristic`, `contest-effect`, `evolution-chain`, `machine`, `super-contest-effect` endpoints are unnamed, the rest are named.

### Named (endpoint)

GET https://pokeapi.co/api/v2/{endpoint}/
    
    {
      "count": 248,
      "next": "https://pokeapi.co/api/v2/ability/?limit=20&offset=20",
      "previous": null,
      "results": [
        {
          "name": "stench",
          "url": "https://pokeapi.co/api/v2/ability/1/"
        }
      ]
    }

View raw JSON (0.213 kB, 11 lines)

#### NamedAPIResourceList (type)

Name| Description| Type  
---|---|---  
count| The total number of resources available from this API. | _integer_  
next| The URL for the next page in the list. | _string_  
previous| The URL for the previous page in the list. | _string_  
results| A list of named API resources. | list _NamedAPIResource_  
  
### Unnamed (endpoint)

GET https://pokeapi.co/api/v2/{endpoint}/
    
    {
      "count": 541,
      "next": "https://pokeapi.co/api/v2/evolution-chain?offset=20&limit=20",
      "previous": null,
      "results": [
        {
          "url": "https://pokeapi.co/api/v2/evolution-chain/1/"
        }
      ]
    }

View raw JSON (0.204 kB, 10 lines)

#### APIResourceList (type)

Name| Description| Type  
---|---|---  
count| The total number of resources available from this API. | _integer_  
next| The URL for the next page in the list. | _string_  
previous| The URL for the previous page in the list. | _string_  
results| A list of unnamed API resources. | list _APIResource_  
  
## Berries (group)

### Berries (endpoint)

Berries are small fruits that can provide HP and status condition restoration, stat enhancement, and even damage negation when eaten by Pokémon. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Berry) for greater detail.

GET https://pokeapi.co/api/v2/berry/{id or name}/
    
    {
      "id": 1,
      "name": "cheri",
      "growth_time": 3,
      "max_harvest": 5,
      "natural_gift_power": 60,
      "size": 20,
      "smoothness": 25,
      "soil_dryness": 15,
      "firmness": {
        "name": "soft",
        "url": "https://pokeapi.co/api/v2/berry-firmness/2/"
      },
      "flavors": [
        {
          "potency": 10,
          "flavor": {
            "name": "spicy",
            "url": "https://pokeapi.co/api/v2/berry-flavor/1/"
          }
        }
      ],
      "item": {
        "name": "cheri-berry",
        "url": "https://pokeapi.co/api/v2/item/126/"
      },
      "natural_gift_type": {
        "name": "fire",
        "url": "https://pokeapi.co/api/v2/type/10/"
      }
    }

View raw JSON (0.608 kB, 31 lines)

#### Berry (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
growth_time| Time it takes the tree to grow one stage, in hours. Berry trees go through four of these growth stages before they can be picked. | _integer_  
max_harvest| The maximum number of these berries that can grow on one tree in Generation IV. | _integer_  
natural_gift_power| The power of the move "Natural Gift" when used with this Berry. | _integer_  
size| The size of this Berry, in millimeters. | _integer_  
smoothness| The smoothness of this Berry, used in making Pokéblocks or Poffins. | _integer_  
soil_dryness| The speed at which this Berry dries out the soil as it grows. A higher rate means the soil dries more quickly. | _integer_  
firmness| The firmness of this berry, used in making Pokéblocks or Poffins. | _NamedAPIResource_ (_BerryFirmness_)  
flavors| A list of references to each flavor a berry can have and the potency of each of those flavors in regard to this berry. | list _BerryFlavorMap_  
item| Berries are actually items. This is a reference to the item specific data for this berry. | _NamedAPIResource_ (_Item_)  
natural_gift_type| The type inherited by "Natural Gift" when used with this Berry. | _NamedAPIResource_ (_Type_)  
  
#### BerryFlavorMap (type)

Name| Description| Type  
---|---|---  
potency| How powerful the referenced flavor is for this berry. | _integer_  
flavor| The referenced berry flavor. | _NamedAPIResource_ (_BerryFlavor_)  
  
### Berry Firmnesses (endpoint)

Berries can be soft or hard. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Category:Berries_by_firmness) for greater detail.

GET https://pokeapi.co/api/v2/berry-firmness/{id or name}/
    
    {
      "id": 1,
      "name": "very-soft",
      "berries": [
        {
          "name": "pecha",
          "url": "https://pokeapi.co/api/v2/berry/3/"
        }
      ],
      "names": [
        {
          "name": "Very Soft",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ]
    }

View raw JSON (0.303 kB, 19 lines)

#### BerryFirmness (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
berries| A list of the berries with this firmness. | list __NamedAPIResource_ (_Berry_)_  
names| The name of this resource listed in different languages. | list _Name_  
  
### Berry Flavors (endpoint)

Flavors determine whether a Pokémon will benefit or suffer from eating a berry based on their nature. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Flavor) for greater detail.

GET https://pokeapi.co/api/v2/berry-flavor/{id or name}/
    
    {
      "id": 1,
      "name": "spicy",
      "berries": [
        {
          "potency": 10,
          "berry": {
            "name": "rowap",
            "url": "https://pokeapi.co/api/v2/berry/64/"
          }
        }
      ],
      "contest_type": {
        "name": "cool",
        "url": "https://pokeapi.co/api/v2/contest-type/1/"
      },
      "names": [
        {
          "name": "Spicy",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ]
    }

View raw JSON (0.446 kB, 26 lines)

#### BerryFlavor (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
berries| A list of the berries with this flavor. | list _FlavorBerryMap_  
contest_type| The contest type that correlates with this berry flavor. | _NamedAPIResource_ (_ContestType_)  
names| The name of this resource listed in different languages. | list _Name_  
  
#### FlavorBerryMap (type)

Name| Description| Type  
---|---|---  
potency| How powerful the referenced flavor is for this berry. | _integer_  
berry| The berry with the referenced flavor. | _NamedAPIResource_ (_Berry_)  
  
## Contests (group)

### Contest Types (endpoint)

Contest types are categories judges used to weigh a Pokémon's condition in Pokémon contests. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Contest_condition) for greater detail.

GET https://pokeapi.co/api/v2/contest-type/{id or name}/
    
    {
      "id": 1,
      "name": "cool",
      "berry_flavor": {
        "name": "spicy",
        "url": "https://pokeapi.co/api/v2/berry-flavor/1/"
      },
      "names": [
        {
          "name": "Cool",
          "color": "Red",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ]
    }

View raw JSON (0.311 kB, 18 lines)

#### ContestType (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
berry_flavor| The berry flavor that correlates with this contest type. | _NamedAPIResource_ (_BerryFlavor_)  
names| The name of this contest type listed in different languages. | list _ContestName_  
  
#### ContestName (type)

Name| Description| Type  
---|---|---  
name| The name for this contest. | _string_  
color| The color associated with this contest's name. | _string_  
language| The language that this name is in. | _NamedAPIResource_ (_Language_)  
  
### Contest Effects (endpoint)

Contest effects refer to the effects of moves when used in contests.

GET https://pokeapi.co/api/v2/contest-effect/{id}/
    
    {
      "id": 1,
      "appeal": 4,
      "jam": 0,
      "effect_entries": [
        {
          "effect": "Gives a high number of appeal points wth no other effects.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ],
      "flavor_text_entries": [
        {
          "flavor_text": "A highly appealing move.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ]
    }

View raw JSON (0.46 kB, 23 lines)

#### ContestEffect (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
appeal| The base number of hearts the user of this move gets. | _integer_  
jam| The base number of hearts the user's opponent loses. | _integer_  
effect_entries| The result of this contest effect listed in different languages. | list _Effect_  
flavor_text_entries| The flavor text of this contest effect listed in different languages. | list _FlavorText_  
  
### Super Contest Effects (endpoint)

Super contest effects refer to the effects of moves when used in super contests.

GET https://pokeapi.co/api/v2/super-contest-effect/{id}/
    
    {
      "id": 1,
      "appeal": 2,
      "flavor_text_entries": [
        {
          "flavor_text": "Enables the user to perform first in the next turn.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ],
      "moves": [
        {
          "name": "agility",
          "url": "https://pokeapi.co/api/v2/move/97/"
        }
      ]
    }

View raw JSON (0.358 kB, 19 lines)

#### SuperContestEffect (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
appeal| The level of appeal this super contest effect has. | _integer_  
flavor_text_entries| The flavor text of this super contest effect listed in different languages. | list _FlavorText_  
moves| A list of moves that have the effect when used in super contests. | list __NamedAPIResource_ (_Move_)_  
  
## Encounters (group)

### Encounter Methods (endpoint)

Methods by which the player might can encounter Pokémon in the wild, e.g., walking in tall grass. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Wild_Pok%C3%A9mon) for greater detail.

GET https://pokeapi.co/api/v2/encounter-method/{id or name}/
    
    {
      "id": 1,
      "name": "walk",
      "order": 1,
      "names": [
        {
          "name": "Walking in tall grass or a cave",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ]
    }

View raw JSON (0.229 kB, 14 lines)

#### EncounterMethod (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
order| A good value for sorting. | _integer_  
names| The name of this resource listed in different languages. | list _Name_  
  
### Encounter Conditions (endpoint)

Conditions which affect what pokemon might appear in the wild, e.g., day or night.

GET https://pokeapi.co/api/v2/encounter-condition/{id or name}/
    
    {
      "id": 1,
      "name": "swarm",
      "values": [
        {
          "name": "swarm-yes",
          "url": "https://pokeapi.co/api/v2/encounter-condition-value/1/"
        },
        {
          "name": "swarm-no",
          "url": "https://pokeapi.co/api/v2/encounter-condition-value/2/"
        }
      ],
      "names": [
        {
          "name": "Schwarm",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        }
      ]
    }

View raw JSON (0.429 kB, 23 lines)

#### EncounterCondition (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
names| The name of this resource listed in different languages. | list _Name_  
values| A list of possible values for this encounter condition. | list __NamedAPIResource_ (_EncounterConditionValue_)_  
  
### Encounter Condition Values (endpoint)

Encounter condition values are the various states that an encounter condition can have, i.e., time of day can be either day or night.

GET https://pokeapi.co/api/v2/encounter-condition-value/{id or name}/
    
    {
      "id": 1,
      "name": "swarm-yes",
      "condition": {
        "name": "swarm",
        "url": "https://pokeapi.co/api/v2/encounter-condition/1/"
      },
      "names": [
        {
          "name": "WÃ¤hrend eines Schwarms",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        }
      ]
    }

View raw JSON (0.319 kB, 17 lines)

#### EncounterConditionValue (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
condition| The condition this encounter condition value pertains to. | _NamedAPIResource_ (_EncounterCondition_)  
names| The name of this resource listed in different languages. | list _Name_  
  
## Evolution (group)

### Evolution Chains (endpoint)

Evolution chains are essentially family trees. They start with the lowest stage within a family and detail evolution conditions for each as well as Pokémon they can evolve into up through the hierarchy.

GET https://pokeapi.co/api/v2/evolution-chain/{id}/
    
    {
      "id": 7,
      "baby_trigger_item": null,
      "chain": {
        "is_baby": false,
        "species": {
          "name": "rattata",
          "url": "https://pokeapi.co/api/v2/pokemon-species/19/"
        },
        "evolution_details": null,
        "evolves_to": [
          {
            "is_baby": false,
            "species": {
              "name": "raticate",
              "url": "https://pokeapi.co/api/v2/pokemon-species/20/"
            },
            "evolution_details": [
              {
                "item": null,
                "trigger": {
                  "name": "level-up",
                  "url": "https://pokeapi.co/api/v2/evolution-trigger/1/"
                },
                "gender": null,
                "held_item": null,
                "known_move": null,
                "known_move_type": null,
                "location": null,
                "min_level": 20,
                "min_happiness": null,
                "min_beauty": null,
                "min_affection": null,
                "needs_overworld_rain": false,
                "party_species": null,
                "party_type": null,
                "relative_physical_stats": null,
                "time_of_day": "",
                "trade_species": null,
                "turn_upside_down": false
              }
            ],
            "evolves_to": []
          }
        ]
      }
    }

View raw JSON (1.227 kB, 47 lines)

#### EvolutionChain (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
baby_trigger_item| The item that a Pokémon would be holding when mating that would trigger the egg hatching a baby Pokémon rather than a basic Pokémon. | _NamedAPIResource_ (_Item_)  
chain| The base chain link object. Each link contains evolution details for a Pokémon in the chain. Each link references the next Pokémon in the natural evolution order. | ChainLink  
  
#### ChainLink (type)

Name| Description| Type  
---|---|---  
is_baby| Whether or not this link is for a baby Pokémon. This would only ever be true on the base link. | _boolean_  
species| The Pokémon species at this point in the evolution chain. | _NamedAPIResource_ (_PokemonSpecies_)  
evolution_details| All details regarding the specific details of the referenced Pokémon species evolution. | list _EvolutionDetail_  
evolves_to| A List of chain objects. | list _ChainLink_  
  
#### EvolutionDetail (type)

Name| Description| Type  
---|---|---  
item| The item required to cause evolution this into Pokémon species. | _NamedAPIResource_ (_Item_)  
trigger| The type of event that triggers evolution into this Pokémon species. | _NamedAPIResource_ (_EvolutionTrigger_)  
gender| The id of the gender of the evolving Pokémon species must be in order to evolve into this Pokémon species. | _integer_  
held_item| The item the evolving Pokémon species must be holding during the evolution trigger event to evolve into this Pokémon species. | _NamedAPIResource_ (_Item_)  
known_move| The move that must be known by the evolving Pokémon species during the evolution trigger event in order to evolve into this Pokémon species. | _NamedAPIResource_ (_Move_)  
known_move_type| The evolving Pokémon species must know a move with this type during the evolution trigger event in order to evolve into this Pokémon species. | _NamedAPIResource_ (_Type_)  
location| The location the evolution must be triggered at. | _NamedAPIResource_ (_Location_)  
min_level| The minimum required level of the evolving Pokémon species to evolve into this Pokémon species. | _integer_  
min_happiness| The minimum required level of happiness the evolving Pokémon species to evolve into this Pokémon species. | _integer_  
min_beauty| The minimum required level of beauty the evolving Pokémon species to evolve into this Pokémon species. | _integer_  
min_affection| The minimum required level of affection the evolving Pokémon species to evolve into this Pokémon species. | _integer_  
needs_overworld_rain| Whether or not it must be raining in the overworld to cause evolution this Pokémon species. | _boolean_  
party_species| The Pokémon species that must be in the players party in order for the evolving Pokémon species to evolve into this Pokémon species. | _NamedAPIResource_ (_PokemonSpecies_)  
party_type| The player must have a Pokémon of this type in their party during the evolution trigger event in order for the evolving Pokémon species to evolve into this Pokémon species. | _NamedAPIResource_ (_Type_)  
relative_physical_stats| The required relation between the Pokémon's Attack and Defense stats. 1 means Attack > Defense. 0 means Attack = Defense. -1 means Attack < Defense. | _integer_  
time_of_day| The required time of day. Day or night. | _string_  
trade_species| Pokémon species for which this one must be traded. | _NamedAPIResource_ (_PokemonSpecies_)  
turn_upside_down| Whether or not the 3DS needs to be turned upside-down as this Pokémon levels up. | _boolean_  
  
### Evolution Triggers (endpoint)

Evolution triggers are the events and conditions that cause a Pokémon to evolve. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Methods_of_evolution) for greater detail.

GET https://pokeapi.co/api/v2/evolution-trigger/{id or name}/
    
    {
      "id": 1,
      "name": "level-up",
      "names": [
        {
          "name": "Level up",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ],
      "pokemon_species": [
        {
          "name": "ivysaur",
          "url": "https://pokeapi.co/api/v2/pokemon-species/2/"
        }
      ]
    }

View raw JSON (0.321 kB, 19 lines)

#### EvolutionTrigger (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
names| The name of this resource listed in different languages. | list _Name_  
pokemon_species| A list of pokemon species that result from this evolution trigger. | list __NamedAPIResource_ (_PokemonSpecies_)_  
  
## Games (group)

### Generations (endpoint)

A generation is a grouping of the Pokémon games that separates them based on the Pokémon they include. In each generation, a new set of Pokémon, Moves, Abilities and Types that did not exist in the previous generation are released.

GET https://pokeapi.co/api/v2/generation/{id or name}/
    
    {
      "id": 1,
      "name": "generation-i",
      "abilities": [],
      "main_region": {
        "name": "kanto",
        "url": "https://pokeapi.co/api/v2/region/1/"
      },
      "moves": [
        {
          "name": "pound",
          "url": "https://pokeapi.co/api/v2/move/1/"
        }
      ],
      "names": [
        {
          "name": "Generation I",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        }
      ],
      "pokemon_species": [
        {
          "name": "bulbasaur",
          "url": "https://pokeapi.co/api/v2/pokemon-species/1/"
        }
      ],
      "types": [
        {
          "name": "normal",
          "url": "https://pokeapi.co/api/v2/type/1/"
        }
      ],
      "version_groups": [
        {
          "name": "red-blue",
          "url": "https://pokeapi.co/api/v2/version-group/1/"
        }
      ]
    }

View raw JSON (0.772 kB, 42 lines)

#### Generation (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
abilities| A list of abilities that were introduced in this generation. | list __NamedAPIResource_ (_Ability_)_  
names| The name of this resource listed in different languages. | list _Name_  
main_region| The main region travelled in this generation. | _NamedAPIResource_ (_Region_)  
moves| A list of moves that were introduced in this generation. | list __NamedAPIResource_ (_Move_)_  
pokemon_species| A list of Pokémon species that were introduced in this generation. | list __NamedAPIResource_ (_PokemonSpecies_)_  
types| A list of types that were introduced in this generation. | list __NamedAPIResource_ (_Type_)_  
version_groups| A list of version groups that were introduced in this generation. | list __NamedAPIResource_ (_VersionGroup_)_  
  
### Pokedexes (endpoint)

A Pokédex is a handheld electronic encyclopedia device; one which is capable of recording and retaining information of the various Pokémon in a given region with the exception of the national dex and some smaller dexes related to portions of a region. See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Pokedex) for greater detail.

GET https://pokeapi.co/api/v2/pokedex/{id or name}/
    
    {
      "id": 2,
      "name": "kanto",
      "is_main_series": true,
      "descriptions": [
        {
          "description": "Rot/Blau/Gelb Kanto Dex",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        }
      ],
      "names": [
        {
          "name": "Kanto",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        }
      ],
      "pokemon_entries": [
        {
          "entry_number": 1,
          "pokemon_species": {
            "name": "bulbasaur",
            "url": "https://pokeapi.co/api/v2/pokemon-species/1/"
          }
        }
      ],
      "region": {
        "name": "kanto",
        "url": "https://pokeapi.co/api/v2/region/1/"
      },
      "version_groups": [
        {
          "name": "red-blue",
          "url": "https://pokeapi.co/api/v2/version-group/1/"
        }
      ]
    }

View raw JSON (0.809 kB, 42 lines)

#### Pokedex (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
is_main_series| Whether or not this Pokédex originated in the main series of the video games. | _boolean_  
descriptions| The description of this resource listed in different languages. | list _Description_  
names| The name of this resource listed in different languages. | list _Name_  
pokemon_entries| A list of Pokémon catalogued in this Pokédex and their indexes. | list _PokemonEntry_  
region| The region this Pokédex catalogues Pokémon for. | _NamedAPIResource_ (_Region_)  
version_groups| A list of version groups this Pokédex is relevant to. | list __NamedAPIResource_ (_VersionGroup_)_  
  
#### PokemonEntry (type)

Name| Description| Type  
---|---|---  
entry_number| The index of this Pokémon species entry within the Pokédex. | _integer_  
pokemon_species| The Pokémon species being encountered. | _NamedAPIResource_ (_PokemonSpecies_)  
  
### Version (endpoint)

Versions of the games, e.g., Red, Blue or Yellow.

GET https://pokeapi.co/api/v2/version/{id or name}/
    
    {
      "id": 1,
      "name": "red",
      "names": [
        {
          "name": "Rot",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        }
      ],
      "version_group": {
        "name": "red-blue",
        "url": "https://pokeapi.co/api/v2/version-group/1/"
      }
    }

View raw JSON (0.292 kB, 17 lines)

#### Version (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
names| The name of this resource listed in different languages. | list _Name_  
version_group| The version group this version belongs to. | _NamedAPIResource_ (_VersionGroup_)  
  
### Version Groups (endpoint)

Version groups categorize highly similar versions of the games.

GET https://pokeapi.co/api/v2/version-group/{id or name}/
    
    {
      "id": 1,
      "name": "red-blue",
      "order": 1,
      "generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
      },
      "move_learn_methods": [
        {
          "name": "level-up",
          "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
        }
      ],
      "pokedexes": [
        {
          "name": "kanto",
          "url": "https://pokeapi.co/api/v2/pokedex/2/"
        }
      ],
      "regions": [
        {
          "name": "kanto",
          "url": "https://pokeapi.co/api/v2/region/1/"
        }
      ],
      "versions": [
        {
          "name": "red",
          "url": "https://pokeapi.co/api/v2/version/1/"
        }
      ]
    }

View raw JSON (0.605 kB, 33 lines)

#### VersionGroup (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
order| Order for sorting. Almost by date of release, except similar versions are grouped together. | _integer_  
generation| The generation this version was introduced in. | _NamedAPIResource_ (_Generation_)  
move_learn_methods| A list of methods in which Pokémon can learn moves in this version group. | list __NamedAPIResource_ (_MoveLearnMethod_)_  
pokedexes| A list of Pokédexes introduces in this version group. | list __NamedAPIResource_ (_Pokedex_)_  
regions| A list of regions that can be visited in this version group. | list __NamedAPIResource_ (_Region_)_  
versions| The versions this version group owns. | list __NamedAPIResource_ (_Version_)_  
  
## Items (group)

### Item (endpoint)

An item is an object in the games which the player can pick up, keep in their bag, and use in some manner. They have various uses, including healing, powering up, helping catch Pokémon, or to access a new area.

GET https://pokeapi.co/api/v2/item/{id or name}/
    
    {
      "id": 1,
      "name": "master-ball",
      "cost": 0,
      "fling_power": 10,
      "fling_effect": {
        "name": "flinch",
        "url": "https://pokeapi.co/api/v2/item-fling-effect/7/"
      },
      "attributes": [
        {
          "name": "holdable",
          "url": "https://pokeapi.co/api/v2/item-attribute/5/"
        }
      ],
      "category": {
        "name": "standard-balls",
        "url": "https://pokeapi.co/api/v2/item-category/34/"
      },
      "effect_entries": [
        {
          "effect": "Used in battle\n:   [Catches]{mechanic:catch} a wild Pokémon without fail.\n\n    If used in a trainer battle, nothing happens and the ball is lost.",
          "short_effect": "Catches a wild Pokémon every time.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ],
      "flavor_text_entries": [
        {
          "text": "The best Poké Ball with the ultimate level of performance. With it, you will catch any wild Pokémon without fail.",
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          },
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ],
      "game_indices": [
        {
          "game_index": 1,
          "generation": {
            "name": "generation-vi",
            "url": "https://pokeapi.co/api/v2/generation/6/"
          }
        }
      ],
      "names": [
        {
          "name": "Master Ball",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ],
      "sprites": {
        "default": "https://pokeapi.co/media/sprites/items/master-ball.png"
      },
      "held_by_pokemon": [
        {
          "pokemon": {
            "name": "chansey",
            "url": "https://pokeapi.co/api/v2/pokemon/113/"
          },
          "version_details": [
            {
              "rarity": 50,
              "version": {
                "name": "soulsilver",
                "url": "https://pokeapi.co/api/v2/version/16/"
              }
            }
          ]
        }
      ],
      "baby_trigger_for": {
        "url": "https://pokeapi.co/api/v2/evolution-chain/1/"
      }
    }

View raw JSON (2.062 kB, 84 lines)

#### Item (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
cost| The price of this item in stores. | _integer_  
fling_power| The power of the move Fling when used with this item. | _integer_  
fling_effect| The effect of the move Fling when used with this item. | _NamedAPIResource_ (_ItemFlingEffect_)  
attributes| A list of attributes this item has. | list __NamedAPIResource_ (_ItemAttribute_)_  
category| The category of items this item falls into. | _NamedAPIResource_ (_ItemCategory_)  
effect_entries| The effect of this ability listed in different languages. | list _VerboseEffect_  
flavor_text_entries| The flavor text of this ability listed in different languages. | list _VersionGroupFlavorText_  
game_indices| A list of game indices relevent to this item by generation. | list _GenerationGameIndex_  
names| The name of this item listed in different languages. | list _Name_  
sprites| A set of sprites used to depict this item in the game. | ItemSprites  
held_by_pokemon| A list of Pokémon that might be found in the wild holding this item. | list _ItemHolderPokemon_  
baby_trigger_for| An evolution chain this item requires to produce a bay during mating. | _APIResource_ (_EvolutionChain_)  
machines| A list of the machines related to this item. | list _MachineVersionDetail_  
  
#### ItemSprites (type)

Name| Description| Type  
---|---|---  
default| The default depiction of this item. | _string_  
  
#### ItemHolderPokemon (type)

Name| Description| Type  
---|---|---  
pokemon| The Pokémon that holds this item. | _NamedAPIResource_ (_Pokemon_)  
version_details| The details for the version that this item is held in by the Pokémon. | list _ItemHolderPokemonVersionDetail_  
  
#### ItemHolderPokemonVersionDetail (type)

Name| Description| Type  
---|---|---  
rarity| How often this Pokémon holds this item in this version. | _integer_  
version| The version that this item is held in by the Pokémon. | _NamedAPIResource_ (_Version_)  
  
### Item Attributes (endpoint)

Item attributes define particular aspects of items, e.g. "usable in battle" or "consumable".

GET https://pokeapi.co/api/v2/item-attribute/{id or name}/
    
    {
      "id": 1,
      "name": "countable",
      "descriptions": [
        {
          "description": "Has a count in the bag",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ],
      "items": [
        {
          "name": "master-ball",
          "url": "https://pokeapi.co/api/v2/item/1/"
        }
      ],
      "names": [
        {
          "name": "Countable",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ]
    }

View raw JSON (0.495 kB, 28 lines)

#### ItemAttribute (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
items| A list of items that have this attribute. | list __NamedAPIResource_ (_Item_)_  
names| The name of this item attribute listed in different languages. | list _Name_  
descriptions| The description of this item attribute listed in different languages. | list _Description_  
  
### Item Categories (endpoint)

Item categories determine where items will be placed in the players bag.

GET https://pokeapi.co/api/v2/item-category/{id or name}/
    
    {
      "id": 1,
      "name": "stat-boosts",
      "items": [
        {
          "name": "guard-spec",
          "url": "https://pokeapi.co/api/v2/item/55/"
        }
      ],
      "names": [
        {
          "name": "Stat boosts",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ],
      "pocket": {
        "name": "battle",
        "url": "https://pokeapi.co/api/v2/item-pocket/7/"
      }
    }

View raw JSON (0.405 kB, 23 lines)

#### ItemCategory (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
items| A list of items that are a part of this category. | list __NamedAPIResource_ (_Item_)_  
names| The name of this item category listed in different languages. | list _Name_  
pocket| The pocket items in this category would be put in. | _NamedAPIResource_ (_ItemPocket_)  
  
### Item Fling Effects (endpoint)

The various effects of the move "Fling" when used with different items.

GET https://pokeapi.co/api/v2/item-fling-effect/{id or name}/
    
    {
      "id": 1,
      "name": "badly-poison",
      "effect_entries": [
        {
          "effect": "Badly poisons the target.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ],
      "items": [
        {
          "name": "toxic-orb",
          "url": "https://pokeapi.co/api/v2/item/249/"
        }
      ]
    }

View raw JSON (0.336 kB, 19 lines)

#### ItemFlingEffect (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
effect_entries| The result of this fling effect listed in different languages. | list _Effect_  
items| A list of items that have this fling effect. | list __NamedAPIResource_ (_Item_)_  
  
### Item Pockets (endpoint)

Pockets within the players bag used for storing items by category.

GET https://pokeapi.co/api/v2/item-pocket/{id or name}/
    
    {
      "id": 1,
      "name": "misc",
      "categories": [
        {
          "name": "collectibles",
          "url": "https://pokeapi.co/api/v2/item-category/9/"
        }
      ],
      "names": [
        {
          "name": "Items",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ]
    }

View raw JSON (0.312 kB, 19 lines)

#### ItemPocket (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
categories| A list of item categories that are relevant to this item pocket. | list __NamedAPIResource_ (_ItemCategory_)_  
names| The name of this resource listed in different languages. | list _Name_  
  
## Locations (group)

### Locations (endpoint)

Locations that can be visited within the games. Locations make up sizable portions of regions, like cities or routes.

GET https://pokeapi.co/api/v2/location/{id or name}/
    
    {
      "id": 1,
      "name": "canalave-city",
      "region": {
        "name": "sinnoh",
        "url": "https://pokeapi.co/api/v2/region/4/"
      },
      "names": [
        {
          "name": "Canalave City",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ],
      "game_indices": [
        {
          "game_index": 7,
          "generation": {
            "name": "generation-iv",
            "url": "https://pokeapi.co/api/v2/generation/4/"
          }
        }
      ],
      "areas": [
        {
          "name": "canalave-city-area",
          "url": "https://pokeapi.co/api/v2/location-area/1/"
        }
      ]
    }

View raw JSON (0.6 kB, 32 lines)

#### Location (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
region| The region this location can be found in. | _NamedAPIResource _ (_Region_)  
names| The name of this resource listed in different languages. | list _Name_  
game_indices| A list of game indices relevent to this location by generation. | list _GenerationGameIndex_  
areas| Areas that can be found within this location. | list __NamedAPIResource_ (_LocationArea_)_  
  
### Location Areas (endpoint)

Location areas are sections of areas, such as floors in a building or cave. Each area has its own set of possible Pokémon encounters.

GET https://pokeapi.co/api/v2/location-area/{id or name}/
    
    {
      "id": 1,
      "name": "canalave-city-area",
      "game_index": 1,
      "encounter_method_rates": [
        {
          "encounter_method": {
            "name": "old-rod",
            "url": "https://pokeapi.co/api/v2/encounter-method/2/"
          },
          "version_details": [
            {
              "rate": 25,
              "version": {
                "name": "platinum",
                "url": "https://pokeapi.co/api/v2/version/14/"
              }
            }
          ]
        }
      ],
      "location": {
        "name": "canalave-city",
        "url": "https://pokeapi.co/api/v2/location/1/"
      },
      "names": [
        {
          "name": "",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ],
      "pokemon_encounters": [
        {
          "pokemon": {
            "name": "tentacool",
            "url": "https://pokeapi.co/api/v2/pokemon/72/"
          },
          "version_details": [
            {
              "version": {
                "name": "diamond",
                "url": "https://pokeapi.co/api/v2/version/12/"
              },
              "max_chance": 60,
              "encounter_details": [
                {
                  "min_level": 20,
                  "max_level": 30,
                  "condition_values": [],
                  "chance": 60,
                  "method": {
                    "name": "surf",
                    "url": "https://pokeapi.co/api/v2/encounter-method/5/"
                  }
                }
              ]
            }
          ]
        }
      ]
    }

View raw JSON (1.405 kB, 64 lines)

#### LocationArea (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
game_index| The internal id of an API resource within game data. | _integer_  
encounter_method_rates| A list of methods in which Pokémon may be encountered in this area and how likely the method will occur depending on the version of the game. | list _EncounterMethodRate_  
location| The region this location area can be found in. | _NamedAPIResource_ (_Location_)  
names| The name of this resource listed in different languages. | list _Name_  
pokemon_encounters| A list of Pokémon that can be encountered in this area along with version specific details about the encounter. | list _PokemonEncounter_  
  
#### EncounterMethodRate (type)

Name| Description| Type  
---|---|---  
encounter_method| The method in which Pokémon may be encountered in an area.. | _NamedAPIResource _ (_EncounterMethod_)  
version_details| The chance of the encounter to occur on a version of the game. | list _EncounterVersionDetails_  
  
#### EncounterVersionDetails (type)

Name| Description| Type  
---|---|---  
rate| The chance of an encounter to occur. | _integer_  
version| The version of the game in which the encounter can occur with the given chance. | _NamedAPIResource _ (_Version_)  
  
#### PokemonEncounter (type)

Name| Description| Type  
---|---|---  
pokemon| The Pokémon being encountered. | _NamedAPIResource _ (_Pokemon_)  
version_details| A list of versions and encounters with Pokémon that might happen in the referenced location area. | list _VersionEncounterDetail_  
  
### Pal Park Areas (endpoint)

Areas used for grouping Pokémon encounters in Pal Park. They're like habitats that are specific to [Pal Park](https://bulbapedia.bulbagarden.net/wiki/Pal_Park).

GET https://pokeapi.co/api/v2/pal-park-area/{id or name}/
    
    {
      "id": 1,
      "name": "forest",
      "names": [
        {
          "name": "Forest",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ],
      "pokemon_encounters": [
        {
          "base_score": 30,
          "rate": 50,
          "pokemon_species": {
            "name": "caterpie",
            "url": "https://pokeapi.co/api/v2/pokemon-species/10/"
          }
        }
      ]
    }

View raw JSON (0.403 kB, 23 lines)

#### PalParkArea (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
names| The name of this resource listed in different languages. | list _Name_  
pokemon_encounters| A list of Pokémon encountered in thi pal park area along with details. | list _PalParkEncounterSpecies_  
  
#### PalParkEncounterSpecies (type)

Name| Description| Type  
---|---|---  
base_score| The base score given to the player when this Pokémon is caught during a pal park run. | _integer_  
rate| The base rate for encountering this Pokémon in this pal park area. | _integer_  
pokemon_species| The Pokémon species being encountered. | _NamedAPIResource _ (_PokemonSpecies_)  
  
### Regions (endpoint)

A region is an organized area of the Pokémon world. Most often, the main difference between regions is the species of Pokémon that can be encountered within them.

GET https://pokeapi.co/api/v2/region/{id or name}/
    
    {
      "id": 1,
      "name": "kanto",
      "locations": [
        {
          "name": "celadon-city",
          "url": "https://pokeapi.co/api/v2/location/67/"
        }
      ],
      "main_generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
      },
      "names": [
        {
          "name": "Kanto",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        }
      ],
      "pokedexes": [
        {
          "name": "kanto",
          "url": "https://pokeapi.co/api/v2/pokedex/2/"
        }
      ],
      "version_groups": [
        {
          "name": "red-blue",
          "url": "https://pokeapi.co/api/v2/version-group/1/"
        }
      ]
    }

View raw JSON (0.649 kB, 35 lines)

#### Region (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
locations| A list of locations that can be found in this region. | list __NamedAPIResource_ (_Location_)_  
name| The name for this resource. | _string_  
names| The name of this resource listed in different languages. | list _Name_  
main_generation| The generation this region was introduced in. | _NamedAPIResource _ (_Generation_)  
pokedexes| A list of pokédexes that catalogue Pokémon in this region. | list __NamedAPIResource_ (_Pokedex_)_  
version_groups| A list of version groups where this region can be visited. | list __NamedAPIResource_ (_VersionGroup_)_  
  
## Machines (group)

### Machines (endpoint)

Machines are the representation of items that teach moves to Pokémon. They vary from version to version, so it is not certain that one specific TM or HM corresponds to a single Machine.

GET https://pokeapi.co/api/v2/machine/{id}/
    
    {
      "id": 1,
      "item": {
        "name": "tm01",
        "url": "https://pokeapi.co/api/v2/item/305/"
      },
      "move": {
        "name": "mega-punch",
        "url": "https://pokeapi.co/api/v2/move/5/"
      },
      "version_group": {
        "name": "red-blue",
        "url": "https://pokeapi.co/api/v2/version/1/"
      }
    }

View raw JSON (0.289 kB, 15 lines)

#### Machine (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
item| The TM or HM item that corresponds to this machine. | _NamedAPIResource_ (_Item_)  
move| The move that is taught by this machine. | _NamedAPIResource_ (_Move_)  
version_group| The version group that this machine applies to. | _NamedAPIResource_ (_VersionGroup_)  
  
## Moves (group)

### Moves (endpoint)

Moves are the skills of Pokémon in battle. In battle, a Pokémon uses one move each turn. Some moves (including those learned by Hidden Machine) can be used outside of battle as well, usually for the purpose of removing obstacles or exploring new areas.

GET https://pokeapi.co/api/v2/move/{id or name}/
    
    {
      "id": 1,
      "name": "pound",
      "accuracy": 100,
      "effect_chance": null,
      "pp": 35,
      "priority": 0,
      "power": 40,
      "contest_combos": {
        "normal": {
          "use_before": [
            {
              "name": "double-slap",
              "url": "https://pokeapi.co/api/v2/move/3/"
            },
            {
              "name": "headbutt",
              "url": "https://pokeapi.co/api/v2/move/29/"
            },
            {
              "name": "feint-attack",
              "url": "https://pokeapi.co/api/v2/move/185/"
            }
          ],
          "use_after": null
        },
        "super": {
          "use_before": null,
          "use_after": null
        }
      },
      "contest_type": {
        "name": "tough",
        "url": "https://pokeapi.co/api/v2/contest-type/5/"
      },
      "contest_effect": {
        "url": "https://pokeapi.co/api/v2/contest-effect/1/"
      },
      "damage_class": {
        "name": "physical",
        "url": "https://pokeapi.co/api/v2/move-damage-class/2/"
      },
      "effect_entries": [
        {
          "effect": "Inflicts [regular damage]{mechanic:regular-damage}.",
          "short_effect": "Inflicts regular damage with no additional effect.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ],
      "effect_changes": [],
      "generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
      },
      "meta": {
        "ailment": {
          "name": "none",
          "url": "https://pokeapi.co/api/v2/move-ailment/0/"
        },
        "category": {
          "name": "damage",
          "url": "https://pokeapi.co/api/v2/move-category/0/"
        },
        "min_hits": null,
        "max_hits": null,
        "min_turns": null,
        "max_turns": null,
        "drain": 0,
        "healing": 0,
        "crit_rate": 0,
        "ailment_chance": 0,
        "flinch_chance": 0,
        "stat_chance": 0
      },
      "names": [
        {
          "name": "Pound",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ],
      "past_values": [],
      "stat_changes": [],
      "super_contest_effect": {
        "url": "https://pokeapi.co/api/v2/super-contest-effect/5/"
      },
      "target": {
        "name": "selected-pokemon",
        "url": "https://pokeapi.co/api/v2/move-target/10/"
      },
      "type": {
        "name": "normal",
        "url": "https://pokeapi.co/api/v2/type/1/"
      },
      "learned_by_pokemon": [
        {
          "name": "clefairy",
          "url": "https://pokeapi.co/api/v2/pokemon/35/"
        }
      ],
      "flavor_text_entries": [
        {
          "flavor_text": "Pounds with fore­\nlegs or tail.",
          "language": {
            "url": "https://pokeapi.co/api/v2/language/9/",
            "name": "en"
          },
          "version_group": {
            "url": "https://pokeapi.co/api/v2/version-group/3/",
            "name": "gold-silver"
          }
        }
      ]
    }

View raw JSON (2.714 kB, 119 lines)

#### Move (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
accuracy| The percent value of how likely this move is to be successful. | _integer_  
effect_chance| The percent value of how likely it is this moves effect will happen. | _integer_  
pp| Power points. The number of times this move can be used. | _integer_  
priority| A value between -8 and 8. Sets the order in which moves are executed during battle. See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Priority) for greater detail. | _integer_  
power| The base power of this move with a value of 0 if it does not have a base power. | _integer_  
contest_combos| A detail of normal and super contest combos that require this move. | ContestComboSets  
contest_type| The type of appeal this move gives a Pokémon when used in a contest. | _NamedAPIResource_ (_ContestType_)  
contest_effect| The effect the move has when used in a contest. | _APIResource_ (_ContestEffect_)  
damage_class| The type of damage the move inflicts on the target, e.g. physical. | _NamedAPIResource_ (_MoveDamageClass_)  
effect_entries| The effect of this move listed in different languages. | list _VerboseEffect_  
effect_changes| The list of previous effects this move has had across version groups of the games. | list _AbilityEffectChange_  
learned_by_pokemon| List of Pokemon that can learn the move | list __NamedAPIResource_ (_Pokemon_)_  
flavor_text_entries| The flavor text of this move listed in different languages. | list _MoveFlavorText_  
generation| The generation in which this move was introduced. | _NamedAPIResource _ (_Generation_)  
machines| A list of the machines that teach this move. | list _MachineVersionDetail_  
meta| Metadata about this move | MoveMetaData  
names| The name of this resource listed in different languages. | list _Name_  
past_values| A list of move resource value changes across version groups of the game. | list _PastMoveStatValues_  
stat_changes| A list of stats this moves effects and how much it effects them. | list _MoveStatChange_  
super_contest_effect| The effect the move has when used in a super contest. | _APIResource _ (_SuperContestEffect_)  
target| The type of target that will receive the effects of the attack. | _NamedAPIResource _ (_MoveTarget_)  
type| The elemental type of this move. | _NamedAPIResource _ (_Type_)  
  
#### ContestComboSets (type)

Name| Description| Type  
---|---|---  
normal| A detail of moves this move can be used before or after, granting additional appeal points in contests. | ContestComboDetail  
super| A detail of moves this move can be used before or after, granting additional appeal points in super contests. | ContestComboDetail  
  
#### ContestComboDetail (type)

Name| Description| Type  
---|---|---  
use_before| A list of moves to use before this move. | list __NamedAPIResource_ (_Move_)_  
use_after| A list of moves to use after this move. | list __NamedAPIResource_ (_Move_)_  
  
#### MoveFlavorText (type)

Name| Description| Type  
---|---|---  
flavor_text| The localized flavor text for an api resource in a specific language. | _string_  
language| The language this name is in. | _NamedAPIResource_ (_Language_)  
version_group| The version group that uses this flavor text. | _NamedAPIResource_ (_VersionGroup_)  
  
#### MoveMetaData (type)

Name| Description| Type  
---|---|---  
ailment| The status ailment this move inflicts on its target. | _NamedAPIResource _ (_MoveAilment_)  
category| The category of move this move falls under, e.g. damage or ailment. | _NamedAPIResource _ (_MoveCategory_)  
min_hits| The minimum number of times this move hits. Null if it always only hits once. | _integer_  
max_hits| The maximum number of times this move hits. Null if it always only hits once. | _integer_  
min_turns| The minimum number of turns this move continues to take effect. Null if it always only lasts one turn. | _integer_  
max_turns| The maximum number of turns this move continues to take effect. Null if it always only lasts one turn. | _integer_  
drain| HP drain (if positive) or Recoil damage (if negative), in percent of damage done. | _integer_  
healing| The amount of hp gained by the attacking Pokemon, in percent of it's maximum HP. | _integer_  
crit_rate| Critical hit rate bonus. | _integer_  
ailment_chance| The likelihood this attack will cause an ailment. | _integer_  
flinch_chance| The likelihood this attack will cause the target Pokémon to flinch. | _integer_  
stat_chance| The likelihood this attack will cause a stat change in the target Pokémon. | _integer_  
  
#### MoveStatChange (type)

Name| Description| Type  
---|---|---  
change| The amount of change. | _integer_  
stat| The stat being affected. | _NamedAPIResource _ (_Stat_)  
  
#### PastMoveStatValues (type)

Name| Description| Type  
---|---|---  
accuracy| The percent value of how likely this move is to be successful. | _integer_  
effect_chance| The percent value of how likely it is this moves effect will take effect. | _integer_  
power| The base power of this move with a value of 0 if it does not have a base power. | _integer_  
pp| Power points. The number of times this move can be used. | _integer_  
effect_entries| The effect of this move listed in different languages. | list _VerboseEffect_  
type| The elemental type of this move. | _NamedAPIResource _ (_Type_)  
version_group| The version group in which these move stat values were in effect. | _NamedAPIResource _ (_VersionGroup_)  
  
### Move Ailments (endpoint)

Move Ailments are status conditions caused by moves used during battle. See [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Status_condition) for greater detail.

GET https://pokeapi.co/api/v2/move-ailment/{id or name}/
    
    {
      "id": 1,
      "name": "paralysis",
      "moves": [
        {
          "name": "thunder-punch",
          "url": "https://pokeapi.co/api/v2/move/9/"
        }
      ],
      "names": [
        {
          "name": "Paralysis",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ]
    }

View raw JSON (0.308 kB, 19 lines)

#### MoveAilment (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
moves| A list of moves that cause this ailment. | list __NamedAPIResource_ (_Move_)_  
names| The name of this resource listed in different languages. | list _Name_  
  
### Move Battle Styles (endpoint)

Styles of moves when used in the Battle Palace. See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Battle_Frontier_\(Generation_III\)) for greater detail.

GET https://pokeapi.co/api/v2/move-battle-style/{id or name}/
    
    {
      "id": 1,
      "name": "attack",
      "names": [
        {
          "name": "Attack",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ]
    }

View raw JSON (0.192 kB, 13 lines)

#### MoveBattleStyle (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
names| The name of this resource listed in different languages. | list _Name_  
  
### Move Categories (endpoint)

Very general categories that loosely group move effects.

GET https://pokeapi.co/api/v2/move-category/{id or name}/
    
    {
      "id": 1,
      "name": "ailment",
      "descriptions": [
        {
          "description": "No damage; inflicts status ailment",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ],
      "moves": [
        {
          "name": "sing",
          "url": "https://pokeapi.co/api/v2/move/47/"
        }
      ]
    }

View raw JSON (0.337 kB, 19 lines)

#### MoveCategory (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
moves| A list of moves that fall into this category. | list __NamedAPIResource_ (_Move_)_  
descriptions| The description of this resource listed in different languages. | list _Description_  
  
### Move Damage Classes (endpoint)

Damage classes moves can have, e.g. physical, special, or non-damaging.

GET https://pokeapi.co/api/v2/move-damage-class/{id or name}/
    
    {
      "id": 1,
      "name": "status",
      "descriptions": [
        {
          "description": "ãƒ€ãƒ¡ãƒ¼ã‚¸ãªã„",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        }
      ],
      "moves": [
        {
          "name": "swords-dance",
          "url": "https://pokeapi.co/api/v2/move/14/"
        }
      ]
    }

View raw JSON (0.349 kB, 19 lines)

#### MoveDamageClass (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
descriptions| The description of this resource listed in different languages. | list _Description_  
moves| A list of moves that fall into this damage class. | list __NamedAPIResource_ (_Move_)_  
names| The name of this resource listed in different languages. | list _Name_  
  
### Move Learn Methods (endpoint)

Methods by which Pokémon can learn moves.

GET https://pokeapi.co/api/v2/move-learn-method/{id or name}/
    
    {
      "id": 1,
      "name": "level-up",
      "names": [
        {
          "name": "Level up",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        }
      ],
      "descriptions": [
        {
          "description": "Wird gelernt, wenn ein Pokémon ein bestimmtes Level erreicht.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        }
      ],
      "version_groups": [
        {
          "name": "red-blue",
          "url": "https://pokeapi.co/api/v2/version-group/1/"
        }
      ]
    }

View raw JSON (0.548 kB, 28 lines)

#### MoveLearnMethod (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
descriptions| The description of this resource listed in different languages. | list _Description_  
names| The name of this resource listed in different languages. | list _Name_  
version_groups| A list of version groups where moves can be learned through this method. | list __NamedAPIResource_ (_VersionGroup_)_  
  
### Move Targets (endpoint)

Targets moves can be directed at during battle. Targets can be Pokémon, environments or even other moves.

GET https://pokeapi.co/api/v2/move-target/{id or name}/
    
    {
      "id": 1,
      "name": "specific-move",
      "descriptions": [
        {
          "description": "Eine spezifische Fähigkeit. Wie diese Fähigkeit genutzt wird, hängt von den genutzten Fähigkeiten ab.",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        }
      ],
      "moves": [
        {
          "name": "counter",
          "url": "https://pokeapi.co/api/v2/move/68/"
        }
      ],
      "names": [
        {
          "name": "Spezifische Fähigkeit",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        }
      ]
    }

View raw JSON (0.592 kB, 28 lines)

#### MoveTarget (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
descriptions| The description of this resource listed in different languages. | list _Description_  
moves| A list of moves that that are directed at this target. | list __NamedAPIResource_ (_Move_)_  
names| The name of this resource listed in different languages. | list _Name_  
  
## Pokémon (group)

### Abilities (endpoint)

Abilities provide passive effects for Pokémon in battle or in the overworld. Pokémon have multiple possible abilities but can have only one ability at a time. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Ability) for greater detail.

GET https://pokeapi.co/api/v2/ability/{id or name}/
    
    {
      "id": 1,
      "name": "stench",
      "is_main_series": true,
      "generation": {
        "name": "generation-iii",
        "url": "https://pokeapi.co/api/v2/generation/3/"
      },
      "names": [
        {
          "name": "Stench",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ],
      "effect_entries": [
        {
          "effect": "This Pokémon's damaging moves have a 10% chance to make the target [flinch]{mechanic:flinch} with each hit if they do not already cause flinching as a secondary effect.\n\nThis ability does not stack with a held item.\n\nOverworld: The wild encounter rate is halved while this Pokémon is first in the party.",
          "short_effect": "Has a 10% chance of making target Pokémon [flinch]{mechanic:flinch} with each hit.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ],
      "effect_changes": [
        {
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          },
          "effect_entries": [
            {
              "effect": "Has no effect in battle.",
              "language": {
                "name": "en",
                "url": "https://pokeapi.co/api/v2/language/9/"
              }
            }
          ]
        }
      ],
      "flavor_text_entries": [
        {
          "flavor_text": "è‡­ãã¦ã€€ç›¸æ‰‹ãŒ\nã²ã‚‹ã‚€ã€€ã“ã¨ãŒã‚ã‚‹ã€‚",
          "language": {
            "name": "ja-kanji",
            "url": "https://pokeapi.co/api/v2/language/11/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        }
      ],
      "pokemon": [
        {
          "is_hidden": true,
          "slot": 3,
          "pokemon": {
            "name": "gloom",
            "url": "https://pokeapi.co/api/v2/pokemon/44/"
          }
        }
      ]
    }

View raw JSON (1.896 kB, 68 lines)

#### Ability (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
is_main_series| Whether or not this ability originated in the main series of the video games. | _boolean_  
generation| The generation this ability originated in. | _NamedAPIResource_ (_Generation_)  
names| The name of this resource listed in different languages. | list _Name_  
effect_entries| The effect of this ability listed in different languages. | list _VerboseEffect_  
effect_changes| The list of previous effects this ability has had across version groups. | list _AbilityEffectChange_  
flavor_text_entries| The flavor text of this ability listed in different languages. | list _AbilityFlavorText_  
pokemon| A list of Pokémon that could potentially have this ability. | list _AbilityPokemon_  
  
#### AbilityEffectChange (type)

Name| Description| Type  
---|---|---  
effect_entries| The previous effect of this ability listed in different languages. | list _Effect_  
version_group| The version group in which the previous effect of this ability originated. | _NamedAPIResource_ (_VersionGroup_)  
  
#### AbilityFlavorText (type)

Name| Description| Type  
---|---|---  
flavor_text| The localized name for an API resource in a specific language. | _string_  
language| The language this text resource is in. | _NamedAPIResource_ (_Language_)  
version_group| The version group that uses this flavor text. | _NamedAPIResource_ (_VersionGroup_)  
  
#### AbilityPokemon (type)

Name| Description| Type  
---|---|---  
is_hidden| Whether or not this a hidden ability for the referenced Pokémon. | _boolean_  
slot| Pokémon have 3 ability 'slots' which hold references to possible abilities they could have. This is the slot of this ability for the referenced pokemon. | _integer_  
pokemon| The Pokémon this ability could belong to. | _NamedAPIResource_ (_Pokemon_)  
  
### Characteristics (endpoint)

Characteristics indicate which stat contains a Pokémon's highest IV. A Pokémon's Characteristic is determined by the remainder of its highest IV divided by 5 (gene_modulo). Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Characteristic) for greater detail.

GET https://pokeapi.co/api/v2/characteristic/{id}/
    
    {
      "id": 1,
      "gene_modulo": 0,
      "possible_values": [
        0,
        5,
        10,
        15,
        20,
        25,
        30
      ],
      "highest_stat": {
        "name": "hp",
        "url": "https://pokeapi.co/api/v2/stat/1/"
      },
      "descriptions": [
        {
          "description": "Loves to eat",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ]
    }

View raw JSON (0.383 kB, 26 lines)

#### Characteristic (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
gene_modulo| The remainder of the highest stat/IV divided by 5. | _integer_  
possible_values| The possible values of the highest stat that would result in a Pokémon recieving this characteristic when divided by 5. | list __integer__  
highest_stat| The stat which results in this characteristic. | _NamedAPIResource_ (_Stat_)  
descriptions| The descriptions of this characteristic listed in different languages. | list _Description_  
  
### Egg Groups (endpoint)

Egg Groups are categories which determine which Pokémon are able to interbreed. Pokémon may belong to either one or two Egg Groups. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Egg_Group) for greater detail.

GET https://pokeapi.co/api/v2/egg-group/{id or name}/
    
    {
      "id": 1,
      "name": "monster",
      "names": [
        {
          "name": "かいじゅう",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        }
      ],
      "pokemon_species": [
        {
          "name": "bulbasaur",
          "url": "https://pokeapi.co/api/v2/pokemon-species/1/"
        }
      ]
    }

View raw JSON (0.329 kB, 19 lines)

#### EggGroup (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
names| The name of this resource listed in different languages. | list _Name_  
pokemon_species| A list of all Pokémon species that are members of this egg group. | list __NamedAPIResource_ (_PokemonSpecies_)_  
  
### Genders (endpoint)

Genders were introduced in Generation II for the purposes of breeding Pokémon but can also result in visual differences or even different evolutionary lines. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Gender) for greater detail.

GET https://pokeapi.co/api/v2/gender/{id or name}/
    
    {
      "id": 1,
      "name": "female",
      "pokemon_species_details": [
        {
          "rate": 1,
          "pokemon_species": {
            "name": "bulbasaur",
            "url": "https://pokeapi.co/api/v2/pokemon-species/1/"
          }
        }
      ],
      "required_for_evolution": [
        {
          "name": "wormadam",
          "url": "https://pokeapi.co/api/v2/pokemon-species/413/"
        }
      ]
    }

View raw JSON (0.359 kB, 19 lines)

#### Gender (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
pokemon_species_details| A list of Pokémon species that can be this gender and how likely it is that they will be. | list _PokemonSpeciesGender_  
required_for_evolution| A list of Pokémon species that required this gender in order for a Pokémon to evolve into them. | list __NamedAPIResource_ (_PokemonSpecies_)_  
  
#### PokemonSpeciesGender (type)

Name| Description| Type  
---|---|---  
rate| The chance of this Pokémon being female, in eighths; or -1 for genderless. | _integer_  
pokemon_species| A Pokémon species that can be the referenced gender. | _NamedAPIResource_ (_PokemonSpecies_)  
  
### Growth Rates (endpoint)

Growth rates are the speed with which Pokémon gain levels through experience. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Experience) for greater detail.

GET https://pokeapi.co/api/v2/growth-rate/{id or name}/
    
    {
      "id": 1,
      "name": "slow",
      "formula": "\\frac{5x^3}{4}",
      "descriptions": [
        {
          "description": "langsam",
          "language": {
            "name": "de",
            "url": "https://pokeapi.co/api/v2/language/6/"
          }
        }
      ],
      "levels": [
        {
          "level": 100,
          "experience": 1250000
        }
      ],
      "pokemon_species": [
        {
          "name": "growlithe",
          "url": "https://pokeapi.co/api/v2/pokemon-species/58/"
        }
      ]
    }

View raw JSON (0.444 kB, 26 lines)

#### GrowthRate (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
formula| The formula used to calculate the rate at which the Pokémon species gains level. | _string_  
descriptions| The descriptions of this characteristic listed in different languages. | list _Description_  
levels| A list of levels and the amount of experienced needed to atain them based on this growth rate. | list _GrowthRateExperienceLevel_  
pokemon_species| A list of Pokémon species that gain levels at this growth rate. | list __NamedAPIResource_ (_PokemonSpecies_)_  
  
#### GrowthRateExperienceLevel (type)

Name| Description| Type  
---|---|---  
level| The level gained. | _integer_  
experience| The amount of experience required to reach the referenced level. | _integer_  
  
### Natures (endpoint)

Natures influence how a Pokémon's stats grow. See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Nature) for greater detail.

GET https://pokeapi.co/api/v2/nature/{id or name}/
    
    {
      "id": 2,
      "name": "bold",
      "decreased_stat": {
        "name": "attack",
        "url": "https://pokeapi.co/api/v2/stat/2/"
      },
      "increased_stat": {
        "name": "defense",
        "url": "https://pokeapi.co/api/v2/stat/3/"
      },
      "likes_flavor": {
        "name": "sour",
        "url": "https://pokeapi.co/api/v2/berry-flavor/5/"
      },
      "hates_flavor": {
        "name": "spicy",
        "url": "https://pokeapi.co/api/v2/berry-flavor/1/"
      },
      "pokeathlon_stat_changes": [
        {
          "max_change": -2,
          "pokeathlon_stat": {
            "name": "speed",
            "url": "https://pokeapi.co/api/v2/pokeathlon-stat/1/"
          }
        }
      ],
      "move_battle_style_preferences": [
        {
          "low_hp_preference": 32,
          "high_hp_preference": 30,
          "move_battle_style": {
            "name": "attack",
            "url": "https://pokeapi.co/api/v2/move-battle-style/1/"
          }
        }
      ],
      "names": [
        {
          "name": "がんばりや",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        }
      ]
    }

View raw JSON (1.031 kB, 48 lines)

#### Nature (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
decreased_stat| The stat decreased by 10% in Pokémon with this nature. | _NamedAPIResource_ (_Stat_)  
increased_stat| The stat increased by 10% in Pokémon with this nature. | _NamedAPIResource_ (_Stat_)  
hates_flavor| The flavor hated by Pokémon with this nature. | _NamedAPIResource_ (_BerryFlavor_)  
likes_flavor| The flavor liked by Pokémon with this nature. | _NamedAPIResource_ (_BerryFlavor_)  
pokeathlon_stat_changes| A list of Pokéathlon stats this nature effects and how much it effects them. | list _NatureStatChange_  
move_battle_style_preferences| A list of battle styles and how likely a Pokémon with this nature is to use them in the Battle Palace or Battle Tent. | list _MoveBattleStylePreference_  
names| The name of this resource listed in different languages. | list _Name_  
  
#### NatureStatChange (type)

Name| Description| Type  
---|---|---  
max_change| The amount of change. | _integer_  
pokeathlon_stat| The stat being affected. | _NamedAPIResource_ (_PokeathlonStat_)  
  
#### MoveBattleStylePreference (type)

Name| Description| Type  
---|---|---  
low_hp_preference| Chance of using the move, in percent, if HP is under one half. | _integer_  
high_hp_preference| Chance of using the move, in percent, if HP is over one half. | _integer_  
move_battle_style| The move battle style. | _NamedAPIResource_ (_MoveBattleStyle_)  
  
### Pokeathlon Stats (endpoint)

Pokeathlon Stats are different attributes of a Pokémon's performance in Pokéathlons. In Pokéathlons, competitions happen on different courses; one for each of the different Pokéathlon stats. See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9athlon) for greater detail.

GET https://pokeapi.co/api/v2/pokeathlon-stat/{id or name}/
    
    {
      "id": 1,
      "name": "speed",
      "affecting_natures": {
        "increase": [
          {
            "max_change": 2,
            "nature": {
              "name": "timid",
              "url": "https://pokeapi.co/api/v2/nature/5/"
            }
          }
        ],
        "decrease": [
          {
            "max_change": -1,
            "nature": {
              "name": "hardy",
              "url": "https://pokeapi.co/api/v2/nature/1/"
            }
          }
        ]
      },
      "names": [
        {
          "name": "Speed",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ]
    }

View raw JSON (0.576 kB, 33 lines)

#### PokeathlonStat (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
names| The name of this resource listed in different languages. | list _Name_  
affecting_natures| A detail of natures which affect this Pokéathlon stat positively or negatively. | NaturePokeathlonStatAffectSets  
  
#### NaturePokeathlonStatAffectSets (type)

Name| Description| Type  
---|---|---  
increase| A list of natures and how they change the referenced Pokéathlon stat. | list _NaturePokeathlonStatAffect_  
decrease| A list of natures and how they change the referenced Pokéathlon stat. | list _NaturePokeathlonStatAffect_  
  
#### NaturePokeathlonStatAffect (type)

Name| Description| Type  
---|---|---  
max_change| The maximum amount of change to the referenced Pokéathlon stat. | _integer_  
nature| The nature causing the change. | _NamedAPIResource_ (_Nature_)  
  
### Pokemon (endpoint)

Pokémon are the creatures that inhabit the world of the Pokémon games. They can be caught using Pokéballs and trained by battling with other Pokémon. Each Pokémon belongs to a specific species but may take on a variant which makes it differ from other Pokémon of the same species, such as base stats, available abilities and typings. See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_\(species\)) for greater detail.

GET https://pokeapi.co/api/v2/pokemon/{id or name}/
    
    {
      "id": 35,
      "name": "clefairy",
      "base_experience": 113,
      "height": 6,
      "is_default": true,
      "order": 56,
      "weight": 75,
      "abilities": [
        {
          "is_hidden": true,
          "slot": 3,
          "ability": {
            "name": "friend-guard",
            "url": "https://pokeapi.co/api/v2/ability/132/"
          }
        }
      ],
      "forms": [
        {
          "name": "clefairy",
          "url": "https://pokeapi.co/api/v2/pokemon-form/35/"
        }
      ],
      "game_indices": [
        {
          "game_index": 35,
          "version": {
            "name": "white-2",
            "url": "https://pokeapi.co/api/v2/version/22/"
          }
        }
      ],
      "held_items": [
        {
          "item": {
            "name": "moon-stone",
            "url": "https://pokeapi.co/api/v2/item/81/"
          },
          "version_details": [
            {
              "rarity": 5,
              "version": {
                "name": "ruby",
                "url": "https://pokeapi.co/api/v2/version/7/"
              }
            }
          ]
        }
      ],
      "location_area_encounters": "/api/v2/pokemon/35/encounters",
      "moves": [
        {
          "move": {
            "name": "pound",
            "url": "https://pokeapi.co/api/v2/move/1/"
          },
          "version_group_details": [
            {
              "level_learned_at": 1,
              "version_group": {
                "name": "red-blue",
                "url": "https://pokeapi.co/api/v2/version-group/1/"
              },
              "move_learn_method": {
                "name": "level-up",
                "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
              },
              "order": 1
            }
          ]
        }
      ],
      "species": {
        "name": "clefairy",
        "url": "https://pokeapi.co/api/v2/pokemon-species/35/"
      },
      "sprites": {
        "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/35.png",
        "back_female": null,
        "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/35.png",
        "back_shiny_female": null,
        "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/35.png",
        "front_female": null,
        "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/35.png",
        "front_shiny_female": null,
        "other": {
          "dream_world": {
            "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/35.svg",
            "front_female": null
          },
          "home": {
            "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/35.png",
            "front_female": null,
            "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/shiny/35.png",
            "front_shiny_female": null
          },
          "official-artwork": {
            "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/35.png",
            "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/shiny/35.png"
          },
          "showdown": {
            "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/back/35.gif",
            "back_female": null,
            "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/back/shiny/35.gif",
            "back_shiny_female": null,
            "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/35.gif",
            "front_female": null,
            "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/shiny/35.gif",
            "front_shiny_female": null
          }
        },
        "versions": {
          "generation-i": {
            "red-blue": {
              "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/35.png",
              "back_gray": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/gray/35.png",
              "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/35.png",
              "front_gray": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/gray/35.png"
            },
            "yellow": {
              "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/back/35.png",
              "back_gray": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/back/gray/35.png",
              "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/35.png",
              "front_gray": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/gray/35.png"
            }
          },
          "generation-ii": {
            "crystal": {
              "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/back/35.png",
              "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/back/shiny/35.png",
              "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/35.png",
              "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/shiny/35.png"
            },
            "gold": {
              "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/back/35.png",
              "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/back/shiny/35.png",
              "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/35.png",
              "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/shiny/35.png"
            },
            "silver": {
              "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/back/35.png",
              "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/back/shiny/35.png",
              "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/35.png",
              "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/shiny/35.png"
            }
          },
          "generation-iii": {
            "emerald": {
              "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/emerald/35.png",
              "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/emerald/shiny/35.png"
            },
            "firered-leafgreen": {
              "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/firered-leafgreen/back/35.png",
              "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/firered-leafgreen/back/shiny/35.png",
              "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/firered-leafgreen/35.png",
              "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/firered-leafgreen/shiny/35.png"
            },
            "ruby-sapphire": {
              "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/ruby-sapphire/back/35.png",
              "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/ruby-sapphire/back/shiny/35.png",
              "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/ruby-sapphire/35.png",
              "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/ruby-sapphire/shiny/35.png"
            }
          },
          "generation-iv": {
            "diamond-pearl": {
              "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/back/35.png",
              "back_female": null,
              "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/back/shiny/35.png",
              "back_shiny_female": null,
              "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/35.png",
              "front_female": null,
              "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/shiny/35.png",
              "front_shiny_female": null
            },
            "heartgold-soulsilver": {
              "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/back/35.png",
              "back_female": null,
              "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/back/shiny/35.png",
              "back_shiny_female": null,
              "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/35.png",
              "front_female": null,
              "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/shiny/35.png",
              "front_shiny_female": null
            },
            "platinum": {
              "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/back/35.png",
              "back_female": null,
              "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/back/shiny/35.png",
              "back_shiny_female": null,
              "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/35.png",
              "front_female": null,
              "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/shiny/35.png",
              "front_shiny_female": null
            }
          },
          "generation-v": {
            "black-white": {
              "animated": {
                "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/back/35.gif",
                "back_female": null,
                "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/back/shiny/35.gif",
                "back_shiny_female": null,
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/35.gif",
                "front_female": null,
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/shiny/35.gif",
                "front_shiny_female": null
              },
              "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/back/35.png",
              "back_female": null,
              "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/back/shiny/35.png",
              "back_shiny_female": null,
              "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/35.png",
              "front_female": null,
              "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/shiny/35.png",
              "front_shiny_female": null
            }
          },
          "generation-vi": {
            "omegaruby-alphasapphire": {
              "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vi/omegaruby-alphasapphire/35.png",
              "front_female": null,
              "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vi/omegaruby-alphasapphire/shiny/35.png",
              "front_shiny_female": null
            },
            "x-y": {
              "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vi/x-y/35.png",
              "front_female": null,
              "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vi/x-y/shiny/35.png",
              "front_shiny_female": null
            }
          },
          "generation-vii": {
            "icons": {
              "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/icons/35.png",
              "front_female": null
            },
            "ultra-sun-ultra-moon": {
              "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/ultra-sun-ultra-moon/35.png",
              "front_female": null,
              "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/ultra-sun-ultra-moon/shiny/35.png",
              "front_shiny_female": null
            }
          },
          "generation-viii": {
            "icons": {
              "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-viii/icons/35.png",
              "front_female": null
            }
          }
        }
      },
      "cries": {
        "latest": "https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/35.ogg",
        "legacy": "https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/legacy/35.ogg"
      },
      "stats": [
        {
          "base_stat": 35,
          "effort": 0,
          "stat": {
            "name": "speed",
            "url": "https://pokeapi.co/api/v2/stat/6/"
          }
        }
      ],
      "types": [
        {
          "slot": 1,
          "type": {
            "name": "fairy",
            "url": "https://pokeapi.co/api/v2/type/18/"
          }
        }
      ],
      "past_types": [
        {
          "generation": {
            "name": "generation-v",
            "url": "https://pokeapi.co/api/v2/generation/5/"
          },
          "types": [
            {
              "slot": 1,
              "type": {
                "name": "normal",
                "url": "https://pokeapi.co/api/v2/type/1/"
              }
            }
          ]
        }
      ],
      "past_abilities": [
        {
          "generation": {
            "name": "generation-iv",
            "url": "https://pokeapi.co/api/v2/generation/4/"
          },
          "abilities": [
            {
              "ability": null,
              "is_hidden": true,
              "slot": 3
            }
          ]
        }
      ]
    }

View raw JSON (15.38 kB, 309 lines)

#### Pokemon (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
base_experience| The base experience gained for defeating this Pokémon. | _integer_  
height| The height of this Pokémon in decimetres. | _integer_  
is_default| Set for exactly one Pokémon used as the default for each species. | _boolean_  
order| Order for sorting. Almost national order, except families are grouped together. | _integer_  
weight| The weight of this Pokémon in hectograms. | _integer_  
abilities| A list of abilities this Pokémon could potentially have. | list _PokemonAbility_  
forms| A list of forms this Pokémon can take on. | list __NamedAPIResource_ (_PokemonForm_)_  
game_indices| A list of game indices relevent to Pokémon item by generation. | list _VersionGameIndex_  
held_items| A list of items this Pokémon may be holding when encountered. | list _PokemonHeldItem_  
location_area_encounters| A link to a list of location areas, as well as encounter details pertaining to specific versions. | _string_  
moves| A list of moves along with learn methods and level details pertaining to specific version groups. | list _PokemonMove_  
past_types| A list of details showing types this pokémon had in previous generations | list _PokemonTypePast_  
past_abilities| A list of details showing abilities this pokémon had in previous generations | list _PokemonAbilityPast_  
sprites| A set of sprites used to depict this Pokémon in the game. A visual representation of the various sprites can be found at [PokeAPI/sprites](https://github.com/PokeAPI/sprites#sprites) | PokemonSprites  
cries| A set of cries used to depict this Pokémon in the game. A visual representation of the various cries can be found at [PokeAPI/cries](https://github.com/PokeAPI/cries#cries) | PokemonCries  
species| The species this Pokémon belongs to. | _NamedAPIResource_ (_PokemonSpecies_)  
stats| A list of base stat values for this Pokémon. | list _PokemonStat_  
types| A list of details showing types this Pokémon has. | list _PokemonType_  
  
#### PokemonAbility (type)

Name| Description| Type  
---|---|---  
is_hidden| Whether or not this is a hidden ability. | _boolean_  
slot| The slot this ability occupies in this Pokémon species. | _integer_  
ability| The ability the Pokémon may have. | _NamedAPIResource_ (_Ability_)  
  
#### PokemonType (type)

Name| Description| Type  
---|---|---  
slot| The order the Pokémon's types are listed in. | _integer_  
type| The type the referenced Pokémon has. | _NamedAPIResource_ (_Type_)  
  
#### PokemonFormType (type)

Name| Description| Type  
---|---|---  
slot| The order the Pokémon's types are listed in. | _integer_  
type| The type the referenced Form has. | _NamedAPIResource_ (_Type_)  
  
#### PokemonTypePast (type)

Name| Description| Type  
---|---|---  
generation| The last generation in which the referenced pokémon had the listed types. | _NamedAPIResource_ (_Generation_)  
types| The types the referenced pokémon had up to and including the listed generation. | list _PokemonType_  
  
#### PokemonAbilityPast (type)

Name| Description| Type  
---|---|---  
generation| The last generation in which the referenced pokémon had the listed abilities. | _NamedAPIResource_ (_Generation_)  
abilities| The abilities the referenced pokémon had up to and including the listed generation. If null, the slot was previously empty. | list _PokemonAbility_  
  
#### PokemonHeldItem (type)

Name| Description| Type  
---|---|---  
item| The item the referenced Pokémon holds. | _NamedAPIResource_ (_Item_)  
version_details| The details of the different versions in which the item is held. | list _PokemonHeldItemVersion_  
  
#### PokemonHeldItemVersion (type)

Name| Description| Type  
---|---|---  
version| The version in which the item is held. | _NamedAPIResource_ (_Version_)  
rarity| How often the item is held. | _integer_  
  
#### PokemonMove (type)

Name| Description| Type  
---|---|---  
move| The move the Pokémon can learn. | _NamedAPIResource_ (_Move_)  
version_group_details| The details of the version in which the Pokémon can learn the move. | list _PokemonMoveVersion_  
  
#### PokemonMoveVersion (type)

Name| Description| Type  
---|---|---  
move_learn_method| The method by which the move is learned. | _NamedAPIResource_ (_MoveLearnMethod_)  
version_group| The version group in which the move is learned. | _NamedAPIResource_ (_VersionGroup_)  
level_learned_at| The minimum level to learn the move. | _integer_  
order| Order by which the pokemon will learn the move. A newly learnt move will replace the move with lowest order. | _integer_  
  
#### PokemonStat (type)

Name| Description| Type  
---|---|---  
stat| The stat the Pokémon has. | _NamedAPIResource_ (_Stat_)  
effort| The effort points (EV) the Pokémon has in the stat. | _integer_  
base_stat| The base value of the stat. | _integer_  
  
#### PokemonSprites (type)

Name| Description| Type  
---|---|---  
front_default| The default depiction of this Pokémon from the front in battle. | _string_  
front_shiny| The shiny depiction of this Pokémon from the front in battle. | _string_  
front_female| The female depiction of this Pokémon from the front in battle. | _string_  
front_shiny_female| The shiny female depiction of this Pokémon from the front in battle. | _string_  
back_default| The default depiction of this Pokémon from the back in battle. | _string_  
back_shiny| The shiny depiction of this Pokémon from the back in battle. | _string_  
back_female| The female depiction of this Pokémon from the back in battle. | _string_  
back_shiny_female| The shiny female depiction of this Pokémon from the back in battle. | _string_  
  
#### PokemonCries (type)

Name| Description| Type  
---|---|---  
latest| The latest depiction of this Pokémon's cry. | _string_  
legacy| The legacy depiction of this Pokémon's cry. | _string_  
  
### Pokemon Location Areas (endpoint)

Pokémon Location Areas are ares where Pokémon can be found.

GET https://pokeapi.co/api/v2/pokemon/{id or name}/encounters
    
    [
      {
        "location_area": {
          "name": "kanto-route-2-south-towards-viridian-city",
          "url": "https://pokeapi.co/api/v2/location-area/296/"
        },
        "version_details": [
          {
            "max_chance": 10,
            "encounter_details": [
              {
                "min_level": 7,
                "max_level": 7,
                "condition_values": [
                  {
                    "name": "time-morning",
                    "url": "https://pokeapi.co/api/v2/encounter-condition-value/3/"
                  }
                ],
                "chance": 5,
                "method": {
                  "name": "walk",
                  "url": "https://pokeapi.co/api/v2/encounter-method/1/"
                }
              }
            ],
            "version": {
              "name": "heartgold",
              "url": "https://pokeapi.co/api/v2/version/15/"
            }
          }
        ]
      }
    ]

View raw JSON (0.837 kB, 34 lines)

#### LocationAreaEncounter (type)

Name| Description| Type  
---|---|---  
location_area| The location area the referenced Pokémon can be encountered in. | _NamedAPIResource_ (_LocationArea_)  
version_details| A list of versions and encounters with the referenced Pokémon that might happen. | list _VersionEncounterDetail_  
  
### Pokemon Colors (endpoint)

Colors used for sorting Pokémon in a Pokédex. The color listed in the Pokédex is usually the color most apparent or covering each Pokémon's body. No orange category exists; Pokémon that are primarily orange are listed as red or brown.

GET https://pokeapi.co/api/v2/pokemon-color/{id or name}/
    
    {
      "id": 1,
      "name": "black",
      "names": [
        {
          "name": "é»’ã„",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        }
      ],
      "pokemon_species": [
        {
          "name": "snorlax",
          "url": "https://pokeapi.co/api/v2/pokemon-species/143/"
        }
      ]
    }

View raw JSON (0.326 kB, 19 lines)

#### PokemonColor (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
names| The name of this resource listed in different languages. | list _Name_  
pokemon_species| A list of the Pokémon species that have this color. | list __NamedAPIResource_ (_PokemonSpecies_)_  
  
### Pokemon Forms (endpoint)

Some Pokémon may appear in one of multiple, visually different forms. These differences are purely cosmetic. For variations within a Pokémon species, which do differ in more than just visuals, the 'Pokémon' entity is used to represent such a variety.

GET https://pokeapi.co/api/v2/pokemon-form/{id or name}/
    
    {
      "id": 10041,
      "name": "arceus-bug",
      "order": 631,
      "form_order": 7,
      "is_default": false,
      "is_battle_only": false,
      "is_mega": false,
      "form_name": "bug",
      "pokemon": {
        "name": "arceus",
        "url": "https://pokeapi.co/api/v2/pokemon/493/"
      },
      "sprites": {
        "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/493-bug.png",
        "back_female": null,
        "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/493-bug.png",
        "back_shiny_female": null,
        "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/493-bug.png",
        "front_female": null,
        "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/493-bug.png",
        "front_shiny_female": null
      },
      "types": [
        {
          "slot": 1,
          "type": {
            "name": "bug",
            "url": "https://pokeapi.co/api/v2/type/7/"
          }
        }
      ],
      "version_group": {
        "name": "diamond-pearl",
        "url": "https://pokeapi.co/api/v2/version-group/8/"
      }
    }

View raw JSON (1.103 kB, 37 lines)

#### PokemonForm (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
order| The order in which forms should be sorted within all forms. Multiple forms may have equal order, in which case they should fall back on sorting by name. | _integer_  
form_order| The order in which forms should be sorted within a species' forms. | _integer_  
is_default| True for exactly one form used as the default for each Pokémon. | _boolean_  
is_battle_only| Whether or not this form can only happen during battle. | _boolean_  
is_mega| Whether or not this form requires mega evolution. | _boolean_  
form_name| The name of this form. | _string_  
pokemon| The Pokémon that can take on this form. | _NamedAPIResource_ (_Pokemon_)  
types| A list of details showing types this Pokémon form has. | list _PokemonFormType_  
sprites| A set of sprites used to depict this Pokémon form in the game. | PokemonFormSprites  
version_group| The version group this Pokémon form was introduced in. | _NamedAPIResource_ (_VersionGroup_)  
names| The form specific full name of this Pokémon form, or empty if the form does not have a specific name. | list _Name_  
form_names| The form specific form name of this Pokémon form, or empty if the form does not have a specific name. | list _Name_  
  
#### PokemonFormSprites (type)

Name| Description| Type  
---|---|---  
front_default| The default depiction of this Pokémon form from the front in battle. | _string_  
front_shiny| The shiny depiction of this Pokémon form from the front in battle. | _string_  
back_default| The default depiction of this Pokémon form from the back in battle. | _string_  
back_shiny| The shiny depiction of this Pokémon form from the back in battle. | _string_  
  
### Pokemon Habitats (endpoint)

Habitats are generally different terrain Pokémon can be found in but can also be areas designated for rare or legendary Pokémon.

GET https://pokeapi.co/api/v2/pokemon-habitat/{id or name}/
    
    {
      "id": 1,
      "name": "cave",
      "names": [
        {
          "name": "grottes",
          "language": {
            "name": "fr",
            "url": "https://pokeapi.co/api/v2/language/5/"
          }
        }
      ],
      "pokemon_species": [
        {
          "name": "zubat",
          "url": "https://pokeapi.co/api/v2/pokemon-species/41/"
        }
      ]
    }

View raw JSON (0.315 kB, 19 lines)

#### PokemonHabitat (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
names| The name of this resource listed in different languages. | list _Name_  
pokemon_species| A list of the Pokémon species that can be found in this habitat. | list __NamedAPIResource_ (_PokemonSpecies_)_  
  
### Pokemon Shapes (endpoint)

Shapes used for sorting Pokémon in a Pokédex.

GET https://pokeapi.co/api/v2/pokemon-shape/{id or name}/
    
    {
      "id": 1,
      "name": "ball",
      "awesome_names": [
        {
          "awesome_name": "Pomaceous",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ],
      "names": [
        {
          "name": "Ball",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ],
      "pokemon_species": [
        {
          "name": "shellder",
          "url": "https://pokeapi.co/api/v2/pokemon-species/90/"
        }
      ]
    }

View raw JSON (0.493 kB, 28 lines)

#### PokemonShape (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
awesome_names| The "scientific" name of this Pokémon shape listed in different languages. | list _AwesomeName_  
names| The name of this resource listed in different languages. | list _Name_  
pokemon_species| A list of the Pokémon species that have this shape. | list __NamedAPIResource_ (_PokemonSpecies_)_  
  
#### AwesomeName (type)

Name| Description| Type  
---|---|---  
awesome_name| The localized "scientific" name for an API resource in a specific language. | _string_  
language| The language this "scientific" name is in. | _NamedAPIResource_ (_Language_)  
  
### Pokemon Species (endpoint)

A Pokémon Species forms the basis for at least one Pokémon. Attributes of a Pokémon species are shared across all varieties of Pokémon within the species. A good example is Wormadam; Wormadam is the species which can be found in three different varieties, Wormadam-Trash, Wormadam-Sandy and Wormadam-Plant.

GET https://pokeapi.co/api/v2/pokemon-species/{id or name}/
    
    {
      "id": 413,
      "name": "wormadam",
      "order": 441,
      "gender_rate": 8,
      "capture_rate": 45,
      "base_happiness": 70,
      "is_baby": false,
      "is_legendary": false,
      "is_mythical": false,
      "hatch_counter": 15,
      "has_gender_differences": false,
      "forms_switchable": false,
      "growth_rate": {
        "name": "medium",
        "url": "https://pokeapi.co/api/v2/growth-rate/2/"
      },
      "pokedex_numbers": [
        {
          "entry_number": 45,
          "pokedex": {
            "name": "kalos-central",
            "url": "https://pokeapi.co/api/v2/pokedex/12/"
          }
        }
      ],
      "egg_groups": [
        {
          "name": "bug",
          "url": "https://pokeapi.co/api/v2/egg-group/3/"
        }
      ],
      "color": {
        "name": "gray",
        "url": "https://pokeapi.co/api/v2/pokemon-color/4/"
      },
      "shape": {
        "name": "squiggle",
        "url": "https://pokeapi.co/api/v2/pokemon-shape/2/"
      },
      "evolves_from_species": {
        "name": "burmy",
        "url": "https://pokeapi.co/api/v2/pokemon-species/412/"
      },
      "evolution_chain": {
        "url": "https://pokeapi.co/api/v2/evolution-chain/213/"
      },
      "habitat": null,
      "generation": {
        "name": "generation-iv",
        "url": "https://pokeapi.co/api/v2/generation/4/"
      },
      "names": [
        {
          "name": "Wormadam",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ],
      "flavor_text_entries": [
        {
          "flavor_text": "When the bulb on\nits back grows\nlarge, it appears\fto lose the\nability to stand\non its hind legs.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          },
          "version": {
            "name": "red",
            "url": "https://pokeapi.co/api/v2/version/1/"
          }
        }
      ],
      "form_descriptions": [
        {
          "description": "Forms have different stats and movepools.  During evolution, Burmy's current cloak becomes Wormadam's form, and can no longer be changed.",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ],
      "genera": [
        {
          "genus": "Bagworm",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ],
      "varieties": [
        {
          "is_default": true,
          "pokemon": {
            "name": "wormadam-plant",
            "url": "https://pokeapi.co/api/v2/pokemon/413/"
          }
        }
      ]
    }

View raw JSON (2.373 kB, 102 lines)

#### PokemonSpecies (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
order| The order in which species should be sorted. Based on National Dex order, except families are grouped together and sorted by stage. | _integer_  
gender_rate| The chance of this Pokémon being female, in eighths; or -1 for genderless. | _integer_  
capture_rate| The base capture rate; up to 255. The higher the number, the easier the catch. | _integer_  
base_happiness| The happiness when caught by a normal Pokéball; up to 255. The higher the number, the happier the Pokémon. | _integer_  
is_baby| Whether or not this is a baby Pokémon. | _boolean_  
is_legendary| Whether or not this is a legendary Pokémon. | _boolean_  
is_mythical| Whether or not this is a mythical Pokémon. | _boolean_  
hatch_counter| Initial hatch counter: one must walk Y × (hatch_counter + 1) steps before this Pokémon's egg hatches, unless utilizing bonuses like Flame Body's. Y varies per generation. In Generations II, III, and VII, Egg cycles are 256 steps long. In Generation IV, Egg cycles are 255 steps long. In Pokémon Brilliant Diamond and Shining Pearl, Egg cycles are also 255 steps long, but are shorter on special dates. In Generations V and VI, Egg cycles are 257 steps long. In Pokémon Sword and Shield, and in Pokémon Scarlet and Violet, Egg cycles are 128 steps long. | _integer_  
has_gender_differences| Whether or not this Pokémon has visual gender differences. | _boolean_  
forms_switchable| Whether or not this Pokémon has multiple forms and can switch between them. | _boolean_  
growth_rate| The rate at which this Pokémon species gains levels. | _NamedAPIResource_ (_GrowthRate_)  
pokedex_numbers| A list of Pokedexes and the indexes reserved within them for this Pokémon species. | list _PokemonSpeciesDexEntry_  
egg_groups| A list of egg groups this Pokémon species is a member of. | list __NamedAPIResource_ (_EggGroup_)_  
color| The color of this Pokémon for Pokédex search. | _NamedAPIResource_ (_PokemonColor_)  
shape| The shape of this Pokémon for Pokédex search. | _NamedAPIResource_ (_PokemonShape_)  
evolves_from_species| The Pokémon species that evolves into this Pokemon_species. | _NamedAPIResource_ (_PokemonSpecies_)  
evolution_chain| The evolution chain this Pokémon species is a member of. | _APIResource_ (_EvolutionChain_)  
habitat| The habitat this Pokémon species can be encountered in. | _NamedAPIResource_ (_PokemonHabitat_)  
generation| The generation this Pokémon species was introduced in. | _NamedAPIResource_ (_Generation_)  
names| The name of this resource listed in different languages. | list _Name_  
pal_park_encounters| A list of encounters that can be had with this Pokémon species in pal park. | list _PalParkEncounterArea_  
flavor_text_entries| A list of flavor text entries for this Pokémon species. | list _FlavorText_  
form_descriptions| Descriptions of different forms Pokémon take on within the Pokémon species. | list _Description_  
genera| The genus of this Pokémon species listed in multiple languages. | list _Genus_  
varieties| A list of the Pokémon that exist within this Pokémon species. | list _PokemonSpeciesVariety_  
  
#### Genus (type)

Name| Description| Type  
---|---|---  
genus| The localized genus for the referenced Pokémon species | _string_  
language| The language this genus is in. | _NamedAPIResource_ (_Language_)  
  
#### PokemonSpeciesDexEntry (type)

Name| Description| Type  
---|---|---  
entry_number| The index number within the Pokédex. | _integer_  
pokedex| The Pokédex the referenced Pokémon species can be found in. | _NamedAPIResource_ (_Pokedex_)  
  
#### PalParkEncounterArea (type)

Name| Description| Type  
---|---|---  
base_score| The base score given to the player when the referenced Pokémon is caught during a pal park run. | _integer_  
rate| The base rate for encountering the referenced Pokémon in this pal park area. | _integer_  
area| The pal park area where this encounter happens. | _NamedAPIResource_ (_PalParkArea_)  
  
#### PokemonSpeciesVariety (type)

Name| Description| Type  
---|---|---  
is_default| Whether this variety is the default variety. | _boolean_  
pokemon| The Pokémon variety. | _NamedAPIResource_ (_Pokemon_)  
  
### Stats (endpoint)

Stats determine certain aspects of battles. Each Pokémon has a value for each stat which grows as they gain levels and can be altered momentarily by effects in battles.

GET https://pokeapi.co/api/v2/stat/{id or name}/
    
    {
      "id": 2,
      "name": "attack",
      "game_index": 2,
      "is_battle_only": false,
      "affecting_moves": {
        "increase": [
          {
            "change": 2,
            "move": {
              "name": "swords-dance",
              "url": "https://pokeapi.co/api/v2/move/14/"
            }
          }
        ],
        "decrease": [
          {
            "change": -1,
            "move": {
              "name": "growl",
              "url": "https://pokeapi.co/api/v2/move/45/"
            }
          }
        ]
      },
      "affecting_natures": {
        "increase": [
          {
            "name": "lonely",
            "url": "https://pokeapi.co/api/v2/nature/6/"
          }
        ],
        "decrease": [
          {
            "name": "bold",
            "url": "https://pokeapi.co/api/v2/nature/2/"
          }
        ]
      },
      "characteristics": [
        {
          "url": "https://pokeapi.co/api/v2/characteristic/2/"
        }
      ],
      "move_damage_class": {
        "name": "physical",
        "url": "https://pokeapi.co/api/v2/move-damage-class/2/"
      },
      "names": [
        {
          "name": "ã“ã†ã’ã",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        }
      ]
    }

View raw JSON (1.116 kB, 58 lines)

#### Stat (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
game_index| ID the games use for this stat. | _integer_  
is_battle_only| Whether this stat only exists within a battle. | _boolean_  
affecting_moves| A detail of moves which affect this stat positively or negatively. | MoveStatAffectSets  
affecting_natures| A detail of natures which affect this stat positively or negatively. | NatureStatAffectSets  
characteristics| A list of characteristics that are set on a Pokémon when its highest base stat is this stat. | list __APIResource_ (_Characteristic_)_  
move_damage_class| The class of damage this stat is directly related to. | _NamedAPIResource_ (_MoveDamageClass_)  
names| The name of this resource listed in different languages. | list _Name_  
  
#### MoveStatAffectSets (type)

Name| Description| Type  
---|---|---  
increase| A list of moves and how they change the referenced stat. | list _MoveStatAffect_  
decrease| A list of moves and how they change the referenced stat. | list _MoveStatAffect_  
  
#### MoveStatAffect (type)

Name| Description| Type  
---|---|---  
change| The maximum amount of change to the referenced stat. | _integer_  
move| The move causing the change. | _NamedAPIResource_ (_Move_)  
  
#### NatureStatAffectSets (type)

Name| Description| Type  
---|---|---  
increase| A list of natures and how they change the referenced stat. | list __NamedAPIResource_ (_Nature_)_  
decrease| A list of nature sand how they change the referenced stat. | list __NamedAPIResource_ (_Nature_)_  
  
### Types (endpoint)

Types are properties for Pokémon and their moves. Each type has three properties: which types of Pokémon it is super effective against, which types of Pokémon it is not very effective against, and which types of Pokémon it is completely ineffective against.

GET https://pokeapi.co/api/v2/type/{id or name}/
    
    {
      "id": 5,
      "name": "ground",
      "damage_relations": {
        "no_damage_to": [
          {
            "name": "flying",
            "url": "https://pokeapi.co/api/v2/type/3/"
          }
        ],
        "half_damage_to": [
          {
            "name": "bug",
            "url": "https://pokeapi.co/api/v2/type/7/"
          }
        ],
        "double_damage_to": [
          {
            "name": "poison",
            "url": "https://pokeapi.co/api/v2/type/4/"
          }
        ],
        "no_damage_from": [
          {
            "name": "electric",
            "url": "https://pokeapi.co/api/v2/type/13/"
          }
        ],
        "half_damage_from": [
          {
            "name": "poison",
            "url": "https://pokeapi.co/api/v2/type/4/"
          }
        ],
        "double_damage_from": [
          {
            "name": "water",
            "url": "https://pokeapi.co/api/v2/type/11/"
          }
        ]
      },
      "past_damage_relations": [
        {
          "generation": {
            "name": "generation-v",
            "url": "https://pokeapi.co/api/v2/generation/5/"
          },
          "damage_relations": {
            "no_damage_to": [
              {
                "name": "normal",
                "url": "https://pokeapi.co/api/v2/type/1/"
              }
            ],
            "half_damage_to": [
              {
                "name": "steel",
                "url": "https://pokeapi.co/api/v2/type/9/"
              }
            ],
            "double_damage_to": [
              {
                "name": "ghost",
                "url": "https://pokeapi.co/api/v2/type/8/"
              }
            ],
            "no_damage_from": [
              {
                "name": "normal",
                "url": "https://pokeapi.co/api/v2/type/1/"
              }
            ],
            "half_damage_from": [
              {
                "name": "poison",
                "url": "https://pokeapi.co/api/v2/type/4/"
              }
            ],
            "double_damage_from": [
              {
                "name": "ghost",
                "url": "https://pokeapi.co/api/v2/type/8/"
              }
            ]
          }
        }
      ],
      "game_indices": [
        {
          "game_index": 4,
          "generation": {
            "name": "generation-i",
            "url": "https://pokeapi.co/api/v2/generation/1/"
          }
        }
      ],
      "generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
      },
      "move_damage_class": {
        "name": "physical",
        "url": "https://pokeapi.co/api/v2/move-damage-class/2/"
      },
      "names": [
        {
          "name": "ã˜ã‚ã‚“",
          "language": {
            "name": "ja",
            "url": "https://pokeapi.co/api/v2/language/1/"
          }
        }
      ],
      "pokemon": [
        {
          "slot": 1,
          "pokemon": {
            "name": "sandshrew",
            "url": "https://pokeapi.co/api/v2/pokemon/27/"
          }
        }
      ],
      "moves": [
        {
          "name": "sand-attack",
          "url": "https://pokeapi.co/api/v2/move/28/"
        }
      ]
    }

View raw JSON (2.743 kB, 129 lines)

#### Type (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
damage_relations| A detail of how effective this type is toward others and vice versa. | TypeRelations  
past_damage_relations| A list of details of how effective this type was toward others and vice versa in previous generations | list __TypeRelationsPast_ (_Type_)_  
game_indices| A list of game indices relevent to this item by generation. | list _GenerationGameIndex_  
generation| The generation this type was introduced in. | _NamedAPIResource_ (_Generation_)  
move_damage_class| The class of damage inflicted by this type. | _NamedAPIResource_ (_MoveDamageClass_)  
names| The name of this resource listed in different languages. | list _Name_  
pokemon| A list of details of Pokémon that have this type. | list _TypePokemon_  
moves| A list of moves that have this type. | list __NamedAPIResource_ (_Move_)_  
  
#### TypePokemon (type)

Name| Description| Type  
---|---|---  
slot| The order the Pokémon's types are listed in. | _integer_  
pokemon| The Pokémon that has the referenced type. | _NamedAPIResource_ (_Pokemon_)  
  
#### TypeRelations (type)

Name| Description| Type  
---|---|---  
no_damage_to| A list of types this type has no effect on. | list __NamedAPIResource_ (_Type_)_  
half_damage_to| A list of types this type is not very effect against. | list __NamedAPIResource_ (_Type_)_  
double_damage_to| A list of types this type is very effect against. | list __NamedAPIResource_ (_Type_)_  
no_damage_from| A list of types that have no effect on this type. | list __NamedAPIResource_ (_Type_)_  
half_damage_from| A list of types that are not very effective against this type. | list __NamedAPIResource_ (_Type_)_  
double_damage_from| A list of types that are very effective against this type. | list __NamedAPIResource_ (_Type_)_  
  
#### TypeRelationsPast (type)

Name| Description| Type  
---|---|---  
generation| The last generation in which the referenced type had the listed damage relations | _NamedAPIResource_ (_Generation_)  
damage_relations| The damage relations the referenced type had up to and including the listed generation | TypeRelations  
  
## Utility (group)

### Languages (endpoint)

Languages for translations of API resource information.

GET https://pokeapi.co/api/v2/language/{id or name}/
    
    {
      "id": 1,
      "name": "ja",
      "official": true,
      "iso639": "ja",
      "iso3166": "jp",
      "names": [
        {
          "name": "Japanese",
          "language": {
            "name": "en",
            "url": "https://pokeapi.co/api/v2/language/9/"
          }
        }
      ]
    }

View raw JSON (0.247 kB, 16 lines)

#### Language (type)

Name| Description| Type  
---|---|---  
id| The identifier for this resource. | _integer_  
name| The name for this resource. | _string_  
official| Whether or not the games are published in this language. | _boolean_  
iso639| The two-letter code of the country where this language is spoken. Note that it is not unique. | _string_  
iso3166| The two-letter code of the language. Note that it is not unique. | _string_  
names| The name of this resource listed in different languages. | list _Name_  
  
### Common Models

#### APIResource (type)

Name| Description| Type  
---|---|---  
url| The URL of the referenced resource. | _string_  
  
#### Description (type)

Name| Description| Type  
---|---|---  
description| The localized description for an API resource in a specific language. | _string_  
language| The language this name is in. | _NamedAPIResource_ (_Language_)  
  
#### Effect (type)

Name| Description| Type  
---|---|---  
effect| The localized effect text for an API resource in a specific language. | _string_  
language| The language this effect is in. | _NamedAPIResource_ (_Language_)  
  
#### Encounter (type)

Name| Description| Type  
---|---|---  
min_level| The lowest level the Pokémon could be encountered at. | _integer_  
max_level| The highest level the Pokémon could be encountered at. | _integer_  
condition_values| A list of condition values that must be in effect for this encounter to occur. | list __NamedAPIResource_ (_EncounterConditionValue_)_  
chance| Percent chance that this encounter will occur. | _integer_  
method| The method by which this encounter happens. | _NamedAPIResource_ (_EncounterMethod_)  
  
#### FlavorText (type)

Name| Description| Type  
---|---|---  
flavor_text| The localized flavor text for an API resource in a specific language. Note that this text is left unprocessed as it is found in game files. This means that it contains special characters that one might want to replace with their visible decodable version. Please check out this [issue](https://github.com/veekun/pokedex/issues/218#issuecomment-339841781) to find out more.  | _string_  
language| The language this name is in. | _NamedAPIResource_ (_Language_)  
version| The game version this flavor text is extracted from. | _NamedAPIResource_ (_Version_)  
  
#### GenerationGameIndex (type)

Name| Description| Type  
---|---|---  
game_index| The internal id of an API resource within game data. | _integer_  
generation| The generation relevent to this game index. | _NamedAPIResource_ (_Generation_)  
  
#### MachineVersionDetail (type)

Name| Description| Type  
---|---|---  
machine| The machine that teaches a move from an item. | _APIResource _ (_Machine_)  
version_group| The version group of this specific machine. | _NamedAPIResource_ (_VersionGroup_)  
  
#### Name (type)

Name| Description| Type  
---|---|---  
name| The localized name for an API resource in a specific language. | _string_  
language| The language this name is in. | _NamedAPIResource_ (_Language_)  
  
#### NamedAPIResource (type)

Name| Description| Type  
---|---|---  
name| The name of the referenced resource. | _string_  
url| The URL of the referenced resource. | _string_  
  
#### VerboseEffect (type)

Name| Description| Type  
---|---|---  
effect| The localized effect text for an API resource in a specific language. | _string_  
short_effect| The localized effect text in brief. | _string_  
language| The language this effect is in. | _NamedAPIResource_ (_Language_)  
  
#### VersionEncounterDetail (type)

Name| Description| Type  
---|---|---  
version| The game version this encounter happens in. | _NamedAPIResource_ (_Version_)  
max_chance| The total percentage of all encounter potential. | _integer_  
encounter_details| A list of encounters and their specifics. | list _Encounter_  
  
#### VersionGameIndex (type)

Name| Description| Type  
---|---|---  
game_index| The internal id of an API resource within game data. | _integer_  
version| The version relevent to this game index. | _NamedAPIResource_ (_Version_)  
  
#### VersionGroupFlavorText (type)

Name| Description| Type  
---|---|---  
text| The localized name for an API resource in a specific language. | _string_  
language| The language this name is in. | _NamedAPIResource_ (_Language_)  
version_group| The version group which uses this flavor text. | _NamedAPIResource_ (_VersionGroup_)
