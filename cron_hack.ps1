# Loop to run the script 20 times
for ($i = 0; $i -lt 20; $i++) {
    # Print current iteration
    Write-Output "Running iteration: $($i+1)"

    # Call the Python script using the full path to the Python executable in the venv and the script
    & 'C:\Users\narfa\py\wavecomb\venv\Scripts\python.exe' 'C:\Users\narfa\py\wavecomb\get_surfline_data.py'
    
    # Sleep for 60 minutes (3600 seconds)
    Start-Sleep -Seconds 3600
}
