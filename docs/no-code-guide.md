# Collect Lever jobs without code

Open [Lever Jobs Scraper](https://apify.com/datascraperes/lever-jobs-scraper?fpr=edudata), choose Input and paste company board URLs or slugs into `boardUrls`. For a first run use one board and a total limit of one job, as in [sample input](../data/sample-input.json).

Review the Pricing tab, set the maximum charge and timeout in Console, then click Start. Once finished, open the Dataset to inspect and export JSON or CSV. Inspect `SUMMARY` and `ERRORS` in the key-value store: a run can preserve useful jobs while a requested board is unavailable. Missing SUMMARY means completeness cannot be confirmed.

Descriptions are enabled by default through `includeDescription`. Departments, teams and workplace labels are included when available. The Actor collects specified boards; it does not discover every company using Lever.
