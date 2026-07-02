---
title: "Suggestion: Plan an Independent YARN Resource Pool When Hadoop Is Shared by Data Cube and Other Systems (GTS Product Convergence Solution)"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001276948960.html"
depth: 6
---
# Suggestion: Plan an Independent YARN Resource Pool When Hadoop Is Shared by Data Cube and Other Systems (GTS Product Convergence Solution)

**Specification name**: General\_DataFactory\_Batch\_LightETL\_Independent\_Resource\_Pool

**Description**: In the co-deployment scenario (GTS Product Convergence Solution) where Hadoop is shared by multiple businesses, you need to plan an independent YARN resource pool and allocate some independent Hadoop hosts and bind them to an independent queue. This prevents host resource contention during host sharing and further prevents fragmented resources and stacked tasks.

**Check guide**: Check whether Hadoop is shared by multiple businesses.

**Positive example**: See the [FusionInsight resource pool planning guide](../nottoctopics/en-us_topic_0000001175640921.html).

**Parent topic:** [[Batch Processing or Lightweight ETL|Batch Processing or Lightweight ETL]]