# Band 2 LNA bias values extraction tool

This application serves the purpose of performing the data extraction part of the automation of the LNA bias programming on the SPF SHIELD software.

## Format

This application takes in 1 argument in the form of a string. This string should be the full serial number of the LNA. Ex `SLB007`

The application shall return a .txt file with the LNA bias data in the following format:

The text file will be named after the serial number argument. *If the text file exists, it WILL be overwritten.*

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

Example:

`python dataExtract.py "SLB008"` or compiled version: `LNADataExtract.exe "SLB008"`

returns:
```
0.8     
0.93    
0.98    
6   
6   
7.5     
-0.184  
-0.166  
-0.116  
41.05975121951219   
```

in a text file named `SLB008.txt` in the same directory as it's excel file `Alphawave Services\EA Production - SARAO - SARAO\DocumentControl\Test data\317-022005\SLB008`.

# Compilation

run `python -m pip install pyinstaller` in cmd prompt or powershell etc.

Run the .bat file. This will create 2 folders, one called build, the other dist.
The release binary file is located in /dist - this is to be used from SPF SHIELD