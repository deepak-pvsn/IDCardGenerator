import csv

def create_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Title', 'Photo_Location']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

# Example data
data = [
    {'Name': 'Venkata Sai Polakam', 'Title': 'Software Engineer', 'Photo_Location': 'photos/venkatasai_polakam.jpeg'},
    {'Name': 'Krishnakanth Burugu', 'Title': 'Data Scientist', 'Photo_Location': 'photos/krishnakanth_burugu.jpeg'},
    {'Name': 'Maryam Moshrefizadeh', 'Title': 'Scrum Master', 'Photo_Location': 'photos/maryam_moshrefizadeh.jpeg'},
    {'Name': 'Brijitha Tialu', 'Title': 'Technical Lead', 'Photo_Location': 'photos/brijitha_tialu.jpeg'},
    {'Name': 'Ashwin Pawar', 'Title': 'Project Manager', 'Photo_Location': 'photos/ashwin_pawar.png'},
]

# Name of the CSV file to create
filename = 'employee_data.csv'

# Call the function to create the CSV file
create_csv(data, filename)
