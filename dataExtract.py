import os, sys
import pandas as pd

def extractExcelData(serialNumber, outputFile):
    # Specify the root directory where you want to search for folders
    rootDir = 'C:/Alphawave Services/EA Production - SARAO - SARAO/DocumentControl/Test data/317-022005'  # Replace with your actual directory path

    # Search for the folder with the specified serial number
    for folderName in os.listdir(rootDir):
        folderPath = os.path.join(rootDir, folderName)
        if os.path.isdir(folderPath) and folderName == serialNumber:
            # Look for an Excel file (.xlsx) within the serialNumber folder
            for fileName in os.listdir(folderPath):
                if fileName.lower().endswith('.xlsx'):
                    excelFilePath = os.path.join(folderPath, fileName)
                    break
            else:
                print(f"No Excel file found in folder '{serialNumber}'.")
                return

            # Read the Excel file and extract relevant data
            try:
                df = pd.read_excel(excelFilePath, sheet_name="Introduction", header=None)
                serial_row = df.iloc[10, 8]  # Columns I to N (0-based index)
                # print(serial_row)
                if serial_row == serialNumber:
                    performance_df = pd.read_excel(excelFilePath, sheet_name="Performance")
                    dataToWrite = performance_df.iloc[2:11, 3].tolist()  # D4 to D17
                    dataToWrite.append(performance_df.iloc[15, 3])
                else:
                    print(f"Serial number '{serialNumber}' not found in the Excel file.")
                    return
            except Exception as e:
                print(f"Error reading Excel file: {e}")
                return

            # Write the extracted data to a text file
            outputFile = rootDir + "/" + serialNumber + "/" + outputFile
            with open(outputFile, 'w') as txtFile:
                for line, cellValue in enumerate(dataToWrite, start=1):
                    txtFile.write(f"{cellValue}\n")
                print(f"Data written to '{outputFile}' successfully.")
            return

    print(f"Folder '{serialNumber}' not found in the specified directory.")

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python dataExtract.py <Serial Number>")
        sys.exit(1)
    serialNumberArg = sys.argv[1]
    outputFile = serialNumberArg + ".txt"

    extractExcelData(serialNumberArg, outputFile)
