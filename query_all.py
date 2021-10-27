import requests
import json

endpoint = "https://graphql.epicgames.com/graphql"


# This query thing is what was sent to the server
# when loading the page, I couldn't figure out how
# to write it ourselves so I basically copy pasted
# the binary data in the payload.
query = b'{"query":"\\n            query storefrontDiscoverQuery(\\n              $locale:String,\\n              $country:String\u0021\\n            )  {\\n              Storefront {\\n                storefrontModules(locale: $locale) {\\n                  ... on StorefrontBreaker {\\n                    type\\n                    title\\n                    titleGroup\\n                    description\\n                    backgroundColors\\n                    layout\\n                    link {\\n                      src\\n                      linkText\\n                    }\\n                    image {\\n                      src\\n                      alt\\n                    }\\n                  }\\n                  ... on StorefrontFreeGames {\\n                    type\\n                    title\\n                  }\\n                  ... on StorefrontCardGroup {\\n                    type\\n                    title\\n                    link {\\n                        src\\n                        linkText\\n                    }\\n                    offers {\\n                      namespace\\n                      id\\n                      offer {\\n                        \\n          title\\n          id\\n          namespace\\n          description\\n          keyImages {\\n            type\\n            url\\n          }\\n          seller {\\n              id\\n              name\\n          }\\n          urlSlug\\n          items {\\n            id\\n            namespace\\n          }\\n          customAttributes {\\n            key\\n            value\\n          }\\n          categories {\\n            path\\n          }\\n          price(country: $country) {\\n            totalPrice {\\n              discountPrice\\n              originalPrice\\n              voucherDiscount\\n              discount\\n              fmtPrice(locale: $locale) {\\n                originalPrice\\n                discountPrice\\n                intermediatePrice\\n              }\\n            }\\n            lineOffers {\\n              appliedRules {\\n                id\\n                endDate\\n              }\\n            }\\n          }\\n          linkedOfferId\\n          linkedOffer {\\n            effectiveDate\\n            customAttributes {\\n              key\\n              value\\n            }\\n          }\\n        \\n                      }\\n                    }\\n                  }\\n                  ... on StorefrontFeaturedCarousel {\\n                    type\\n                    title\\n                    slides {\\n                      title\\n                      eyebrow\\n                      description\\n                      backgroundColor\\n                      image {\\n                        src\\n                        alt\\n                      }\\n                      mobileImage {\\n                        src\\n                        alt\\n                      }\\n                      link {\\n                        src\\n                        linkText\\n                      }\\n                    }\\n                  }\\n                  ... on StorefrontTiles {\\n                    type\\n                    title\\n                    tiles {\\n                      label\\n                      genre\\n                      link {\\n                        src\\n                        linkText\\n                      }\\n                    }\\n                  }\\n                }\\n              }\\n            }\\n            ","variables":{"locale":"en-US","country":"US"}}'

data = requests.post(endpoint, headers={"Content-type": "application/json;charset=UTF-8"
                                       }, data=query)
print(data.json())

with open("query_all.json", "w", encoding="utf-8") as f:
    json.dump(data.json(), f)