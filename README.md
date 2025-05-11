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

### Report info

* **ip**: Reported IP
* **ip_an**: If the reported IP has been anonymized
* **cmt**: Reported comment
* **cat**: Reported category
* **time**: Time the report was received

### Reporter info

* **by**: Anonymized reporter IP (*IP4: /24, IP6: /56*)
* **fp**: [JA4 client TLS-fingerprint](https://github.com/O-X-L/haproxy-ja4) of the reporter
* **user**: Short-Hash of the user that sent the report (*when a token was used*)

----

## License

**[BSD-3-Clause](https://opensource.org/license/bsd-3-clause)**

Free to use.

If you are nice, you can **optionally** mention that you use this IP data:

```html
<p>IP address data powered by <a href="https://risk.oxl.app">OXL</a></p>
```
