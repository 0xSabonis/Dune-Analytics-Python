Here's the simplified version of your README, followed by the GitHub README content:

---

### Dunebuggy

Dunebuggy is a lightweight (unofficial) Python SDK for [Dune.com](https://dune.com/home). It allows you to interact with public queries on Dune, fetch results, and even create new queries using SQL.

---

### Installation

To install Dunebuggy, run:

```sh
pip install dunebuggy
```

---

### Getting Started

#### Retrieving a Public Query

To retrieve a query, you just need the `query_id` of the public query you want. For example, let's fetch the "Custom NFT Floor Tracker" query by `@smaroo`:

```python
from dunebuggy import Dune

dune = Dune()
query = dune.fetch_query(83579)
```

You can then access the query results as a pandas DataFrame:

```python
print(query.df.head())
```

You can also view basic information about the query:

```python
print(query.info)
```

#### Customizing a Parameterized Query

Some queries on Dune are parameterized, meaning they allow you to enter custom values. For example, the "Custom NFT Floor Tracker" query has parameters for NFT contract address, time interval, and start date.

To modify the parameters and re-fetch the query:

```python
params = query.parameters
params[0].value = 'new_nft_contract_address'

custom_query = dune.fetch_query(83579, parameters=params)
print(custom_query.df.head())
```

You can also create a fresh set of parameters:

```python
from dunebuggy.models.query import QueryParameter

param_to_change = QueryParameter(
    key='Enter NFT Contract Address',
    value='new_nft_contract_address',
)
params[0] = param_to_change
custom_query = dune.fetch_query(83579, parameters=params)
print(custom_query.df.head())
```

#### Creating a New Query

You can create a new query by providing the query name, SQL query string, and dataset ID.

Example SQL query:

```python
query_string = "SELECT * FROM ethereum.transactions LIMIT 100"
```

To create the query:

```python
from dunebuggy.models.constants import DatasetId

created_query = dune.create_query("My Query's Name", query_string, DatasetId.ETHEREUM)
print(created_query.df.head())
```

---

### Saving to CSV

To save a query's results to a CSV file:

```python
created_query.df.to_csv('my_test_data.csv')
```

---

### Roadmap

- [ ] Cleanup TODO comments
- [ ] Add support for embedding Dune graphs
- [ ] Add tests
- [ ] Support query updates
- [ ] Investigate dashboard support
- [ ] Handle large data sets by querying in batches
- [ ] Improve column formatting
- [ ] Add Documentation

---

### Notes

This project was inspired by the [itzemstar's duneanalytics repo](https://github.com/itzmestar/duneanalytics).

---

### GitHub README

```md
# Dunebuggy

Dunebuggy is a lightweight (unofficial) Python SDK for [Dune.com](https://dune.com/home). It allows you to interact with public queries on Dune, fetch results, and even create new queries using SQL.

## Installation

To install Dunebuggy, run:

```sh
pip install dunebuggy
```

## Getting Started

### Retrieving a Public Query

To retrieve a query, you just need the `query_id` of the public query you want. For example, let's fetch the "Custom NFT Floor Tracker" query by `@smaroo`:

```python
from dunebuggy import Dune

dune = Dune()
query = dune.fetch_query(83579)
```

You can then access the query results as a pandas DataFrame:

```python
print(query.df.head())
```

You can also view basic information about the query:

```python
print(query.info)
```

### Customizing a Parameterized Query

Some queries on Dune are parameterized, meaning they allow you to enter custom values. For example, the "Custom NFT Floor Tracker" query has parameters for NFT contract address, time interval, and start date.

To modify the parameters and re-fetch the query:

```python
params = query.parameters
params[0].value = 'new_nft_contract_address'

custom_query = dune.fetch_query(83579, parameters=params)
print(custom_query.df.head())
```

You can also create a fresh set of parameters:

```python
from dunebuggy.models.query import QueryParameter

param_to_change = QueryParameter(
    key='Enter NFT Contract Address',
    value='new_nft_contract_address',
)
params[0] = param_to_change
custom_query = dune.fetch_query(83579, parameters=params)
print(custom_query.df.head())
```

### Creating a New Query

You can create a new query by providing the query name, SQL query string, and dataset ID.

Example SQL query:

```python
query_string = "SELECT * FROM ethereum.transactions LIMIT 100"
```

To create the query:

```python
from dunebuggy.models.constants import DatasetId

created_query = dune.create_query("My Query's Name", query_string, DatasetId.ETHEREUM)
print(created_query.df.head())
```

### Saving to CSV

To save a query's results to a CSV file:

```python
created_query.df.to_csv('my_test_data.csv')
```

## Roadmap

- [ ] Cleanup TODO comments
- [ ] Add support for embedding Dune graphs
- [ ] Add tests
- [ ] Support query updates
- [ ] Investigate dashboard support
- [ ] Handle large data sets by querying in batches
- [ ] Improve column formatting
- [ ] Add Documentation


## Contact
Telegram | [dogewhiz](https://t.me/dogewhiz)
