# **Data Tracking with DVC in GitHub Codespaces**

This project demonstrates how to track raw and processed data using **DVC** and push these files to a remote storage (Google Drive). Participants will learn to version datasets, ensuring reproducibility in a collaborative setting.

---

## Steps to complete the task

---


### **1. Install Required Packages**
Install all required Python dependencies and DVC extensions

### **2. Initialize DVC**
DVC is already installed in your Codespace. Initialize DVC for the project.

### **3. Add Remote Storage**
- Set up Google Drive as the remote storage.
- Authenticate DVC with Google Drive.

### **4. Track Raw Data**
- Use DVC to track the raw data
- Commit the changes 
- Push the raw data to remote storage
- Tag this version of raw data as version 1.

### **5.Get the preprocessing data and track it**
- Pull the raw data from remote storage.
- Run the preprocessing.py script to generate processed data from raw data.
- Track the processed data with DVC (follow the same procedure) 
- Tag this version of processed data as version 2.

## Notes
- link for the dataset used in this assignment : https://archive.ics.uci.edu/dataset/222/bank+marketing
- Drive Authentication: Ensure DVC is authenticated with Google Drive (DVC-gdrive is installed by default in this project).
- Use dvc status to check the tracking status of your files.
