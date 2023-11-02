# Elasticsearch

-   The Elastic Stack
    -   beats, logstash, elasticsearch, kibana
    -   Take data in any format, search, analyze and visualize it in real-time
    -   Use cases
        -   Logging (Blizzard game)
        -   Metrics (Mars rover)
        -   Security Analytics (Slack)
        -   Business Analytics (Tinder)
-   Elasticsearch
    -   Heart of elastic stack 
    -   Store, search and analyze data
    -   Focusses on speed and relevance of search
    -   Kibana helps to visualize (and manage) data
        -   think of it as a web interface to elasticsearch
    -   Architecture
        -   Node:
            -   An instance of elasticsearch
            -   Has unique ID and a name
            -   Belongs to a single cluster
            -   There could be one to many nodes within a single cluster that are distributed across separate machines
            -   Each node could be assigned one to multiple roles (eg: storing data)
            -   Data is stored as documents (JSON object)
            -   Documents that have the same structure are grouped into an index
            -   Index is a virtual mechanism to keep track of where documents are stored (?)
        -   Sharding
            -   Data is actually stored inside a "shard" and this is where the search runs
            -   When an index is created, one shard comes with it by default, but this can be configured to include multiple shards (distributed across nodes). This is known as sharding (add sharding in index and distributing across nodes).
            -   Each shard is assigned to a node, so the number of documents a shard can hold depends on the capacity of the node.
            -   Sharding speeds up searching through parallel searches across nodes (shards?)
            -   To sum up, sharding can help store more data (horizonatal scaling) and also help speed up search.

## Setup
- Follow instructions given on the website
### Elasticsearch
- By default, stored at `/usr/share/elasticsearch`
- Uses `https` by default - configure at `elasticsearch.yml`
- Certificate at `/etc/elasticsearch/certs/http_ca.crt`
- For cURL, the URL is of the format
  `https://elastic:PASSWORD@localhost:9200/`
- For password reset, give the arg `-u elastic` for the script
  `elastic-reset-password`
#### Elasticdump
- Use `--transform='doc._source=Object.assign({}, doc)'` to prevent the error
  `Compressor detection can only be called ...`
  - See [here](https://github.com/elasticsearch-dump/elasticsearch-dump#module-transform) for more info on `--transform`
- The above error can be entirely avoided if the input JSON is of the format as
  in [here](https://github.com/elasticsearch-dump/elasticsearch-dump/blob/master/test/seeds.json)
- [Example](https://stackoverflow.com/questions/64920407/elasticdump-with-tls-unable-to-verify-the-first-certificate)
  command with https

## ES Requests
- To list all indices: `curl -XGET http://localhost:9200/_cat/indices`
- To insert a document: `POST http://localhost:9200/_doc`
- To delete a document: `DELETE http://localhost:9200/_doc/id`
- To return all records
```json
{
	"query": {
		"match_all": {}
	}
}
```
- Deleting an index: `curl -XDELETE localhost:9200/shop`
- Range query
```json
{
  "query": {
    "range": {
      "age": {
        "gte": 10,
        "lte": 20,
        "boost": 2.0
      }
    }
  }
}
```
- Terms query
```json
{
  "query": {
    "terms": {
      "user.id": [ "kimchy", "elkbee" ],
      "boost": 1.0
    }
  }
}
```
- Use `term` to check for a single value
- [Bodybuilder to ES Query](https://bodybuilder.js.org/)
