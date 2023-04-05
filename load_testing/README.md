# Load testing analysis <!-- omit in toc -->

# Table of Contents <!-- omit in toc -->
- [Introduction](#introduction)
- [Running tests](#running-tests)
- [Architecture Version 1.0.0](#architecture-version-100)
  - [Architecture Overview](#architecture-overview)
  - [Ingestion API](#ingestion-api)
  - [Serving API](#serving-api)

## Introduction

In order to test if the solution scales, it is interesting to do load testing because it measures
how well the API will handle a large number of concurrent transactions and show potential bottlenecks
for solution architecture.

## Running tests

In order to run the tests you need to install the packages using `pipenv install --dev` in this folder and run `locust`,
this will start the [Locust](https://docs.locust.io/en/stable/index.html) UI and then choose your load on
[`http://localhost:8089`](http://localhost:8089) the Ingestion API is in the following url: `http://localhost:8080`, the Serving API is in the following url: `http://localhost:9000`.

## Architecture Version 1.0.0

### Architecture Overview

The architecture is the following:

![figure](../docs/v1/Annotation%20platform%20v1.drawio.png)

We can see that the potential fail points consist mainly on adding and fetching data from Argilla. The assumption is that over a certain load it will not insert any data on Argilla and we will not be able to fetch data using the serving API as well.

### Ingestion API

For the first load testing, we run 50 users at a rate of 1 second each. We have two interesting results:

1) We find an interesting error:

```bash
ERROR:argilla.client.client: client.py:103
Cannot log data in dataset
'toxic_texts'
Error: LiveError
Details: Only one live display may be active at once
```

This error means that we have data that is lost on the upload to argilla. This problem comes up because that by adding the data directly from the Ingestion API we make several POSTs to Argilla asynchronously and Argilla doesn't supports this. We can surpass this problem by delegating the upload to argilla to another part, for instance, the Ingestion API adds data to a database or file storage and then after an amount of time we upload this data to argila in batch format.

2) The plot regarding the load testing is the following:

![load testing Ingestion API figure](images/load_testing_ingestion_api_50_users_per_second.png)

When the number of users increases, the load on the system also increases, which can cause a strain on the available resources such as server capacity and bandwidth. If the resources are insufficient to handle the increased load, it could lead to slower response times and an increased number of failed requests, which could ultimately impact the user experience. 

The limited Request per Second is an indication of the maximum number of requests that the API can handle in a given period. When this limit is reached, any additional requests will be rejected, leading to failed requests and possibly a degraded user experience. Response times of ~60 seconds indicate that the ingestion API is struggling to process requests efficiently. When response times are slow, it leads to a poor user experience, and should be addressed.

One way of addressing it is storing data in a database or file could be a feasible solution to this problem. By doing so, data can be processed and analyzed in batches, which could improve the overall efficiency of the system. This approach could also provide a buffer for handling a sudden surge in requests. However, implementing a database or file storage system requires additional resources and could increase the complexity of the system. Therefore, it is essential to carefully evaluate the trade-offs between performance, cost, and complexity when considering this solution.

### Serving API

This plot shows load testing of the serving API. However, the test has limited data with only ~100 toxic and ~100 non-toxic texts. As the number of texts increases, the query time will also increase:

![load testing Serving API figure](images/load_testing_serving_api_50_users_per_second.png)

The relationship between the number of users and response time is an important consideration when designing and scaling software systems. As the number of users accessing a system grows, the demand for resources increases, and the system may experience performance issues, such as increased response time. 

The figure that shows the relationship between the number of users and response time is usually a graph, where the x-axis represents the time as the number of users ar scaled up, and the y-axis represents the response time. As the number of users increases, the response time also increases, indicating that the system is taking longer to respond to requests. When response times are slow, it leads to a poor user experience.

 As stated before, the best solution is to serve the data on a database, in this case an analytical database is best suited as it can handle a huge amount of data.
