import os, sys
import pandas as pd

def checkFolder(serialNumber, Dir):
    # Search for the folder with the specified serial number
    for folderName in os.listdir(Dir):
        folderPath = os.path.join(Dir, folderName)
        if os.path.isdir(folderPath) and folderName == serialNumber:
            return folderPath
        else:
            pass
    return "False"

def checkExcel(FP, SN):
    # Look for an Excel file (.xlsx) within the serialNumber folder
    for fileName in os.listdir(FP):
        if fileName.lower().endswith('.xlsx'):
            # excelFilepath
            return os.path.join(FP, fileName)
        else:
            pass
    logError("error.txt", f"No Excel file found in folder '{SN}'.")
    return "False"

def extractExcelData(serialNumber, outputFile):
    # Specify the root directory where you want to search for folders
    symbolicRootDir = '/Alphawave Services/EA Production - SARAO - SARAO/DocumentControl/Test data/317-022005'  # Replace with your actual directory path
    rootDir = os.getcwd()

    folderPath = checkFolder(serialNumber, rootDir)
    
    if folderPath == "False":
        folderPath = checkFolder(serialNumber, symbolicRootDir)
        if folderPath == "False":
            logError("error.txt", f"Directory not found.")
            return
    # Read the Excel file and extract relevant data
    try:
        excelFilePath = checkExcel(folderPath, serialNumber)
        if excelFilePath == "False":
            return
        
        df = pd.read_excel(excelFilePath, sheet_name="Introduction", header=None)
        serial_row = df.iloc[10, 8]  # Columns I to N (0-based index)
        if serial_row == serialNumber:
            performance_df = pd.read_excel(excelFilePath, sheet_name="Performance")
            dataToWrite = performance_df.iloc[2:11, 3].tolist()  # D4 to D17
            dataToWrite.append(performance_df.iloc[15, 3])
        else:
            logError("error.txt", f"Serial number '{serialNumber}' not found in the Excel file.")
            return
    except Exception as e:
        logError("error.txt", f"Error reading Excel file: {e}")
        return
    
    # Write the extracted data to a text file
    outputFile = folderPath + "/" + serialNumber + ".txt"
    with open(outputFile, 'w') as txtFile:
        for line, cellValue in enumerate(dataToWrite, start=1):
            txtFile.write(f"{cellValue}\n")

def logError(file, errMsg):
    with open(file, 'a') as textFile:
        textFile.write(errMsg)

if __name__ == "__main__":

    if len(sys.argv) != 2:
        err = f"Please add serial number as an argument.\n"
        logError("error.txt", err)
        sys.exit(1)
    else:
        serialNumberArg = sys.argv[1]
        outputFile = serialNumberArg + ".txt"
    try:
        extractExcelData(serialNumberArg, outputFile)
    except Exception:
        logError("error.txt", f"Application failed to run.\n")