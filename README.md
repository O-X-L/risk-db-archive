# Open IP, Network & ASN Risk-Database

This data will be and stay open-source!

We publish this raw report-data to keep the Risk-DB process transparent.

You can also use this data for your custom projects and analysis.

If you find this project useful - leave a star and consider to also report abusers to the API!

Main repository: [O-X-L/risk-db](https://github.com/O-X-L/risk-db)

----

## Reporting, Processing & Processed Data

You can find the processed data and source-code for the reporting/processing of data here: [O-X-L/risk-db](https://github.com/O-X-L/risk-db)

----

## Report content

The reports are in CSV-format.

The report-values are de-duplicated to keep them as compact as possible. The ID's inside the report columns reference the lookup-tables contained in the `dedupe` directory. You can run the `redupe.py` script to revert all reports to their original state.

### Report info

* **ip**: Reported IP
* **an**: If the reported IP has been anonymized
* **cmt**: Reported comment
* **cat**: Reported category
* **time**: Time the report was received

### Reporter info

* **by**: Anonymized reporter IP (*IP4: /24, IP6: /56*)
* **user**: Short-Hash of the user that sent the report (*when a token was used*)

----

## License

**[BSD-3-Clause](https://opensource.org/license/bsd-3-clause)**

Free to use.

If you are nice, you can **optionally** mention that you use this IP data:

```html
<p>IP address data powered by <a href="https://risk.oxl.app">OXL</a></p>
```
