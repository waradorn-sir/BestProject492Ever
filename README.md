BestProject492Ever

This project requires Python 3.0 or higher.

To install the necessary modules, run the following commands in your terminal:

pip install Flask
pip install numpy
pip install scipy
pip install -U scikit-learn

Don't forget to check IP of your connection.

To run the program using PowerShell:

Navigate to the "BestProject492Ever" directory.
Run the "Backend.py" file by typing "python Backend.py" in the terminal to start the server.
Copy the IP address that is displayed in the terminal.
Update the IP address in the "BackendMotion", "BackendSwitch", and "BackendTemp" folders to match the IP address of the server (keep the default port).
Navigate to each of the folders mentioned above and run the "Backend.py" file.

IoT Part:

Navigate to the "BestProject492Ever\Frontend" directory.
To send fake packets to the server, run "send_fake_data.py".
To send data from the temperature device, run "send_real_data_auto(temp).py".
To send data from the motion sensor or light switch device, run "send_real_data_manual.py" and use the argument "motion" or "switch" to specify which device to send data from.

That's it!
