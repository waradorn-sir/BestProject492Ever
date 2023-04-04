BestProject492Ever

This project requires Python 3.0 or higher.

To install the necessary modules, run the following commands in your terminal:

1)pip install Flask
2)pip install numpy
3)pip install scipy
4)pip install -U scikit-learn

Don't forget to check IP of your connection.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

To run the program using PowerShell:

1) Navigate to the "BestProject492Ever" directory.
2) Run the "Backend.py" file by typing "python Backend.py" in the terminal to start the server.
3) Copy the IP address that is displayed in the terminal.
4) Update the IP address in the "BackendMotion", "BackendSwitch", and "BackendTemp" folders to match the IP address of the server (keep the default port).
5) Navigate to each of the folders mentioned above and run the "Backend.py" file.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

IoT Part:

1) Navigate to the "BestProject492Ever\Frontend" directory.
2) To send fake packets to the server, run "send_fake_data.py".
3) To send data from the temperature device, run "send_real_data_auto(temp).py".
4) To send data from the motion sensor or light switch device, run "send_real_data_manual.py" and use the argument "motion" or "switch" to specify which device to send data from.

That's it!
