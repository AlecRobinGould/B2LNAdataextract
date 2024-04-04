# Band 2 LNA bias values extraction tool

This application serves the purpose of performing the data extraction part of the automation of the LNA bias programming on the SPF SHIELD software.

## Format

This application takes in 1 argument in the form of a string. This string should be the full serial number of the LNA. Ex `SLB007`

The application shall return a .txt file with the LNA bias data in the following format:

The text file will be named after the serial number argument.

```
Drain voltage 1
Drain voltage 2
Drain voltage 3
Drain current 1
Drain current 2
Drain current 3
Gate voltage 1
Gate voltage 2
Gate voltage 3
Mean gain
```