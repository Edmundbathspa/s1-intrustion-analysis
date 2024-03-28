from ftplib import FTP

def connect_to_ftp_server(hostname, username, password):
    try:
        # Connect to the FTP server
        ftp = FTP(hostname)
        ftp.login(username, password)

        # Print success message
        print(f"Connected to FTP server {hostname} successfully!")

        # Print the current working directory
        print(f"Current working directory: {ftp.pwd()}")

        # List the files in the current directory
        print("Files in the current directory:")
        ftp.dir()

        # Close FTP connection
        ftp.quit()
    except Exception as e:
        print(f"Failed to connect to FTP server: {e}")

# FTP server credentials
hostname = "38.111.196.111"
username = "pavel.gladyshev@ucd.ie"
password = "Pa$hka123"

# Call the function to connect to the FTP server
connect_to_ftp_server(hostname, username, password)
