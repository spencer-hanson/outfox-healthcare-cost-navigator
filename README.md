# outfox-healthcare-cost-navigator

# Docker Setup Instructions
- Run `docker-compose build` then `docker-compose up`
- This will build the required containers, configure them, and then start them up

# Database seeding instructions
- After setting up docker, run `python seed_database.py` to create the initial schema
- To load data into the database run `python etl.py example_data.csv`


# Sample cURL commands

- To get all providers in the zipcode 23185, you can run the cURL command

`curl -XGET 'http://127.0.0.1:8080/providers/23185'`

- This will return a JSON list of the providers, here is an example result

```json
[
  {
    "id": 2818,
    "provider_id": "490143",
    "provider_name": "Riverside Doctors' Hospital Of Williamsburg",
    "provider_city": "Williamsburg",
    "provider_state": "VA",
    "provider_zipcode": 23185
  }
]
```

- To ask a question of the API


`curl -XGET 'http://127.0.0.1:8080/ask?query=What%20is%20the%20closest%20hospital%20to%20me%3F'`


- TODO integrate database results and query OpenAI API
