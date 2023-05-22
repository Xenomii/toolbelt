with open('filename.txt', 'r') as file:
    ip_list = file.readlines()
    ip_list = [ip.strip() for ip in ip_list] # Remove newline characters
    ip_set = set(ip_list) # Convert list to set to remove duplicates
    ip_list = list(ip_set) # Convert set back to list for sorting

ip_list.sort(key=lambda ip: [int(num) for num in ip.split('.')]) # Sort by IP address octets

with open('sorted_filename.txt', 'w') as file:
    for ip in ip_list:
        file.write(ip + '\n') # Write sorted IP addresses to new file

