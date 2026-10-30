# Data Engineering: ETL and Data Pipelines

Data engineering is about moving, storing, transforming, and validating data reliably.

## 1. Core concepts
- ETL: extract, transform, load
- batch processing
- streaming processing
- data pipelines
- schema management
- data quality
- orchestration

## 2. ETL workflow
1. extract raw data from source systems
2. clean and transform data
3. validate schema and data quality
4. load into warehouse or lake
5. monitor pipeline health

## 3. Common tools
- Python
- SQL
- Airflow
- Spark
- Kafka
- dbt
- Snowflake / BigQuery / Redshift
- ElasticSearch / ClickHouse (optional)

## 4. Batch vs streaming
### Batch
- data processed in intervals
- suitable for historical reporting

### Streaming
- data processed in near real-time
- suitable for monitoring, alerts, and live pipelines

## 5. Data warehouse vs lake
### Data warehouse
- structured, query-optimized
- common in BI and analytics

### Data lake
- stores raw and structured data
- more flexible but often more complex

## 6. Data quality checks
- null checks
- duplicates
- schema validation
- range checks
- freshness checks
- consistency checks

## 7. Example ETL snippet
```python
import pandas as pd

raw = pd.read_csv("raw_data.csv")
clean = raw.dropna().rename(columns={"old_name": "new_name"})
clean.to_csv("processed_data.csv", index=False)
```

## 8. Why this matters in AI
Data engineering makes sure ML models receive:
- correct data
- timely updates
- clean features
- consistent labels
- reliable pipelines

## 9. Goal
A strong AI engineer understands how data is produced, cleaned, stored, and served to models at scale.
